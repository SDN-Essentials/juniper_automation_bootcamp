#!/usr/bin/env python
#


from ncclient import manager
import sys
import xml.dom.minidom
import xmltodict
from pprint import pprint
import json


HOST = 'ios-xe-mgmt.cisco.com'
PORT = 10000
USER = 'root'
PASS = 'D_Vay!_10&'
FILE = 'get_ietf_interface_stats.xml'


# Function to retrieve information via NETCONF
def get_netconf(xml_filter):
    """
    Main method that retrieves information via NETCONF get.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get(f.read()))


def create_message(interface):
    """
    Create a Markdown formatted message about interface state
    """
    # MISSION: Replace XXX with the correct leaf
    message = "## Interface Stats: Interface %s \n" % (interface["name"])
    message += "* Speed: %s \n" % (interface["speed"])
    message += "* Status: %s \n" % (interface["oper-status"])
    message += "* MAC Address: %s \n" % (interface["phys-address"])
    message += "* Statistics \n"
    message += "    * Octets In: %s \n" % (interface["statistics"]["in-octets"])
    message += "    * Octets Out: %s \n" % (interface["statistics"]["out-octets"])
    message += "    * Packets In: %s \n" % (interface["statistics"]["in-pkts"]["#text"])
    message += "    * Packets Out: %s \n" % (interface["statistics"]["out-pkts"]["#text"])
    message += "    * Errors In: %s \n" % (interface["statistics"]["in-errors"])
    message += "    * Errors Out: %s \n" % (interface["statistics"]["out-errors"])
    return(message)


def main():
    netconf = get_netconf(FILE)
    print(xmltodict.parse(netconf.xml))
    """
    try:
        netconf = get_netconf(FILE)
        print(xmltodict.parse(netconf.xml))
        interface = xmltodict.parse(netconf.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]
        print(create_message(interface))
    except Exception as e:
        print("Uh oh! Ran into an issue")
        print(e)
        sys.exit()
    """

if __name__ == '__main__':
    sys.exit(main())
