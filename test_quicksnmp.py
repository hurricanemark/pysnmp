from pysnmp import hlapi
import quicksnmp 
from getpass import getpass

print('Welcome to quick SNMP access.  Enter Agent Info below.\n')
hostip = input('Host IP Address: ')
community = getpass('Community name: ')

# Using SNMPv2c, we set the hostname of the remote device to 'SNMPHost'
# NOTE: if your community name is set for rocommunity, then this next line 'set' will throw an exception
#quicksnmp.set(hostip, {'1.3.6.1.2.1.1.5.0': 'mySNMPAgent'}, hlapi.CommunityData(community))

# Using SNMPv2c, we retrieve the hostname of the remote device
print(quicksnmp.get(hostip, ['1.3.6.1.2.1.1.5.0'], hlapi.CommunityData(community)))

# We get interface name and Cisco interface description for all interfaces
# The last parameter is the OID containing the number of interfaces, so we can loop 'em all!
its = quicksnmp.get_bulk_auto(hostip, [
    '1.3.6.1.2.1.2.2.1.2 ',
    '1.3.6.1.2.1.31.1.1.1.18'
    ], hlapi.CommunityData(community), '1.3.6.1.2.1.2.1.0')
# We print the results in format OID=value
for it in its:
    for k, v in it.items():
        print("{0}={1}".format(k, v))
    # We leave a blank line between the output of each interface
    print('')
