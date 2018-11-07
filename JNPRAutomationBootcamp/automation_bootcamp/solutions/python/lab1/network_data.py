#!/usr/bin/env python

import re
import sys
import yaml


# Step 1.1
def get_yaml(file_name=None):
    """Basic function that returns a Python data structure from a YAML file.

    Parameters: File name of YAML file
    """

    if file_name is None:
        raise ValueError("No YAML file passed to function!")

    try:
        return yaml.load_all(open(file_name))
    except IOError:
        print('Oops! Check the name of the YAML file passed as an argument.')
        print('The file passed during execution does not appear to exist.')
        sys.exit()


# Step 1.2
def normalize_macs(network_data):
    """Simple function to iterate over network data and return a dictionary
    mapping hostname to MAC address.

    Parameters: Network data as a dictionary
    """
    host_macs = {}
    # Step 1.3
    mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[\.:-]?){5}([0-9A-Fa-f]{2})$')
    # Step 1.2
    for document in network_data:
        for hostname, device_data in document.iteritems():
            # print(hostname, device_data)
            # Step 1.3
            if mac_regex.match(device_data['mac_address']):
                # Step 1.4
                host_macs[hostname] = ''.join(re.findall(r'[0-9A-Fa-f]+',
                                              device_data['mac_address'].upper()))
            else:
                host_macs[hostname] = None
    # Step 1.4
    return (host_macs)


# Bonus Step 1.5
def sort_macs(host_macs):
    sorted_host_macs = []
    for hostname, mac in host_macs.iteritems():
        sorted_host_macs.append((hostname, mac))
    # print(sorted_host_macs)
    return (sorted(sorted_host_macs, key=lambda host_macs: host_macs[1], reverse=True))


def main():
    """Main method to iterate over data structures imported from YAML files.

    Parameters: None
    """
    if len(sys.argv) != 2:
        print('Oops! Might want to check your syntax!')
        print('You should run this example like this:')
        print('python {f} <NAME OF YAML FILE>'.format(f=__file__))
        sys.exit()
    else:
        _YAML_FILE = sys.argv[1]

    network_data = get_yaml(_YAML_FILE)
    host_macs = normalize_macs(network_data)
    # print(host_macs)
    sorted_macs = sort_macs(host_macs)
    print(sorted_macs)

if __name__ == '__main__':
    main()
