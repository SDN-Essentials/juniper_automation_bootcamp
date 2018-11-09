#!/usr/bin/env python
"""Example code for BGP ASN 'data modeling' exercise."""


import argparse
import sys


def validate_bgp_asn(asn):
    """Function to validate BGP ASN."""
    if 1 <= asn <= 4294967294:
        return True
    else:
        return False


def main():
    parser = argparse.ArgumentParser(description='Configure BGP ASN.')
    parser.add_argument('--asn', type=int, help='Enter 16-bit or 32-bit ASN.')
    args = parser.parse_args()
    if validate_bgp_asn(args.asn) is True:
        print('Valid ASN!')
    else:
        print('Invalid ASN. :(')

if __name__ == '__main__':
    sys.exit(main())
