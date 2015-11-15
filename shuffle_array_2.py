import random

def shuffler(arr):
    for idx in range(len(arr) - 1):
        random_pos = random.randint(idx+1, len(arr) - 1)
        temp = arr[idx]
        arr[idx] = arr[random_pos]
        arr[random_pos] = temp
    return arr

def main():
    arr = [1,4,6,7,8,13,17,19,21,22,29,101]
    print shuffler(arr)
    
main()