configure
delete system services web-management
delete security policies from-zone trust to-zone trust
delete security policies from-zone untrust to-zone trust
delete security policies from-zone trust to-zone untrust
delete security zones security-zone untrust screen
delete security screen ids-option untrust-screen
delete security zones security-zone trust
delete security zones security-zone untrust
delete security
set system login user netconf class super-user authentication encrypted-password "$1$b1e7j6ek$4d/RrS9Zw/n6PrmyxKdN7."
set interfaces lo0.0 family inet address 10.11.12.2/32
set interfaces ge-0/0/1 unit 0 family mpls
set security zones security-zone vpn host-inbound-traffic system-services all
set security zones security-zone vpn host-inbound-traffic protocols all
set security zones security-zone vpn interfaces ge-0/0/3.0
set security policies from-zone trust to-zone trust policy all match source-address any
set security policies from-zone trust to-zone trust policy all match destination-address any
set security policies from-zone trust to-zone trust policy all match application any
set security policies from-zone trust to-zone trust policy all then permit
set security policies from-zone vpn to-zone trust policy all match source-address any
set security policies from-zone vpn to-zone trust policy all match destination-address any
set security policies from-zone vpn to-zone trust policy all match application any
set security policies from-zone vpn to-zone trust policy all then permit
set security policies from-zone trust to-zone vpn policy all match source-address any
set security policies from-zone trust to-zone vpn policy all match destination-address any
set security policies from-zone trust to-zone vpn policy all match application any
set security policies from-zone trust to-zone vpn policy all then permit
set security zones security-zone trust host-inbound-traffic system-services all
set security zones security-zone trust host-inbound-traffic protocols all
set security zones security-zone trust interfaces ge-0/0/1.0
set security zones security-zone trust interfaces lo0.0
set routing-options autonomous-system 65412
set protocols ospf area 0.0.0.0 interface ge-0/0/1.0
set protocols ospf area 0.0.0.0 interface lo0.0 passive
set protocols ldp interface ge-0/0/1.0
set protocols mpls interface ge-0/0/1.0
set protocols bgp group IBGP-MESH type internal
set protocols bgp group IBGP-MESH local-address 10.11.12.2
set protocols bgp group IBGP-MESH log-updown
set protocols bgp group IBGP-MESH family inet-vpn unicast
set protocols bgp group IBGP-MESH family inet unicast
set protocols bgp group IBGP-MESH neighbor 10.11.12.1
set protocols bgp group IBGP-MESH export EXPORT-DIRECT
set policy-options prefix-list R2-DIRECT 192.168.10.0/24
set policy-options policy-statement EXPORT-DIRECT term R2-DIRECT from protocol direct
set policy-options policy-statement EXPORT-DIRECT term R2-DIRECT from prefix-list R2-DIRECT
set policy-options policy-statement EXPORT-DIRECT term R2-DIRECT then accept
commit and-quit
