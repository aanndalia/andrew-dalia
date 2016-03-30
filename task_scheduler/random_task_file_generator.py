# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 23:03:57 2016

@author: stree_001
"""

from random import randint
from random import sample

def getYamlText():
    numTasks = randint(1,1000)
    taskNamesUsed = []
    maxParents = 100
    taskText = ""
    for taskId in range(numTasks):
        taskName = "task%d" % taskId
        taskText += "%s:\n" % taskName
        coresRequired = randint(1,10)
        taskText += "    cores_required: %d\n" % coresRequired
        executionTime = randint(10,1500)
        taskText += "    execution_time: %d\n" % executionTime
        hasParents = randint(0,1)

        if hasParents and taskId > 0:
            k = randint(1, min(len(taskNamesUsed), maxParents))
            parents = sample(taskNamesUsed, k)
            taskText += "    parent_tasks: %s\n" % (", ".join(parents))
        taskNamesUsed.append(taskName)
    return taskText
    

def writeRandomTaskYaml(outFileName):
    with open(outFileName, 'wb') as stream:
        stream.write(getYamlText())

def main():
    outFileName = "tasks102.yaml"
    writeRandomTaskYaml(outFileName)
    
main()