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

## Learning Log 5 kickoff question

- Question/Problem: How can I remember the jist of Prim's vs Djisktras graph algorithms? 
- When Identified:11:45pm 9/9/2026
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:

## 

- Question/Problem:
- When Identified:
- Importance:
- How to Learn:
- Insight/Answer:
- Hours Spent Learning:
- Minutes Spent Documenting:
- Confidence:







