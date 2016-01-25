__author__ = 'vikram'

import csv
capitals = {}
with open('us-state-capitals.csv', mode='rt') as csv_file:
    reader = csv.DictReader(csv_file)
    print reader
    for row in reader:
        print row
        capitals[row['state']] = row['capital']
print capitals

capitals = {}
with open('us-state-capitals.csv', mode='rt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for