#!/usr/bin/env python

from ncclient import manager
import sys


# the variables below assume the user is leveraging the
# student lab and accessing csr1000v using NET
HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your csr1000v NAT
PORT = 10000
# use the user credentials for your csr1000v device
USER = 'root'
PASS = 'D_Vay!_10&'


# Basic main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # Create an XML filter to retrieve only the hostname
        hostname_filter = '''
                          <filter>
                              <configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm">
                                  <interfaces></interfaces>
                              </configuration>
                          </filter>
                          '''
        print('* Here is the device configuration *')
        # print Junos configuration in XML
        print(m.get_config('running'))
        print(m.get_config('running', hostname_filter))

if __name__ == '__main__':
    sys.exit(main())
