# -*- coding: utf-8 -*-
"""
Uber ATC task scheduling assignment

The program generates a process schedule for a set of tasks running against
a heterogeneous cluster of computers.

This program will take a file containing tasks to run and a file containing
computers that can process these tasks as input. The output will be the 
schedule that tasks are processed in.  

@author: Andrew Dalia
"""

import yaml
import argparse
from collections import defaultdict
from sortedcontainers import SortedSet

def enum(**enums):
    return type('Enum', (), enums)

class Task(object):
    def __init__(self, taskName, executionTime, coresNeeded, parents=[]):
        self.taskName = taskName
        self.executionTime = executionTime
        self.coresNeeded = coresNeeded
        self.timeLeft = executionTime
        self.compName = None
        self.parents = set(parents)
        self.parentsLeft = set(self.parents)
        
class Computer(object):
    def __init__(self, computeName, numCores):
        self.computeName = computeName
        self.numCores = numCores
        self.availableCores = numCores

class Scheduler(object):
    
    def __init__(self, tasksDict, computesDict):                     
        self.schedule = []
        self.taskMap = self.populateTaskMap(tasksDict)
        self.computerMap = self.populateComputerMap(computesDict)
        self.dependentsMap = self.populateDependentsMap()
        self.numCompletedTasks = 0
        
        # maintain ready tasks in order of how many dependents they have
        # using a custom keyed SortedSet and populate initially with all 
        # tasks that have have no parents
        initialReadyTasks = set([task.taskName for task in self.taskMap.values() if not len(task.parentsLeft)]) 
        self.readyTasks = SortedSet(iterable = initialReadyTasks, key = lambda parent: len(self.dependentsMap[parent]) if parent in self.dependentsMap else 0)
        
        # contains all running tasks
        self.runningTasks = set()
        
    def populateTaskMap(self, tasksDict):
        """
        Populates the task map of task name to Task given initial dictionary
        loaded from the tasks file
        
        :param tasksDict: tasks dictionary loaded from file
        :type tasksDict: dict
        
        :rtype: dict
        """
        taskMap = {}
        for taskName, taskDict in tasksDict.iteritems():
            parentTasks = taskDict['parent_tasks'].split(', ') if 'parent_tasks' in taskDict else []
            taskMap[taskName] = Task(taskName, taskDict['execution_time'], taskDict['cores_required'], parentTasks)
        return taskMap
            
    def populateComputerMap(self, computesDict):
        """
        Populates the computer map of computer name to Computer given initial 
        dictionary loaded from the computer file
        
        :param computesDict: tasks dictionary loaded from file
        :type computesDict: dict
        
        :rtype: dict
        """
        computerMap = {}
        for computerName, numCores in computesDict.iteritems():
            computerMap[computerName] = Computer(computerName, numCores)
        return computerMap
            
    def populateDependentsMap(self):
        """
        Populates the dependents map of the parent task to dependent tasks 
        given
        
        :param tasksDict: tasks dictionary loaded from file
        :type tasksDict: dict
        
        :rtype: dict
        """
        dependentsMap = defaultdict(set)
        for taskName, task in self.taskMap.iteritems():
            for parent in task.parents:
                dependentsMap[parent].add(taskName)
        return dependentsMap
    
    def checkTasksAgainstComputers(self):
        """
        Performs a sanity check by comparing if the most expensive task in terms
        of needed cores can run on the available resources.
        
        :rtype: bool
        """
        mostCoreComputer = max(self.computerMap.values(), key = lambda comp: comp.numCores)
        mostCoreTask = max(self.taskMap.values(), key = lambda tsk : tsk.coresNeeded)
        if mostCoreTask.coresNeeded > mostCoreComputer.numCores:
            print "Impossible to schedule since at least one task uses more cores than the most powerful computer has"
            return False
        else:
            return True    
    
    def _addTaskToSchedule(self, taskName, computerName, timeStep):
        """
        Adds the given task on the given computer to the schedule
        
        :param taskName: the task name
        :type taskName: str
        :param computerName: the computer name
        :type computerName: str
        :param timeStep: the time step of the overall execution
        :type timeStep: int
        """
        endTime = timeStep + self.taskMap[taskName].executionTime
        coresFormat = "%d/%d" % (self.computerMap[computerName].availableCores, self.computerMap[computerName].numCores)
        addToSchedule = (timeStep, endTime, taskName, computerName, coresFormat)
        self.schedule.append(addToSchedule)
    
    def _handleReadyTasks(self, timeStep):
        """
        Ready tasks are those in queue waiting for a computer with enough
        available cores to pick it up. If there are no computers with enough
        cores it will have to wait. A task that does get picked up by a 
        computer will put in RUNNING state.
        """
        
        # will contain the tasks to promote to RUNNING status
        readyTasksToRemove = set() 
        
        # has a map with key being the number of cores available and value the
        # set of computers that have this amount of available cores. This is
        # used to match a task against the best possible computer        
        coresAvailableToComputer = defaultdict(set)
        for compName, computer in self.computerMap.iteritems():
            coresAvailableToComputer[computer.availableCores].add(compName)
            
        # The RUNNING tasks are already ordered by the number of dependents they have 
        # since they are in a SortedSet.
        # If we traverse this from most to least dependents (reverse), then this will
        # minimize the time tasks with lots of dependencies spend in the WAITING state
        for taskName in reversed(self.readyTasks):
            maxCores = max(coresAvailableToComputer.keys())
            if self.taskMap[taskName].coresNeeded > maxCores:
                # move on if given task requires more cores than the max available 
                continue
            
            # A task needs to be processed by a computer that has at least
            # as many cores available as the task requires. Find a computer
            # that has more but as close to the number of available cores as
            # the task needs to best utilize computing resources
            lowestSatisfyingCores = self.taskMap[taskName].coresNeeded
            while lowestSatisfyingCores not in coresAvailableToComputer:             
                lowestSatisfyingCores += 1
            processingCompName = coresAvailableToComputer[lowestSatisfyingCores].pop()
            if not len(coresAvailableToComputer[lowestSatisfyingCores]):
                del coresAvailableToComputer[lowestSatisfyingCores]
                
            # adjust the computing resources available appropriately, mark the 
            # task as RUNNING
            reducedAvailableCores = self.computerMap[processingCompName].availableCores - self.taskMap[taskName].coresNeeded
            self.computerMap[processingCompName].availableCores = reducedAvailableCores
            coresAvailableToComputer[reducedAvailableCores].add(processingCompName)
            self.taskMap[taskName].compName = processingCompName
            self.runningTasks.add(taskName)
            readyTasksToRemove.add(taskName)
            
            # add newly running task to schedule
            self._addTaskToSchedule(taskName, processingCompName, timeStep)
        
        # remove the RUNNING tasks from READY status        
        self.readyTasks -= readyTasksToRemove
    
    def _handleRunningTasks(self):
        """
        Running tasks are execution for their executionTime on a computer
        till completion. If they are not completing their time left to process
        will be decremented. If they are completing, then they are put in
        DONE status.
        """
        
        # contains the tasks to be promoted to DONE status
        runningTasksToRemove = set()
        
        for taskName in self.runningTasks:
            if self.taskMap[taskName].timeLeft == 0:
                # if RUNNING task is done, mark them as DONE and adjust the 
                # tasks' parents and children appropriately. Also free the 
                # computing resources it took
                self.numCompletedTasks += 1
                if taskName in self.dependentsMap:
                    for dependentName in self.dependentsMap[taskName]:
                        self.taskMap[dependentName].parentsLeft.discard(taskName)
                        # if task has no more incomplete parents, flag it to 
                        # be marked as ready
                        if not len(self.taskMap[dependentName].parentsLeft):
                            self.readyTasks.add(dependentName)
                    del self.dependentsMap[taskName]
                self.computerMap[self.taskMap[taskName].compName].availableCores += self.taskMap[taskName].coresNeeded                               
                runningTasksToRemove.add(taskName)
            else:
                self.taskMap[taskName].timeLeft -= 1
        
        # remove the DONE tasks from RUNNING status
        self.runningTasks -= runningTasksToRemove
    
    def scheduleTasks(self):
        """
        Schedule the tasks in time series by handling all possible states
        across time
        """
        
        # Sanity check to make sure the tasks should be schedulable
        if self.checkTasksAgainstComputers() == False:
            return
        
        # Check if all tasks are in DONE status throughout the execution
        timeStep = 0
        while self.numCompletedTasks < len(self.taskMap):
            
            ### Handle READY Tasks
            self._handleReadyTasks(timeStep)            
            
            ### Handle RUNNING Tasks
            self._handleRunningTasks()
            
            # increment time step
            timeStep += 1

    def printTimedSchedule(self):
        """
        Prints the schedule with the start time, end time, task, computer,
        and number of cores available of the total in a computer at the 
        time of execution.
        """
        print "\nTimed Schedule:"
        print "Start\tEnd\tTask\tComputer\tCores\n"
        for tup in self.schedule:
            print '%d\t%d\t%s\t%s\t%s' % tup
            
    def printFormatSchedule(self):
        """
        Prints a simple schedule with task to computer pairs
        """
        print "\nFormat Schedule:"
        for tup in self.schedule:
            print "%s: %s" % (tup[2], tup[3])

def getDictionaryFromYaml(fileName):
    """
    Reads the data from a yaml file as a dictionary
    
    :param fileName: the yaml file name to read and load
    :type fileName: str
    
    :rtype: dict
    """
    with open(fileName, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print exc
            return
        except IOError as ioExc:
            print ioExc
            return

def getArgs():
    """
    Parses and gets all the arguments passed in by command line using argparse.
    Comes with information to display a help menu.

    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Task Scheduler on a Heterogeneous Computing Cluster')
    parser.add_argument('-t', help='The tasks yaml file to load', action='store', dest='tasks', default='tasks.yaml')
    parser.add_argument('-c', help='The computers yaml file to load', action='store', dest='computers', default='computers.yaml')
    args = parser.parse_args()
    return args
        
def main():
    inputArgs = getArgs()
    tasksFile = inputArgs.tasks
    computersFile = inputArgs.computers
    tasksDict = getDictionaryFromYaml(tasksFile)
    computesDict = getDictionaryFromYaml(computersFile)
    if not tasksDict or not computesDict:
        print "There was an error in getting data from the tasks or computes - cannot continue"
        return
    
    scheduler = Scheduler(tasksDict, computesDict)
    scheduler.scheduleTasks()
    #scheduler.printTimedSchedule()
    scheduler.printFormatSchedule()
    
    
main()
        