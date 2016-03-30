# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 23:03:57 2016

@author: stree_001
"""

from random import randint
from random import sample

def getYamlText():
    numComputes = randint(1,20)
    computeText = ""
    for idx in range(numComputes):
        computeName = "compute%d" % idx
        computeText += "%s: %d\n" % (computeName, randint(1,16))
    return computeText
    

def writeRandomComputesYaml(outFileName):
    with open(outFileName, 'wb') as stream:
        stream.write(getYamlText())

def main():
    outFileName = "computes102.yaml"
    writeRandomComputesYaml(outFileName)
    
main()