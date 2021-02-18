from csv import DictReader
from itertools import groupby
from pprint import pprint
import json

with open('pp-monthly-update-new-version_1.csv') as csvfile:
    r = DictReader(csvfile, skipinitialspace=True)
    data = [dict(d) for d in r]

    groups = []
    uniquekeys = []

    for k, g in groupby(data, lambda r: (r['PAON'], r['SAON'],r['Street'],r['Locality'],r['Town/City'],r['District'],r['County'],r['Postcode'],r['Property Type'])):
        groups.append({
            "PAON": k[0],
            "SAON": k[1],
            "Street": k[2],
            "Locality": k[3],
            "Town/City": k[4],
            "District": k[5],
            "County": k[6],
            "Postcode": k[7],
            "Property Type": k[8],
            "Transactions": [{k:v for k, v in d.items() if k not in ['PAON','SAON','Street','Locality','Town/City','District','County','Postcode','Property Type']} for d in list(g)]
        })
        uniquekeys.append(k)

#pprint(groups)

jsonfile = open('pp-monthly-update-new-version_1.json', 'w')

for row in groups:
    json.dump(row, jsonfile,indent=4)
    jsonfile.write('\n')