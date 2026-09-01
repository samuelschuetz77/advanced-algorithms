# Name: Samuel Schuetz
# Course: Advanced Algorithms
# Date: 8/27/2026 - 9/03/2027

import random
import time
import pytest
import pandas as pd
import itertools
import statistics

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
# start at i = 1, progressivly build a subarray/sublist if you encounter an i that is less than any number in the sublist insert it in the position it would go.   

unsorted = [77, 33, 12, 35, 98, 2] 

#print(unsorted[0:1])

# evolved implementation (optimal solution)
def insertion_sort(lst):
    if not lst:
        return []
    for i in range(1,len(lst),1):   
        temp = lst[i]
        for j in range(i-1, -1, -1): 
            if lst[j] > temp: 
                lst[j+1] = lst[j]
                lst[j] = temp
            else:
                break
    return lst


# selection sort

def selection_sort(lst):
    for i in range(0, len(lst)-1, 1):
        a = lst[i]
        b = min(lst[i+1:])
        if a > b:
            #swap
            lst[i], lst[lst.index(b)] = lst[lst.index(b)] , lst[i]
        else:
            break
    return lst




# you have the list: [7, 8, 3, 1, 12, 8, 8, 3]
# counting sort main idea:
# Store the frequency of each number from the original array at its corresponding index in a new "count array":
# [0, 1, 0, 2, 0, 0, 0, 1, 3, 0, 0, 0, 1] is this count array notice at index 8 we store 3, because 8 occurs 3 times in the original array

def counting_sort(lst):     # O(n+k) where k is length of count_array 
    if not(lst):
        return []
    # make count_array:
    max_num = max(lst)
    counts = [0] * (max_num + 1)
    for num in lst: 
        counts[num]+=1  
    # return list of nums:
    lst2 = []
    for i in range(0, max_num + 1, 1):
       lst2 += [i] * counts[i]
    return lst2


def reverse_sorted(lst): 
    sorted(lst, reverse=True)
    return lst

def unchanged(lst):
    return lst

print(insertion_sort(unsorted))
print()
print()
print(selection_sort(unsorted))
print()
print()
print(counting_sort(unsorted))


# --- Part 1 -----

sorts = [insertion_sort, selection_sort, counting_sort]

# 
# 
@pytest.mark.parametrize("original",[
[],
[1],
[1,2,3],
[44, 22, 11, 12, 11, 562],
[1, 2, 3 , 4, 5, 6, 7],
[1, 2, 3, 7, 6, 7, 6, 7, 6, 9],
[64, 12, 9, 37, 36, 5, 11, 66, 8]
])
def test_all(original):
    for sort in sorts:
        a = list(original) #make copy
        sort(a)
        assert a == sorted(original), f"failed to sort {original} with {sort.__name__}."

def time_sort(original, prep, sort):
   a = prep(list(original))
   start = time.perf_counter()
   sort(a)
   end = time.perf_counter() 
   return end - start

def aggregated_time_sort(lists, length, prep, sort, repetitions, timeout):
    return statistics.median(
        [time_sort(a[:length], prep, sort)
        for a in lists
        for _ in range(repetitions)])

# --- Part 2 ---- 

if __name__ == '__main__':
    random.seed(4567)
    preps = [sorted, reverse_sorted, unchanged]
    num_lengths = 7
    length_base = 10
    max_value = 1024
    max_length = 1000000
    random_lists = [[random.randint(0, max_value) for _ in range(max_length)] for _ in range(3)]
    lengths = [10, 100, 1000, 10000, 100000, 1000000]
    repetitions = 3
    timeout = 0.1
    results = []
      
    for prep in preps:
        print(f'\n{prep.__name__}')
        for sort in sorts:
            print(f'\n\t{sort.__name__}', end='')
            for length in lengths:
               median_time = aggregated_time_sort(lists=random_lists, length=length,
                                             prep=prep, sort=sort, repetitions=repetitions,
                                             timeout=timeout)
               print('.',end='')
               results.append(dict(
                  sort=sort.__name__,
                  prep=prep.__name__,
                  length=length,
                  time=median_time))
               if median_time > timeout:
                  # don't consider longer lists if it already was too long on this one
                  break
    print()
    print(results)
    pd.DataFrame(results).to_csv("sort_times.csv")
    import seaborn as sns

    sns.set_theme()
    data = pd.read_csv("sort_times.csv")
    plot = sns.relplot(data=data, kind='line', x='length', y='time', style='prep', hue='sort')
    plot.savefig("sort_times.png")








