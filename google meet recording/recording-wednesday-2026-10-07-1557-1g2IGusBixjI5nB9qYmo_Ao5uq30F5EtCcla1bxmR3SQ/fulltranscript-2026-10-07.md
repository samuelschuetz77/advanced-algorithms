# Local archive metadata

Source: https://docs.google.com/document/d/1g2IGusBixjI5nB9qYmo_Ao5uq30F5EtCcla1bxmR3SQ
Document ID: 1g2IGusBixjI5nB9qYmo_Ao5uq30F5EtCcla1bxmR3SQ
Title: Meeting started 2026/10/07 15:57 MDT - Notes by Gemini
Meeting start: 2026-10-07 15:57 America/Denver

All source text follows; rich links use Markdown. Embedded images are linked to the original tab, not downloaded. Transcript elapsed time is not a verified meeting duration.

---

# Source tab: Transcript

Oct 7, 2026
Meeting Oct 7, 2026 at 15:57 MDT - Transcript
00:00:03

Harry Cook: This is going to have to be added to. So this is one thing. This is just the cost to this is just the cost to go through that route.
Samuel Schuetz: Mhm.
Harry Cook: And then we need to add the cost of all the times that we get that
Samuel Schuetz: Yeah.
Harry Cook: route. So we have the expected total frequency of that span. And we're also going to need R frequency R. So then we also need to add frequency of R times rotation if needed plus H Oh yeah. Okay. Okay. Plus because Yeah. Plus cost return to zero, right?
Samuel Schuetz: cost to return to zero. Yeah, you have to do that at the end. But that's but that's after every book.
Harry Cook: Yeah.
Samuel Schuetz: So we have to calculate the frequency of like
Harry Cook: You're right.
Samuel Schuetz: we have we have rotation the first
Harry Cook: Uh oh, no, no, because that because that goes to that goes to the the child, right?


00:02:33

Harry Cook: Because then then we have to do uh what do we call it optimal
Samuel Schuetz: changing direction.
Harry Cook: cost or something of High low. So the high would be R minus one low our current position which is R and what do we call it? direction
Samuel Schuetz: Wait, why? Why R minus one?
Harry Cook: because that is the high point of the sub tree on the left, right?
Samuel Schuetz: Oh, right. Yeah, R minus one
Harry Cook: Plus
Samuel Schuetz: and R. When you say R, that's just the index of root, right?
Harry Cook: Yeah. Yeah. R R + one R. Ah, I keep typing four. R. Correction. There we go. Yeah. So, I think this is this is our gross algebraic way.
Samuel Schuetz: Yeah. Stop.
Harry Cook: Wow. Yeah, that's nasty. That's messy. So, this is our answer to C. If we have each candidate as root r, we have the expected total frequency that span. Yeah. Yeah.


00:04:35

Harry Cook: Yeah. Yeah. cost to use it would be
Samuel Schuetz: Let's
Harry Cook: does that work? Yeah.
Samuel Schuetz: lower.
Harry Cook: Okay. And then what is D? B, how will it decide how to combine the role? The Okay. Yeah. So, this is just uh return min cost of
Samuel Schuetz: It's going to be fine.
Harry Cook: R. Yeah,
Samuel Schuetz: Wait, let's see.
Harry Cook: because that's how it's combining everything. You remember in class when we were going over that like uh test like a test quiz,
Samuel Schuetz: Mhm.
Harry Cook: if we're trying to find the minimum cost, this is how we combine all of our answers is just like take all of the costs of R and grab them
Samuel Schuetz: Oh, yeah.
Harry Cook: in.
Samuel Schuetz: Right.
Harry Cook: Yeah.
Samuel Schuetz: What did he use for that? He had like a at first he did like an array.
Harry Cook: Yeah, it just depends. I think it's like this is that's the cache thing that we're doing.


00:06:06

Samuel Schuetz: It was the aside. It was like a side or something or Yeah. I don't I don't remember.
Harry Cook: Okay. So now we need to write optimal cost backtracking so that it passes test backtracking finds the optimal cost without memorization or any other dynamic programming technique.
Samuel Schuetz: Do you have that on a second monitor screen?
Harry Cook: Yeah,
Samuel Schuetz: Okay, that's it.
Harry Cook: because I'm just sharing I'm just sharing this window in the end because it's a pain if I'm like navigating because
Samuel Schuetz: Yeah.
Harry Cook: then if I let's see if I stop this and I share again and I just do this, you're just going to see this all the time as I like go grab other things, which is fine, but
Samuel Schuetz: Yeah, I don't like uh dual monitor setup because it's just too much for me. I like just simple. I don't like seeing too much stuff.
Harry Cook: Yeah, fair enough. Okay. So now we came here and we need to be optimal cost tracking. Okay. So, the way that we had this, let's see.


00:07:48

Harry Cook: I think this is what we called optimal cost. So, we're going to need this. Yeah. Uh, and we can actually check in here because it's test
Samuel Schuetz: Mhm.
Harry Cook: optimal cost backtracking. Yep. So, it's expecting in a specific order frequencies, cost per rotation, move cost per distance, cost per scan. So, let's just grab that actually. There we go. Okay,
Samuel Schuetz: That's our high level.
Harry Cook: this is No, this is a different thing actually. Uh, this was I got confused because this is not the same thing because this is how you carve off part of the sub problem. So, this is our nested function.
Samuel Schuetz: Oh, what we just made.
Harry Cook: No, this is our top level and what I was grabbing was accident.
Samuel Schuetz: Okay.
Harry Cook: That's this see frequencies cost per variation cost this right this is our top level we would call it
Samuel Schuetz: Yeah,
Harry Cook: optimal cost he called it optimal cost backtracking yeah and
Samuel Schuetz: that's annoying. Okay,


00:09:06

Harry Cook: then this is this is our little sub sub thing right so
Samuel Schuetz: what do we want to name sub guy?
Harry Cook: um did it say what we wanted to
Samuel Schuetz: Just optimal opt cost or something.
Harry Cook: name it maybe best we could just name it this.
Samuel Schuetz: Yeah,
Harry Cook: Okay.
Samuel Schuetz: sure.
Harry Cook: So, let's see. The first thing we want is we want to store. Oh, I guess we don't need to store anything. That's best.
Samuel Schuetz: Uhhuh.
Harry Cook: There we go.
Samuel Schuetz: Okay.
Harry Cook: So, what is our base case? Right. Base case will be if an did problem receives an empty span. So if
Samuel Schuetz: Yeah.
Harry Cook: low is greater than high, right? High. Let me actually rename this. That's a bad name. I don't know why I said high.
Samuel Schuetz: Yes. Yes.
Harry Cook: If low is greater than high,
Samuel Schuetz: turn zero.
Harry Cook: then we need to Yeah. turn zero.


00:10:26

Samuel Schuetz: And that's just because that
Harry Cook: And then we need to come in here and we need sum expected frequencies, right?
Samuel Schuetz: Uhhuh.
Harry Cook: Yeah. Sum expected frequencies is going to equal the sum of frequencies from low to high.
Samuel Schuetz: Uh,
Harry Cook: Low to high plus one,
Samuel Schuetz: you need a you need a colon.
Harry Cook: right?
Samuel Schuetz: Yeah, but I think it's a colon, not a comma, right?
Harry Cook: I think you're right. Yeah. Yeah. Yeah. Yep. Yep. Yep.
Samuel Schuetz: I'm gonna get back to cleaning. Okay,
Harry Cook: Um and then for each of our
Samuel Schuetz: I'll be back.
Harry Cook: roots are in range from this is where it's comma low low plus one Right.
Samuel Schuetz: We're R and right. So, we're picking all the roots that we could pick. And then
Harry Cook: Do we need to define a visit cost?
Samuel Schuetz: Um well um maybe are you looking at your old project?
Harry Cook: You know, I'm just thinking


00:12:21

Samuel Schuetz: Um well here don't we just do well actually root minus one and root + one. So here we're just recursing but we're not because that's the old problem. We have to do all the the algebra here.
Harry Cook: Yeah, I think so. So, let's see. um need some things.
Samuel Schuetz: Yeah.
Harry Cook: What we want ultimately is to
Samuel Schuetz: Bunny.
Harry Cook: return this thing, right?
Samuel Schuetz: Yeah, I just I'm not
Harry Cook: So, we have that.
Samuel Schuetz: Yeah.
Harry Cook: Uh, let's let's let's fix some of this. This is bad indentation. How do you do multi-line additions? Or do I just need to not do that?
Samuel Schuetz: I don't know.
Harry Cook: So all this needs to be wrapped like that. There we go. Okay. Why does it not like this? This was not closed,
Samuel Schuetz: Need one more parentheses at the end.
Harry Cook: but I'm trying to figure out where I'm missing one from. Sum of expected frequencies times a bunch of this addition stuff.


00:14:36

Samuel Schuetz: Well, I don't some expected frequency. I think you're multiplying each frequency by the cost of that choosing that route if that like I'm trying to understand here what I'm saying but
Harry Cook: Let me see.
Samuel Schuetz: you know you you would you would find each cost is associated with
Harry Cook: Let's do con equals
Samuel Schuetz: retrieving all the books of the span and See?
Harry Cook: Let's not worry about this for now. Let's just see what's going on. What's it mad about here? Parenthesis parentheses parenthesis parenthesis. I guess rotation if needed doesn't exist. So,
Samuel Schuetz: Yeah.
Harry Cook: how do we calculate rotation if needed?
Samuel Schuetz: equation.
Harry Cook: H. This might be something that I need to just like work on for a while and see if I can
Samuel Schuetz: some time.
Harry Cook: Yeah. I don't know.
Samuel Schuetz: Yeah, I'm I'm not much help right now at all, but I'm My AI is saying that you are mostly correct.
Harry Cook: What's it saying?
Samuel Schuetz: It says your formula matches the cost model I verified against all eight tests and the 50 ben case.


00:17:58

Samuel Schuetz: um fixes for the write up. The two rotation if needed terms are different. The first one applies when the direction towards R differs from the direction the robot is facing.
Harry Cook: Yeah. I mean, yeah,
Samuel Schuetz: That is why direction.
Harry Cook: it's not the same thing each time. It's just like you are still handling the rotation if needed. And it's not going to be the same answer both times. It's just it still needs to be part of the calculation.
Samuel Schuetz: Yeah. It says the second applies only if the robot arrived at R facing positive since it must face negative to head home.
Harry Cook: Yeah.
Samuel Schuetz: Both are cost per rotation when they apply and zero otherwise.
Harry Cook: Yeah.
Samuel Schuetz: And it says to spell out cost return to zero because it's just move cost per distance times R.
Harry Cook: Oh, that's true.
Samuel Schuetz: I guess why why is that though?
Harry Cook: Yeah, I didn't think about that. That's that's that's very simple because R is our index,


00:19:03

Samuel Schuetz: I don't Yeah,
Harry Cook: right? So, it's R times move cost.
Samuel Schuetz: but are we always returning to So we're always Oh, because all we care about is root. We're at root.
Harry Cook: Yeah.
Samuel Schuetz: So root cost back is just move cost to zero which is
Harry Cook: Yeah.
Samuel Schuetz: always our Oh clever.
Harry Cook: I might I might let you go and see if I can figure this out.
Samuel Schuetz: Yeah, I I'm gonna work on it with my cousin tonight, too.
Harry Cook: Yeah.
Samuel Schuetz: He's uh my cousin's pretty smart.
Harry Cook: Okay.
Samuel Schuetz: So,
Harry Cook: Yeah. Let's see if we can maybe both figure this out a little more and then I'm gonna be at
Samuel Schuetz: you want to join
Harry Cook: ethics bowl tonight until like late.
Samuel Schuetz: ethics ball.
Harry Cook: Yeah.
Samuel Schuetz: What's that?
Harry Cook: Uh it's like um ethics debate.
Samuel Schuetz: Is that like a club here at snow or are you traveling somewhere?
Harry Cook: It's an athletic. It's not an athletic. It's a it's a academic team I think is how they've described


00:20:17

Samuel Schuetz: Nice.
Harry Cook: it.
Samuel Schuetz: Interesting.
Harry Cook: Yeah. So,
Samuel Schuetz: I'm not fer. No.
Harry Cook: yep. And they've done really well in the past, but we'll see. I think it'll be fun.
Samuel Schuetz: Who? Which teacher does it?
Harry Cook: Uh, Saladrinsky and Dr. Wright.
Samuel Schuetz: Never heard of him.
Harry Cook: Yeah, makes sense. We don't spend much time in the humanities buildings.
Samuel Schuetz: Okay.
Harry Cook: Okay.
Samuel Schuetz: Yeah.
Harry Cook: All right.
Samuel Schuetz: Let's uh Yeah,
Harry Cook: I'll chew on this and see if I can Figure it out a little more.
Samuel Schuetz: I'll I'll try. Yeah. I I just realized like I'm not very good at uh it's like some of this stuff is like there's there's a point where being on a team is or you know trying to study together is useful and I think it for like setting up a problem or whatever talking about it but then like I don't know I get left
Harry Cook: Mhm.
Samuel Schuetz: behind or I you know I don't I'm quickly off page because I get confused easily.
Harry Cook: right? Yeah. Yeah.
Samuel Schuetz: But so like my ideal learning session is just like yell at Claude, why?
Harry Cook: Okay.
Samuel Schuetz: Why? Why?
Harry Cook: Yeah. Okay.
Samuel Schuetz: Then I take a gander, you know, I take a stab at it and it's like, okay,
Harry Cook: Yeah.
Samuel Schuetz: yeah, you're mostly right, but you're forgetting something. I'm like through a computer screen.
Harry Cook: Yeah. All right. Okay. Well,
Samuel Schuetz: Yeah.
Harry Cook: I'll see you sometime tomorrow to keep working on this then. Okay. See you.
Samuel Schuetz: All right. See you.
Harry Cook: Bye.


Transcription ended after 00:22:25

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

