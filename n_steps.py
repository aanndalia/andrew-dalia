import time

def nStepsCount(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    oneSteps = nStepsCount(n-1)
    twoSteps = nStepsCount(n-2)
    threeSteps = nStepsCount(n-3)
    
    totalSteps = oneSteps + twoSteps + threeSteps
    return totalSteps
    
def nStepsCountDP(n, cache):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    if n in cache:
        return cache[n]
        
    oneSteps = nStepsCountDP(n-1, cache)
    twoSteps = nStepsCountDP(n-2, cache)
    threeSteps = nStepsCountDP(n-3, cache)
    
    totalSteps = oneSteps + twoSteps + threeSteps
    cache[n] = totalSteps
    return totalSteps
    
def main():
    n = 27
    print "Non-DP solutions:"
    nonDpStart = time.time()
    for i in range(n):
        print i, nStepsCount(i)
    nonDpTime = time.time() - nonDpStart
    print "time taken:", nonDpTime    
    
    print "\nDP solutions:"
    dpStart = time.time()    
    for i in range(n):
        print i, nStepsCountDP(i, {})
    dpTime = time.time() - dpStart
    print "time taken:", dpTime
        
main()