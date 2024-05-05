# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(U, L, C):
    # Implement your solution here
    u_rem = U
    l_rem = L

    result = [[0 for _ in range(len(C))] for _ in range(2)]
    for i, num in enumerate(C):
        if num == 2:
            result[0][i] = 1
            result[1][i] = 1
            u_rem -= 1
            l_rem -= 1
        if num == 1:
            if u_rem > l_rem:
                result[0][i] = 1
                u_rem -= 1
            else:
                result[1][i] = 1
                l_rem -= 1


