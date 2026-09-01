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
  - took a while to understand it, I think I got it to work. Looks like i needed to add that to my other
  -  looks like i need to add this to if not lst:
        return [] too
  - my question of whether this was a correct implementation was correct after i fixed that empy list bug, it worked in your full test harness
- Hours Spent Learning: 2.5
- Minutes Spent Documenting: 10 
- Confidence: 4

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







