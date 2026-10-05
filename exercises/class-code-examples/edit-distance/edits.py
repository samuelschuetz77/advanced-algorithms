
# 1) Name the root and params
# 2) Name the nested and params (don't repass the root param stuff)
# 3) use nested to solve root
# 4) indent nested base cases
# 5) indentifying one decsion to make in the nested method, and get the list
# 6) pick the best option
# 7) only solve each subproblm once: (memoize)

from functools import cache

@cache
def edit_distance(before, after):
    def suffix_edit_distance(i, j):
        """returns the edit ditsnace between beofre[i:] and after [j:]"""
        if i == len(before) and j == len(after):
            return 0
        options = []
        # delete -> i++
        if i < len(before):
            options.append(1+ suffix_edit_distance(i+1,j))

        #insert -> j++
        if j < len(after):
            options.append(1+ suffix_edit_distance(i,j+1))
            
        # match/subtitute -> i++, j++
        if i < len(before) and j < len(after):
            sub_cost = 0 if before[i] == after[j] else 1
            options.append(sub_cost+ suffix_edit_distance(i+1,j+1))
        return min(options)
    return suffix_edit_distance(0,0)





def tests(): 
    assert edit_distance("", "") == 0
    assert edit_distance("a", "") == 1
    assert edit_distance("", "a") == 1
    assert edit_distance("b", "a") == 1 # edit distance is always the cheapest of the available conversions


    