import time

class Timer(object):    
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

def isPalindrome(s):
    length = len(s)
    if length < 2:
        return True
        
    for i in range(length/2):
        if s[i] != s[length-1-i]:
            return False
    return True
    
def minPalindromePartitions(s):
    if isPalindrome(s):
        return 0
    
    length = len(s)
    absoluteMinPartitions = length
    for k in range(length-1):
        minLeftPartitions = minPalindromePartitions(s[0:k+1])
        minRightPartitions = minPalindromePartitions(s[k+1:length])
        minPartitionsAtK = minLeftPartitions + minRightPartitions + 1
        absoluteMinPartitions = min(minPartitionsAtK, absoluteMinPartitions)
    return absoluteMinPartitions
    
def minPalindromePartitionsDynamic(s, cache):
    if s in cache:
        return cache[s]
        
    if isPalindrome(s):
        return 0
    
    length = len(s)
    absoluteMinPartitions = length
    for k in range(length-1):
        leftString = s[0:k+1]
        rightString = s[k+1:length]
        minLeftPartitions = minPalindromePartitionsDynamic(leftString, cache)
        minRightPartitions = minPalindromePartitionsDynamic(rightString, cache)
        minPartitionsAtK = minLeftPartitions + minRightPartitions + 1
        absoluteMinPartitions = min(minPartitionsAtK, absoluteMinPartitions)
    cache[s] = absoluteMinPartitions
    return absoluteMinPartitions
    
def main():
    s = 'ababbbabbababa'
    print isPalindrome(s)
    
    with Timer() as t1:
        print minPalindromePartitions(s)
        
    with Timer() as t2:
        print minPalindromePartitionsDynamic(s, {})
        
    print 'Non dynamic palindrome partition took %.03f sec.\nDynamic palindrome partition took %.03f sec' % (t1.interval, t2.interval)