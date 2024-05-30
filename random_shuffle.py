import random


def uniform_shuffle_with_randint(arr):
    for div in range(0, len(arr) - 1):
        rand_right = random.randint(div, len(arr) - 1)
        arr[div], arr[rand_right] = arr[rand_right], arr[div]


