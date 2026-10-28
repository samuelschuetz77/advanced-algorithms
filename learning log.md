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
- How to Learn: lay out a few possible plans for the week, compare them to what has actually worked for me before, then pick one
- Insight/Answer:
    - The week has three moving pieces: Learning Log 7, the Optimal BST assignment due Wednesday, and the assigned reading.
    - Plan A: do all the reading first, then start the assignment after class.
    - Problem with A: my best learning logs usually come from wrestling with code, not only reading before coding.
    - Plan B: start Part 1 from the pseudocode, then read once I know what is confusing me.
    - Problem with B: if Part 1 takes too long, the reading gets pushed too late.
    - Plan C: split the assignment by day and keep Tuesday open for the hardest derivation piece.
    - Problem with C: it is organized, but maybe too rigid if one part takes longer than expected.
    - My actual plan: read JEA 2.5 Saturday, start Part 1 Sunday, then use the coding struggle to finish this log.
    - Then Monday is Parts 2-3, Tuesday is the hard derivation piece, and Wednesday is final cleanup and submission.
    - This plan feels best because it gives me some reading context without making the log feel detached from actual problem solving.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 20
- Confidence: 4, confident in the plan, less confident yet in Part 4 since I haven't seen the incomplete pseudocode I have to complete myself

## Sunday 9/20/2026 : Learning Log 7

- Question/Problem: How do I figure out what an optimal Binary Search Tree is actually optimizing, and why do key frequency, root choice, and left/right subproblems change the total cost?
- When Identified: 9/20/2026 7:30am
- start time: 7:30am 9/20/2026
- Importance: 5
- How to Learn:
    - I tried to do this as an audio-first lesson, but I realized pretty quickly that binary search trees are too visual for me to understand time-effectively only through voice.
    - I used a tiny anchor example with keys A B C D E and frequencies 2 1 1 2 3, then worked through what happens when different keys are chosen as the root at first through an audio conversation with ai.
    - When the voice lesson was not clicking, I switched modes and had ai make it visual by generating a pdf with diagrams: tree diagrams, left/right split tables, a cost table, and then code. I had ai voice enabled so it could answer questions as I looked at the pdf it generated.
    - I found this questioning / visual document strategy extremely effective and cost efficient for my learning. Very excited about the implications of this learning strategy!
    - I compared what I learned back to the textbook section after the idea was more concrete. JEA section 2.8 has the recurrence and the formal explanation, but it is not slow/visual enough for the exact part I was confused about.
- Insight/Answer:
    - The first big thing that clicked is that Optimal BST is not asking me to search for one particular key right now. It is asking me to design a tree that will be used for many future searches.
    - I originally thought frequency might mean there are multiple copies of the same key in the tree. That was wrong. Each key appears once. Frequency means how often that key is searched for in the workload. So A with frequency 2 means one A node, searched twice, not two A nodes.
    - Another thing that clicked is that we start with sorted keys plus their frequencies, not with a finished BST. The sorted order is fixed, but the shape of the tree is not fixed.
    - The BST rule I need here is simple: for any root, smaller keys go somewhere in the left subtree and larger keys go somewhere in the right subtree. "Somewhere" is important. If A is the root, B C D E are in A's right subtree, but that does not mean every edge after A has to be a right edge. Inside that right subtree, those keys can still branch left or right as long as the BST rule is preserved.
    - SL 1 finally made sense as: try every possible root. For each root, split the keys into a left subproblem and a right subproblem, recursively solve both, add the cost, and keep the cheapest result.
    - The cost idea clicked when I stopped thinking about the tree as just shape and started thinking about repeated searches. Cost is frequency times comparisons. A frequent key deep in the tree is expensive because I pay that extra depth over and over because you have to start at the root node and do more comparisons to get to the bottom of the tree where is high frequency node lives (in a place it shouldn't actually live)
    - For the anchor example:

        keys:        A B C D E
        frequencies: 2 1 1 2 3

      the optimal tree from the visual walkthrough was:

          D
         / \
        B   E
       / \
      A   C

      The cost is 19:
        - D: 2 searches * 1 comparison = 2
        - B: 1 search * 2 comparisons = 2
        - E: 3 searches * 2 comparisons = 6
        - A: 2 searches * 3 comparisons = 6
        - C: 1 search * 3 comparisons = 3
        - total = 19
    - The part that helped most was realizing that D as root can beat a more obviously "balanced-looking" idea because E is searched often and D/E staying near the top matters. The optimal tree is not necessarily the prettiest balanced tree; it is the one with the lowest weighted search cost.
    - The recurrence now has a meaning instead of just being symbols:

        OptCost(start, end)
        =
        best left subtree cost
        + best right subtree cost
        + sum of frequencies in the current range

      The sum of frequencies gets added because every key in the current range pays one comparison at this level before the recursive subtrees account for deeper comparisons.
    - The biggest meta-insight is that some algorithm topics are not good audio-only lessons for me at first. For tree problems especially, I may need a visual anchor before the recurrence or code will feel real.
- Hours Spent Learning: 1
- Minutes Spent Documenting: 20
- Confidence: 4, because the basic root/frequency/cost idea finally clicked, but I still need to implement the recursive function and then extend it to returning the actual tree structure.

## Sunday 9/20/2026 : Learning Log 7

- Question/Problem: Is JEA 2.5's Text Segmentation algorithm rearranging letters to find words (like Scrabble), or something else?
- When Identified: 9/20/2026 8:30pm
- Importance: 2
- How to Learn: worked through it in conversation while reproducing the Splittable algorithm from the reading in code
- Insight/Answer:
    - I had it backwards: the algorithm never rearranges anything. The letters stay locked in their original left-to-right order the whole time.
    - The only thing the algorithm is choosing is where to cut the string into consecutive pieces, not which letters go together out of order.
    - This connects back to the reading's suffix-independence point: past decisions (which cuts you already made) stop mattering, only how far into the string you've gotten does, and that only makes sense if the string's order is fixed to begin with.
- Hours Spent Learning: 0.25
- Minutes Spent Documenting: 5
- Confidence: 2, marked weak on purpose, planning to rewrite this entry

## Monday 9/21/2026 : Learning Log 7

- Question/Problem: Why is the base case in the Optimal BST recursive function start > end instead of start == end?
- When Identified: 9/21/2026 4:15pm
- end time:9/21/2026 5:15pm
- Importance: 5
- How to Learn:
    - Work through the smallest confusing case by hand instead of staying abstract.
    - Use the A B C slice with indices 0, 1, 2 and choose A as the root.
    - Plug those values into the recursive left call solve(start, root - 1).
    - Compare what start > end catches versus what start == end catches.
- Insight/Answer:
    - The key step was plugging in the numbers. If the slice is A B C and A is chosen as the root, the left recursive call is solve(0, -1).
    - I first thought solve(0, -1) might mean the same thing as solve(0, 0), because in Python a[-1] means the last item. That was wrong here. The function is not using -1 as a list lookup. It is using start and end as boundaries for a slice of keys.
    - solve(0, -1) means "the slice that starts at index 0 and ends before index 0." There are no keys in that slice. It is an empty subtree.
    - start == end would only catch a one-key slice, like solve(2, 2). It would not catch solve(0, -1), because 0 == -1 is false.
    - Empty child slices happen whenever the chosen root is at one end of the current slice. For example, choosing A has no left subtree, and choosing C has no right subtree.
    - That is why the required base case is:

        if start > end:
            return 0

      An empty subtree has cost 0.
    - A start == end case can be added as a shortcut, but it is not required. If solve(2, 2) runs normally, the only root is index 2, the left and right calls are empty and return 0, and the total becomes 0 + 0 + freqs[2]. That is exactly the cost of a one-key tree.
    - The simple way I understand it now is: start > end means "no keys left," so return 0. start == end means "one key left," which the normal loop can already handle.
- Hours Spent Learning: 1
- Minutes Spent Documenting: 10
- Confidence: 4, because the empty-slice case finally makes sense, but I still want more practice recognizing this pattern without help.

## Monday 9/21/2026 : Learning Log 7

- Question/Problem: Can I find the cheapest Optimal BST with a shortcut formula instead of trying every possible root?
- When Identified: 9/21/2026 5:45pm
- Importance: 5
- How to Learn:
    - Start with tiny three-key examples where every possible tree can be checked by hand.
    - Test the formula I came up with against different frequency layouts.
    - Compare frequency-by-depth cost against the recursive "pay sum_slice_freqs, then solve the subtrees" view.
- Insight/Answer:
    - I came up with a possible shortcut for three keys: sum_slice_freqs + (sum_slice_freqs - max_freq). My thought was that the highest-frequency key should be the root, and then the other two keys would each be one level below it.
    - That shortcut works for frequencies 1, 5, 1. The biggest frequency is in the middle, so B can be the root with A on the left and C on the right:

          B
         / \
        A   C

      The cost is 5 * 1 + 1 * 2 + 1 * 2 = 9, and the shortcut also gives 7 + (7 - 5) = 9.
    - But the shortcut does not always work. With frequencies 1, 1, 5, the biggest frequency is C, which is on the end. If C is the root, both A and B have to go on C's left side because both are smaller than C:

          C
         /
        A
         \
          B

    - In that tree, A and B cannot both be immediately below C. One of them has to be one more level down. The real cost is C at depth 1, A at depth 2, and B at depth 3:

        5 * 1 + 1 * 2 + 1 * 3 = 10

      My shortcut would give 7 + (7 - 5) = 9, which is too low.
    - The insight is that frequency is not the only thing that decides depth. The BST ordering rule also matters. If the highest-frequency key is on the end of the sorted list, the other keys may all be forced onto one side, which can push one key deeper.
    - I also found a useful way to check a finished tree: start with sum_slice_freqs for the root level, then add i * freq for each key below the root, where i is how many extra levels below the root the key sits. For the C-A-B example, sum_slice_freqs is 7, A is 1 extra level down, and B is 2 extra levels down, so 7 + 1 + 2 = 10.
    - This helps me understand why the recursion works. Each recursive call pays the next layer's sum_slice_freqs. A key that is deeper appears in more nested slices, so it gets charged once per level without the code needing to track depth directly.
    - The final answer is that there is not a reliable shortcut formula. The algorithm tries every possible root because the best root depends on both frequency and where the key sits in sorted order.
- Hours Spent Learning: 1
- Minutes Spent Documenting: 12
- Confidence: 4, because I understand why my formula failed and why the recursive try-every-root structure is necessary.


## Monday 9/21/2026 : Learning Log 8 

- Question/Problem: How do I return the tree, not just its cost? (The assignment due friday)
- When Identified: 9/21/2026 10:00pm
- End Time: 9/21/2026 11:00pm
- Importance: 5
- How to Learn: I made sure I understood this particular recursion, return values, and how tuples represent a tree.
- Insight/Answer:
    - I do not need another algorithm. The same recursion can return the tree.
    - Each call returns (bestCost, bestTree)
    - A tree is (root, leftTree, rightTree). An empty subtree would be null/none.
    - An empty range returns (0, None) kinda like cdr
    - I started with appending only nodes. Each call actually nests a root around two returned subtrees.
- Hours Spent Learning: 1
- Minutes Spent Documenting: 15
- Confidence: 4, because I understand the root/left/right tuple idea now, but I still need to keep practicing reading nested tuple output without getting overwhelmed, I think im scared of the weeds here. 

## Monday 9/21/2026 : Learning Log 8 

- Question/Problem: How do I add left penalty, and can it change the best tree?
- When Identified: 9/21/2026 11:00pm
- End Time: 9/21/2026 11:30pm
- Importance: 5
- How to Learn: I made sure I understood search frequencies, left subtrees, and worked through a polynomial list of plausibele places to add the cost too in my head. 
- Insight/Answer:
    - I first thought L was added once if a left child exists.
    - Actually, every search into the left subtree pays the per L cost
    - So the extra cost is L * sum(frequencies[start:root]).
    - Add that cost when comparing possible roots.
    - Changing L can change which tree wins, not just its cost. Obviously. If you are paying a left cost it will skew trees to more right branching shapes. This has a ton of implications, it kind of makes me wonder if you could do tree animations similar to game of life. It prbably wouldn't work. 
    - Each recursive call charges its left subtree, so searches pay L for every left turn down the tree.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 10
- Confidence: 4, because I understand where the L * sum_left_slice term comes from

## Monday 9/28/2026 : Learning Log 8

- Question/Problem: Now that Friday's final-project assignment is unlocked and my canvas account is unlocked too, how should I plan this week's readings, learning logs, and presentation so we find an optimal order and streategy? [I tried to delete azure resources with claude-in-chrome and it locked me out of my school microsoft account - had to get it unblocked]
- When Identified: 9/28/2026 1:30pm
- start time: 9/28/2026 1:30pm
- end time: 9/28/25 7:35pm
- Importance: 5
- How to Learn: Understand what this week's readings cover and what Friday's deliverable requires, then find tasks that advance both.
- Insight/Answer:
    - Reading first: pros: builds NP basics and helps compare topics; con: delays the time i spend sitting with the problem i am choosing for this assingment.
    - Project first: pros: claims early and gives examples; cons: I risk jumping into a problem without undestanding np/np-hard/np-complete in general, maybe underlying concepts that would help the presentation go better friday
    - Hybrid: choose and claim a problem, then read the NP sections needed to explain it.
    - Best path: look at and claim a problem first
    - I looked for a few minutes and found optimal facility location - this is something i am really interested in - particulalry how scale.ai is finding optimal locations for military assets based on millions of data points and sensors
    - Figure out what faciliti4es and weights would be good to introduce the optimal facility location as a not too technical example
    - Use JEA 3.4-3.5 and 3.9 as a primer to get into some juicy logs wednesday
- Hours Spent Learning: 2
- Minutes Spent Documenting: 25
- Confidence: 5

## Monday 9/28/2026 : Learning Log 8

- Question/Problem: Why would a solver for NP-hard problems need a router? If we think of an NP hard problem solution as some magic black box solver what would it actually do, especially in refernce to routing to an NP problem? 
- When Identified: 5:35pm 9/28/26
- start time: same as when identified
- end time 7:40pm
- Importance: 5
- How to Learn: Compare one fixed problem the box accepts with a different problem translated into that format.
- Insight/Answer:
    - The black box was a useful abstraction for my fuzzy understanding of NP-hardness.
    - A 3-SAT box takes a Boolean formula and answers whether any assignment makes it true.
    - It answers one fixed kind of question and the reduction translates other questions into that form - but what does that even mean? 
    - I still do not fully understand why that translation establishes hardness or a good example of what translation looks like since all these problems are so tough. 
- Hours Spent Learning: 1.5
- Minutes Spent Documenting: 15
- Confidence: 3: this is hard stuff

## Monday 9/28/2026 : Learning Log 8

- Question/Problem: Does "polynomial calls" mean the box (the oracle) loops through every kind of NP problem?
- When Identified: 4:30pm 9/28/26
- start time: same
- end time 8:00pm
- Importance: 4
- How to Learn: Separate the wrapper's work, its number of calls, and the oracle's assumed response time. oracle means our black box, the magic np-hard solver.
- Insight/Answer:
    - In the oracle model, "polynomial calls" bounds how often the wrapper asks its fixed oracle a question.
      - wrapper means the program trying to sovle the original problem
        - oracle means the imaginary helper function
       - problem a (algorithm for A) must call the imaginary function for problem B a polynomial amount of times
        - And this algotrithm must both ask/formulate the questions and do its other work in polynomial time - the work is not all just the questions to that imaginary helper  
    - The wrapper must also construct its questions within polynomial time.
    - I had placed the adapting and looping inside the box; they belong to the surrounding algorithm.
- Hours Spent Learning: 2
- Minutes Spent Documenting: 15
- Confidence 3: It is keeping track of all these metaphors that is extremely confusing, and makes learning slow but I am slowly getting this I think. 

#

## [extract_from_gpt_chat] : Learning Log [fill in]

- Question/Problem: How can a problem be both NP-hard and NP-complete, and how can every NP problem reduce to it?
- When Identified: [fill in]
- Importance: [fill in]
- How to Learn: Trace the chain from an NP verifier to SAT, then from SAT to another problem.
- Insight/Answer:
    - NP-hard means every NP problem can be translated into this problem in polynomial time.
    - NP-complete means NP-hard and its proposed solutions can be checked in polynomial time.
    - I treated the labels as competing ranks; NP-complete satisfies both conditions.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence: [fill in]

# 10/02/2026 : Learning Log 9

- Question/Problem: When complexity theory says "fast," does it always mean O(1)?
- When Identified: 10/02/26
- Importance: 4
- How to Learn: Compare an ideal oracle call with the runtime required of actual solver.
- Insight/Answer:
    - 'Fast' here means polynomial time, including O(n) or O(n^2).
    - The oracle's instant answer is an assumption used to study the surrounding work.
    - I confused the oracle's imagined O(1) response with the requirement for a real fast algorithm.
- Hours Spent Learning: .75
- Minutes Spent Documenting: 15
- Confidence: 5

## 10/02/2026 : Learning Log 9

- Question/Problem: In JEA 12.7 (Maximum Independent Set), some pairs of people can't be together. I must never include two such people, and I want the largest group possible. In graph terms, people are vertices, a conflict is an edge, and an independent set has no edges between its members. Why call choosing the largest compatible group impractical when I could guess, check, and backtrack?
- When Identified: 10/02/26
- Importance: 5
- How to Learn: Trace choices with 40 people, then consider what changes when the required group size grows.
- Insight/Answer:
    - Checking 5 proposed people requires checking only their ten pairs.
    - Finding a group with no conflicts may require undoing choices 
    - Backtracking builds a group one person at a time. If the group so far already contains a conflict, it stops and undoes the last choice.
    - Biggest insight: checking a proposed group stays cheap, but the number of possible groups explodes as the list grows.
    - With a fixed group size of five, 40 people give only 658,008 possible groups, which is manageable.
    - If the group size can grow with the list, 40 people allow about a trillion possible groups.
    - My 5 person example hid this. Worst-case growth shows up only when the group size grows with the list.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 15
- Confidence: 4

## Saturday 10/3/2026 : Learning Log 9

- Question/Problem: What is my best route to Friday's robot-BST project and Monday's log?
- When Identified: 10/3/2026 3:45pm
- Importance: 5
- How to Learn: Understand what this week's readings cover and what Friday's deliverable requires, then find tasks that advance both.
- Insight/Answer:
    - Reading-first option: builds DP vocabulary and prepares multiple quiz examples; con: delays validating the robot's cost model.
    - Project-first option: exposes modeling mistakes early and creates screenshot milestones; con: leaves Monday's assigned DP examples underprepared.
    - Best path: combine project work with targeted reading, starting by hand-checking the three smallest provided robot cases.
    - Use JEA 3.4 and 3.9 to identify the project's subproblem questions.
    - Read JEA 3.1 and 3.6–3.8, comparing states, base cases, choices, and repeated work.
    - Use a real cost-model or subproblem confusion for Monday's log.
    - Practice DP explanations before Wednesday's in-class quiz.
    - Finish backtracking, memoization, and tree reconstruction before Friday, with one passing-test screenshot per part.
    - Keep greedy and MST prep scheduled, but prioritize the DP work.
    - Recheck class notes after meetings; test my understanding Friday after submitting the project.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 25
- Confidence: 5

## 10/05/26 : Learning Log 9

- Question/Problem: In the robot book-retrieval problem, how does a binary search tree relate to a flat shelf of bins? Why jump past bins without scanning them? Is getting to the root a climb up the tree that could need direction changes?
- When Identified:(Google Meet call with Harry, Oct 5, 2026, 3:41pm)
- Importance: 5
- How to Learn: Asked Harry in the meeting, then restated it myself ("the tree is just a way to pick better than scanning every book").  walk one robot retrieval by hand using only bin indexes.
- Insight/Answer:
  - The shelf is a flat array of bins. The BST is only instructions saying which bin to check next.
  - Directions mean toward or away from bin 0, not up or down tree levels.
  - Going left or right in the tree means facing negative or positive on the shelf.
  - The robot can pass bins without scanning them. It scans only at tree nodes, always at the root first.
  - Skipping a layer saves scan cost but not movement cost, because distance is measured in bin indexes.
  - I kept picturing the robot climbing the tree. Harry corrected this, and I recognated into something I can understand.
- Hours Spent Learning: 0.75
- Minutes Spent Documenting: 15
- Confidence: 5

## 10/05/26 : Learning Log 9

- Question/Problem: How many rotations does one delivery cost? Does "move 5 units" mean 5 tree levels? Do you only move one way to reach the root?
- When Identified: 4:35pm
- Importance: 5
- How to Learn: Reviewed canvas spec's rules. Discuss with Harry
  - The robot starts at bin 0 facing negative, so a root at bin 0 needs no rotation or movement and incurs no cost from either. 
  - Units are bin-index distance, not tree levels. A root at bin 5 means moving five bins. This is the simple rule
  - Reaching a root above bin 0 takes one rotation to face positive, then one move.
  - After finding the book, the robot needs at most one rotation to face negative and return to 0.
  - open for tuesday: during the search, each left or right step may need another rotation. We didn't hand check an example of this.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 15
- Confidence: 4

## 10/05/26 : Learning Log 10 : Robot BST

- Question/Problem: Why is the optimal cost for [5] equal to 10 when no target is given? Why scan the root five times? How do frequencies and the cost parameters fit in?
- When Identified: 10/05/2026
- Importance: 5
- How to Learn: Worked test case 1 with Harry and reread the spec's hint about total frequency. Suggested next test: hand-compute the [4, 3] and [4, 30] cases.
- Insight/Answer:
  - Frequencies are expected requests per day. Optimal cost is the total cost of all of them.
  - Each request pays its own scan, movement and rotation costs, so costs are weighted by frequency.
  - Every request passes through the root, so root cost uses the span's total frequency (the spec's hint).
  - The tests list the cost parameters (rotation, move, scan) next to the frequencies. Optimal cost depends on them, so it needs no target.
  - I thought the cost belonged to one search for one target. It is the whole day's cost. For one bin, that is 5 × scan cost of 2 = 10.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 15
- Confidence: 4

## 10/05/2026 : Learning Log 10 : Robot BST

- Question/Problem: Is the recursive optimal-cost function top-down or bottom-up, and what do those terms mean?
- When Identified: 10/05/2026
- Importance: 4
- How to Learn: Harry looked up the definitions during the meeting and we worked through them
- Insight/Answer:
  - Top-down is recursion plus memoization: start with the whole problem, split it, cache each subproblem's answer.
  - Bottom-up starts from base cases and fills a table until it reaches the original problem.
  - Picking a root first, then solving the left and right spans, is top-down; memoizing makes each span solved once.
  - I thought "base case hits the bottom first" meant bottom-up. Recursion order isn't the test; caching versus table-filling is.
- Hours Spent Learning: 0.6
- Minutes Spent Documenting: 15
- Confidence: 4

## 10/07/2026 : Learning Log 10 : Robot BST

- Question/Problem: What parameters does the nested recursive function need, versus what the top-level function already holds?
- When Identified: 10/07/2026
- Importance: 5
- How to Learn: Discuss with Harry
- Insight/Answer:
  - A nested Python function can read the outer function's variables, so it doesn't need them passed in.
  - Frequencies and the rotation, move and scan costs stay fixed, so only the subproblem's span (low, high) is needed.
  - The top-level function has no start or end index. The nested one needs them to name a subproblem.
  - I first thought the nested function needed frequencies too. It doesn't, because it inherits them from the enclosing scope.
- Hours Spent Learning: 0.3
- Minutes Spent Documenting: 15
- Confidence: 4

## 10/07/2026 : Learning Log 10 : Robot BST

- Question/Problem: Does the memoized subproblem need position and direction, or is the robot always at the root?
- When Identified: 10/07/2026
- Importance: 5
- How to Learn: Harry's example was a root of 10 with children 6 and 7. He was passing in position and direction. As I worked through this problem with my cousin Joel, we arrived at a solution that could derive both from parent index and grandparent index. Clever
- Insight/Answer:
  - A memoized subproblem is identified by everything that changes its answer, not only its index range.
  - Harry's claim: movement and turning costs depend on where the robot is and which way it faces.
  - Facing matters to me, since turning around costs extra. Position is still unconvincing; I haven't resolved it.
  - Open question: when entering a subtree, is the robot's position fixed by the parent's root or variable?
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 15
- Confidence: 3


## 10/12/2026 : Learning Log 10 : Krustkal's post-class analysis

- Question/Problem: If we switched edge D–E with cost 6 with H–F cost of 9, what does Kruskal's do right after skipping A–B (5)? https://drive.google.com/file/d/1Xz7vL1IgmySbF-xGg5nMJiWf1GYr0Dj1/view?usp=sharing
- When Identified: 10/12/2026 
- Importance: 5
- How to Learn: Re-trace Kruskal's by hand after swapping the two edge weights. https://drive.google.com/file/d/1Xz7vL1IgmySbF-xGg5nMJiWf1GYr0Dj1/view?usp=sharing
- Insight/Answer:
  - Kruskal's follows the sorted weight list, not whichever edge touches the tree built so far.
  - D–E (6) gets added as its own tree {D, E}, separate from {A, B, C, H}.
  - So the forest can hold several growing trees that only merge later.
  - I thought the example mostly goes in order. There was confusion about what happens when i can't connect the edge that is next up in lowest cost. 
- Hours Spent Learning: 0.33 
- Minutes Spent Documenting: 15
- Confidence: 4

## 10/12/2026 : Learning Log 10 : Krustkal's post-class analysis

- Question/Problem: When union merges two trees, does it matter which vertex becomes the root (why C and not A)?
- When Identified: 10/12/2026 
- Importance: 5
- How to Learn: Think about what responsibilites a root has in a krustkals mst solution
- Insight/Answer:
  - The root is just a name tag for the group; any member can be it.
  - In other words, the only question union-find ever answers is "are these two in the same group?" It answers by checking whether both lead to the same root. 
  - Any member can be that shared root, and the answer comes out the same.
  - Picking B or C flips the pointer direction, so internal shape does differ.
  - In other words, the pointers are the actual arrows in memory. If C is the root, B points to C. If B is the root, C points to B. 
  - The accept/skip decisions stay the same, because Find only checks "same root or not."
  - I assumed you would try both roots and recurse; it is one arbitrary choice with no backtracking.
  - The assumption was that the root choice could change the answer. It can't, so there is nothing to compare by trying both.
- Hours Spent Learning: 0.42 
- Minutes Spent Documenting: 15
- Confidence: 5

## 10/12/2026 : Learning Log 10 : Krustkal's post-class analysis

- Question/Problem: If Kruskal's just skips edge A–B, how does A still end up in the MST?
- When Identified: 10/12/2026 4:30pm
- Importance: 5
- How to Learn: Unfart brain
- Insight/Answer:
  - An MST has zero loops; loops are not minimized, they are never allowed.
  - From example Adam drew on board monday: https://drive.google.com/file/d/1Xz7vL1IgmySbF-xGg5nMJiWf1GYr0Dj1/view?usp=sharing
  - Find(A) and Find(B) both return C, so A–B would close the A–B–C loop.
  - Skipping an edge never drops a vertex; A was already connected through A–C (3).
  - I was mixing up skipping an edge with skipping a vertex; the output is a list of kept edges.
- Hours Spent Learning: 0.05 
- Minutes Spent Documenting: 10
- Confidence: 5

## 10/12/2026 : Learning Log 10 : Krustkal's post-class analysis

- Question/Problem: Is a union-find tree always one level deep?
- When Identified: 10/12/2026 
- Importance: 5
- How to Learn: Draw parent pointers for a deep tree, then compress it.
- Insight/Answer:
  - No; attaching one root under another can stack up multiple levels.
  - Path compression is occuring here and it means if we run Find(x), every node on the path from x to the root has its parent pointer set directly to the root of the tree that x is in, and also what find(x) returns
  - Every node it passed on the way gets re-pointed straight at the root.
  - So one slow Find makes later Finds on those nodes a single hop.
  - What caught my interest: union-find keeps shortening each node's path of parent pointers to its root, so later Finds stay fast.
  - Union by rank attaches the shorter tree under the taller one to stop long chains.
  - unions make trees deeper, Finds make the paths they touch shallower.
  - Every union in our trace went directly under C, so it looked flat; I have not yet traced a deep one.
- Hours Spent Learning: 1
- Minutes Spent Documenting: 30
- Confidence: 4

## 10/13/26 : Learning Log 10 : Huffman

- Question/Problem: In Huffman after we do a merge it seems like we have to put the merged sum back in order to select the next smallest pair? It seems like this introduces oppurtunities to be slow/inefficient if I'm not careful, so what is the best approach to select the next best 2. is using min first on the first min and then min again on all the other elements good enouigh to find the smallest two? 
- When Identified: 10/13/2026 5:45pm
- Importance: 5
- How to Learn: Code Huffman with two mins and then use heapq. Understand time/space complecity of each
- Insight/Answer:
    - short answer is while my two min idea could work it is slow.
    - each min would be scanning the whole array twice O(2n) -> then we figure you have to do n-1 total merges so that ends up being O(n^2)
    - also figure that our alphabet has 26 letters but emojis / other alphabets are bigger. As n grows it gets more inefficient. 
    - the other option is resorting after every merge; this is worse by my calculations? n log n * n-1 merges = n^2 log n
    - we can do better with a min-heap using python's heapq
    - if i had read the assignment I would have understood that this approach was chosen and we are to use our Project 2's min-heap priority queue with a locator dict (neat!)
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 10/13/26 : Learning Log 10

- Question/Problem: How can I remember what is a min-heap, what is a priority queue, and what is a locator dict, at a simple high level? Does a priority queue inherently need some way to measure what is more important, and in our case is that the min? Also, can a valid min-heap also be a valid binary search tree (as a visualization or structure)?
- When Identified: 10/13/2026 
- Importance: 5
- How to Learn: Ask for a plain, high-level refresher on each of the three terms.
- Insight/Answer:
    - Priority queue: a line where the most important thing always goes next, no matter when it showed up. Think of an ER waiting room: the sickest person is seen first.
    - Min-heap: one way to build that line. It is a pile arranged so the smallest thing is always sitting on top, and adding or removing something only takes a little reshuffling.
    - In the heap array, the children of the item at index i sit at 2i + 1 and 2i + 2.
    - Locator dict: a cheat sheet that says where each thing currently sits in the pile, so you can grab a specific one without digging for it.
    - A valid min-heap cannot also be a valid binary search tree, except for a tree with one node.
    - The rules clash on the left child. A min-heap says the parent is less than or equal to both children. A binary search tree says the left child is less than the parent. 
    - The heap shape forces a left child. A heap fills each level left to right, so any heap with two or more nodes has a left child, and the clash is unavoidable.
- Hours Spent Learning: 0.25
- Minutes Spent Documenting: 15
- Confidence: 5

## [date] : Learning Log [number]

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## [date] : Learning Log [number]

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## [date] : Learning Log [number]

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## Monday 10/12/2026 : Learning Log 10

- Question/Problem: What is my best route to Wednesday's greedy quiz and Thursday's Huffman assignment?
- When Identified: 10/12/2026 [time: fill in]
- Importance: [fill in]
- How to Learn: Understand this week's readings and end-of-week deliverable, then find a small number of tasks that advance both.
- Insight/Answer:
    - Reading-first option: pros?builds exchange-proof foundations and covers assigned stable matching; con?delays codec work before Thursday.
    - Assignment-only option: pros?targets rubric requirements and exposes Project 2 integration gaps; con?neglects Wednesday's MST quiz preparation.
    - Best path: assignment-centered hybrid; first hand-trace the six-symbol example alongside JEA 4.4.
    - Monday: understand prefix-free codes and weighted depths; inspect my Project 2 graph and priority-queue interfaces.
    - Tuesday: analyze alternative selection methods and representation costs; independently implement the codec and write original tests.
    - Before Wednesday's quiz: practice greedy proofs, Huffman, Prim, Kruskal, and union-find without notes.
    - Read assigned JEA 4.1 and 4.4?4.5; use 4.2?4.3 as proof bridges and 7.2/7.4?7.5 for MST review.
    - The tentative Wednesday reading is JEA 5.5?5.6; preview traversal variants before class and revisit afterward.
    - Wednesday: complete Learning Log 10 requirements and submit it and the quiz before 11:59pm Mountain.
    - Thursday: finish required explanations, codec, and original tests; submit before 11:59pm Mountain, before considering bonus work.
    - Volume 2 benchmarking is optional troubleshooting; prioritize JEA and targeted Volume 1 heap or graph refreshers.
    - Possible next question: why must a newly merged Huffman node compete with all remaining nodes?
    - Friday: distinguish union-find parent pointers from selected MST edges; explain one safe-edge exchange on a fresh graph.
    - October 14 and 16 class-note headings are currently empty; reread after class before choosing additional review topics.
    - This is a proposed study plan, not a claim that the readings, implementation, or understanding checks are complete.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence: [fill in]




## 10/22/26 : Learning Log 11.666

- Question/Problem: What does PreVisit(v) do, and is u.post the clock value when I am done visiting u and all its children?
- When Identified: [fill in]
- Importance (1-5): [fill in]
- How to Learn: Ask Gemini to explain the clock assignments, then restate postvisit as finishing the node and all its children.
- Insight/Answer:
  - PreVisit increments the shared clock and saves the new value as the vertex's discovery timestamp.
  - PostVisit increments the clock and records completion after the vertex's neighbors and all recursive child calls are handled.
  - When v is u's ancestor, event order is v.pre < u.pre < u.post < v.post.
  - For a directed edge u → v, pointing back to an active ancestor closes a cycle.
  - I understood u.post as finishing u and its children; the interval records the whole call, including recursive work.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence (1-5): [fill in]

## 10/21/23 : Learning Log 11.666

- Question/Problem: Does 'mark v' mean recording its previsit timestamp, or is it like checking a visited list in recursive DFS?
- When Identified: [fill in]
- Importance (1-5): [fill in]
- How to Learn: Compare the textbook's 'mark v' and 'if w is unmarked' with adding to and checking a visited collection.
- Insight/Answer:
  - Marking a vertex records that DFS has discovered it.
  - A visited set implements this: add v on entry, and recurse only when a neighbor is absent.
  - The mark prevents repeated discovery; the previsit timestamp records when discovery happened.
  - Next test: explain the difference between a discovered vertex and one whose DFS call is still active.
  - My question connected unfamiliar 'mark' pseudocode to the visited collection I already recognized.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence (1-5): [fill in]

## 10/21/23 : Learning Log 11.666

- Question/Problem: What is a DFS forest, and are its parent pointers and nested intervals describing the recursive call stack?
- When Identified: [fill in]
- Importance (1-5): [fill in]
- How to Learn: Ask what 'forest' means, then translate parents, ancestors, and intervals into recursive calls and returns.
- Insight/Answer:
  - A DFS forest is the collection of discovery trees produced by the traversal.
  - When DFS(u) discovers v and calls DFS(v), u becomes v's parent.
  - DFSAll starts another tree whenever its outer loop reaches an unvisited vertex.
  - The active stack shows one ancestor path; parent pointers preserve the discovery trees after calls return.
  - My breakthrough was recognizing the forest and nested intervals as records of recursive calls I already understood.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence (1-5): [fill in]

## 10/22/26 : Learning Log 11.666

- Question/Problem: Context: same video, slide "The cost of tokens". It says every token is put in the pile once and taken out once, one put or take costs T, and the total is (2E + 1) x T, about 2E x T. What does "take" mean, and what is T?
- When Identified: [fill in]
- Importance (1-5): [fill in]
- How to Learn: Map "put" and "take" onto push and pop (or making a call and running it). Then match the slide's panel of 2E puts and 2E + 1 takes to the token count.
- Insight/Answer:
  - "Put" means pushing a token onto the pile; "take" means popping it off to check and use it.
  - T is a constant: the cost of one push or one pop, including the visited check.
  - Puts total at most 2E, one per neighbor of each expanded vertex; takes total at most 2E + 1.
  - The extra take is the starting token on the first station, which no expansion wrote.
  - Total (2E + 1) x T is about 2E x T, dropping the +1 as negligible next to 2E.
  - Underlying confusion: "take" was unfamiliar wording for pop. Next test: explain why dead tokens still cost T each.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence (1-5): [fill in]

## 10/22/26 : Learning Log 11.666

- Question/Problem: From JEA 6.1, Figure 6.2: What is the difference between the two DFSAll formulations (loop over vertices vs. adding vertex s)?
- When Identified: [fill in]
- Importance (1-5): [fill in]
- How to Learn: Trace both versions on a graph where one vertex is unreachable from the first start.
- Insight/Answer:
  - Both visit every vertex; they differ in how they guarantee full coverage.
  - Loop version restarts DFS at each unmarked vertex, producing a forest of separate trees.
  - Super-source version adds s with an edge to every vertex, then runs DFS(s) once.
  - The result is one tree whose children of s are the forest's roots.
  - Real code uses the loop version; s mainly simplifies proofs by giving a single root.
  - Open question: do both versions give identical timestamps, or only equally valid orders?
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence (1-5): [fill in]

## 10/22/26 : Learning Log 11 : .5

- Question/Problem: From JEA 6.1, Figure 6.3: Why does DFS bring in a clock, is it like c# stopwatch or something else? 
- When Identified: 10/21/26 
- Importance : 5
- How to Learn: Consider the code and ask ai, try to understand what uses clock e.g. pre and post visits
- Insight/Answer:
  - The clock is a reference that increments throughout DFS and gives pre and post a time to mark, the clock never goes backwards just like time, its just a counter. 
  - The intervals just span the range when the previsit is recorded (what was clock at when we started pre for a vertex), and when post visit (what waws clock's value when we were done with that vertex)
  - The intervals dont overlap between vertexes; either a vertex is nested meaning the vertex that it is nested in is its ancestor or its part of a different tree entirely.
  - Crossing is impossible because a vertex cannot finish while a child call is still open.
  - In the pseudocode, that arrow is equivalent to =; I hadn't realized that. 
  - The intervals weren't immediately intuitive because my mind was hung up on the fact that we were bringing a alleged c#-like-stopwatch into this algorithm.
  - Instead clock is just a place to record pseudo-timestamps for enters and exits of a vertex.
- Hours Spent Learning: 0.25
- Minutes Spent Documenting: 10
- Confidence: 5 

## 10/22/26 : Learning Log 11 : 1

- Question/Problem: Why does A’s interval end at 22 when I only counted 11 vertices? What do these intervals actually represent?
- Context: JEA figure 6.4 including the interval diagram
- When Identified: 10/22/26
- Importance: 5
- How to Learn: Trace DFS in 6.4 by hand and try to think through the intervals marking pre and post 
- Insight/Answer:
  - Preorder records when calls start; postorder records when calls finish.
  - Because each vertex has two main actions (entered and return), each action becomes a clock incremenet. 
  - A’s tree contains 11 vertices; 11 vertices * 2 clock increments/vertex means we arrive at clock 22 when A and the tree are completely finished
  - Already understand that all children must be done before a parent can finish, which explains why we have nested intervals.
  - Before a sibling can start the other sibling and all its children must be done.
  - This is why O finishes before sibling P starts; both calls happen inside L’s active interval.
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 10
- Confidence: 5

## 10/22/26 : Learning Log 11 : 2

- Question/Problem: I wanted to understand why a new tree would be created so I considered the following: Why does E start a new DFS tree, while B is another recursive call within A’s tree?
- Context: Following DFSAll into A’s search and then E’s search.
- When Identified: 10/22/26
- Importance: 5
- How to Learn: Follow the calls from DFSAll into A’s search, back to the outer loop, and then into E’s search.
- Insight/Answer:
  - DFS records discovery relationships; it does not choose or care about a shortest or “best” tree. It wants to travel to each node once in a way that prioritizes beelines to the leaves/sinks.
  - An unvisited neighbor is a vertex connected by an outgoing edge that DFS has not reached yet. 
  - Calling DFS on an unvisited neighbor makes it a child of the vertex we came from (graph -> tree repressentations), in the same tree of discoveries from this starting call.
  - You can see this inside DFS(u), where v is a neighbor of u:

    if v not in visited:
        parent[v] = u
        DFS(v)

  - Finishing one leaf does not finish the tree; earlier calls may still have unexplored neighbors.
  - After A’s entire search returns, DFSAll continues checking vertices and skips those already visited.
  - E starts a new tree because it remains unvisited when the outer loop reaches it.
  - The distinction is who calls DFS: another active vertex creates a child; the outer loop starts a root.
  - The other short answer to my original question is that there is no incoming arrows to e or any of the nodes connected to e by green arrows from any nodes on a's green tree
  - these graphs are distinct not because they dont have any connections to nodes from a's tree's but because the nodes they do connect to on a's tree have already been explored.
- Hours Spent Learning: 0.33
- Minutes Spent Documenting: 15
- Confidence: 5

## 10/22/26 : Learning Log 11 : 3

- Question/Problem: Are blue forward edges skipped within one tree and gray cross edges skipped between different trees?
- Context: From JEA 6.1, Figures 6.4 and 6.5.
- When Identified: 10/22/26
- Importance: 5
- How to Learn: Compare T -> V and W -> V in Figure 6.5 with E -> F in Figure 6.4.
- Insight/Answer: 
  - A forward edge (blue) points to a descendant discovered through another path within the starting vertex’s recursive search.
  - We don't travel a blue edge because while recursively gunning it straight to a first leaf node we already discovered the node the blue arrow points to
  - In Figure 6.5, T reaches V through U, so its direct edge T -> V becomes a forward edge.
  - A cross edge points to a finished vertex in a separate branch, potentially within the same tree - but could be a different tree. 
  - In 6.5, W -> V crosses two sibling vertices; in Figure 6.4, E -> F crosses between trees. 
  - When I saw the first gray cross edge in figure 6.4, I assumed that they were only for seperate trees, but in figure 6.5, when I saw a cross edge between sibling vertices of the same tree it disrupted my understanding of what a cross edge really is. 
  - The ground zero parent of a tree is the node that starts the tree.
  - Having differing ground zero parents can be a hallmark of a cross edge, but not an absolute requirement
  - The most important insight to distinguish forward and cross edges is that you should use ancestry, not whether their endpoints belong to different trees.
  - The particular question is: are the nodes that make up these edges ancestors of each other 
- Hours Spent Learning: 0.5
- Minutes Spent Documenting: 25
- Confidence: 5

## 10/22/26 : Learning Log 11 :  4

- Question/Problem: How can V start before U for an edge U -> V?
- Context: U and V are common variables used in code and the book and elsewhere to describe an edge from U to V. I was assuming U had to be the ancestor. Used Figure 6.4 in JEA to reason through this.
- When Identified: 10/22/26
- Importance: 5
- How to Learn: Use the edge G -> A in Figure 6.4 in JEA, substituting G for U and A for V, then compare their pre and post times.
- Insight/Answer:
  - U and V identify an edge’s starting and ending vertices; they do not automatically identify parent and child.
  - For G -> A, U is G and V is A.
  - A is already active when G starts, so G -> A points back to an ancestor.
  - A.pre < G.pre < G.post < A.post? Yes, satisfied
  - The tree path A -> B -> F -> G plus G -> A forms a cycle. We don't like cycles, but to answer my question U happens to be a descendent of V here.
  - I was thinking too tree and not enough graph
- Hours Spent Learning: 0.25
- Minutes Spent Documenting: 10
- Confidence: 5

## 10/22/26 : Learning Log 11 : Entry 5

- Question/Problem: Why is it 2E + 1, and why does every undirected track count twice?
- Context: I was watching a self-made explainer video on whatever-first graph search (Video 2 of 6, based on Erickson's Algorithms, section 5.5, p.219). It uses a 7-station, 12-track "metro map" and keeps a pile of "tokens", each a pending note saying "go visit this station". At 0:48 it asked how many tokens get written in total. The answer is 25.
- When Identified: [fill in]
- Importance: 5
- How to Learn: Relate tokens to recursive DFS calls, which I already understand. Then count tokens on the metro map from each station's neighbor list. Suggested next test: count them on a directed graph.
- Insight/Answer:
  - A token is one pending "visit this vertex" request; in recursive DFS it equals one call.
  - Each expanded vertex writes one token per neighbor, so total tokens equal 1 plus the sum of degrees.
  - An undirected edge sits in both endpoints' neighbor lists, so it is written once from each end.
  - Metro map: 2 x 12 + 1 = 25 tokens; with directed edges it would be E + 1.
  - Underlying confusion: the doubling comes from how undirected edges are stored, not from DFS itself.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence: [fill in]

## 10/22/26 : Learning Log 11 : Entry 6

- Question/Problem: Does a token still get written when its station was already visited, and does that "dead" call (a dead call is a when we make a call but we can see it was already visited) count toward the 25 tokens placed in the pile over the whole search? Total number of requests added overall (how many tokens did we add to the bag)
- Context: Chapter 5 JEA video I had claude generate (whatever-first search, token pile, metro map with 7 stations and 12 tracks).
- When Identified: 10/22/26
- Importance: 5
- How to Learn: Trace one full run on the metro map and label each token live (visits a new station) or dead (station already visited). 
- Insight/Answer:
  - A token for an already-visited vertex is still written, taken out, and checked, then discarded.
  - Dead tokens count because this version checks "already visited" only when a token is taken out.
  - Dead calls are why DFS runs in O(V + E), not O(V).
  - On the metro map, 7 tokens do real work and the other 18 of 25 are dead.
  - Underlying confusion: I saw that a call that does nothing still costs work, so it must be counted.
- Hours Spent Learning: 0.33
- Minutes Spent Documenting: 15
- Confidence: 4

## 10/22/26 : Learning Log 11 : Entry 7

- Question/Problem: What does "Preprocess" mean in the DFSAll wrapper, and why does the wrapper unmark every vertex first?
- Context: From JEA 6.1.
- When Identified: [fill in]
- Importance: 5
- How to Learn: Fill in Preprocess, PreVisit and PostVisit for pre/post timestamps, then for counting components, and compare.
- Insight/Answer:
  - Preprocess, PreVisit and PostVisit are empty hooks; each DFS-based algorithm fills them in differently.
  - Preprocess runs once before traversal, typically setting up variables like clock = 0 or count = 0.
  - Unmarking gives a clean slate; leftover marks would make DFS skip vertices it never visited.
  - The DFS skeleton stays fixed; only the hooks change between algorithms.
  - I read Preprocess as a mysterious step; it is just setup, left open on purpose.
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence: [fill in]

