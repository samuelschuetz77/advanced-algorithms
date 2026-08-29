# Name: Samuel Schuetz
# Course: Advanced Algorithms
# Date: 8/27/2026 - 9/03/2027

import random
import time

import pandas as pd
import pytest


# python refresher

nums = [1,2,3,4,7,6,5,8,9]

# sub_of_nums = nums[1:5]  # ends at '7'  because: start-included, end-excluded e.g called half-open slice ends at '5'

# print(sub_of_nums)


# Prints 2, 4, 6, 8 (Starts at 2, stops before 10, counts by 2) this is similar to a classic forloop 
# for i in range(2, 10, 2):
#     print(i) 

# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index {index} is {fruit}")


# --- useful tools ---
# range(1, len(nums))          - start at index 1; a 1-element list is already sorted
# while loop counting backward - inner shift loop isn't a clean for-loop
# nums[j], nums[j+1] = nums[j+1], nums[j]  - tuple swap, no temp variable needed
# nums[:] or list(nums)        - copy a list to keep the original unsorted version
# time.time()                  - benchmark sorted vs reverse-sorted vs random input
# random.shuffle(nums)         - generate randomized test cases



# --- insertion sort ----
# plan of attack
#               start at i = 1, progressivly build a snake subarray/sublist if you encounter an i that is less than any number in the sublist insert it in the position it would go.   

unsorted = [77, 33, 35, 12, 98, 2] 

#print(unsorted[0:1])


def insertion_sort(list):
    for i in range(1,len(list),1):   
        sub = list[0:i+1]    # 1: [77, 33]    2: [33, 77, 35] 3: [33, 35, 77, 12] 4: [12,33,35,77, 98]
        for j in range(0, i+1, 1):  # e.g j = 0, j = 1   2: j 0,1,2  3: j 0,1,2,3    4: 0,1,2,3,4 
            if list[j] > list[i]: # if 77 > 33   2: if 33 > 35 nope 3: if 77 > 33 yes  4: if 33 > 12 yes 5: x > 98 no no no no 
                # wrong: list[j], list[i] = list[i], list[j]  # 1:[33 <swapped> 77, 35, 12,98 etc] 2:[ 33, 35, 77, 12, 98,2] 3: [12,33,35,77,98,2]
                temp = list[i]
                for q in range(i, j, -1):
                    value_moving = list[q-1]
                    erased = list[q]
                    list[q] = list[q-1]
                    # og [77, 33, 35, 12, 98, 2] 
                list[j] = temp
                break
    return list


print(insertion_sort(unsorted))
print()
print()





