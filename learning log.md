### Learning Log

## Wednesday 8/26/2026 : Learning Log 1

- Question/Problem: I really have some anxieties about catching up with algorithms from the intro course, I understand it takes me a while to pick these things up so I guess I'm looking for a happy path zero to proficient hero for all those basic algorithms. My questions are:
- which algorithms should I hone in on that can quickly get from basic bubble sort to dynamic programming problems? 
- How can I use my time well and memorize what these algorithms are doing conceptually - so these concepts are solid in my head?
- I know I'm going to have to refresh on python so I'm sure there is some path to kill 1+ (my deficiency) birds per stone, what are they?  
- Part of this question, I'm expecting might be guided by what you tell us on Monday 8/31/2026 or whats updated in canvas. (I'm asking this before the course schedule was/is posted.)
- When Identified: 8/26/2026 3:30pm
- Importance: 4
- How to Learn: - sprint 1: selection / insertion + coinduction proof reveiw
        -sprint 2: bubble / counting sort - non- recursive sorts
        -sprint 3: recursion basics refresh / merge sort / quick sort
        -sprint 4: Big O / asymtoptic notation / contradiction proof verifies the sorts from sprints 2-3 are actually correct/efficient
        -sprint 5: make sure good at binary addition works
- Insight/Answer:
    - problem: I don't want to get confused with similar algorithms (ones from the intro class)
        - possible solution: start with the most confused algorithm pairs:
            - [merge sort / quick sort]
            - [binary search / Find-(first or last)-occurrence]
            - [insertion sort / selection sort]
        - another: use visualizations on YouTube or websites (I'm sure they exist)
    - problem: I'm not experienced with Python
        - solution: practice a lot, and use it as my language to learn/refresh on those basic algorithms
    - solution: Adam posted a study guide and a textbook, look like there is aan assignment with 4 of the 6 i selected, maybe ill shift to focus on those. ixnayed on binary + first/last and ill do bubble and counting instead
    - worth noting: from the introduction it seems inportant that I also refresh on proofs from discrete like induction and contradiction - bummer i took this course almost 3 years ago. "

    - my revised algorithm/preq sprints: 
        - sprint 1: selection / insertion + conduction proof reveiw
        -sprint 2: bubble / counting sort - non- recursive sorts
        -sprint 3: recursion basics refresh / merge sort / quick sort
        -sprint 4: Big O / asymtoptic notation / contradiction proof verifies the sorts from sprints 2-3 are actually correct/efficient
        -sprint 5: make sure good at binary addition works

- Hours Spent Learning: 0.33
- Minutes Spent Documenting: 10
- Confidence: 5, that this seems like a good (probably too-thought-out) strategy
- End time: 7:45pm thursday 8/27/2026

## Friay 8/28/2026 ~7pm : Learning Log 1

- Question/Problem:

the following is  not sorting right, and I want to know how come?

unsorted = [77, 33, 35, 12, 98, 2] 

def insertion_sort(list):
    for i in range(1,len(list),1):   
        sub = list[0:i+1]    # 1: [77, 33]    2: [33, 77, 35] 3: [33, 35, 77, 12] 4: [12,33,35,77, 98]
        for j in [0, i+1, 1]:  # e.g j = 0, j = 1   2: j 0,1,2  3: j 0,1,2,3    4: 0,1,2,3,4 
            if list[j] > list[i]: # if 77 > 33   2: if 33 > 35 nope 3: if 77 > 33 yes  4: if 33 > 12 yes 5: x > 98 no no no no 
                list[j], list[i] = list[i], list[j]  # 1:[33 <swapped> 77, 35, 12,98 etc] 2:[ 33, 35, 77, 12, 98,2] 3: [12,33,35,77,98,2]
                break
    return list

print(insertion_sort(unsorted))

- When Identified: 7:00pm 8/28/2026
- start time: 7:00pm 8/28/2026
- Importance: 5
- How to Learn: 
     - walk through debugger, stepping into fucntions, stepping over, and continuing until you understand what is going on, ask claude for help if you burn more than 30 minutes on this 
- Insight/Answer:
        - swapping was working good, and the list looked good through the whole process until the end
        - i noticed i was tryig to do pythons version of a conventional for loop, but at first i was iterating off of sub, and I realized i was itending to have the same kinda for i in range(1,len(list),1): 
        but instead i had   on line 52  for j in [0, i+1, 1]: 
        -this is bad because instead of a trad for loops conditions i was basically just making j each element of a 3 item list instead of constructing the iterator part of a conventional for loop. 
        - I discovered the above because i kept hitting 'continue/f5' in debugger and discovered a sequnece was j=2, then next f5 press it was j=1, that tipped me off that my for loop was having severely retarded behavior.
        - fixed on 52: for j in range(0, i+1, 1):
- Hours Spent Learning: 1
- Minutes Spent Documenting: 15
- Confidence: 5

## Saturday 8/29/2026 11:30pm : Learning Log 1

- Question/Problem:
   why won't this code work?

    unsorted = [77, 33, 35, 12, 98, 2] 
    def insertion_sort(list):
        for i in range(1,len(list),1):   
            sub = list[0:i+1]    # 1: [77, 33]    2: [33, 77, 35] 3: [33, 35, 77, 12] 4: [12,33,35,77, 98]
            for j in range(0, i+1, 1):  # e.g j = 0, j = 1   2: j 0,1,2  3: j 0,1,2,3    4: 0,1,2,3,4 
                if list[j] > list[i]: # if 77 > 33   2: if 33 > 35 nope 3: if 77 > 33 yes  4: if 33 > 12 yes 5: x > 98 no no no no 
                    list[j], list[i] = list[i], list[j]  # 1:[33 <swapped> 77, 35, 12,98 etc] 2:[ 33, 35, 77, 12, 98,2] 3: [12,33,35,77,98,2]
                    # break
        return list
        print(insertion_sort(unsorted))
        - specifically why does it print [2, 35, 77, 33, 98, 12] instead of sorted?

- When Identified: 11:30pm 8/28
- start time: 11:30pm friday night 8/28
- end time: 9:35am Saturday morning 8/29
- Importance: 5
- How to Learn: 
    -Use debugger, f5 repeat with break point on line 86
    -reveiw tuple swapping, suspect maybe tuple swap isn't quite right here
    - visualize the 'game' so you can learn play it
- Insight/Answer:
    - of course it doesnt work [for longer sublists (sub) we can't just swap, we have to shift multiple values right], but the reason I didn't notice at first is because the first two swaps just happened to work with that swap logic because there weren't other indexes that needed moving because our sub was 1-3 values long then. 
    - I suspect I might need to make list[i]'s into list[i+1]'s e.g bump everything up/shift right on the list in other words
    - The answer was I thought I could do a clean tuple swap and get the right answer, but that isnt the case. I have to store the temp and shift everything right on the list. 
    - changed: list[j], list[i] = list[i], list[j]
    - changed to:
                temp = list[i]
                for q in range(i, j, -1):
                    value_moving = list[q-1]
                    erased = list[q]
                    list[q] = list[q-1]
                    # og [77, 33, 35, 12, 98, 2] 
                list[j] = temp 
    - this change got my expected output list: [2, 12, 33, 35, 77, 98]! yay!
    -final work: though this is a correct implementation
- Hours Spent Learning: 1.5
- Minutes Spent Documenting: 20
- Confidence: 3, I'm still not sure this will work with every list and I think 3 forloops is one too many.

## Saturday 8/29/2026 10:30am : Learning Log 1 

- Question/Problem: How could I make the following function for insertion sort use 2 loops instead of 3?

def insertion_sort(list):
    for i in range(1,len(list),1):   
        sub = list[0:i+1]    
        for j in range(0, i+1, 1):   
            if list[j] > list[i]: 
                temp = list[i]
                for q in range(i, j, -1):
                    value_moving = list[q-1]
                    erased = list[q]
                    list[q] = list[q-1]
                list[j] = temp
                break
    return list


- When Identified: same day at around 10:15am
- start time: 10:30am sat
- end time: 8:25pm saturday 
- Importance: 5 if I only need 2 loops and I have 3 I will never acheive o(n) best case, all will be o(n^2)
- How to Learn: 
    - reducing from 3 to 2 means there is a way i can do what my last 2 loops do in one loop. 
    - look at potential ways to fulfill the purpose of each those two loops in a single loop somehow

- Insight/Answer:
    - the loops I need combining are the j loop and the q loop
    - j loop has purpose: loop through already sorted sublist from indices 0 to the one right list[i] to see if there is a number in the sublist that is greater than the value stored in list[i] / temp. 
    - a simple purpose of j is to figure out what index temp value belongs in the list

    - q loop has the purpose of starting at where shifting every value in the list between list[i] and the index j loop deteremined that the list[i] / temp value should live up one so that each value now lives in the next index as it previously did. 
    - a simple purpose of q loop is to shift all the values necessary so that that peurpose of the j loop can be realized

    - if i combine those simple purposes my new loop would need to determine where the temp value would go and properly shift stuff over so temp can be inserted in right place 

    - thought: instead of counting up in j then counting down (im talking j++ in j and q-- in q) what if I just counted down for the j loop? 

    - aha: if we traverse the list down from list[i] / (e.g temp value index) we would basically be checking on each step:
            - i have a value at index[i], are you bigger than that? 
            - if the first value, list[i-1], is bigger than list[i] we have enough evidence to conclude that list[i] belongs somewhere else, which means we can also conclude that list[i-1]'s value should be shifted right to make space for wherever list[i] / temp should go. 
            - ***if we know list[i] is going somehwere else, we don't need to know where its going yet to know that list[i-1] needs a right shift by 1 ***
            - every j iteration (--) we can check 1) is list[j] bigger than list[] if so we can perform the shift
            -after a few times this is what i landed on:
            def insertion_sort(list):
            
            for i in range(1,len(list),1):   
                temp = list[i]
                for j in range(i-1, -1, -1): 
                    if list[j] > temp: 
                        list[j+1] = list[j]
                        list[j] = temp 
            return list

- Hours Spent Learning: 1
- Minutes Spent Documenting: 20
- Confidence: 5, i believe I now have a correct implementation with correct complexity

## Sunday 8/30/2026 : Learning Log 2 

- Question/Problem:
    - How does selection sort work?
- When Identified: 8/30/2026 2:40pm
- Importance: 4
- How to Learn: 
    - utilize that cool asian guys website on github to see a good stepped animation: https://yongdanielliang.github.io/animation
    - learn how to play the game
- Insight/Answer:
    - this one is less complicated than insertion sort in my understanding
    - as I understand it you iterate from i = 0  up and do a swap with the current element and the min of cdr of the list (borrowing from racket terms) (if I am allowed to use the min(), this shouldn't be too difficult)
    - you keep swapping list[i] and the min of 
    - if i had the list [77, 33, 35, 12, 98, 2]:
    - startiting at i=0, list[1:] would represent the cdr e.g. [33,35,12,98,2] while list[i] = 77
    - I think min(list([i+1:])) would find the right potential value to swap, but we'd have to make sure min(list([i+1:])) is less than list[i]
    - min(list([i+1:])) is the min of the cdr of the sublist starting at i -> i guess this is a more accurate way to say it.
    - okay I'm sure I'm missing pieces but I think I'm ready to implemenet
- Hours Spent Learning:0.25
- Minutes Spent Documenting: 10
- Confidence: 4, confident enough to begin coding

## Sunday 8/30/2026 : Learning Log 2

- Question/Problem: in this implementation where I'm using lst[lst.index(b)] would it still work if I had multiple values that are the same as the value for b 

        def selection_sort(lst):
            for i in range(0, len(lst), 1):
                a = lst[i]
                b = min(lst[i+1:])
                if a < b:
                    # tup swap
                    lst[i], lst[lst.index(b)] = lst[lst.index(b)] , lst[i]
                else:
                    break

- When Identified: 3:05pm 8/30/2026 Sunday
- Importance: 4
- How to Learn:
    - Think about it - what could go wrong? 
    - Hypothesize: my initial thought is it wouldn't matter 
    - test, this is pretty easy to test throw two 2's in a list and see what happens: would the 2 selected for the swap be the one with a smaller index?
- Insight/Answer:
    - well i thought this would be straightforward but i got this error: 
     
    b = min(lst[i+1:])
        ^^^^^^^^^^^^^^
    ValueError: min() arg is an empty sequence

    - I thought about why I might be getting this and realized we iterate to the last term of the list
    - the problem with that is min of the cdr of the last number (and i guess the rest of the lsit) on the list would just be null.
    - this is where the racket knowledge is useful. every list has the numbers in it + null. 
    - I also realizsed i forgot a return value

    - this is what stuck and (worked): 

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



- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 5 
- Confidence: 4, i got it right, but unsure if this is an optimal solution or not in terms of big o

## Sunday 8/31/26 : Learning Log 2 

- Question/Problem: I'm still bad at determining if a basic algortihm implemenatnion is an optimal solution or not, how can I learn and never forget? 

- When Identified: 3:35pm 
- start time: 3:35pm
- end time: 4:15pm
- Importance: 4
- How to Learn: Ask ai for a guide, watch youtube videos on big o
- Insight/Answer:
 - after asking ai a good way to learn this and remember it gave me some heavy mathematical forumalas for calcualting time
  including one for if a loops inner bounds depend on outer loop variables. That got me all the way confused so I asked if I could get an example of what it meant when inner loop bounds depend on outer loop variables
  - I got frustrated because I never want to do or look at that formula ever and I didn't want this learning session to scope creep into something ugly and horrible that I never want to do - so I asked ai if there is a way to aproximate complexity and be fairly accurate as opposed to mathematically certain and this is what it said: 
  - "Yes. You can get very accurate Big-O answers here without doing the summation formula.

    An inner loop bound depends on the outer loop when the number of times the inner loop runs changes based on the current value of the outer loop variable."

- as it turned out, my last function i worked on for selection sort is a good example of this: 

in this part: b = min(lst[i+1:])

The amount of work min() does depends on i. At first it checks almost the whole list, then a little less each time. 
is n is len(lst) then it the outer for loop goes n times, while the inner sum is doing about n worth of work, though the list grows smaller and smaller.. 

this just generalizes to O(n^2), which is good enough for me


- Hours Spent Learning: 0.65
- Minutes Spent Documenting: 10
- Confidence: 3, although I think what I learned was a good refresher, when we get into recursion things will get a lot harder, I wouldn
t have ended this session but I'm curious to see what we learn in regards to this stuff in class


## Monday 8/31/2026 : Learning Log 2

- Question/Problem: Is this implementation for counting sort correct and/or optimal? 


def counting_sort(lst):                 # O(n+k) where k is length of count_array 
    # make count_array:
    max_num = max(lst)
    counts = [0] * (max_num + 1)
    for num in lst:                     # n traversal
        counts[num]+=1  
    # return list of nums:
    lst2 = []
    for i in range(0, max_num + 1, 1):  # k traversal
       lst2 += [i] * counts[i]
    return lst2 


- When Identified: 6:00pm 
- Start time: 4:30pm
- end time: 8:30pm
- Importance: 4
- How to Learn: Use/set up the testing framework proposed in sorting.py assignment
- Insight/Answer:
 - before I began setting up the pytest framework I noticed that an empty list, I tried an empy list and got this result: 

 Max_num = max(lst)
              ^^^^^^^^
ValueError: max() arg is an empty sequence, 

so I fixed that with:

if not(lst):
    return []    

  - Wow your code was pretty amazing for the testing harness, and 54 total lists to tests per sort. 
  - took a while to understand it, I think I got it to work. Looks l
  -  looks like i need to add this to selection sort too:
     if not lst:
        return [] too
  - my question of whether this was a correct implementation was correct after i fixed that empy list bug, it worked in your full test harness
- Hours Spent Learning: 2.5
- Minutes Spent Documenting: 10 
- Confidence: 4

## Tuesday 9/01/2026 : Learning Log 3

- Question/Problem: What are the components of recursion? 
- When Identified: 11:20am 
- start time: 11:20am
- end time: 8:25pm
- Importance: 5
- How to Learn: 
  - read about the basics of recursion via AI and others
  - read about merge sort, identify each component of recursion in a merge sort algorithm
- Insight/Answer:
  - I've always understood the base case is the end condition that stops the recursion from happening, but I read that it can also be thought of as "The smallest version of the problem you already know the answer to"
  - I think its easy to think in my head what is the value we have to stop at, but I think in more complicated recursion thinking about the smallest subproblem is superior
  - With the recursive step, I've always thought of it as the part we are repeating.
  - I think a better way for me to conceptualize this is: 
  
    distilling the problem to a few instances and preserving enough structure so that their solutions can be combined into the original soltuion you were after.

    if we think of a factorial alg: 

    solution to n = 
    n * solution to n - 1

  - lets talk merge sort:
  - the base case is when you can't split a sublist anymore, when n = 1 or n = 0. becuase technically a list of length 0 and 1 are both 'sorted'
  - but if we think in terms of 'distilling the problem to a few instances and preserving enough structure so that their solutions can be combined into the original soltuion you were after.' we have something like: 
      sort(big list)
      =
      merge(sort(left half),
           sort(right half))

      but we still need a way to compse those solutions for left and right half

  - the hardest part about recursive decomposition is preserving the property you care about and isloating it from the stuff that doesn't need to be solved yet. If done right, each recursive call becomes a smaller version of the same problem. 
  - Three important things to remember when thinking about your recursive step implemenation: 
    1) What smaller instance of the same problem am I creating. in simple recursion this could be passing the same funtion an n+1 or n-1..
    2) How does solving that smaller instance help me solve the bigger one?
    3) How many subproblems am I creating, and how quickly are they shrinking

    def is_palindrome(str)
        if len(str) >= 1:
            return True
        if str[0] != str[-1]
            return False
        return is_palidrome(str[1:-1]) 
        
        
        1) What smaller instance of the same problem am I creating? -> is the inner layer a palidrome?  
        2) How does solving that smaller instance help me solve the bigger one? -> 
           if the outside chars match then the whole string is a palidrome if the inner layer is a palindrome
        3) lets take is_palindrome("racecar")

           recursive calls are: "racecar"       # initial call has 7 chars
                                 "aceca"
                                  "cec"
                                   "e" 
           
           insight: each recursive call only produces 1 other subcall which is why we have a single chain of subproblems. 

            insight: each subcall reduces the number of chars by 2 because it takes one off each end

            important 2 things to remember with 3) How many subproblems am I creating, and how quickly are they shrinking:
              - how many branches? 1 in this case
              - n shrinkage in between call and subsequent call? in this case n shrinks by 2?

            with those two components you can calculate how many recursive calls after original does it take to reach the base case?             
                   
- Hours Spent Learning: 1.15
- Minutes Spent Documenting: 30
- Confidence: 4

## Tuesday 9/01/2026: Learning Log 3 

- Question/Problem: Among the different types of recursive algorithms, what are all the important things to know about to avoid mistakes and optimize memory and storage? 
- When Identified: 11:21am 
-start time 11:21am
-end time 11:15pm
- Importance: 5
- How to Learn:
  - reveiw the types of recursion
  - play a game where you look a few project euler problems that are commonly solved with a recursive function and guess what kind of recursion it will take to solve the problem from these 'types' i've already inventoried
  -try a that one project euler solution again

- Insight/Answer:
  - Distnguishing the types of recursion comes down to four questions: 
    1) Does the function call itself directly or through another function? options: direct, indirect/mutual
    2) How many recursive calls/branches are created? options: linear/single recursion, binary recursion, multiple/tree recursion
    3) Where is the recursive call? If there is work after the recursive call it is not a tail recursive alg. options: tail and non-tail/head recursion
    4) How is the problem reduced? options: structural recursion, divide-and-conquer / generative recursion
  
  - the last line of a standard factorial recurive algorithm is: 

    return n * factorial(n-1)

    because we multiply n to whatever factorial(n-1), that means the recursive call isn't the final op -- the multiplication is 
    that means factorial is not tail-recursive
  - Mutual recursion is where A calls B and B eventually calls A  
  - I'm looking at a project eueler problem I solved once upon a time with Adam's help

- Hours Spent Learning: 2
- Minutes Spent Documenting: 20
- Confidence: 4, need more experience writing recursive functions to solve problems - though i know work done this entry will help immensely


## Wednesday 9/02/2026: Learning Log 3

- Question/Problem: I got a RecursionError: maximum recursion depth exceeded while attempting merge sort and I want to know why
                    Is it because my algorithm is majorly flawed or minorly flawed?
    
    ######### start code ############################################################
    def merge_sort(lst):
    def merge(right, left):
        r = l = 0
        while(r < len(right) or l < len(left)):
            # take index and find min
            val = min(right[r], left[l])
            if right[r] == val:
                r+=1
            else:
                l+=1
            lst += val
        # while loop terminates because one or both lists has been run thru
        # determine if another list hasn't been run through and if so append those remaining items to lst 
        if (r == len(right)-1 and l != len(left)-1):
            return lst + left[l:]
        else:
            return lst + right[r:]

    # base case: if length of lst = 1 or 0 its sorted, return the sorted lst
    if (len(lst) <= 1): 
        return lst
    mid_i = len(lst) // 2 # floor division means just integer division if you use / you could produce floats
    # I know this is binary recursion / tree recursion because we produce two branches per call
    return merge(merge_sort(lst[:mid_i+1]), merge_sort(lst[mid_i+1:]))

    ######### end code #####################################################################

- When Identified: Wednesday 9/02/2026 9:45am
- start time: Wednesday 9/02/2026 9:45am
- Importance: 2
- How to Learn: identify what could cause these errors in beginner merge sort attempts 
- Insight/Answer: 
    - here is what I found after googling: 
    1) The Bug: Checking if len(arr) == 0: instead of if len(arr) <= 1:.
      - this makes sense because if we set it to end at 0 all the len 1 sub arrays would get split to a lnother len 1 and a len 0, those len1 splits would continue on forever
      - this makes sense but its not my problem
    2) Slicing Mistakes
       2a) Using floating division / instead of integer division // 
           - again not my problem 
       2b) Off-by-one slices, if you dont break it up correctly it could fail
           - I intially thought this couldn't be my problem.. 
           - I tried working through an initial lst merge_sort call where lst len = 2
           - ex) lst = [9, 2]
           - here was my two original lines relevant to slicing:
           - 1)   mid_i = len(lst) // 2
           - 2)   return merge(merge_sort(lst[:mid_i+1]), merge_sort(lst[mid_i+1:]))
           - I would expect it to work like:
           -      return merge(merge_sort(9), merge_sort(2))
           - but I suspect it doesn't
           - lets see: mid_i = len(lst) // 2 = 2 // 2 = 1
           - I already see my problem but I'll spell it out: 
               - I thought mid would correlate to the last element of the first list, but it obviosuly correlates with the first element of the second list. 
               - since mid_i = 1 here my algorithm would make the second sub list start at lst[mid_i + 1] = lst[2] -> that is out of bounds but we probably didnt even reach that error because we hit max depth exceeded first
               - that would mean the first list would go from 0 to but not including index 2. in other words index 0 and index 1 -> but thats what we started with... i can see how this is similar to this Bug: Checking if len(arr) == 0: instead of if len(arr) <= 1:.
            - to correct this I need: 
            - return merge(merge_sort(lst[:mid_i]), merge_sort(lst[mid_i:]))
            - insight: hey I think i'm starting to understand why pythons weird slicing defaults can be nice sometime! haha!
            - I have another problem but I'm ending this, because I found the answer to my question
- Hours Spent Learning: 0.8
- Minutes Spent Documenting: 20
- Confidence: 5

## Wednesday 09/02/2026: Learning Log 3 

- Question/Problem: I now understand the quick sort implementation with uno cards - what are the nuances of actually implementing it? What will my insights be? 
- When Identified: Wednesday 09/02/2026 4:31pm
- Start time: 4:31pm 9/02/2026 wednesday 
- Importance: 5
- How to Learn: 
  - prepped by buying two decks of unos at dollar tree and really making sure I understand the 'game' that is quick sort - asking ai questions when i needed clarifications - stuff that there wouldn't be enough time in class for me to articulate before another student needs your help
  - then implement and see what dust is kicked up - this dust might offer clues of where im getting tripped up understanding recursion in general 
- Insight/Answer:
  - first insight was this is the first memorable implemenation of tree recursion where the recursion inst directly in the return statement.. whereas merge was something like
  
  return merge(merge_sort(left), merge_sort(right))

  this one has its recursive calls just happening in place, not follwoing a return statement. This is an interesting concept to me because quick was way harder to understand for me than merge, and i think thats concsistent with the complexity of the algorithm. because the partitioning step handles rearranging and finding the sticky pivot before recursing, unlike merge sort which has to do its combining work after.

  - another idea was this idea of having the override function with 1 arg instead of the 3 it typically takes just to get the fucntion to work with your framework code. I thought this would be trickier than it was, very cool how simple that ended up being, I can see lots of applications for this -> a question that follows is: Is this what happens when you have constructor overloads in c# or is there nuances?
    - answering that question they are similar distict: we have two functions in python vs true constructor overloads in c# use the compiler to basically say, "how many args does your call have?" maps to the constructor with  corresponding # of args. what is closer to this parent 1 arg quick_sort calling the 3 arg one is default params, i could have figured out a way to solve this with pythonsdefaults but I tried and it wasn't trivial. 

  - Finally, yesterday I implemented merge_sort but before I even started I did my learning_log entry on types of recursion. I found learning about the types of recursion to be a very good investment of time, and learning about these subtle differences makes identifying the the recursive step a much cleaner process often and can sometimes make understanding what the base case should be better. Anyway I want to run through what kind of recursion quick_sort is from those recursion-type areas i found yesterday. 

  - 1) it  is direct meaning quick sort calls itself not through some other function
  - 2) like merge sort it is the binary recursion because each call births two branches. binary is a subset of tee recursion which can be far more than two branches each time. # of branches though is not indicative of recursion depth, and quick_sort is less stable off the bat than merge because how there is a spectrum of luckiness we can get when selecting our pivot. 
  - 3) tail recursiveness of quicksort:
        this one is tricky because the we have two recursive calls since binary recursive. from what im reading the second call is truly tail recursive because it is the last thing the fucntion does, but since the first call is not the last thing - the quick_sort as a whole is not truely tail_recursive. by definition binary recursion cannot be tail recursive even though i guess parts of it can be.. But i found a website I do not want to read right now but im putting it here to read over it later: 
        https://cs.wellesley.edu/~cs251/f20/notes/tailrec.html for the purpose of understanding how binary recursive algorithms can be manipulated into tail recursive algorithms.. this will probably come up in our coursework too, but dual exposure would be good. 
    - 4) this is generative as opposed to structural, and it relies on randomness in pivot to (hope for) avoiding the worst case
- End time: 7:04pm
- Hours Spent Learning: 2 and 33min
- Minutes Spent Documenting: 20
- Confidence:4 

## Tuesday 9/01/2026: Learning Log 4 

- Question/Problem: How will I know when using @lru_cache is advantageous?
- When Identified: Tuesday 9/01/2026: 10:45pm
- start time: Tueday 9/01/2026 10:45pm
- Importance: 5
- How to Learn: search the web for real stories on how people use @lru_cache, and read Python's documentation on it
- Insight/Answer:
    - lru stands for least recently used and is a caching eviction policy among others like FIFO or least frequently used. It says which things are we getting rid of from cache and wagers that if you haven't used it in awhile then it probably won't be as important as the stuff most recently used.
    - how @lru_cache works: it saves return values attached to specific args so that if those args show up again it pulls the result quickly from cache. When dealing with recursive functions this is basically a built in "I'll handle memoization and make it easy" feature.
    - I found from the documentation that you can and should use @lru_cache when you are expecting to use the same args in multiple function calls, so because this is a very common thing with recursion, you can almost always use it when dealing with pure recursive implementations. One caveat is that when your recursive functions have side effects (network calls, print statements, modifying global vars, dealing with randoms, db writes, non deterministic behavior) you should not use it. That makes sense.
    - Adding this to concrete the idea of non deterministic functions in my head. If you try to use @lru_cache for non deterministic functions, for example maybe your function does something with a current time stamp, the cached version will always be based on the first call. So even though you have matching args you'd have different behavior and it wouldn't be advantageous to save a cached version if that version is different (even if only slight) from what you would expect if you didn't skip computations.
- Hours Spent Learning: 0.75
- end time: 9:30pm 9/8/2026
- Minutes Spent Documenting: 15
- Confidence: 5

## Tuesday 9/08/2026 : Learning Log 4

- Question/Problem: What is the priority and what is the key in the priority queue?
- When Identified: 7:15pm 9/8/2026
- start time: 7:15pm 9/8/2026
- Importance: 4
- How to Learn: read the Sheehy chapters, ask questions to AI about heap order / priority queues until confident in understanding about graphs / priority queues / min heaps
- Insight/Answer:
    - priority is just the value the whole structure is "sorted" by
    - by "sorted" I mean heap ordered, which basically means a node's (up to 2) children must be greater than or equal to the parent
    - adding a new node we call updating, and it will either add a node if the key isn't used, or update the data of that node - because we are eventually using Prim's algorithm, we have to put some check to make sure we are only fulfilling updates that include a lower number than current for priority
- Hours Spent Learning: 1
- end time: 8:12pm 9/8/2026
- Minutes Spent Documenting: 14
- Confidence: 5

## Wednesday 9/9/2026 : Learning Log 4

- Question/Problem: In min-heap priority queue with some locator dict, why is it not enough to swap the heap array entries during sift-up/sift-down, and why do the corresponding locator dictionary values need to be updated as a packaged deal with the heap-array swap?
- When Identified: 4:45pm 9/9/2026
- start time: 4:45pm 9/9/2026
- end time: 6:45pm 9/9/2026
- Importance: 4
- How to Learn: Understand the benefit of the locator dict, understand how this optimized data structure should/would work, and then go over scenarios where things malfunction and what would be the net effect.
- Insight/Answer:
    - to find a key's index fast instead of a linear scan: we could just do a dic that stores the same key but its value would just be the index it lives at
    - this sift would not ever swap a child node with some node at the parents level (but not the same node as the parent), in other words you are always swapping between a parent and a child, always
    - Whenver you are performing sifting/swapping something always needs to happen concerning the locator dict: you would need to swap the values of these two keys, especially because you are using the locator dict in some capacity for the swaps of the min-heap array.
    - the locator dic would not be updated if it didnt happen, youd have a stale key index mapping that would screw things up significantly -- swap values, not keys: if locator["b"] == 2 and locator["e"] == 5 before a swap, after swapping array indices 2 and 5 you need locator["b"] == 5 and locator["e"] == 2, keep the keys, swap the index values
    - if the locator isn't updated: it would swap potentially an old value for e with 0, it would swap something that might not even be e -- it would look for e's index and it would swap the element at the index e used to be at, causing a dilemma. the failure is temporally displaced from its cause, and it never announces itself -- you get plausible-looking wrong answers instead of a stack trace
    - on order vs atomicity: I don't think it matters which you do first, I think it just matters that you do each as a unit, and try to eradicate/minimize any steps in between the operations
    - these should be bundled as a packaged deal whenever there is a shift up or down because if they weren't wrapped in the swap function I'm going to implement, it could cause problems -- there is a safe way to make it impossible for code to run in between these two iterable modifications, and it has to do with atomicity
- Hours Spent Learning: 2
- Minutes Spent Documenting: 15
- Confidence: 5

## Wednesday 9/9/2026 : Learning Log 4

- Question/Problem: Why did my sift_up/update implementation for the locator-heap priority queue keep breaking, and what specific bugs were causing it?
- When Identified: 6:00pm 9/9/2026
- start time: 5:30pm 9/9/2026
- end time: 11:30pm 9/9/2026
- Importance: 4
- How to Learn: Write and concpetualize sift_up but think about the iterative version of a base case
- Insight/Answer:
    - first insight: I referenced parent_key in the while condition before it was ever assigned and i  fixed it by computing parent_index/parent_key before the while loop and refreshing them at the end of each iteration.
    - My while condition / root guard was backwards (curr <= 0 instead of curr > 0) - this would yerminate the while before anything meaningful could get done.
    - I realized new keys were never being registered in self.locator_dict, only swaps updated it in sift_up, so a fresh key's index was never recorded, causing sift_up to combust into a fiery explosion of autism
    - When updating an existing key to a lower priority, I was appending a new tuple instead of overwriting the existing one at its current index... since im using a list of tuples with keys this was theroretically possible but it shouldn't have been at all. I should have buttoned that up.
- Hours Spent Learning: 2.5
- Minutes Spent Documenting: 12
- Confidence: 3 I'm confident my insights are getting me closer to being done with this, but I'm not done yet

## Backlog on 5

- Question/Problem: How can I remember the jist of Prim's vs Djisktras graph algorithms? 
- When Identified:11:45pm 9/9/2026
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## Friday 9/11/2026 5:45pm : Learning Log 5

- Question/Problem: How should I study/review for this assignment in a way where I'm using the reading to excel and be competent on the assignment due Friday 9/18, especially considering class today with recursion trees did not click well?
- When Identified: Friday 9/11/2026 5:45pm
- start time: Friday 9/11/2026 5:45pm
- end time 10:21pm friday 9/11/2026
- Importance: 5 my plan for getting the stuff done I've found makes the diffeence between passive getting-by in a class and actually exceling
- How to Learn: there are multiple ways I could go about studying this week and getting ready for the project due friday, a few options I found:
    1) finish reading JEA 1.6-1.7 and also read the JEA induction notes pdf plus redo the recursion tree math from fidays 9/11 class by hand until the geometric series part actually makes sense, before touching any code. Good because it goes straight at the part that didn't click and the project grades the recursion tree analysis just as much as the actual code, but bad because more abstract math right after class already didn't work today so doing more of the same thing might not work either or might take more time than trying a different problem and circling back. 
    2) code first, theory later: start with the easy warm up tests and divide_and_conquer_multiply tomorrow, get it passing on real numbers, then do karatsuba, and only after both are working go back and do the recursion tree / big theta analysis using my own code instead of trying to follow along with fridays lecture - good because im seeing new material faster and it grounds the abstract tree stuff in something i actually built, and I figure when I eventually do circle back to what we went over today in class It will make more sense. TLDR f(time invested) yields more progress this way - is my hypothesis. f returns being able too fully conceptualize and complete this assignment along with umderstanding umbrella concepts. 
    3) split it up by day instead of by topic: sat/sun is reading (jea 1.6-1.7 plus the induction notes), mon-wed is implementation (warm up tests -> divide_and_conquer_multiply -> karatsuba, one thing at a time), thu is the recursion tree analysis plus the benchmark and plot - good because the recursion tree part actually gets its own dedicated day instead of getting crammed in at the end like it probably would with the other two options, bad because it's a rigid schedule and if any day runs long everything after it gets squeezed
- Insight/Answer: 
    - I inintally favored option 2 because I'm seeing more  material more quickly. The plan would be to try working a different recursion-tree problem on my own first, then come back to the concrete worked example we did in class - the understanding should compound, and I'll have more success concretizing the idea that way.
    - But I also like that option 3 lays out the daily steps to get there. When goals are more thought out - the when, how, why, how long are answered they are more likley to happen -- so i like that this specific strategy has my ultimate goal for this week broken down to smaller tasks by the day. This is also good. 
    - If I combined the two strategies I would still have a day/days to do list, but I would still try having some code that I worked through myself before getting heavy into math - which i think is very valauble and a superior way to do it. 
    - I think this hybrid strategy could look like this: 
        - saturday/ sunday: light reading/skimming limit to about 1 hour total  trying hard to get exposure but puprosely not entertaining too many tangents. reading would be jea 1.6-1.7 + jea induction notes
        - monday / tuesday: code first (option 2 inspired): warm up tests, divide_and_conquer_multiply, karatsuba, get everything passing maybe a 3-4 hour sprint at tops
        - wed: do a recursion tree analysis of the stuff we built monday / tuesday - understand every inch of this process / have good questions for class and when you reach some friction / concretize by referring and understanding fridays lecture
        - thursday: get the benchmarking done as well as the reflection. use this as a buffer day in case the previous steps took longer than expected or didn't find/make the time for them. 
        - friday: touch ups and turn in
    - That is my strategy ^ and answer to my question
- Hours Spent Learning: 1
- Minutes Spent Documenting: 25
- Confidence: 4

## Sunday 9/13/2026 : Learning Log 5

- Question/Problem: How do I go from a recursion tree picture to a big O bound and why does recognizing whether level totals are decreasing, equal, or increasing, determine the answer?
- When Identified: 5:00pm 9/13/2026
- start time: 10:00pm 9/14/2026
- end time: 7:30pm 9/13/2026
- Importance: 5
- How to Learn: read JEA 1.6-1.7, then practice deriving T(n) recurrences from hand-drawn recursion trees of varying shapes (balanced, unbalanced, different branching factors) and classifying each as decreasing/equal/increasing
- Insight/Answer:
    - given a tree where each node splits into r children each of size n/c, and non-recursive work at a node is proportional to its own size, T(n) = r*T(n/c) + O(n) — the r is just "how many subproblems," c is "how much smaller each one is"
    - practiced this on a few shapes: r=2,c=2 (mergesort, T(n)=2T(n/2)+O(n)), r=3,c=3 (T(n)=3T(n/3)+O(n)), and an unbalanced one with two unequal children (T(n)=T(n/4)+T(n/2)+O(n))
    - mergesort is the "Equal" case: every level totals n (2^i nodes * n/2^i work each = n), so T(n) = O(n log n)
    - worked through T(n)=3T(n/2)+O(n) (Karatsuba's recurrence) as an "Increasing" example: level totals go n, 1.5n, 2.25n... growing by a constant factor each level, so the leaves dominate and T(n) = O(n^log2(3)) ≈ O(n^1.585)
    - key insight on why the level-by-level classification determines the whole answer: T(n) is the sum of all level totals. If levels are flat, sum = (one level's value) × (number of levels). If shrinking, the top level alone is basically the whole sum, thats where all the work happens. If growing, the bottom level alone is basically the whole sum (it outweighs everything above it combined). So whichever level dominates, that's the answer there is no need to add up every level individually, just spot the pattern and take the dominant term
    - still shaky: haven't actually worked a "Decreasing" case by hand yet (T(n) = T(n/2) + O(n)), and want more reps recognizing the Increasing case since that's the one that'll show up with Karatsuba on the actual assignment
- Hours Spent Learning: 2.5
- Minutes Spent Documenting: 15
- Confidence: 4 because I still haven't looked much at the cases when levels are increasing like karatsuba

## Monday 9/14/2026 : Learning Log 5

- Question/Problem: I watched a YouTube video on Karatsuba multiplication before touching the assignment code, and wondered how does the algorithm's break up numbers especially when two are different lengths like say one number is 9 digits and the other is 3 - what then?
- When Identified: 9/14/2026
- start time: 3:45pm 9/14/2026
- end time: 5:35pm 9/14/2026
- Importance: 4
- How to Learn: I watched a walkthrough video of Karatsuba, then I will research how the same high/low block split applies when the two numbers aren't the same length
- Insight/Answer:
    - the algorithm works by breaking each number into a high block and a low block, then recursing on those smaller blocks instead of multiplying the whole numbers directly
    - I correctly identified that the recursion has to bottom out at single digits, where the multiplication can just be looked up/done directly instead of split further -- I got this right without prompting because it's the same base-case instinct from my recursion learning log entry (9/1): the base case is "the smallest version of the problem you already know the answer to," and for digit multiplication that's a single digit - and you return that single digit similar to merge sort's single digit list.
    - update although there could be some way to make the base case i chose work, upon further reflection I got it wrong. the base case is going ot be more complex than I had first anticipated 
    - the payoff for only doing 3 recursive multiplications instead of 4 is that you trade a costly fourth multiplication for a couple of extra additions/subtractions. in other words its not just a multiplication, its also another recursion. 
    - broader question this raised for me: how do divide-and-conquer strategies in general get their speedup? What are all the ways you can speed up a divide and conquer strategy?
    - last insight (unfortunately): I didn't notice that this assingment's 4 recrusive split multiple doesn't require me to do
- Hours Spent Learning: 0.83
- Minutes Spent Documenting: 25
- Confidence: 3, solid on why the trick saves a multiplication, still unsure about the mechanism of recursion - i think a recursion tree analysis would probably concrete this

## Monday 9/14/26 : Learning Log 5

- Question/Problem: Based on this assignment, how would divide_and_conquer_multiply and karatsuba each actually work as recursive functions  and how does the difference in how many recursive multiplications they make (four vs. three) change what the code for each one has to look like? What else do we have to do to accomadate the non multiplation arithmetic ops. 
- When Identified: 4:27pm 9/14
- start time: 7:00pm 9/14/2026
- end time: 9:30pm
- Importance: 5
- How to Learn: - try to derive base cases from contraints, then look it up - if anything is unexpected record it as an insight 
- Insight/Answer:
    - Well the first thing I realized that was cool, is that since these are essentially very similar algorithms my first instinct is that they will share a super similar base case because the base case only cares about how small the inputs are, not about how many recursive multiplications happen after it.
    - second insight is that because we are doing padding I dont have to worry about having different lengths like I was previously worried about, but this also means they will each shrink exactly the same as far as digits go
    - divide_and_conquer_multiply calls itself 4 times and looks like xhi*yhi, xhi*ylo, xlo*yhi, xlo*ylo karatsuba calls itself only 3 times and looks like xhi*yhi, xlo*ylo, and (xhi+xlo)*(yhi+ylo). 
    - karatsuba gets the middle value algebraically from the 3rd and last product: middle number = (xhi+xlo)*(yhi+ylo) - xhi*yhi - xlo*lo
    - karatsuba's combine step needs an extra to do those two subtracts after the multiply - but we are given a function for that.
- Hours Spent Learning: 1.15
- Minutes Spent Documenting: 25
- Confidence: 3, still need to just sit down and impelment this, didnt code as much as I wanted to here.

## 9/15/2026 : Learning Log 6

- Question/Problem: Just finished with divide_and_conquer_multiply, but for Karatsuba, after reusing the same base case, padding, and split from divide_and_conquer_multiply, how do I combine the three recursive products using n_digit_add, n_digit_subtract, and left_shift?  
- When Identified: 9/15/2026 10:30am
- start:  9/15/2026 10:30am
- end time:  9/15/2026 8:30pm
- Importance: 5
- How to Learn: Break down all the compents that need to happen, then determine the chronological order keeping in mind that I will need to subtract before shifting the middle product.
- Insight/Answer: 
    - to determine the optimal place to left shift we have to uinderstand what left shift is supposed to do - and that is to just allow us to add things correctly. 
    - so lets take karatsuba's first recursion which is basically hi * hi, this is just like the first one in divide n conquer so it gets shifted 2 * splitted_index
    - next we have low * low, in divide_and_conquer we didn't shift it at all because it already the lowest digit in the string
    - then we have the middle which is a bit nuanced in karatsuba: 
       - first the mult part of middle: prod = (hi1 + lo1) * (hi2 + lo2) = prod
       - then the subtracts: prod -  rec1( which was hi * hi) - rec2 (which was lo * lo)
    - essentially id have something like: n_digit_add(n_digit_add(left_shift(rec1, 2*splitted_index), left_shift(n_digit_subtract(n_digit_subtract(prod, rec1), rec2), splitted_index)), rec2)
- Hours Spent Learning: 2
- Minutes Spent Documenting: 30
- Confidence: 4

## 9/16/2026 : Learning Log 6

- Question/Problem: I still dont understand all the concepts/variables of recursion tree analysis (which I'm assuming is where you go from T(n) = something -> buildiing a treee doing maths -> you prove O(n) somehow), so in this learning log i will understand all the variables
- When Identified: 9/16/2026 9:00pm
- start time: 9/16/2026 9:00pm
- end time: 9/16/2026 10:15pm
- Importance: 5
- How to Learn: Ask the internet for a recursion tree analysis variable roster
- Insight/Answer:
  - n = algorithm input size
  - r = branching factor
        - this means how many new branches created at each necursive call
  - c = shrink factor
        - How much smaller the input gets in refernec to the last input
  - i = index level   root node is always i == 0
  - d = how many levels before base case   d is always the maximum value i takes
  - number of nodes at level i   ==      r^i
  - work per node at level i     ==   O(n/c^i)
  - total work at level i        ==   r^i * O(n/c^i)
  - leaves = nodes on the final level 
  - leaves = r^d
  - T(n) equation = total work as a function of n 
  - O(n) the end result after T(n) simplifies after levels are summed or bounded

- Hours Spent Learning: 1
- Minutes Spent Documenting: 15
- Confidence: 4

## 9/17/2026 : Learning Log 6 

- Question/Problem: How do I do recrusion tree analysis on karatsuba using these variables I learned? 
- When Identified: 5:30pm 9/17
- start time: 5:30 9/17/2026
- end time: 7:20pm 9/17/2026
- Importance: 5
- How to Learn: Work through the tree and derive each variable, understand logarithmic magic that always trips you up whenever you re-encounter it
- Insight/Answer:
    - the biggest insight was depth for depth, which i understand is the max i starting at i = 0
        - to calculate karatsuba's i max, (d), you have to understand you are halfing n at each iteration
        - you also have to understand the base case of karatsuba which for us is when the input string hits one char
        - so if n is 32 what is d
        - well you would have to keep cutting it in half until it reaches the base case 1
        - 32 i=0, 16 i=1, 8 i=2, 4 i=3, 2 i=4, 1 i=5 it takes exactly 5 halvings, so d = 5
        - if only there was some log trick we could do 
        - oh we can, this is log(base 2) n.   2 to the what == n? answer is log(base 2)n
        - log(base2)32 = 5, great that works 
    - once we have depth we can figure out how many leaves we'll have with respect to n 3 ^ d
    - and because by definition of our base case being 1, each leaf has constant work O(1), it is no longer looping through stuff because its working with just 1 value and our base case says thats when we stop doing everything but a return of that final thing. 
    - so 3 ^ d = nodes and d = logb2 n is the same as saying n ^ logb2 3 amount of work at the end
    - when the leaves dominate total work and you have a lenth ==1 base case like karatsuba:
    - bottom work = leaves * O(1)
    - and O(n) work = bottom work
- Hours Spent Learning: 1.2
- Minutes Spent Documenting: 15
- Confidence: 5

## 9/17/2026 : Learning Log 6

- Question/Problem: How do I do my divide_and_conquer_multiply analysis
- When Identified: 7:20pm
- start time: 7:20pm
- end time: 8:20pm
- Importance: 5 
- How to Learn: Work through it exactly like I did karatsuba understanting points of divergence with this less efficient algorithm
- Insight/Answer:
    - recurrence is T(n) = 4T(n/2) + O(n), because this one makes 4 recursive multiplications on half sized inputs, so r = 4 and c = 2
    - first thing is depth is the same as karatsuba, we are still halving n until we hit the one digit base case
        - so d = log(base 2)n in the clean half sized tree, same question as before: 2 to the what == n?
        - making 4 branches instead of 3 doesn't make the tree deeper, it makes it wider
    - at level i there are 4^i nodes, and the work per node is O(n/2^i)
    - so the level total is 4^i * O(n/2^i), which simplifies to O(n * (4/2)^i) = O(n * 2^i)
        - drawing it out helped here: the level totals go n, 2n, 4n, 8n etc
        - karatsuba's went n, 1.5n, 2.25n, 3.375n, so both are increasing but this one doubles with each new level
    - increasing by that constant factor means the leaves dominate, the sum of all the levels is within a constant factor of the bottom level's work
    - once we have depth we can figure out how many leaves: 4^d = 4^(log(base 2)n)
        - same log trick from karatsuba, swap the 4 and n: 4^(log(base 2)n) = n^(log(base 2)4)
        - 2 to the what == 4? thats 2, so we have n^2 leaves
    - each leaf has O(1) work because we hit the one digit base case, so bottom work = n^2 * O(1), and the final bound is O(n^2)
    - so splitting the numbers up recursively didn't improve the growth rate over grade school multiply, which is also O(n^2). the difference with karatsuba is saving that fourth recursive multiplication at every split, which is why its exponent is log(base 2)3 instead of log(base 2)4
    
- Hours Spent Learning: 1
- Minutes Spent Documenting: 25
- Confidence: 5

## Saturday 9/19/2026 : Learning Log 7

- Question/Problem: What is a good plan/order for tackling this week's learning logs, assigned readings, and assignment due Wednesday?
- When Identified: 9/19/2026
- Importance: 4
- How to Learn: lay out a few different sequencing strategies for the week (reading vs. coding first, when to write the log entry) and weigh them against what's actually worked for me before, then pick one
- Insight/Answer:
    - the week's real shape: Backtracking for Optimal BSTs (5 staged parts: warm-up recurrence, refactor to closure, retrieve tree structure, derive a leftPenalty variation, implement that variation) due Wed 9/23, with §2.5 as Monday's class reading and §12.1-12.3 as Wednesday's class reading, plus this log entry due Mon 9/21
    - plan A: read both §2.5 and §12.1-12.3 up front over the weekend, write the log entry off that reading, then do all 5 assignment parts Mon-Wed once the reading's already done. Pro: walk into every class already prepped, no surprises going into Wednesday. Con: writing the log before touching any code makes it read thinner, and it's not how my best entries (karatsuba, locator-heap) actually happened
    - plan B: skip reading and start Part 1 straight off the given pseudocode since it's self-contained, then circle back to §2.5 afterward and let the assignment itself drive when I actually read. Pro: mirrors how karatsuba went for me, code-first grounds the abstract stuff. Con: if the spec publishes late or Part 1 takes longer than expected, reading gets squeezed in later than ideal
    - plan C: split by day like my Project 3 hybrid strategy, with Tuesday reserved as a dedicated buffer/derivation day specifically for Part 4 (the leftPenalty variation), since that's the piece most likely to be this assignment's "recursion trees didn't click" moment. Pro: insurance against a repeat of last week's crunch. Con: a more rigid schedule, less room to lean into whichever mode (reading or coding) is actually working that day
    - plan G (the hybrid I landed on): read §2.5 tonight (Saturday) only, and start this log entry off that reading same night. Tomorrow (Sunday), open the assignment and do Part 1 cold off the pseudocode, then come back and finish this log entry tomorrow night using both the reading and whatever Part 1's coding surfaced. Monday is class + Parts 2-3, Tuesday is Part 4 derivation + implementation, Wednesday morning is Part 5 plus a quick read of §12.1-12.3 before class, then screenshot/reflection/submit Wednesday
    - ultimately I think G is best: it keeps A's advantage of not walking into Monday's class cold, but the log entry itself doesn't get written until it has real code-contact behind it (B's advantage), which is closer to how my strongest past entries actually got written. It also still leaves Tuesday free enough to absorb overflow if Part 4 turns out to be the hard part, without needing to name that in advance the way plan C does
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 20
- Confidence: 4, confident in the plan, less confident yet in Part 4 since I haven't seen the incomplete pseudocode I have to complete myself

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:







