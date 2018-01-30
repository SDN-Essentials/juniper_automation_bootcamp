#!/usr/bin/python
"""
PyEZ Custom Table and View Part 2.

darien@sdnessentials.com
"""

from jnpr.junos import Device
from jnpr.junos.op.bgp import BGPNeighborTable
import sys

# Step 1.7
def main():
    """Simple main method to view custom BGP table."""
    routers = ['10.11.12.1', '10.11.12.2']
    username = 'netconf'
    password = 'test123'
    for router in routers:
        dev = Device(host=router, user=username, password=password)
        dev.open()
        dev_info = BGPNeighborTable(dev)
        dev_info.get()
        for key in dev_info.keys():
            bgp_info = dev_info[key]
            print('#' * 60)
            print('This host         : {host}'.format(host=bgp_info.local_address))
            print('Belongs to ASN    : {ver}'.format(ver=bgp_info.local_as))
            print('And peers with    : {host}'.format(host=bgp_info.peer_address))
            print('In ASN            : {ver}'.format(ver=bgp_info.peer_as))
            print('The peer type is  : {ver}'.format(ver=bgp_info.peer_type))
            print('The peer state is : {flap}'.format(flap=bgp_info.peer_state))
            print('The peer is advertising   : {sent}'.format(sent=bgp_info.nlri_type_peer))
            print('We peer are advertising   : {recv}'.format(recv=bgp_info.nlri_type_session))
            print('We are applying policy    : {act}'.format(act=bgp_info.export_policy))
            print('With route preference     : {recv}'.format(recv=bgp_info.preference))
            print('Using holdtime            : {acc}'.format(acc=bgp_info.holdtime))
            print('#' * 60)
        dev.close()


if __name__ == '__main__':
    sys.exit(main())
