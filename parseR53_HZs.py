#!/usr/bin/env python

import json

filename = "AWSR53_hostedzones_mainacct.json"
fh = open(filename, "r")
data = json.loads(fh.read())

# print(len(data['HostedZones']))

for hzones in data['HostedZones']:
    rrs_count = hzones['ResourceRecordSetCount']
    hz_id = hzones['Id']
    hz_name = hzones['Name']
    hz_config = hzones['Config']
    hz_privatezone = hzones['Config']['PrivateZone']
    if 'Comment' in hz_config:
        hz_comment = hz_config['Comment']
    else:
        hz_comment = ''
    print("{}\t{}\t{}\t{}\t{}".format(hz_name,hz_privatezone,hz_comment,hz_id,rrs_count))

