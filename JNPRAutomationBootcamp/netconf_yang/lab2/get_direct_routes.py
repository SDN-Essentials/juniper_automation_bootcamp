#!/usr/bin/env python

from ncclient.xml_ import *
from ncclient import manager
import sys
import xmltodict


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

        print('* Here are the direct routes in the routing table *')
        # Create the XML RPC to retrieve direct routes from Junos
        get_direct_routes = new_ele('get-route-information')
        sub_ele(get_direct_routes, 'protocol').text = 'direct'
        xml_data = m.dispatch(get_direct_routes)
        print(xml_data)
        print('* Here are the structured direct routes *')
        print('Prefix         Interface')
        print('---------      -------------')
        # Direct routes accepts an XML buffer or string object
        direct_routes = xmltodict.parse(xml_data.xml)
        for route in direct_routes['rpc-reply']['route-information']['route-table']:
        # for route in direct_routes['rpc-reply']['route-information']['route-table']['rt']:
            print(route)
            # print('{pf}    {int}'.format(pf=route['rt-destination'], int=route['rt-entry']['nh']['via']))


if __name__ == '__main__':
    sys.exit(main())
