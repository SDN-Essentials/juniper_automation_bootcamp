#!/usr/bin/env python
"""
PyEZ retrieve syslog.

darien@sdnessentials.com
"""

from jnpr.junos import Device
import re
import sqlite3
import sys


# Step 1.2
def write_log_to_database(db, log):
    """Write log entry to database."""
    try:
        db_connection = sqlite3.connect(db)
        db_cursor = db_connection.cursor()
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS logs(timestamp VARCHAR(20) PRIMARY KEY,
                                                             hostname VARCHAR(8),
                                                             interface VARCHAR(20),
                                                             message VARCHAR(30))''')
        sql_cmd = 'INSERT INTO logs (timestamp, hostname, interface, message) VALUES(?,?,?,?)'
        db_cursor.execute(sql_cmd, (log[0], log[1], log[2], log[3]))
        db_connection.commit()
        db_connection.close()
    except sqlite3.IntegrityError as e:
        print("Avoiding duplicate entries.")
        print('Here is the error {error}'.format(error=e))


def main():
    """Simple main method to enter log entries."""
    routers = ['10.11.12.1', '10.11.12.2']
    pyez_user = 'netconf'
    pyez_pass = 'test123'
    netdata_db = 'network_data.db'
    link_down = re.compile('(\w{1,3}\s{1,3}\d{1,2}\s{1,3}\d{1,2}:\d{1,2}:\d{1,2}).*SNMP_TRAP_LINK_DOWN.*ifName ([gax]e-\d{1,2}\/\d{1,2}\/\d{1,2})\n', flags=0)
    for router in routers:
        try:
            device = Device(host=router, user=pyez_user, password=pyez_pass)
            device.open()
            logs = device.rpc.get_log(filename='messages')
            for log_content in logs.iter("file-content"):
                # print(log_content.text)
                messages = link_down.finditer(log_content.text)
                if messages:
                    # print(messages.group(0))
                    for log in messages:
                        entry = []
                        # Step 1.1
                        print(log.group(1))
                        print(log.group(2))
                        print(log.group(0))
                        # Step 1.3
                        print(log.group(1).replace(' ', '_') + '_' + device.facts['fqdn'])
                        entry.append(log.group(1).replace(' ', '_') + '_' + device.facts['fqdn'])
                        entry.append(device.facts['fqdn'])
                        entry.append(log.group(2))
                        entry.append(log.group(0))
                        write_log_to_database(netdata_db, entry)
            device.close()
        except Exception as e:
            print("Uh oh! We had a problem retrieving the messages log file.")
            print('Here is the error {error}'.format(error=e))

if __name__ == '__main__':
    sys.exit(main())
