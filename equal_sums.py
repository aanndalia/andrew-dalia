A = [3,4,7,1,2,9,8]

sums = {}
for i in range(len(A)):
    for j in range(i+1, len(A)):
        add = A[i] + A[j]
        if add not in sums:
            sums[add] = (i,j)
        elif sums[add] != (i,j):
            print (sums[add][0], sums[add][1], i, j)