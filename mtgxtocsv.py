#! /usr/bin/python
# This script can be used to generate a CSV file from the mtgx file. A mtgx file is a file created by saving the Maltego graph.
# Currently it only extracts the entities and not the details of the edges.
from BeautifulSoup import BeautifulSoup
import csv
import zipfile
import sys
file=sys.argv[1]
zp=zipfile.ZipFile(file)
path=str(zp.namelist()[0])
data=zp.read(path)
xmlbs=BeautifulSoup(data)
psxml=xmlbs.graph.findAll("node")
entity=[]
entvalue=[]
outcsv=open('maltegoop.csv', 'wb')
csvwriter = csv.writer(outcsv)
for node in psxml:
  ent=node.findAll("mtg:maltegoentity")[0]["type"]
  entity.append(ent)
  nod=node.findAll("mtg:value")[0].contents
  for nd in nod:
    entvalue.append(nd)
for val in (entity, entvalue):
    csvwriter.writerow(val)
outcsv.close()
