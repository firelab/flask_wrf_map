#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:21:59 2017

@author: tanner
"""

import glob
#
#pngDir='/home/tanner/src/cloneKML/kml/'
#pathDir='/home/tanner/src/cloneKML/kml/'
#writeDir='/home/tanner/src/cloneKML/kml/'

pathDir='/ninja/wrfSim/temperature_kml/'
pngDir='/home/ubuntu/ninjaInput/wrfSim/temperature_kml/'
writeDir=pngDir

kZ=glob.glob(pngDir+'*.png')
xZ=glob.glob(pngDir+'*.kml')

for i in range(len(kZ)):
    if kZ[i].find('legend')>-1:
        print True,i
        kZ.pop(i)
        break
kZ.sort()

baseFiles=[]

for i in range(len(kZ)):
    baseFiles.append(kZ[i][-11:])

for i in range(len(baseFiles)):
    if baseFiles[i]=='ayer.10.png':
        baseFiles[i]='layer.10.png'

pathFiles=[]
kmlFiles=[]
#CreatePathDirs
for i in range(len(baseFiles)):
    pathFiles.append(pathDir+baseFiles[i])
    kmlFiles.append(writeDir+baseFiles[i][:-3]+'kml')


coords=[47.63107,46.90489,-112.97979,-113.99359]

def createLatLonBox(coords):
    north="<north>"+str(coords[0])+"</north>\n"
    south="<south>"+str(coords[1])+"</south>\n"
    east="<east>"+str(coords[2])+"</east>\n"
    west="<west>"+str(coords[3])+"</west>\n"
    return north+south+east+west





kmlHead="""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<GroundOverlay>
<name>layer</name>
<Icon>
<href>"""
kmlMid="""</href>
<viewBoundScale>0.75</viewBoundScale>
</Icon>
<LatLonBox>\n"""

kmlEnd="""</LatLonBox>
</GroundOverlay>
</kml>"""

for i in range(len(pathFiles)):
    kmlFile=kmlHead+pathFiles[i]+kmlMid+createLatLonBox(coords)+kmlEnd
    fout=open(kmlFiles[i],'w')
    fout.write(kmlFile)
    fout.close()
#    kmlFiles.append(kmlFile)
