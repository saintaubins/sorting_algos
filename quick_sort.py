import random 
import time

def display_arr(arr):
    # space in-between the iterations
    print('\n' * 5)
    for rows_view in arr:
        print('*' * rows_view)
    time.sleep(2)

def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    print('from partition\n')
    display_arr(array)
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)
    print('from quick sort recursion\n')
    display_arr(array)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    print('from quick sort\n')
    display_arr(array)
    return quick_sort_recursion(array, begin, end)

arr1 = [random.randrange(1,50) for i in range(1, 20)]
print(arr1)
quick_sort(arr1)
print(arr1)