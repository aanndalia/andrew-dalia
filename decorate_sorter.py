def decorateNums(fn):
    def check(nums):
        nums = fn(nums)
        outputNums = []
        for n in nums:
            #print "n", n
            if n[0] == "0":
                outputNums.append("+91" + " " + n[1:6] + " " + n[6:])
            else:
                if len(n) == 10:
                    outputNums.append("+91" + " " + n[0:5] + " " + n[5:])
                else:
                    outputNums.append("+91" + " " + n[2:7] + " " + n[7:])

        return outputNums
    return check

@decorateNums
def sortNums(nums):
    return sorted(nums)
    
def main():
    fileinput = ["3", "07895462130", "919875641230","9195969878"]
    lines = []
    for line in fileinput:
        lines.append(line)
    
    inputLines = lines[1:]
    outputLines = sortNums(inputLines)
    
    for outLine in outputLines:
        print outLine
        
main()
