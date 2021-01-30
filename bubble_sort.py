import random
import time

def display_list(lst):
    # space in-between the iterations
    print('\n' * 5)
    for rows_view in lst:
        print('@' * rows_view)
    time.sleep(2)
    #raw_input('')

def bubble_sort(lst):
    # this happens from the back ot the array
    for passesLeft in range(len(lst) - 1, 0, -1):
        for index in range(passesLeft):
            if lst[index] < lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
        display_list(lst)
    return lst

lst1 = [random.randrange(1, 50) for i in range(1, 20)]
print(lst1)
#raw_input("")
bubble_sort(lst1)
print(lst1)