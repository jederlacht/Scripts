## python2
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
source = ET.parse('Settings.xml')
raw = ET.parse('strings.xml')
rawroot = raw.getroot()
srcroot = source.getroot()
src1 = ET.parse('phone.xml')
src1root = src1.getroot()
translated=0
for r in rawroot.getchildren():
	found=False
	for s in srcroot.getchildren():		
		if (r.attrib==s.attrib):
			found=True
			r.text=s.text
			translated+=1
	if (not found):
		for s in src1root.getchildren():
			if (r.attrib==s.attrib):
				r.text=s.text
				translated+=1
			

for r in rawroot.getchildren():
	print(r.text)			
print('translated:', translated)

raw.write('trans.xml','utf-8')
	
  
