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

unsorted = [77, 33, 35, 12, 98, 2] 

print(unsorted)



