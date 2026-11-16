# Archive metadata

Source: https://docs.google.com/document/d/1f3F2pbf1EYt28G4Dpz1AffUEx0sTtpkUdVAsF7m1JW0
Meeting start: 2026-11-13 11:01 MST (America/Denver), verified from document title and source date metadata.
Classification: Advanced Algorithms lecture (network flow, linear programming/simplex, max-flow/min-cut, vertex splitting and shortest-path relaxation).
Duration evidence: transcript terminal marker 00:27:25, not independently verified recording duration.
Complete available source text follows, including timestamps and machine-generated caveats. Embedded images are linked to original tabs, not downloaded. Source sharing unchanged.

---

## Source tab: Transcript

https://docs.google.com/document/d/1f3F2pbf1EYt28G4Dpz1AffUEx0sTtpkUdVAsF7m1JW0/edit?tab=t.t9g9kr7y3ogg

Nov 13, 2026
Untitled Meeting - Transcript
00:00:06

Right. Okay. So only the graphity only the total sets two question. This is the only one that actually has two things in it. both conservation at each vertex which says the sum of the variables representing the edge going in equals the sum of the variables representing the edge flows out and um did you notice that that likes to you use things like like sum some function just from Python you don't have to use any special thing just um so if you have you know uh you can use you can actually say the sum


00:00:54

let's say you have a dictionary uh which is what I recommend you have like a edge to low variable um let's say we're let's say we're looking at the constraint that says here's here's a node node B and we're going to say that the sum of the edge flow. This is a dictionary. We're going to look up the edge from some neighbor to B. This gives me a variable.


00:01:32

We add it up to four like B in neighbors in um B whatever equal. So this is a sum that we can say we can just say something like problem plus equals sum of this equals the sum of the outing stuff. Right? So in other words, since P overloads the plus operator on these variables, then the sum function inside of built into Python is just reducing over that plus operator and it will do it.


00:02:17

It will do the right thing. So this gives me it's as if I said H1 plus H2 plus H3 where those edges are they and then over here have been out. So that's kind of nice that makes that makes me wonder why is there such a thing as like a pop dictionary dictionary there but I don't know why you don't just why not just use this regular other than that anyway so yes conservation at each vertex that's what that is the capacity limits on each edge when you make a new variable you can set the capacity you know the upper and lower bound.


00:03:06

Okay, I might give you the answer. You guys should get the answer. Yeah, he'll get the answer. Conservation means that at every non-source C vertex inflow must equal outflow. Yeah. Yeah. Capacity. Oh, good. I'm glad that Yeah. Not the capacity equals the out capacity but the inflow equals the out.


00:03:34

Good. Um, and notice this thing. This would be an easy way if you run your your solver and it says, "Oh, I have a max flow of zero all the time." Probably because your source has no incoming edges and therefore no incoming flow. And you definitely can't if that has to equal outflow, you will have no outflow from the source.


00:03:56

And same thing with the sink. you have no inflow into this as so make sure you skip the source and the target in your expo. Don't add in this constraint for the source list. Alternatively, you can just type um elucinate infinite um capacity pipe that goes from the target to the source. If you did add in that edge, an unconstrained blow there, it'd be equivalent to skipping over those two notes when you go through that.


00:04:37

Well, I feel like this feels more obscure. The point of reducing max flow to LP rather than using forkerson directly is I'm curious whether what we're going to see here. What is the point avoid needing a source? Um I don't think so. Reuse general purpose solver instead of implementing max specific algorithm. Yeah, I like to reuse something that's general purpose.


00:05:12

guarantee an approximate answer. Yeah, I like that. I just don't know exactly what it is. You get a faster asmtotic running time in all cases that's not true. Obviously, if this is a general purpose more general purpose solver, then asmtoically we must be more constrained. uh there might be a chance that we can solve max flow even faster than LPS in general, but it could be the case that a general wellused LP solver might have been highly optimized by people that care about solving a problem that isn't max flow.


00:05:55

And yet now my max flow sol uh implementation goes faster on their LP solver because they went they they cared about it enough to make it fast. So it's kind of more of a practical thing that more users could lead to a better tool. Um but theoretically that tool that has to do more can't be as probably better at doing everything including my practical might better.


00:06:39

All right. If we do have time, I I think the the place where we could spend some more time is on uh looking at more applications of max flow and wanted to look a little bit how the simplex algorithm works. To clarify one thing, simplex algorithm is the algorithm that kind of looks it goes around this feasible region which is some sort of a highdimensional polygon polyte a feasible uh region.


00:07:12

It's a convex region which anybody know what that means convex region. If you put a rubber band, if you take any two points inside the region, even if it's on the corners or on the sides or whatever, any two points, the point right in between those two points is also so what it means is yeah. So what would not be convex?


00:07:43

Yeah, like a right. is to have those two points that's midpoint is not there. So convex is nice because it's kind of closed under this operation of give me the midpoint take two take two points and the midpoint is also in the region. So some things work efficiently if it's not convex. It is convex because when we chop it something in half then everything on this half is still on that uh I don't know I don't know how to um since these are straight lines we're going to


00:08:24

have a complex the simplex algorithm works by kind of just moving in the direction trying corners and moving to the next corner that that increases the objective function the most but It's actually not it's not poly time in the worst case this simplex algorithm there are LP solver algorithms on called like flipoid algorithm um that that are approve so just know that most people talk about the simplex algorithm when they talk about how LP LPS are solved but it's not actually quality time worst case states although it tends to be quite fast


00:09:13

it tends to be quality time and and quite a good time but it's there are there are cases but so I want you to know that it theoretically is quality time and I want you and I think it is valuable to think about how kind of walking the corners can be a way to find the optimal because it's always going to be a quarter.


00:09:37

But I just know that that's not that isn't the poly time solution to this problem. Let's do this problem. Okay. So pass through a flow network to be edge disjoint disjoint. This means that the edges don't you can't reuse an edge on two different paths. That's what edge disintro paths are. races going on the in the city and we're not allowed to have a race use the same road two different races the same road two different paths use the same so to limit pass through a flow network to the edges so do you remember how we do this


00:10:22

capacity yeah cap edge capacity at once so that it can appear once path good because um read off the answer here. So I've got this flow problem is edge disjoint means the edges of one path cannot overlap with the edges of another path. So if we want the maximum number of edge distract paths from S to T then we can do one like this and one like this and that's it.


00:11:17

Two is the most we could have. And I think that's even if this were like this. Two is still the most we can have. Even though it's not obvious from here. Looks like we got three, but we have a cup right there. That proves to us source. No removal. to model a vertex capacity.


00:11:52

So now I want to say hey not only can you do you have capacity on the edges but you also have capacity on how much can flow through an edge through a node. Remember the trick for this split the vertex into an entry point and an exit port and then we can put the capacity on that. Everybody that goes through the node has to come into the node.


00:12:16

So we haven't changed anything that way. Everything that comes out of the node has to, you know, it's gonna come out of the node. But now we've limited how many can do that. Even if this is like five and 10, there's a square and a pentagon in that. Oh, nice. And then you could do a hexagon.


00:12:46

Max flow duality states that the maximum flow from source to sync equals the minimum capacity cut the max flow from source to sequ whatever the minimum cut is is going to um be our bottle and can't get any better than that but we can that is the minimum on this. What's the duality thing with your programs two days ago?


00:13:23

We spent a lot of last time we actually what is the dual problem for problem for LP. This is the triangle. If the most profit from our chocolate, how much chocolates we sell times how much the profit for each type of chocolate is subject to all these constraints. And we so dual problem essentially says what?


00:14:01

What does the y represent? Yeah. Combination of the constraint. Think of that matrix A as the rows of matrix A are each of the string this many of this plus this many of this be by this constant we're gonna make a new a new constraint by combining rows make an upper bound subject to the fact that the left hand side of this is the objective function.


00:14:32

So we're going to find a new conraint that on the right because the left is down function and we're going to try to make that right side as small as possible upper bound. So yeah that can give us a proof of optimality because we can clearly see if we can clearly see that the combination of those beads gives us the objective that we actually achieved from the final.


00:15:03

We know we must have gotten the best possible. Um let's talk just for a minute about this idea using this picture. So notice here if the objective wants to point in this direction then this is the optimal right. Notice at this point how many constraints actually matter. One two three. At this point, it's just those two that are pre that that are like making a difference in our life.


00:15:45

If if these were gone, we'd go a little bit further this way. Yeah. But these other ones could disappear entirely and we would still be headed in the same direction. So um the dual variables those ways that we're combining the constraints only those two only only the y's corresponding to those two constraints are going to be non zero this thing our new constraint is going to be a combination of the ones that are tight and apparently what their value is corresponds to if I was to move this out by How much would that allow?


00:16:26

So, I leave this other constraint in place, but I let this one go out by one. How much more objective function would I achieve if it weren't for this grumpy d, you know, right? So, I can move that if I move that out by one, how much more will my objective function increase versus if I move this one out by one?


00:16:50

Um, I think I think those actually correspond to the real values of the Y eyes. But regardless, at least we're clear on the fact that when I make my mega constraint, it's only going to involve the two that are tight at the Is that just that's just a 2D? This is just two variables. That's it could be three variables.


00:17:14

Hard to visualize. All right. The last thing I want to show you because um I this relax you remember how the code was like relax the edge on the last one kept talking about relax the edge finally asked to help me get the intuition relax. Here we go. Let me show you what I go straight.


00:17:38

Remember when we did um the bell and for algorithm we said at the beginning we know how we're it's a single shortest path. So we have a way to get from S to X with zero cost. Right. Miss and miss. It's okay. Good other stuff. Okay. Um, but everybody else is infinite away.


00:18:04

So, this is at infinity. These red things are rubber bands. They're tight because we have an edge from S to A of length two. An edge from S to B of length five. And yet in our table, the best we found we've reported to have found is infinite. Okay. So you see that those two edges are tight.


00:18:29

They're stretched to infinity even though we just we should acknowledge that they should be length two. So when we go to the next step, we're going to relax an edge. We took that two um and we let go and let it come back to two away. So now it's at two away from S. A is now two away from S, but that did pull.


00:18:52

Now look, we tightened another edge. So now it says that we we've only recorded an infinite cost of B. But we can plainly see that if we get A and two, we should have B up there one. But it's so it's relax. It's tense because it's showing a higher cost than what it should be. Okay.


00:19:15

Okay. So when we relax this edge from S to B next now, okay, now it's going it's only five away. Um oh now B is the B to C and the B to T those are now typed. So the algorithm is he said the single source shortest path algorithm in general is pick a edge that's typed that shows that you should have a way of getting there in less than what you've recorded so far and just write it down


00:19:50

record that you found a better one. So I'm going to relax that uh this B. Okay, it says that you're three away, but you should only be one away because I have an edge directly there. the um it says that it sees over there at infinity, but I know that you should be able to get there in 2 + 5. So, oh, we're gonna go with this one.


00:20:15

B is three and we're four away. So, that should be that. Why does it equ what's what's going to happen here? We've got B which is at three and a cost of two. So that would be five is one option or you start at five and get a cost of 98. So which of these is two g?


00:20:58

Well, C would be five plus three, so that be eight. It is still that that would leave this other edge tight. I mean, we could do it in two steps, but we but if we run the cheapest one is to relax it. Now, we're all relaxed. Anyway, relax the edge. Then says the current recorded value looks further away.


00:21:17

It's stretched further than it really should be. Let's relax that by having a count. Take that edge that's being stretched and pull it to the actual weight of that edge. Anyway, um there is a connection between uh this kind of relaxing uh in the meeting talked about relax. So that that reminded me that's what there's a connection to the LPS here.


00:21:45

He solves a bunch of stuff for your project. Let's do so on. That's I get how it works. Then give us All right. What? Someone fixed that door. I fixed that door. Yeah. There's a weight everywhere. getting Oh, that's for you.


00:26:27

It's not for me. It's our research project is our research project is trying to figure out what programs college can integrate so that we have more connection with potential employers. We'll ask So they were designing this inventory. They're designing plants for their responses and they have found that they in order to get pretty good reliability. Heart patient.


Transcription ended after 00:27:25

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

