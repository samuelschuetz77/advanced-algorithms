# Archive metadata

Source: https://docs.google.com/document/d/1oo6oJ6LcVNZhEG991rreNkrtUS0ZmU52V9LPV70_CvE
Meeting start: 2026-11-16 10:33 MST (America/Denver), verified from document title and source date metadata.
Classification: Advanced Algorithms lecture (NP-hardness reductions, circuit satisfiability, decision-to-search, complexity theory and integer linear programming).
Duration evidence: transcript terminal marker 00:50:17, not independently verified recording duration.
Complete available source text follows, including timestamps and machine-generated caveats. Embedded images are linked to original tabs, not downloaded. Source sharing unchanged.

---

## Source tab: Transcript

https://docs.google.com/document/d/1oo6oJ6LcVNZhEG991rreNkrtUS0ZmU52V9LPV70_CvE/edit?tab=t.mddedr2dzz3g

Nov 16, 2026
Untitled Meeting - Transcript
00:00:01

In fact to saw that I had a different assignment in there where I was going to have you actually do your presentation on your for your final project. It would have been a good idea. I think um even though I'm not going to have you do that this Friday, probably is a good week to spend working on that reduction anyway.


00:00:36

So, um so as we don't I don't think we have that much stuff to talk about for this week um from chapter 12. stuff. Uh let's we can spend some time in class and spend time outside class thinking about that reduction. How are you gonna reduce one of those three problems that are going to be empty hard to your problem which is going to show that your problem must empty hard and empty I'm saying both of these why is that okay like why are both of these true why is it the case that subset sum subset also is why


00:01:49

so the problems that I chose that are on the list are both because if they went then the reduction won't be would go both ways. Uh yeah, if the reaction does go both ways, then actually just forget about that. Don't worry about it. Um okay, so um just really quick, let's have you go around just tell again everybody what your problem is.


00:02:24

Knowing what everybody else's problem is going to be useful because hey, maybe they're working on the reduction. You can see that it's kind of similar. In fact, you might even say, "Hey, if I can reduce their problem to mine, they can help me learn how to reduce that to their problem." And I've got kind of this, you know, shoe jump if you want.


00:02:42

Or maybe you'll be able to see. Oh, okay. So, SAT um reduces to so what's your problem? Yeah. TSP. And then um and and then I can see how ts is very similar for which is yes almost like cheating. Um the difference between this is a cycle and this one is like cycle that the difference here has to be a cycle.


00:03:19

right there. I think you described it as a cycle and that was why I was those two. But Hamiltonian is you have to connect all edges. Yeah, you have to connect all but it doesn't care about distance or edges. So yours mine but mine takes that into account. Yeah, exactly. Does it have to be a cycle?


00:03:46

Uh I don't think so. No. Yeah, because it would it wouldn't go the same twice. Well, one of them says like you start here and then you have to end back there. Oh, yes. Yeah. Yeah. Yeah. So has like a budget plus it's a cycle but very similar.


00:04:02

So you know TSP and you might be able to see that. Oh yeah, I can see actually a way to directly do similar thing and go straight to Hamiltonian path or just do you got to learn how to do it and then I'm going to do this other thing. So it's worth like knowing what each other are doing for this because it'll help you out teach you how to do steps.


00:04:31

Um, so just to get everybody thinking about, may can you share remind us what your problem is? Say the name as well as a quick explanation of what your problem is. Uh, go ahead. Well, I it's kind of funny also because n queens I know does reduce to Hamiltonian cycle. That's how they proved that it was kind of funny.


00:04:56

the desert is always der that that is like maybe the canonical one where the first person to discover true that used a particular so n queens is if you have a chess board that is n by n and you play well so it's that technically the problem is called um n queens completed is it completed like yeah because it's it's can an arrangement of queens on an n byn board be completed to satisfy that no queens are attacking each other.


00:05:30

Um, so you get an n byn board with some number of queens and it's a random number. If it's one you can definitely do it and then it's after one it gets harder. Okay? Because there's a pattern and so with one you can do it and if and if they follow the existing pattern you can do it but then if they're randomly placed and there's like five of them on a 10 x10 board it's really hard to tell.


00:05:53

Interesting. And and maybe with a lot of these even like I don't remember like graph coloring I think it was like three color is hard you know can it be colored with just three it's like wow so like I'm think guessing maybe even like with the small exit five it's already hard. Yeah it gets I mean if you have two queens it's already hard.


00:06:15

Okay. Right. Like it doesn't matter like the one queen is just easy because there's an existing pattern to solve it on any board of any size. Um so with one you just start the pattern there and then it's fine but n is always the end by yes okay cool. Um Sam remind us what you uh optimal facility location.


00:06:41

Okay. So the input looks like possible facil facilities have locations and do you can do yeah you can do possible facilities and then you can do uh like you can minimize you could do a minimum or you could do a maximum and it's based off just however you want to build it. I chose to do some weird thing that AI suggested.


00:07:20

But okay, but uh you're basically deciding should I put a facility here? Yeah. And it's going to service. Yeah. If you do put it there, there's costs. Yeah. So facility I'm behind on that. I I probably should have done those ones. I've been working on the pro the uh the other homework assignments, but I'll get to it.


00:07:47

Okay. So, K here is kind of path. Describe really quickly what that means. Um it's is there a path that connects all that doesn't have Okay, Ben, you already explained yours. disrupt the salesman person and uh um you said it's what's the for a budget can I do a path that connects everybody for this budget and back to the so it's almost Hamiltonian cycle except for that you've got a budget that the cycle version would be an obvious budget to choose slide and


00:08:35

it is trying to find with given by graph with either as a mine or it has a number lines nearby it solution that will satisfy all the mines next to next to a number without given the numbers and the question is And you have minus the numbers are only partial right what are only partial you don't have all numbers okay so given some number is there a layout of bombs yes so we're just as we are a lot of what we have from the reading this week is kind of review.


00:09:30

We're going to take advantage while we're doing talking about the hard stuff to also have in your minds looking about like should be working on your reduction to prove that your uh problem is hard by proving that it's verifiable and quality time and also thinking about how you're going to reduce How do those two problems to your problem? And so talking about how it's useful to know what everybody else's problems are.


00:10:02

This if you can see a way to reduce their problem to yours, they can see a way to reduce to theirs then you can have them help you make. Okay. And Chinese. Okay. Where you have to start from all the paths. So you you have a why you want to visit all paths.


00:10:41

And then well I think that's the way it but for now you have ages like two two ages and I'm making it mix so that it becomes so you can have a oh okay that's right so you have both undirected edges as well as directed edges in yours you start from one place and you come But I only have to visit this edge one way or the other.


00:11:19

Yeah, it's apparently that but that could be both ways. It could be both. I could go both ways but you know one could be both ways. Yeah. And the one is like only one way traffic. This one goes only one way. Yeah. Yeah. But you have to at least once.


00:11:45

At least once. Yeah. It's interesting that that's what makes it because it sounds if it weren't for that then we're it's like we're doing something similar It's easy until we did the mix. I just called Can you present right now? Sure. Perfect. Yes. Problems. No, it's just that she hasn't presented yet and I always keep forgetting.


00:12:15

This is like a perfect like it because it's one of the only Why can't you do Sudoku? Well, I haven't been able to. It's just I can only do up to Well, I don't know. Maybe. So this one feels easier to scope. It could just be that the average size of the puzzles like average I get is actually technically lower.


00:12:59

Yeah. But I guess I think it is interesting that it won't I don't know if I'll be able to get out of full screen. Okay. I No, you're you're good. It's just this interface is terrible. It's like Yeah. I always feel like no it's just like it's so slow to like expand down by the time I I give up on the fact that it was good.


00:13:33

So I used to like so um so the problem is given a rows by col grid and clues I'll explain later for each row and column is there exclusion for this grid and I think the part so the puzzle is called named after the greater than like who was one of the inventors and There are great games that have so example one.


00:14:13

So you see uh when I say clues, you see those like little numbers that are on top of every column or like on the side of every row. Those are clues. And those numbers indicate the length of each cluster or the length of each one which is a word prefer to use its. So basically let's look at the first row.


00:14:37

You see how at the left there's two one all your visible. Okay. Okay. You see this? You see this? Okay. Two one. That means there is a cluster of lengths two, some gap and then a cluster of length one. For example, uh this column clue right five.


00:15:00

It means there's just one cluster of five and you know. So this row say one two means there's a cluster of one and then a cluster of two. It doesn't say anything about how long the gas is. you're just supposed to like um use all the clues together to deduce the um conclude whatever like where it should be getting and technically um some puzzles like some sets of uh ro clues and clues may have more


00:15:32

than one solution and just mention this and um puzzle makers should typically check if there are more solutions before they put in their Um, example two, is there a solution for this? And there is indeed a solution that is compatible with the set of clues that we have. So the output is yes, there is valid solution. Uh this example has no valid solution because uh if you think about it two loose al so you can see it used to be valid um that I just added my two there.


00:16:15

So uh two so these two should be filled right correct this column has a one which means either one of these would be filled but that's not compatible with any of these clues not all at once. So we would say the set of clues does not have a bad solution. That sounds that sounds like when she was talking about that it made me think of circuits all right.


00:16:41

Okay. These both have to and maybe I don't know. Wait, are you with John's account on this? They cancel. Say no. Jonathan, go away. So for each scan left to right compared to that go value then repeat for each column except only if all row close to column clues um match with what you find in the solution.


00:17:30

So theoretically that would cost about O of N squ or O of R time C. So it's just looking at every cell per each row, per each column. It's just this pretend the numbers aren't there. finding if uh like the information here is compatible with the column that is in. find the information here isible but the row isn't it also gives you a good way to generate it's all you do is just generate the picture


00:18:06

yeah solution so if the numbers from here we say oh two and one yeah it broke the problem it matches it's correct it works So root for solution um algorithm you basically try every possible combination and because one cell is either filled or not filled there are two options and there are n cells that will be about o to the power n forcing so yeah first class it be all zer so No fill at all.


00:18:53

That's verification. Second pass. Every every cell is filled except I said this one or whatever. Yeah. So that okay so this okay so it's further elaborating on the idea of what would happen if they did the boot for solution. So generating a solution candidate is also all up to the end just because there's only two options is like um which of the three problems subset sum three set or three coloring coloring is going to be easiest to reduce to your problem.


00:20:10

Um, I just binary plastic problem. Okay. Well, let's just review a few things um from here. and if you have ideas about your projects um or questions. So um we already talked about um this this problem where somebody comes and they give they have this box. It's got some boolean circuit in there.


00:20:56

They've got the whole schematic for you. And their question is, well, here's the inputs. Is there any way to turn the light on with these inputs? Um, so that's the question. This is circuit sap. And we know there's there's one way to answer this question, which is try all of the inputs.


00:21:20

And um how hard could this be? Right? There's let's say there's only five there's only five inputs. We try both versions of this on and then the rest is off and then the rest. So there's two * 2 * 2. Yeah. 32 options. Okay. So we could try them all.


00:21:47

And um oh okay so you're saying well if we got the circuit then we could say well I've got let's say an and gate here or something like that right so you say I know that this is has to be on so that this endate has to be on so one of these has to be on all of these have to be on yeah okay so all these have to be on and then Yeah.


00:22:17

Interesting. So, but the truth is that it's not easier. Um, why is that? Why is it not easier? Oh, the problem is that anywhere where we have a four, you're not having one. So, they can just keep that one. Now I know well I know they don't both have to be on only one of them has now I'm kind of back to the situation of everywhere I have or gate I've got to essentially try both versions oh they fixed the or is it this one that has to be on or is it this one that has to be


00:22:58

on both oh okay so now I've got three choices now I've got to try this one on this one on or both of them okay so I got three choices for or but um so let's see um we just want solution right again we just want false solution we just want a solution is there a solution that's right yeah so anyway so this is circuit set and it is NP hard meaning what does that mean to be NP hard np you can verify NP we can verify in poly times.


00:23:41

NP hard means with a solver to an NP hard problem we could solve any NP problem in polomial number of calls to that plus polomial. Does anybody remember how we said that they that we could prove? How was this originally proved that circuit sat could was NP hard? How do they prove that any NP problem could be solved by a reduction to circuit?


00:24:18

Kind of mentioned it, but here's the idea. The idea it was the idea was if it's NP okay if it's NP that means we can verify it poly time with the touring machine we can take a regular touring machine a regular circuit okay if if we can if we can verify poly time we'll take the code for the verifier and make hardware that does that code and that hardware is going to be poly size in the input you don't have to put more than poly number of gates in there and then we can run it in poly


00:24:54

timer and therefore we can make a circuit that will output one if and only if the input is verified to be correct. Okay, so what does that mean? It means that what does that mean? So this is a circuit set problem. The question is, is there an input that makes our verifier happy? Is there an input that makes our verifier happy?


00:25:23

This is a circuit set instance and uh circuit stack would then if circuit set could answer that question, we could answer the question of uh whatever is that can we find a ver you know solution that will verify this problem or that problem. Any problem that you any problem that you have make a verifier for it that if given a correct solution would say be happy think that we now plug that into circuit set and they'll say yes this uh uh yes you can make


00:25:58

this happy okay so n heart's ambition is any problem that at least as hard as hard as problems in NP and I think the idea how we proved um it be hard or like a problem would be hard is set is at least as hard as circuit set. That's right. So that in other words we could use it to solve circuit set.


00:26:23

Yeah. Right. Because we already know that circuit set can be used to solve any problem. Right. Okay. Right. Oh so right. So that goes on the truth or like the whatever we derive that circuit that is the hardest right is the hardest in yeah right okay NP has a verifier let's make a let's make a circuit that runs that verifier that means circuit sat can tell us can we find something that will please the verifier so this was a trick tricky one and that's a little hand wavy of a proof but that's the idea of how circuit set must be


00:27:03

hard enough or good enough to solve any NP problem. So that was this one is the outlier. We had to start somewhere. Circuit sat was the place or sat some sort of in our in our version of the story. Um with our hindsight, we're going to say circuit side was our first NP hard problem that we discovered.


00:27:23

We discovered it was NP hard because it was hard enough that any NP problem would have a verifier that could then be um used as an input as a circuit to the circuit that problem. Therefore, we use circuits at to solve a and b problem. Okay, so here's the big question though. Sure, it says yes, it can be ver.


00:27:47

Yes, I can find something that will please the verifier. But how do we actually get it? What good is it? What good is it to say yes, you can if I don't actually get a solution? Is there a solution? It feels like okay, but if there is, then how do I get it?


00:28:06

Is there a way of turning on the switches? You say there is, but now I want the solution. So, how do we get the how do we do the search problem? Try if I all I have is a decision. Try all the Okay, but notice now we're not trying all this is important. We're not trying all the way all the combinations of right.


00:28:27

We just have to try one at a time. Mhm. So I only have to say if I turn this one on now I have another pro instance of SAS with an extra constraint. This has to be on. Okay. Is it still possible you know to get um to satisfy this? And if it is then what do I know about X1 true?


00:28:50

Yeah. And then if it was if there isn't then I know it must be false. Right. So in general if we have something that can tell us is there a solution we can hard code make a new instance that hard codes one part of the answer to one of a small set and now I can be sure about whether this one is breaking or not.


00:29:11

I know that that X1 is is one and I can move on. Now linear time in a linear number of calls to my solver to my yes no my decision solver I can get the search result but here is one and then remember we also talked about well sure I can find a Hamiltonian path but I want the smallest Hamiltonian path the one that I want to have I'm a traveling salesperson I want to visit all of them in this least time so now what do I I ask the decision.


00:29:46

I can I can say hey which should I go to this city first? Should I go to this city first? Should I go to this city first? So I can uh is there a way to Okay, so the question is how do I get how go go to the optimization problem if all I have is a decision solver I know I can get a search solver with the like hard code in


00:30:07

the part of the answer and how do I do the um this the optimization part then how do I go from I want to find the best if all I have is a solver that says yes or no increasing bounds right but yeah the word is budget the key word here is budget which is what meant by bounds right yeah um we just tweak the problem and say okay I won't say you have to find the


00:30:37

best the smallest path let's just say can you find a path with this budget within this budget and then if you tell me yes then I can say oh and if I want to know which path it is I'll add these additional okay can you find if I start here can Okay. Can you find if I start here and then go here?


00:30:59

Still can. Okay. I'm gonna can if I start here, go here and then I go here. Oh, I can't. Let me try. What if I go to the other one? Yes. Okay, then. Right. So, I can I can now for a given budget ask yes no questions and work through at for each variable.


00:31:15

Um, I'll just try all the options. One of them has to be okay. If there is a responsible So, this is the the way we tie together all of this. stuff back to the original to the to the decision problem which all goes back to we had circuit set known to be the decision problem is empty hard because you can use it to solve any empty problem because it had a verifier.


00:31:42

Now we have a new problem like GSP. Um how are we going to characterize how hard TSP is? Um we're going to do two things. Okay. So first well P versus NP. Do you okay please help us remember why do we why is it called NP? First of all why is it called P?


00:32:04

What is it? polinomial meaning it's a problem that we know can be solved in big O of N to the P for some power right for some so this is it's problem we know can be solved in a polomial run time so big O to some power oh sorry this is misleading the N in NP is not gonna have anything to do with this N so maybe I'll just say N to the K for um some power


00:32:37

k is a set of problems though not a set of algorithms. Is that fair? Particular algorithm might help us achieve a poly time. We just need that one algorithm. We don't even have to know what it is. We just have to know that there is one to be able to know that a problem is okay.


00:32:56

NP was an income. from it's it's not non I mean it's not non polinomial it's non what nondeterministic touring machine it's not empty yeah it's it's because a touring machine that we can uh fake it always has to say I'm out of state so remember do you guys know what a training machine actually looks is machine has like infinite tape.


00:33:32

This is our memory. Our memory is stored in a tape of this and at any point I'm like at this goes on this goes on forever. Um at any point I'm right here I'm at some position here and I can read the bit. Is it a zero or a one? And I also have another bit of memory that's finite.


00:33:55

So this part is infinite. The tape is infinite. The finite part is a lookup table that says well sorry is I have a sticky note which is my state and that holds um tells me where what state I'm in. And then for each um and I guess it's a three by I guess it's just a then I have an array here.


00:34:26

This is a touring machine where my symbols are zeros and ones. You could have uh more symbols than that. But let's pretend we just have um our symbols are zeros and ones and then we have states many states there are. Okay. So there's a fixed number of possible states in here and then and then there's a lookup table says next state.


00:34:53

So this is next state given current state. Okay. So this is my full um touring machine infinite tape. So there is some sort of infinite memory here. A finite bit of like one simp one state that I've written down. But in the table it says for each state that I'm in if I see a one what should I go to next?


00:35:22

If I see a zero, should I go to next? Um, oh, and in addition to this, uh, I guess it also has an action associated with. So, the actions are like write uh, write something zero or one and then move left and or move right. We can do two things. This is basically a D. So, we're going to be able to decide what state we are moving to and also So whether we should move left or right and whether or not we're going to write down.


00:36:00

So I guess we have three three things we do. Next state, we have next state. We have like what we write down. And then we have like left or right, left, right, or I guess we do. So So for every um state um thing that we're reading there, we're gonna have a lookup table that tells us which of those things to do.


00:36:25

Oh yeah. Anyway, that's the basic idea of what a transition is. So notice at x point we're going to do exact we're going to look it up in the table and do exactly one thing in a nondeterministic turning machine. Um let's see. We're gonna say, oh, oh, there is one other there's also finally like an accept.


00:37:10

There's a final action which is are we going to accept? There's an accepting state. So, one of these states is like we're done. You're just going to stay in there. And the question is for given input a starting part of the tape is there sequence event are we going to get to an accepting state deterministic machine set of rules prescribes at most one action to be performed for any given situation.


00:37:45

The action is going to be these three things. What are we going to write to the table? What direction are we going to move? And then what do you state? So that's deterministic. So um okay in contrast to deterministic training machine and nondeterministic turning machine the set of rules may prescribe more than one action.


00:38:22

Okay so the the actual program itself is no longer if you're in the state and this is your input you will it'll be you can choose one of these actions. Okay. So you're going to be have a set of actions that you can choose from. in some ADU flipping ones where um yes, let's see the set of per example an X on the T in state three might allow the non-deterministry to write a Y move


00:39:03

right switch to state five or write an X move left stay because there can be multiple actions that can follow from a given situation there can be multiple possible sequences of steps that the noneterministic machine starting from if at least one of these possible sequences leads to an accept state then the nondeterministic machine is accept So a regular deterministic machine is going to accept an input if running the program and eventually it ends up in a like


00:39:39

except nondeterministic means if there's one of them that ends up it will accept it. So running a nondeterministic turn machine is a little bit slow. Yeah. Are we still? Yes. Is it time? Yeah. Okay. Thanks. Um Okay. And it's Max. I know you do it in class anyways.


00:40:21

You do it. Is that the right? Yeah. Max, go ahead. You guys I don't think you should need any scratch paper, but if you do, let me know. And or if you open up like a you just want like a Xbox By the way, the punch line was just that NP means it can be solved in poly time by another.


00:41:50

I think I need actually Okay, be careful on the reduction one. The key with the max flow thing those problems not only like you need to make sure that the actual reduction to max flow will do what it what it's supposed to do. So you might know that you can solve a particular problem with max flow rather than having you have to solve them from scratch.


00:42:20

and giving you a reduction but that reduction might just think about whether it will or will not solve the problem. I do that so you won't have to come up with the answer from scratch but you have to be able to think oh yeah will that solve the problem And also you don't need to need five more minutes at the end whenever This is awesome.


00:47:21

full answer if you want it that way. This is also true. So think of NLP as being your maximizing or minimizing objective. That's your goal subject to these constraints. Yeah. But it's just it's like what changes. So this is I had an LP and I want to add another constraint which is okay. It's got to be old numbers. So think of the problem you want to solve now is the exact same LP but plus this conraint. So does that have a solution? Yeah, that's right. Does this say that the new problem has no has no best answer? It's


Transcription ended after 00:50:17

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

