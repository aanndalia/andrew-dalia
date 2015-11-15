# Given an n x n square matrix, 
# find sum of all sub-squares of size k x k

def calc_inner_squares(n, k, arr):
    output = [[0 for _ in xrange(n-k+1)] for _ in xrange(n-k+1)]                                
    for i in range(0, n - k + 1):
        for j in range(0, n -k + 1):
            sum_square = 0
            for sub_i in range(i, i+k):
                for sub_j in range(j, j+k):
                    sum_square += arr[sub_i][sub_j]
                    output[i][j] = sum_square
    return output
    
def main():
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print calc_inner_squares(4, 2, arr)
    
main()
