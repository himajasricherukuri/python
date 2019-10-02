import csv
import array
import os

with open('/Users/himaja/Desktop/jg/file1.csv') as f:
    r = csv.reader(f, delimiter=',')
    dict1 = {row[0]: row[3] for row in r}

with open('/Users/himaja/Desktop/jg/file2.csv') as f:
    r = csv.reader(f, delimiter=',')
    #dict2 = {row[0]: row[r] for row in r}
    dict2 = {row[0]: row[3] for row in r}

print str(dict1)
print str(dict2)

keys = set(dict1.keys() + dict2.keys())
with open('Z:\\Desktop\\jg\\output.csv', 'wb') as f:
    w = csv.writer(f, delimiter=',')
    w.writerows([[key, dict1.get(key, "''"), dict2.get(key, "''")] for key in keys])