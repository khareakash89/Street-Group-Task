import csv
import json

csvfile = open('pp-monthly-update-new-version.csv', 'r')
jsonfile = open('pp-monthly-update-new-version.json', 'w')

reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile,indent=4)
    jsonfile.write('\n')