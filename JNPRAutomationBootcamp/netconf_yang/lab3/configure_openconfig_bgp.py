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
CONFIG = 'configure_openconfig_bgp.xml'


# create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         look_for_keys=False, allow_agent=False) as m:

        print('* Configure csr1000v using OpenConfig *')
        with open(CONFIG) as f:
            xml_data = m.edit_config(target='running', config=f.read())
            print("Success? {}".format(xml_data.ok))
            #xml_data = m.dispatch(f.read())


if __name__ == '__main__':
    sys.exit(main())
