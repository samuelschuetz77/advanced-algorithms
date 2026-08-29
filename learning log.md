### Learning Log

## Wednesday 8/26/2026 : Learning Log 1

- Question/Problem: I really have some anxieties about catching up with algorithms from the intro course, I understand it takes me a while to pick these things up so I guess I'm looking for a happy path zero to proficient hero for all those basic algorithms. My questions are:
- which algorithms should I hone in on that can quickly get from basic bubble sort to dynamic programming problems? 
- How can I use my time well and memorize what these algorithms are doing conceptually - so these concepts are solid in my head?
- I know I'm going to have to refresh on python so I'm sure there is some path to kill 1+ (my deficiency) birds per stone, what are they?  
- Part of this question, I'm expecting might be guided by what you tell us on Monday 8/31/2026 or whats updated in canvas. (I'm asking this before the course schedule was/is posted.)
- When Identified: 8/26/2026 3:30pm
- Importance: 4
- How to Learn: - sprint 1: selection / insertion + conduction proof reveiw
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
- Hours Spent Learning: 1.5
- Minutes Spent Documenting: 20
- Confidence: 3, I'm still not sure this will work with every list 

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





