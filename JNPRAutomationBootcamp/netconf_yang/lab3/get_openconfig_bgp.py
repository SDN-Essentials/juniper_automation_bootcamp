#!/usr/bin/env python


from ncclient import manager
import sys
import xml.dom.minidom

# the variables below assume the user is leveraging the
# student lab and accessing csr1000v using NET
HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your csr1000v NAT
PORT = 10000
# use the user credentials for your csr1000v device
USER = 'root'
PASS = 'D_Vay!_10&'


def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # Create an XML filter to retrieve only the hostname
        filter = '''
            <filter>
              <bgp xmlns="http://openconfig.net/yang/bgp"/>
            </filter>
        '''
        print('* Here is the device configuration *')
        # print Junos configuration in XML
        print(m.get_config('running', filter))

if __name__ == '__main__':
    sys.exit(main())
