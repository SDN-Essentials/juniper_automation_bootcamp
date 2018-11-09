#!/usr/bin/env python


from pprint import pprint
import sys
import xmltodict


SW = 'software_version.xml'


def main():
    with open(SW) as sw:
        sw_info = xmltodict.parse(sw.read().strip())
        pprint(sw_info)
        print('Hostname: {}'.format(sw_info['software-information']['host-name']))
        print('Version: {}'.format(sw_info['software-information']['package-information']['comment']))
        print('Platform: {}'.format(sw_info['software-information']['product-model']))


if __name__ == '__main__':
    sys.exit(main())
