from random import randint
import time
    
def knapSack(weightCapacityLeft, itemWeights, itemValues, numItemsLeft):
    if not itemWeights or not itemValues or not numItemsLeft:
        return 0
        
    if len(itemWeights) != len(itemValues):
        print "There are an unequal number of item weights and values"
        return 0
        
    if weightCapacityLeft <= 0:
        return 0
    
    leaveLastItem = knapSack(weightCapacityLeft, itemWeights, itemValues, numItemsLeft - 1)
    if weightCapacityLeft - itemWeights[numItemsLeft - 1] < 0:
        return leaveLastItem
        
    takeLastItem = itemValues[numItemsLeft - 1] + knapSack(weightCapacityLeft - itemWeights[numItemsLeft - 1], itemWeights, itemValues, numItemsLeft - 1)     
    
    return max(takeLastItem, leaveLastItem)
    
def knapSackDP(weightCapacityLeft, itemWeights, itemValues, numItemsLeft, cache={}):
    if not itemWeights or not itemValues or not numItemsLeft:
        return 0
        
    if len(itemWeights) != len(itemValues):
        print "There are an unequal number of item weights and values"
        return 0
        
    if weightCapacityLeft <= 0:
        return 0
    
    if (weightCapacityLeft, numItemsLeft) in cache:
        return cache[(weightCapacityLeft, numItemsLeft)]
    
    leaveLastItem = knapSackDP(weightCapacityLeft, itemWeights, itemValues, numItemsLeft - 1, cache)
    if weightCapacityLeft - itemWeights[numItemsLeft - 1] < 0:
        cache[(weightCapacityLeft, numItemsLeft)] = leaveLastItem
        return leaveLastItem
        
    takeLastItem = itemValues[numItemsLeft - 1] + knapSackDP(weightCapacityLeft - itemWeights[numItemsLeft - 1], itemWeights, itemValues, numItemsLeft - 1, cache)     
    
    res = max(takeLastItem, leaveLastItem)
    cache[(weightCapacityLeft, numItemsLeft)] = res
    return res
        

def main():
    n = 40
    print "num items: %d" % n
    itemValues = [randint(10,150) for _ in xrange(n)]
    print "values: %s" % str(itemValues)
    itemWeights = [randint(5,50) for _ in xrange(n)]
    print "values: %s" % str(itemWeights)
    weightCapacity = randint(50, 120)
    print "weight capacity: %d" % weightCapacity
    
    start = time.time()
    print knapSack(weightCapacity, itemWeights, itemValues, len(itemWeights))
    end = time.time()
    print "non dp took %s secs" % str(end-start)
    
    start = time.time()
    print knapSackDP(weightCapacity, itemWeights, itemValues, len(itemWeights))
    end = time.time()
    print "dp took %s secs" % str(end-start)
    
main()