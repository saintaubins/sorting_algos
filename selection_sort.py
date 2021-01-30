import random
import time

def display_arr(arr):
    # space in-between the iterations
    print('\n' * 5)
    for rows_view in arr:
        print('*' * rows_view)
    time.sleep(2)


def selection_sort(arr):
    # this happens from the front of the array        
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j
        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
        display_arr(arr)

arr1 = [random.randrange(1,50) for i in range(1, 20)]
print(arr1)
selection_sort(arr1)
print(arr1)