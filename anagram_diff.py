# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

def anagramDiff2(word):
    word = word.rstrip('\n')
    if not word:
        return -1
    
    if len(word) % 2 == 1:
        return -1 
    
    mid = len(word) / 2
    word1 = word[:mid]
    word2 = word[mid:]
    
    word1list = list(word1)
    word2list = list(word2)
    word1list.sort()
    word2list.sort()
    
    i1 = 0
    i2 = 0
    td = 0
    #ld = 0
    while i1 < mid and i2 < mid:
        if word1list[i1] == word2list[i2]:
            i1 += 1
            i2 += 1
        elif word1list[i1] < word2list[i2]:
            td += 1
            i1 += 1
        else:
            #td += 1
            i2 += 1
            
    while i1 < mid:
        td += 1
        i1 += 1
        
    while i2 < mid:
        #td += 1
        i2 += 1
        
    return td

def anagramDiff(word):
    word = word.rstrip('\n')
    if not word:
        return -1
    
    if len(word) % 2 == 1:
        return -1
    
    mid = len(word) / 2
    word1 = word[:mid]
    word2 = word[mid:]
    charToFreq = {}
    charToFreq2 = {}
    for c in word1:
        if c in charToFreq:
            charToFreq[c] += 1
        else:
            charToFreq[c] = 1
            
    for c in word2:
        if c in charToFreq2:
            charToFreq2[c] += 1
        else:
            charToFreq2[c] = 1
    
    print charToFreq
    print charToFreq2
    
    totalDiff = 0
    loners = 0
    for char, freq in charToFreq.iteritems():
        if char in charToFreq2:
            totalDiff += abs(charToFreq2[char] - freq)
        else:
            totalDiff += freq
        
    #for char, freq in charToFreq2.iteritems():
        #if char not in charToFreq:
            #totalDiff += freq
        
    #print charToFreq
    
    #totalDiff = 0
    #for char, freq in charToFreq.iteritems():
    #    totalDiff += abs(freq)
        
    return totalDiff

lines = []
for line in fileinput.input():
    lines.append(line)
    
N = lines[0]

for word in lines[1:]:
    print anagramDiff2(word)