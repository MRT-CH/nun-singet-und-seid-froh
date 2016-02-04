# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:34:46 2016

@author: jonathan_scholbach
"""

# this script extracts information from a  from a meta.ily formatted
# corresponding to the nun-singet-und-seid-froh standard and writes it into
# a text file that describes a well-formatted MediaWiki infobox

# script needs to be called with the path of the meta.ily as paramater

import sys
import os
import re

#get the path of the meta.ily as first argument of call
if not(len(sys.argv) == 1):
  path = str(sys.argv[1])
else:
  print "error: No path given."

filename = os.path.join(path,'meta.ily')
print "processing " + filename

with open(filename,'r') as f: 
  meta = f.read() 


#reading

composerPrename = re.search('composerPrename.*?=.*?"(.*?)"', meta, flags=0)
if composerPrename:
  composerPrename = composerPrename.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no composerPrename found!"
  
composerSurname = re.search('composerSurname.*?=.*?"(.*?)"', meta, flags=0)
if composerSurname:
  composerSurname = composerSurname.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no composerSurname found!"

arrangerPrename = re.search('arrangerPrename.*?=.*?"(.*?)"', meta, flags=0)
if arrangerPrename:
  arrangerPrename = arrangerPrename.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no arrangerPrename found!"
  
arrangerSurname = re.search('arrangerSurname.*?=.*?"(.*?)"', meta, flags=0)
if arrangerSurname:
  arrangerSurname = arrangerSurname.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no arrangerSurname found!"

poetPrename = re.search('poetPrename.*?=.*?"(.*?)"', meta, flags=0)
if poetPrename:
  poetPrename = poetPrename.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no poetPrename found!"
  
poetSurname = re.search('poetSurname.*?=.*?"(.*?)"', meta, flags=0)
if poetSurname:
  poetSurname = poetSurname.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no poetSurname found!"

opus = re.search('opus.*?=.*?"(.*?)"', meta, flags=0)
if opus:
  opus = opus.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no opus found!"
  
epoque = re.search('epoque.*?=.*?"(.*?)"', meta, flags=0)
if epoque:
  epoque = epoque.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no epoque found!"
  
language = re.search('language.*?=.*?"(.*?)"', meta, flags=0)
if language:
  language = language.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no language found!"  
  
instrumentation = re.search('instrumentation.*?=.*?"(.*?)"', meta, flags=0)
if instrumentation:
  instrumentation = instrumentation.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no instrumentation found!"

difficulty = re.search('difficulty.*?=.*?"(.*?)"', meta, flags=0)
if difficulty:
  difficulty = difficulty.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no difficulty found!"

form = re.search('form.*?=.*?"(.*?)"', meta, flags=0)
if form:
  form = form.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no form found!"

root = re.search('root.*?=.*?"(.*?)"', meta, flags=0)
if root:
  root = root.group(1) 
else:
  print "error: "+ path + " is not well-formatted - no root found!"
  
# writing

categories = '' #the string calling the categories of the piece
labels = []
data = []

m = open(os.path.join(path, 'mediawiki.txt'),'w')
print 'writing ' + os.path.join(path, 'mediawiki.txt') + ' ...'

#creating the infobox
if not(composerSurname == ""):
  if not(composerPrename == ""):    
    categories = categories + '[[Category: ' + composerSurname + ', ' + composerPrename + ']] '
    labels.append("Komponist")
    data.append(composerSurname + ', ' + composerPrename)
  else:
    categories = categories + '[[Category: ' + composerSurname + ']] '
    labels.append("Komponist")
    data.append(composerSurname + '')

if not(arrangerSurname == ""):
  if not(arrangerPrename == ""):    
    categories = categories + '[[Category: ' + arrangerSurname + ', ' + arrangerPrename + ']] '
    labels.append("Arrangeur")
    data.append(arrangerSurname + ', ' + arrangerPrename)
  else:
    categories = categories + '[[Category: ' + arrangerSurname + ']] '
    labels.append("Arrangeur")
    data.append(arrangerSurname)

if not(poetSurname == ""):
  if not(poetPrename == ""):    
    categories = categories + '[[Category: ' + poetSurname + ', ' + poetPrename + ']] '
    labels.append("Dichter")
    data.append(poetSurname + ', ' + poetPrename)
  else:
    categories = categories + '[[Category: ' + poetSurname + ']] '
    labels.append("Dichter")
    data.append(poetSurname)

if not(root == ""):
  categories = categories + '[[Category: ' + root + ']] '
  labels.append("Wurzel")
  data.append(root)

if not(opus == ""):
  categories = categories + '[[Category: ' + opus + ']] '
  labels.append("Opus")
  data.append(opus)

if not(language == ""):
  categories = categories + '[[Category: ' + language + ']] '
  labels.append("Sprache")
  data.append(language)
  
if not(instrumentation== ""):
  categories = categories + '[[Category: ' + instrumentation + ']] '
  labels.append("Besetzung")
  data.append(instrumentation)
    
if not(epoque == ""):
  categories = categories + '[[Category: ' + epoque + ']] '
  labels.append("Epoche")
  data.append(epoque)
  
if not(form == ""):
  categories = categories + '[[Category: ' + form + ']] '
  labels.append("Typ")
  data.append(form)

if not(difficulty == ""):
  categories = categories + '[[Category: ' + difficulty + ']] '
  labels.append("Schwierigkeitsgrad")
  data.append(difficulty)
  


m.write('{{Infobox\n')
for i in range(0,len(labels)):
  m.write('|label' + str(i+1) + ' = ' + labels[i] + '\n')
m.write('\n')
for i in range(0,len(data)):
  m.write('|data' + str(i+1) + ' = [[:Category: ' + data[i] + ']]\n')
m.write('}}\n\n')

m.write(categories)