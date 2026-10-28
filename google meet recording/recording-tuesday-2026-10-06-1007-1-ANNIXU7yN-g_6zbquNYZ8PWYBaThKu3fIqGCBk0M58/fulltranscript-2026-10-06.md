# Local archive metadata

Source: https://docs.google.com/document/d/1-ANNIXU7yN-g_6zbquNYZ8PWYBaThKu3fIqGCBk0M58
Document ID: 1-ANNIXU7yN-g_6zbquNYZ8PWYBaThKu3fIqGCBk0M58
Title: Meeting started 2026/10/06 10:07 MDT - Notes by Gemini
Meeting start: 2026-10-06 10:07 America/Denver

All source text follows; rich links use Markdown. Embedded images are linked to the original tab, not downloaded. Transcript elapsed time is not a verified meeting duration.

---

# Source tab: Transcript

Oct 6, 2026
Meeting Oct 6, 2026 at 10:07 MDT - Transcript
00:00:17

Samuel Schuetz: Hey, dude.
Harry Cook: Hey, how's it going?
Samuel Schuetz: Pretty good.
Harry Cook: No worries about late.
Samuel Schuetz: Sorry about that. Yeah.
Harry Cook: No, no,
Samuel Schuetz: Uh
Harry Cook: no. Don't worry about it. Um, I spent a long time thinking about this problem thing and I think I figured it out.
Samuel Schuetz: Nice.
Harry Cook: Do you think you figured it out?
Samuel Schuetz: Uh for well I haven't started code coding but I think I understand
Harry Cook: Oh, yeah.
Samuel Schuetz: the problem better.
Harry Cook: Yeah, I haven't started coding either, but
Samuel Schuetz: Yeah. I just kind of worked through an example and that kind of helped under helped me understand there's a lot of uh ambiguity sometimes probably not in the actual description from the textbook but in his summary. So
Harry Cook: I think I think it made sense. It just took a little bit of like realizing what he was getting at for
Samuel Schuetz: now right
Harry Cook: me. Anyway, so my understanding that might make more sense is basically just what we said last night, which is you're choosing a route.


00:01:33

Harry Cook: You're choosing a binary search tree and the robot
Samuel Schuetz: duck.
Harry Cook: will always be going there first for every book lookup.
Samuel Schuetz: going to the root.
Harry Cook: Yep.
Samuel Schuetz: Yeah.
Harry Cook: And the route can be at zero or the route can be at 58. You know, wherever it ends up,
Samuel Schuetz: Right.
Harry Cook: but your robot's always going there first.
Samuel Schuetz: And it's always it's always the position in the array that that's how many
Harry Cook: And then it's Yep.
Samuel Schuetz: moves.
Harry Cook: Yeah.
Samuel Schuetz: That's
Harry Cook: And then the big thing to me that like really clicked was it's an unbalanced binary search tree.
Samuel Schuetz: Right.
Harry Cook: That's the key thing that I think I was like, "Ah, this is what I was missing is that it's it's an unbalanced binary search tree."
Samuel Schuetz: Right. It it favors long long chain like long chains without switching direction.
Harry Cook: Yeah. Yep. So, so that's the big thing is just that it is a binary search tree, but it is,
Samuel Schuetz: Yeah.


00:02:34

Harry Cook: you know,
Samuel Schuetz: Yeah.
Harry Cook: so
Samuel Schuetz: Good. Okay. Well, what do we want to do today?
Harry Cook: yeah.
Samuel Schuetz: Just start take the starter.
Harry Cook: So, I think we've got part one. Where did I put that? I had a tab open somewhere with that assignment in it, but it's gone. That's okay. Part one is to write out what the problem we're solving is and like mathematically describe it and name the things and you know all that stuff.
Samuel Schuetz: Yeah.
Harry Cook: So I think that's where we start and I think and I think I
Samuel Schuetz: on part one.
Harry Cook: think I'm ready to get part one like basically done.
Samuel Schuetz: Yeah, let's just knock it knock it out.
Harry Cook: Uh not the stuff advanced algorithms spin.
Samuel Schuetz: So, do we want to do like part one through four? Like a markdown for part Wait.
Harry Cook: What's this? How robot works. That's uh was this like AI generated description thing?
Samuel Schuetz: Yeah, that's new.


00:03:36

Samuel Schuetz: Yeah,
Harry Cook: Okay.
Samuel Schuetz: it was just helpful for me.
Harry Cook: I thought you sent a message. Yeah. I just didn't have time to like Yeah.
Samuel Schuetz: My idea was we just delete it. But before that, you might want to Well, I don't know. I think it's it's really helpful to see just
Harry Cook: Let me see what it's saying.
Samuel Schuetz: a
Harry Cook: Yep. Yep. Yep. Yep. Yep. Yes. Okay.
Samuel Schuetz: Yeah. And then you just multiply them at the end with
Harry Cook: Yep. Yeah. Okay. Yeah. All this all this is all this makes sense. Yeah,
Samuel Schuetz: I'll just keep it and we can delete it when we submit.
Harry Cook: we're just going to submit one like Python file and some paragraphs,
Samuel Schuetz: All right. Yeah. So we can keep it.
Harry Cook: right? Like good answers for questions in part one. We're just going to write as text and then we'll copy and paste it into the box.


00:04:28

Samuel Schuetz: Yeah.
Harry Cook: So,
Samuel Schuetz: Yeah. I might return to it as we're coding just
Harry Cook: yeah. Yeah. Yeah, for sure.
Samuel Schuetz: so Okay.
Harry Cook: For sure. Let's Let's share this. Let's share that one. There we go. Okay. There we go. Okay.
Samuel Schuetz: Okay.
Harry Cook: So, here's all this.
Samuel Schuetz: So,
Harry Cook: Let me pull up the assignment part one.
Samuel Schuetz: we're doing part one.
Harry Cook: Yep. So, art one one. What is the best name we can think of? I'm just going to copy and paste this in actually.
Samuel Schuetz: Yeah, right. Um, for our nested, is this the one the nested one?
Harry Cook: Lest on what?
Samuel Schuetz: It says, what is the best name that you can think of for the top level function that only returns the optimal cost?
Harry Cook: Yes. Um
Samuel Schuetz: Get optimal cost or just optimal cost.
Harry Cook: well I think yeah what is the best name we can go for the top level function that returns only the optimal cost not the tree.


00:05:48

Samuel Schuetz: Yeah, I did for
Harry Cook: What parameters should the function accept and what does the function return? H okay. Interesting.
Samuel Schuetz: I did I just did opt cost. If we're just doing the optimal cost, it doesn't matter. Optimal cost. This is a dumb question.
Harry Cook: Uh I don't think it's a dumb question. I think it's I think it's getting it getting it good naming conventions, you know.
Samuel Schuetz: Yeah. Um optimal cost That's
Harry Cook: See,
Samuel Schuetz: That's what I did for the last assignment. And that's I mean that's what it returns, right?
Harry Cook: let's see. Fascinating. You can think of the top level function only and what parameters should the function accept and what does that function return?
Samuel Schuetz: Parameters
Harry Cook: Yeah, optimal cost or opt cost that makes sense.
Samuel Schuetz: start and
Harry Cook: I think it's got to take it's got to take the list of frequencies. It's got to have the cost per rotation. It has to have the cost per distance.


00:06:56

Harry Cook: It has to have the cost per scan. And I think that's it, right?
Samuel Schuetz: Um, a starting and an ending index.
Harry Cook: Not for the top level function that has the optimal cost because it's not the tree.
Samuel Schuetz: Oh, you're saying because we have frequencies, we can assert start and end from that.
Harry Cook: Um, no, it's just that that's the recursive part, right?
Samuel Schuetz: Let me share my screen so you can because I'm I'm confused. What? Let me see. Sure. Okay. So, this was that last assignment and it was like kind of iterative.
Harry Cook: Mhm. Mhm.
Samuel Schuetz: And here's the first one that doesn't do
Harry Cook: return best for root and range start end. Well,
Samuel Schuetz: for root in range.
Harry Cook: yeah, this is like a this is a recursive one though, right?
Samuel Schuetz: Yeah.
Harry Cook: I think the difference is that it's asking about a top level function. It's not we're we're not building a tree. And I think we're going to take that approach because we're using memoization eventually where


00:08:41

Samuel Schuetz: Yeah.
Harry Cook: recursive part is like a a little function that's inside of the function,
Samuel Schuetz: Yeah.
Harry Cook: right?
Samuel Schuetz: Yeah. I just don't understand how um we do it. First of all, I don't really remember this much. I I know start and end are just in indexes, but I I'm trying to think of how we would do it without start and end.
Harry Cook: I think
Samuel Schuetz: And I'm just coming I'm coming up with a blank.
Harry Cook: so. I'm like I'm like writing this out to try and think about this. I think we need if we're doing optimal cost, we need our list of frequencies, right?
Samuel Schuetz: Yeah,
Harry Cook: We need our cost
Samuel Schuetz: if we have our list of frequencies.
Harry Cook: per rotate rotation.
Samuel Schuetz: Yeah. Oh, is that what it's asking?
Harry Cook: Move cost per distance.
Samuel Schuetz: Oh, so this is talking about Harry.
Harry Cook: cost per scan.
Samuel Schuetz: Is this talking about optimal cost with all of our It's not just the simple optimal cost.


00:10:03

Harry Cook: It's talking about this, right?
Samuel Schuetz: The whole right the robot.
Harry Cook: This number, right? It's saying if we give you some tree or some some some span of
Samuel Schuetz: Yeah.
Harry Cook: bins, right?
Samuel Schuetz: Mhm.
Harry Cook: what's the optimal cost of navigating those bins?
Samuel Schuetz: All right.
Harry Cook: And in order to calculate that we will have to like the problem is I think he's he's asking because uh in the assignment
Samuel Schuetz: Yeah. So,
Harry Cook: we're going to have top level function first that like analyzes it.
Samuel Schuetz: yeah. Without printing.
Harry Cook: Yeah. Without making the tree, right?
Samuel Schuetz: Yeah.
Harry Cook: And because it's not making the tree and also because I think it's going to do this thing where we like def something that does something, right?
Samuel Schuetz: Yeah. Yeah. It's going to have a nested that and that something that does something is there a cursor.
Harry Cook: Yeah.
Samuel Schuetz: That's a art or a curse.
Harry Cook: This is the recursive part, but the top level part doesn't need the start index and the end index, right?


00:11:16

Samuel Schuetz: Yeah.
Harry Cook: It just needs it just needs the whole thing.
Samuel Schuetz: All right.
Harry Cook: So that's what I'm thinking.
Samuel Schuetz: But our our nested our nested one could have start and end.
Harry Cook: Yes, our nested one I think would have start and end because you need that.
Samuel Schuetz: Is that what he means by top level is like the outside and not the
Harry Cook: Yeah.
Samuel Schuetz: inside?
Harry Cook: Yes. Yeah. Exactly.
Samuel Schuetz: Optimum cause. It's so much better. I feel like it's so much better working on this with another person cuz when you do when I spend like five hours on an assignment or whatever without talking to someone, it's just brutal, you know?
Harry Cook: Yeah.
Samuel Schuetz: It's nice to be able to talk about it.
Harry Cook: Yeah. It helps keep you from getting like stuck in some weird way of thinking about it,
Samuel Schuetz: Yeah.
Harry Cook: right?
Samuel Schuetz: Yeah. We have cost per distance and cost per scan. If cost per distance is such a weird,


00:12:52

Harry Cook: Yeah.
Samuel Schuetz: but whatever. Yeah, I won't gripe about it, but that is
Harry Cook: Yeah. Yeah. No, it's a it's it's quite a wordy name. Um, sorry, let me move this over here. The reason we proved it this way is because what? Because ah because it's not turning a tree. Instead, it's exploring all possible trees and returning the minimum cost. I'm returning the cost of what the minimum minimum free would be. I think that's clear,
Samuel Schuetz: Yeah.
Harry Cook: right?
Samuel Schuetz: Yep. It's It's exploring all the all the costs from all the trees.
Harry Cook: span of bins movement period. Okay. Yeah.
Samuel Schuetz: Yeah. And and for this we would do like um just so we're clear the bins are all in order in the array but where does would would our ISBN be just data stored in that node or
Harry Cook: Um, sorry. Say it one more time.
Samuel Schuetz: is we go by I Our function's not really caring about ISBN.


00:14:54

Samuel Schuetz: It's just caring about what index it what index each uh bin slash ISBN is in the flat array, right?
Harry Cook: Um, sorry. I was reading my own work, so I I couldn't really I wasn't processing what you're saying. Say one more time.
Samuel Schuetz: Um D uh ISBN doesn't really come into play yet with this is what I'm saying. I I don't think cuz that's just that would
Harry Cook: Yeah. Yeah. I think
Samuel Schuetz: just be like data but
Harry Cook: Yeah. Really I think the the important thing is that like we can treat the bins as ISBNs, right?
Samuel Schuetz: yeah sure but
Harry Cook: Um so like you know in here we can treat these as ISBNs. Uh no no we can't we can't yeah we have no idea.
Samuel Schuetz: those are frequencies. is
Harry Cook: We only know that we can treat the index as the ISBN. That's what I meant because the index is always ascending right to basically treat it as ISBN zero 1 2 3 4.


00:16:01

Samuel Schuetz: yeah no yeah we can treat we can we can treat it but we we can't
Harry Cook: Yeah,
Samuel Schuetz: we don't use ISBN but but then my my
Harry Cook: we never actually touched the ISBN.
Samuel Schuetz: question then would be like in the assignment it's asking when we we give our robot and ISBN. So somewhere in there,
Harry Cook: Mhm.
Samuel Schuetz: probably when we get closer to the end,
Harry Cook: Mhm.
Samuel Schuetz: we would need to check that. And that I don't think that affects our costs at all, but it does affect the uh efficiency maybe of the program slightly. But yeah, it doesn't matter for now, I don't think.
Harry Cook: Yeah. Okay. Yeah, sure. I think but yeah. Yeah. Yeah, that's fair. Okay. So, yeah, there we go.
Samuel Schuetz: That's good. Two.
Harry Cook: Two, how would you can you carve out a part of the problem be solved by nested recursive function and what parameters would be necessary to identify a particular sub?


00:17:13

Harry Cook: Okay,
Samuel Schuetz: Yeah.
Harry Cook: so the sub does he do it as one word or does he do it with a dash?
Samuel Schuetz: Uh, so
Harry Cook: Sub problem sub problem. We've identified is finding the optimal route for a span of that make sense to
Samuel Schuetz: it's not Well, That's not just it. Oh. Oh, you're talking about each sub. Yeah. Okay, I see what you're saying. Yeah.
Harry Cook: right?
Samuel Schuetz: Yeah. I was thinking of the whole like you're talking about one piece of the recursion. I was thinking of well what's the s yeah because that yeah
Harry Cook: Or I guess yeah,
Samuel Schuetz: that was what sub problem is but I was thinking where you have highlighted sub problem I was thinking nested nest it
Harry Cook: I think you're right. I think you're I think we're talking about this still.
Samuel Schuetz: Yeah.
Harry Cook: So I think I was answering the wrong question. I'm jumping ahead of myself. Is finding the best or the cheapest sub three


00:18:39

Samuel Schuetz: Yeah. Yep. The cheapest sub tree.
Harry Cook: order to find the best cost in optimal cost.
Samuel Schuetz: Mhm.
Harry Cook: We need to pick a single route from span of bins. Then explore options for the right and left children root and then the cheapest
Samuel Schuetz: Which are that? Yeah. Yeah.
Harry Cook: object for each. I think that makes sense. Um and then this is where we need low high, right?
Samuel Schuetz: Yeah. First start and Yeah.
Harry Cook: Yeah. So we need to know this sub problem would need arguments. What would it need? So it would need
Samuel Schuetz: frequencies still.
Harry Cook: doesn't need frequencies.
Samuel Schuetz: It doesn't need all of them, but um I feel like that would be easiest. I don't think it would be much. It I don't think it would be much. Uh well, it has to have frequencies, right? Because it's still trying to find it's still trying to find the best
Harry Cook: Yeah, it's still relevant, right?


00:20:28

Samuel Schuetz: cost. Those are part of the calculation.
Harry Cook: Yeah,
Samuel Schuetz: But I mean, we could pass some of them instead of all of them.
Harry Cook: but I guess No, no,
Samuel Schuetz: It would just be frequencies that start start to end.
Harry Cook: because because here's what I'm thinking.
Samuel Schuetz: It would be the range.
Harry Cook: Because we have deaf something, right? Or deaf optic cost.
Samuel Schuetz: Mhm.
Harry Cook: And then we're going to have death. Uh, what would we name this smaller one
Samuel Schuetz: Um high low.
Harry Cook: best?
Samuel Schuetz: Uh are you are you talking about parameters?
Harry Cook: Yeah, because because if we already have like n equals frequencies, right?
Samuel Schuetz: Uhhuh.
Harry Cook: Then everything in here will still have access to frequencies.
Samuel Schuetz: Oh, yeah.
Harry Cook: Right.
Samuel Schuetz: I think
Harry Cook: So we don't actually need to give it frequencies because we already have it at the top level.
Samuel Schuetz: yeah.
Harry Cook: So it can still access it.
Samuel Schuetz: Oh, I see.
Harry Cook: Yeah. So we don't need to pass it.


00:21:41

Samuel Schuetz: That's
Harry Cook: I think I think does that work? I'm pretty sure that's how Python works, right?
Samuel Schuetz: think it works. Yeah. I don't see why it wouldn't.
Harry Cook: Let's see. We can try it really here.
Samuel Schuetz: And and uh why do we have to do the n equals frequencies?
Harry Cook: You know what? You're right. That's a good point. I don't know. Yep, that works. It's accessible.
Samuel Schuetz: Okay.
Harry Cook: Okay, so we don't need to pass it because we already have it. So the real question is what is our sub problem dealing with, right?
Samuel Schuetz: Yep.
Harry Cook: Because it's it we don't need to give it cost per rotation, move cost per distance, or cost per scan because it's already got all of that. And it doesn't need frequencies because it's already got all of that.
Samuel Schuetz: Yep. Yeah.
Harry Cook: So what does it need?
Samuel Schuetz: Just it's high and low.
Harry Cook: So,
Samuel Schuetz: It needs your start index and end index.


00:22:53

Harry Cook: high low. Does it need anything else? It needs your start index. Uh, it needs to know where you are,
Samuel Schuetz: Um No,
Harry Cook: right?
Samuel Schuetz: because we reset after
Harry Cook: Yeah. Because that's important because like if if if you're looking for the best, if if you chose like some node way off on the right as you're starting, there's going to be some cost to choosing the next node as the farthest one on the left, right?
Samuel Schuetz: Yeah, I'm trying to think of this. So my understanding was it started or I mean it's reset it it it's in such a way that when you start like each cost um to move to a particular node is a full circuit. I mean you you're ending where you started initially.
Harry Cook: Well, I think what I'm thinking is is because we because there is a cost to movement,
Samuel Schuetz: Mhm.
Harry Cook: in order to calculate it, you have to know where you came from.
Samuel Schuetz: Okay. Yeah.
Harry Cook: That's why I'm giving it position, right?


00:24:10

Harry Cook: So like position is where am I right now?
Samuel Schuetz: Oh,
Harry Cook: If I'm at zero, it changes if I should choose, you know, position 8 as my root node or not because 0 to 8 has some cost. And maybe moving instead just to three will get me similar results but without that initial move cost.
Samuel Schuetz: yeah. I'm just This is way above my head because when I think of position, I'm thinking of just one tree. But it has to dry out all these different trees.
Harry Cook: So right so our top level function right takes
Samuel Schuetz: Mhm.
Harry Cook: frequencies cost per rotation move cost per distance cost per scans let's say this is our frequency span right to find the best we're going to go over each of these and pretend it's our root Right.
Samuel Schuetz: Yeah.
Harry Cook: So let's assume we've made it to six. We're choosing six as our route. We have to now know if we're finding the best. We have to find the best for this and the best for that.


00:25:21

Harry Cook: Right?
Samuel Schuetz: Yeah.
Harry Cook: So we have to give it the low so that we know where we're starting. We have to give it the high so that we know where we're ending. So that we know that like this is the span we're working with.
Samuel Schuetz: Mhm.
Harry Cook: We have to give it a position so that it can say okay moving to 10 is going to cost you know more than moving to seven. That's relevant. And we have to give it a direction because there is some cost to turn around and go to 10.
Samuel Schuetz: Yeah.
Harry Cook: It's a constant cost, right? Like it's going to be the same cost for seven, eight, n or 10. But it is going to be a cost.
Samuel Schuetz: Yeah. It's just hard to think about recursion here because we're picking six as a root, but there's many. Yeah, there's many different ways to have sixes the root.
Harry Cook: Yeah, because you have all these trees and you have all these trees and all of these could be


00:26:14

Samuel Schuetz: That's if you pick six is the root,
Harry Cook: different.
Samuel Schuetz: it's still the same function, but or it's the it's you're talking about the first decision or the if you pick six is the root, you've solved the whole tree because isn't it bottom
Harry Cook: In order to determine the best tree, you have to pick a route to start with and then pick everything else. Right? This is the whole like backtracking kind of approach is you pick what do you pick to start with and then what do you solve, right?
Samuel Schuetz: Yeah,
Harry Cook: And at each step we have to pick a root and then pick everything else.
Samuel Schuetz: right.
Harry Cook: And then once once we pass this in to the to the little best thing, it would say, "Okay, I have to pick a root and it's going to pick a root." It's going to start with seven because it's doing it, you know, brute force.
Samuel Schuetz: Yeah.
Harry Cook: And then and then it's going to pick everything else. And then it's going to pick eight as the root and then it's going to pick nine as the root and then it's going to pick 10 as the root.


00:27:12

Harry Cook: And it's going to check the cost is going to bubble back up and then it's going to go back and it's going to pick eight as the
Samuel Schuetz: Mhm.
Harry Cook: root and then it's going to pick seven and nine and 10 and then it'll bubble back
Samuel Schuetz: Right. But this is this top down or bottom up a recursion.
Harry Cook: up. Um, I think this would be top down because you're making a top level decision first and then exploring your lower options.
Samuel Schuetz: I was thinking it's bottom up because I
Harry Cook: I don't actually know for sure.
Samuel Schuetz: mean you pick a top but then you're just recursing and the base case is hitting the bottom first and then well I don't know. Yeah, I also I don't have a good grasp of what those mean conceptually either. Um
Harry Cook: Ah, there we go. Okay. top. So this is top down. Top down is recursion plus memoization. So you start with the original problem, break it into smaller sub problems, recursing until you hit a base case and the results get cached.


00:28:20

Samuel Schuetz: yeah.
Harry Cook: So each sub problem is solved only once. Bottom up,
Samuel Schuetz: Okay.
Harry Cook: you start from the smallest sub problems or you start from the base case and build upward filling a table until you reach the answer to the original problem.
Samuel Schuetz: Yeah. Okay.
Harry Cook: So this is top down.
Samuel Schuetz: Stop down.
Harry Cook: Yeah.
Samuel Schuetz: So, we have to pick the route first and then try the that makes and we can
Harry Cook: Yeah. Try everything else.
Samuel Schuetz: memorize to speed it up. Okay. So,
Harry Cook: And the minimalization is basically saying like if you ever end up coming from six to this span,
Samuel Schuetz: Yeah.
Harry Cook: we know what the optimal cost is, right? Like we know what the optimal tree is.
Samuel Schuetz: Mhm.
Harry Cook: That's what the minimization is solving.
Samuel Schuetz: So direction in your arguments, direction is just two options, right?
Harry Cook: direction is important because there's a different cost for the optimal tree or there could be a different cost for this optimal tree.


00:29:25

Samuel Schuetz: Uhhuh.
Harry Cook: If you're saying I'm coming from six and I have this span.
Samuel Schuetz: Yeah.
Harry Cook: If you're facing left, it's a higher cost than if you're facing right. So there is a difference.
Samuel Schuetz: Yep.
Harry Cook: potentially. And so that's why it's important is because it can affect the outcome.
Samuel Schuetz: Right.
Harry Cook: Yeah.
Samuel Schuetz: So you're you're finding the optimal cost with a sub tree, but direction Yeah, direction does matter. And so but but I guess I direction makes sense more sense to me. position is hard for me to wrap my head around because because part of me is thinking like maybe we don't need position because we're always going to the root but that's on the top that's on the nested function or the top level function we're always going to that route I don't know does that make sense
Harry Cook: Sorry, one second. Okay. Say it again. Sorry. When I get typing, I like can't process what you're saying.
Samuel Schuetz: I I'm the same way.


00:31:17

Samuel Schuetz: Um, I guess what I'm saying is it's hard to me for me to imagine what position we're at when we solve a sub problem. Like it part of me thinks maybe it's simple and maybe you're always at the root.
Harry Cook: So the the relevance is yeah the relevance is if
Samuel Schuetz: You're always out start.
Harry Cook: I build this right the reason that position is relevant is you're always going
Samuel Schuetz: Yeah.
Harry Cook: to start with the root but maybe we choose 10 as the root. Right?
Samuel Schuetz: Uhhuh.
Harry Cook: If we choose 10 at the root, we're always going to start there and then go somewhere else. If we choose one as the route, we're always going to go there first and then go somewhere else. Right?
Samuel Schuetz: Yeah.
Harry Cook: So position and direction are important because if say we're always at six, we always have to turn around to face the bookshelf, move to six,
Samuel Schuetz: Uhhuh.
Harry Cook: and then it's cheaper from there to keep going this way than it is to turn around and go this way.


00:32:24

Samuel Schuetz: Right.
Harry Cook: So that's why position and direction are relevant because then if I'm here, I'm already facing this way, right? So, it's not super expensive for me to keep going this way as it is for me to come all the way over here and then turn around and come back this way to find the next thing.
Samuel Schuetz: So, what do we pass in? Well, I guess we'll get there. I'm just It's I won't understand it till we get to coding and then I understand where that comes in.
Harry Cook: Yeah.
Samuel Schuetz: But I wouldn't be surprised if it was something that we could pass a default to, you know, like position equals start or something.
Harry Cook: Well, so the reason we can't do that is because as we explore, right, if we choose this as the route, we're always going to come here, right?
Samuel Schuetz: Mhm.
Harry Cook: If this is not the book that we're getting though, we have to choose to go right or left. If we go left,
Samuel Schuetz: Mhm.
Harry Cook: we can't just assume that we're starting from here because ultimately we're I think maybe where you're getting lost is I I remember I said earlier um I said something about like skipping indexes and that was just me


00:33:39

Samuel Schuetz: Yeah.
Harry Cook: misunderstanding. We're never going to skip when we're looking like if this is the binary search tree that we that we end up with, the robot's always going to come here. And if we're looking for a bigger one, we're going to come here. And if we're looking for a bigger one,
Samuel Schuetz: Yeah.
Harry Cook: we're going to come here. And if we're looking for a bigger one,
Samuel Schuetz: Right.
Harry Cook: we're going to come here. So,
Samuel Schuetz: Uhhuh.
Harry Cook: we're always going to hit every node along the way.
Samuel Schuetz: Yeah.
Harry Cook: And so, at your first choice, yeah, you can always pass whatever your first choice is, but as soon as you get to the second choice,
Samuel Schuetz: Yeah,
Harry Cook: the second choice could be three or two or five or four or six. And the position changes the map.
Samuel Schuetz: but that's we're not we're not but that's we've already passed that on to the next recursion is my point.
Harry Cook: already passed on.
Samuel Schuetz: So it's what we we've passed on that as a subpros.


00:34:25

Samuel Schuetz: Now, now our start and end is our our new route is three. Our start and end is all the values that weren't in the root, right? It's like the range.
Harry Cook: Yeah, it would be like two to well the the left would be just two and the right would be four, five, six.
Samuel Schuetz: Yeah.
Harry Cook: Yeah,
Samuel Schuetz: I
Harry Cook: but we have to pass to each of these trees that we're starting at three because it's a different
Samuel Schuetz: Yeah.
Harry Cook: calculation if you're starting at one or if you're starting at three because there's a cost to move from
Samuel Schuetz: Yeah.
Harry Cook: one to two is different than the cost of moving from three to two depending on the direction you're facing, right? Because you're already facing right and you move to two,
Samuel Schuetz: Yeah.
Harry Cook: that's only one movement cost. But if you start at three and you have to turn around and move to two, that's two costs.
Samuel Schuetz: Uhhuh.
Harry Cook: So that's why we're passing position and direction.
Samuel Schuetz: Yeah.


00:35:28

Samuel Schuetz: Okay.
Harry Cook: And we can't just pass default because we're not always coming from the same node every single time.
Samuel Schuetz: Yeah. We'll see. I don't know.
Harry Cook: Yeah.
Samuel Schuetz: I I think it might it maybe I'm wrong and probably I'm wrong.
Harry Cook: Mhm.
Samuel Schuetz: Like if you understand it and you're confident then you're probably right. But I I also I could see I mean, I I guess I wouldn't be surprised if we wouldn't need or if position would just be Yeah.
Harry Cook: unnecessary.
Samuel Schuetz: Well, I don't know. We'll see because like it might just be always I feel like it would always be root, but I'm not I'm not sure on that because recursion's confusing.
Harry Cook: Yeah. Well, it's because at each level of the recursion, right,
Samuel Schuetz: Yeah.
Harry Cook: if we choose a route and then we come here,
Samuel Schuetz: Yeah. That's our range. Six.
Harry Cook: that's our range,
Samuel Schuetz: Yeah.
Harry Cook: right? High low position is important because to move to


00:36:30

Samuel Schuetz: Right.
Harry Cook: 10 is more expensive than to move to six.
Samuel Schuetz: Right.
Harry Cook: So if we're here and we choose a second route and we choose
Samuel Schuetz: Yeah.
Harry Cook: eight,
Samuel Schuetz: Right.
Harry Cook: the cost to move to seven from 8 is different than the cost to move from five to seven, right?
Samuel Schuetz: The cost to move from seven to eight is different.
Harry Cook: Or 8 to 7, right? So we choose initial root here. The right child,
Samuel Schuetz: Yeah.
Harry Cook: the root is eight.
Samuel Schuetz: Okay.
Harry Cook: The left child, we have now I guess we have one on the left and one on the right. you know, whatever. The point is that like there's a different cost to move from here to here than to move from here to here. And that's why position is relevant because you can't just always say pretend you're at five because when when you for your route, you're always going to go to five, but once you get into this subree here, you're going to be approaching from a different number than five,


00:37:32

Samuel Schuetz: Well,
Harry Cook: and the movement cost will be different.
Samuel Schuetz: if you have if you have the direction if you have the direction getting from getting from the last route to the next to the root of one of the sub trees.
Harry Cook: Okay.
Samuel Schuetz: is it would just yeah it would always be one step down
Harry Cook: So like here to here.
Samuel Schuetz: and um and it would just depend on what direction you're faced in.
Harry Cook: Not necessarily because what if we choose 10 as the root, right?
Samuel Schuetz: If we choose 10 as the route,
Harry Cook: Then we could have like what if we do 10 as the root and as a right child we have
Samuel Schuetz: it's it's still
Harry Cook: like seven and as a left child we have six.
Samuel Schuetz: Yeah. Okay. So, but the cost from five to Yeah,
Harry Cook: Then we're going to have to walk all the way over to six.
Samuel Schuetz: but that's the second that's the second level. We're talking about just one route down like from from five to 10 as you know it's it's just going to be


00:38:24

Harry Cook: Mhm.
Samuel Schuetz: whether whether 10 is like the the cost is I mean the only thing that would that first step down would determine cost for picking her out is whether it's less or more. It would only depend on direction, you know,
Harry Cook: Um,
Samuel Schuetz: I think. But well, let's just see it. I I think this is this will be interesting to see.
Harry Cook: yeah, I think I think I see what you're saying, but I think maybe you're right. Once we get to the code, it'll become more clear because the point that I'm making is that there are there are
Samuel Schuetz: Yeah.
Harry Cook: different costs depending on your current position.
Samuel Schuetz: Yeah.
Harry Cook: And because there are different costs depending on your current position, you have to tell the sub like you know the nested sub problem where you're at to start with.
Samuel Schuetz: Yeah.
Harry Cook: But maybe we'll start coding and it turns out that I'm wrong, right? Like I definitely it definitely could be the case that I'm just mistaken.
Samuel Schuetz: Yeah. I can't really it it doesn't really jive with me.
Harry Cook: Yeah.
Samuel Schuetz: But that's the beauty about recursion is it it all by the end of the problem it all makes sense you know.
Harry Cook: Yeah. Yeah. Well, I actually I have to run,
Samuel Schuetz: Okay.
Harry Cook: but I think we've made some good progress.
Samuel Schuetz: Yeah.
Harry Cook: Um, I'll keep thinking about it. I'll keep working on it, and I will see you in class tomorrow.
Samuel Schuetz: Sounds good.
Harry Cook: Okay, see you.
Samuel Schuetz: Yeah.
Harry Cook: Thanks.
Samuel Schuetz: Yep. Thank you.
Harry Cook: Bye.
Samuel Schuetz: See you.


Transcription ended after 00:40:15

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

