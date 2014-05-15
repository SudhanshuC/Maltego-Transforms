#! /usr/bin/python
# This script can be used to generate a CSV file from the mtgx file. A mtgx file is a file created by saving the Maltego graph.
# It extracts the entities, their type and entity parent(s).
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
key=xmlbs.findAll("key")
edge=xmlbs.findAll("edge")
xkey=""
el=[]
edgelink=["Entity Parent(s)"]
entity=["Entity Type"]
entvalue=["Entity Value"]
link=["Entity ID"]
lnk=""
file=file.split('.')
opfilename=file[0]+".csv"
outcsv=open(opfilename, 'wb')
csvwriter = csv.writer(outcsv)
print ""

for k in key:
  if (k["for"]=="edge"):
    if (k["attr.name"]=="MaltegoLink"):
	 xkey=k["id"]
	 break
  	 
for node in psxml:
  lnk=node["id"]
  link.append(lnk)
  for ed in edge:
    if ed["target"]==lnk:
	  el.append(str(ed["source"]))
  edgelink.append(el)
  el=[]  
  ent=node.findAll("mtg:maltegoentity")[0]["type"]
  entity.append(ent)
  nod=node.findAll("mtg:value")[0].contents
  for nd in nod:
    entvalue.append(nd)
	
for val in (link, entity, entvalue, edgelink):
    csvwriter.writerow(val)
outcsv.close()
