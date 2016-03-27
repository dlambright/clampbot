import urllib2
import re
import json
import copy



def getImages(internetPath):
  links=urllib2.urlopen("http://www.imgur.com/r/dankmemes").read()

  found = re.findall("//i.imgur.com/\w+.(?:jpg|gif|png)", links)

  toWrite = copy.deepcopy(found)

  for i in range(0,len(found)):
    toWrite[i] = "http:" + found[i]


  with open(internetPath + ".clampbot", 'w') as outfile:
    json.dump(toWrite, outfile)

  #print len(found)
  #print found

getImages("dankmemes")
getImages("aww")
getImages("birdswitharms")
