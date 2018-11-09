#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom

HOST = 'ios-xe-mgmt.cisco.com'
PORT = 10000
USER = 'root'
PASS = 'D_Vay!_10&'
FILE = 'get_ietf_interface_stats.xml'
MODULE_NAME = 'ietf-interfaces.yang'


# create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print YANG module
        print('***Saving the YANG Module***')
        data = m.get_schema('ietf-interfaces')
        xml_doc = xml.dom.minidom.parseString(data.xml)
        yang_module = xml_doc.getElementsByTagName("data")

        # save the YANG module to a file
        with open(MODULE_NAME, mode='w+') as f:
            f.write(yang_module[0].firstChild.nodeValue)

if __name__ == '__main__':
    sys.exit(main())
