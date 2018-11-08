#!/usr/bin/env python
"""
PyEZ retrieve syslog.

darien@sdnessentials.com
"""

from jnpr.junos import Device
import re
import sys


# Step 1.1
def main():
    """Simple main method to enter log entries."""
    routers = ['10.11.12.1', '10.11.12.2']
    pyez_user = 'netconf'
    pyez_pass = 'test123'
    # Step 1.3
    # Raw versus non... Forgot.
    link_down = re.compile('(\w{1,3}\s{1,3}\d{1,2}\s{1,3}\d{1,2}:\d{1,2}:\d{1,2}).*SNMP_TRAP_LINK_DOWN.*ifName ([gax]e-\d{1,2}\/\d{1,2}\/\d{1,2})\n')
    for router in routers:
        try:
            device = Device(host=router, user=pyez_user, password=pyez_pass)
            device.open()
            print(device.facts)
            logs = device.rpc.get_log(filename='messages')
            # Step 1.2
            # print(type(logs))
            # print(dir(logs))

            for log_content in logs.iter("file-content"):
                # print(type(log_content))
                # print(dir(log_content))
                print(log_content.text)
                messages = link_down.finditer(log_content.text)
                # Step 1.3
                if messages:
                    for log in messages:
                        # Step 1.4
                        print(log.group(1))
                        # print(log.group(2))
                        # print(log.group(0))
            device.close()
        except Exception as e:
            print("Uh oh! We had a problem retrieving the messages log file.")
            print('Here is the error {error}'.format(error=e))

if __name__ == '__main__':
    sys.exit(main())
