"""
Advanced NAPALM script for safe and controlled configuration changes.
Designed to focus on stability, traceability, and clear operations.

- Connects to multiple network devices using NAPALM
- Backs up running configuration before changes
- Loads and compares candidate configurations (ACL, OSPF)
- Displays interface operational status for visibility
- Commits or discards changes based on configuration diffs
- Records configuration changes for audit and troubleshooting
- Performs rollback to the previous configuration upon failure
"""

from getpass import getpass
from napalm import get_network_driver
import json
import datetime
import logging
import traceback

logging.basicConfig(filename='napalmconfig2.log',level=logging.DEBUG, filemode='w')
driver = get_network_driver('ios')

# Prompt for SSH credentials (used for all devices)
username = input('Enter your SSH username: ')
password = getpass()

# Read IP addresses from file
with open('device') as f:
    devices_list = f.read().splitlines()

for IP in devices_list:
    #IP = IP.strip()
    print (f"\n===== Connecting to device: {IP} =====")
    ios = driver(IP, username, password,optional_args={'fast_cli':False,'read_timeout_override':60})

    # Open NAPALM connection
    try:
        ios.open()
    except Exception as e:
        print (f'Unexpected error on {IP}: {e}')
        continue

    try:
        # Backup current running configuration for rollback safety
        running_config = ios.get_config()['running']
        with open(f"{IP}_backup.cfg", "w") as f:
            f.write(running_config)
        print("Running-config backup backup completed")

        # Check interface status
        print("\n--- Interface Status ---")
        interface = ios.get_interfaces()
        for name, data in interface.items():
            print(f"interface {name}: {'enabled' if data['is_enabled'] else 'disabled'}, {'up' if data['is_up'] else 'down'}")

        # ACL config diff check
        print("\n--- Checking ACL configuration difference ---")
        ios.load_merge_candidate(filename='acl.cfg')
        acl_diff = ios.compare_config()
        if acl_diff:
            print(acl_diff)
            ios.commit_config()
            print("ACL configuration committed")
        else:
            print('No ACL changes required.')
            ios.discard_config()

        # OSPF config diff check
        print("\n--- Checking OSPF configuration difference ---")
        ios.load_merge_candidate(filename='ospf.cfg')
        ospf_diff = ios.compare_config()
        if ospf_diff:
            print(ospf_diff)
            ios.commit_config()
            print("OSPF configuration committed")
        else:
            print('No OSPF changes required.')
            ios.discard_config()

        # Stores change report
        if acl_diff or ospf_diff:
            timestamp = datetime.datetime.now().isoformat()
            with open("config_change_report.txt", "a") as f:
                f.write("=================================\n")
                f.write(f"Device: {IP}\n")
                f.write(f"Change Time: {timestamp}\n\n")
                f.write("=== ACL Diff ===\n")
                f.write(f"{acl_diff}\n\n")
                f.write("=== OSPF Diff ===\n")
                f.write(f"{ospf_diff}\n\n")

               # json.dump({
               # "device": IP,
               # "time": timestamp,
               # "acl_diff": acl_diff,
               # "ospf_diff": ospf_diff}
               # , report, indent=4)

    except Exception:
        print(f"Error occurred on {IP}")
        with open("error_log.txt","w") as log:
            traceback.print_exc(file=log)

        # Attempt rollback using NAPALM rollback
        try:
            ios.rollback()
            print("Rollback completed")
        except Exception:
            # Fallback: replace with saved running-config
            try:
                ios.load_replace_candidate(filename=f"{IP}_backup.cfg")
                ios.commit_config()
                print("Backup configuration restored")
            except Exception as e:
                print(f"Rolleback failed on {IP}: {e}")
                with open("error_log.txt","a") as log:
                    traceback.print_exc(file=log)
            finally:
                try:
                    ios.close()
                except Exception:
                    pass

