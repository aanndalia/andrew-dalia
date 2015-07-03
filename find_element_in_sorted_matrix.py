# find element in row and column wise sorted dim * dim matrix
def find_matrix_element(element, dim, mat):
    # start at top right
    i = dim - 1
    j = 0
    while i >= 0 and j < dim:
        if mat[i][j] == element:
            return i, j
        elif mat[i][j] < element:
            # go down if less than element
            j += 1
        else:
            # go left if greater than element
            i -= 1
            
    return None

def main():
    dim = 4
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    
    print find_matrix_element(50, 4, mat)
    
main()