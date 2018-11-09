#!/usr/bin/env python

from ncclient import manager
import sys


# the variables below assume the user is leveraging the
# student lab and accessing srx_r1 using the loopback
HOST = '172.16.0.1'
# use the NETCONF port for your srx_r1 device
PORT = 830
# use the user credentials for your srx_r1 device
USER = 'netconf'
PASS = 'test123'


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
        interface_filter = '''
                          <filter>
                              <configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm">
                                  <interfaces></interfaces>
                              </configuration>
                          </filter>
                          '''
        print('* Here is the device configuration *')
        # print Junos configuration in XML
        print(m.get_config('running', interface_filter))

if __name__ == '__main__':
    sys.exit(main())
