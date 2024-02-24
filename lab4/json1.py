import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<40s} {:<20s} {:<10s} {:<6s}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for entry in data['imdata']:
    dn = entry['fvRsPathAtt']['attributes']['dn']
    description = entry['fvRsPathAtt']['attributes'].get('descr', '')
    speed = entry['fvRsPathAtt']['attributes'].get('speed', 'inherit')
    mtu = entry['fvRsPathAtt']['attributes'].get('mtu', '')
    print("{:<40s} {:<20s} {:<10s} {:<6s}".format(dn, description, speed, mtu))