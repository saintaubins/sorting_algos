import random
import time

def display_it(arr):
    # space in-between each iteration
    print('\n' * 5)
    for row in arr:
        print('$' * row)
    time.sleep(2)

def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        display_it(arr)
        arr[pos] = cursor

arr1 = [random.randrange(1,50) for i in range(1, 20)]
print(arr1)
insertion_sort(arr1)
print(arr1)