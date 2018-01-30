#!/usr/bin/env python
"""
PyEZ structured change illustration.

darien@sdnessentials.com
"""

from jnpr.junos.cfg.phyport import PhyPortClassic
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys
import time


def main():
    """Simple main method to change port status."""
    routers = ['10.11.12.1', '10.11.12.2']
    pyez_user = 'netconf'
    pyez_pass = 'test123'
    sessions = [Device(host=router, user=pyez_user, password=pyez_pass) for router in routers]

    for session in sessions:
        session.open()
        port = PhyPortClassic(session, namevar='ge-0/0/3')
        # Step 1.1
        # print(port.properties)
        # print(port.admin)

        # Step 1.2
        port.admin = False
        port.write()

        print("Disabling interfaces!")
        cfg = Config(session)
        cfg.commit()
        time.sleep(10)

        port.admin = True
        port.write()

        print("Enabling interfaces!")
        cfg.commit()
        session.close()

if __name__ == '__main__':
    sys.exit(main())
