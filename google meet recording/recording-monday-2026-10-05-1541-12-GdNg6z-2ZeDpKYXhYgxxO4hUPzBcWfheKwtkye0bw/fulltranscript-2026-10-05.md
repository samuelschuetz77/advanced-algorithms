# Local archive metadata

Source: https://docs.google.com/document/d/12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw
Document ID: 12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw
Title: Meeting started 2026/10/05 15:41 MDT - Notes by Gemini
Meeting start: 2026-10-05 15:41 America/Denver

All source text follows; rich links use Markdown. Embedded images are linked to the original tab, not downloaded. Transcript elapsed time is not a verified meeting duration.

---

# Source tab: Transcript

Oct 5, 2026
Meeting Oct 5, 2026 at 15:41 MDT - Transcript
00:00:00

Harry Cook: you run into something that's causing a problem, Gemini is taking notes. Okay. Anyway, when you when you run into something that causes a problem, you fix it on Linux.
Samuel Schuetz: What's your what's your credit card numbers while we're here?
Harry Cook: Yeah. Uh,
Samuel Schuetz: And I'll just forget it.
Harry Cook: so it's 222 3334.
Samuel Schuetz: I'll forget it because it'll I'll forget,
Harry Cook: Yeah.
Samuel Schuetz: right?
Harry Cook: Yeah. Yeah. I believe you.
Samuel Schuetz: Yeah.
Harry Cook: I believe you.
Samuel Schuetz: Okay.
Harry Cook: Anyway, my point is just that like there's some initial friction to set up your system,
Samuel Schuetz: Yeah.
Harry Cook: but then once you set up your system in Linux completely,
Samuel Schuetz: Yeah,
Harry Cook: the benefits of Linux really start to shine and the cost of Windows is like just not worth it eventually and then you just end up never opening Windows again. So,
Samuel Schuetz: I'll I'll think about it.
Harry Cook: yeah, I mean, you don't have to, right? Like I joke a lot, but like if you would rather just use Windows, by all means just use Windows.


00:00:51

Samuel Schuetz: Well, I don't want to, but I'm just like I don't think I'm ready yet, you know? But you're right. I probably am ready and I just need to do it
Harry Cook: Yeah, because really like especially like AI is so good at helping with Linux issues,
Samuel Schuetz: right. It is
Harry Cook: especially if you choose like a friendlier dro like Nyx is probably not what I would recommend now having used Nyx for a while.
Samuel Schuetz: I love it.
Harry Cook: I would recommend I love Nyx too.
Samuel Schuetz: I think
Harry Cook: If you like if that's what you want to do then absolutely. I just think like if somebody came to me and was like Harry I'm trying to switch to Linux. What would you suggest? I would say do like mint or something you know.
Samuel Schuetz: I want to get into like robotics and embedded systems and stuff. And I think the flakes and the like that's
Harry Cook: Oh flakes are so cool.
Samuel Schuetz: that sounds pretty cool to me, but I still don't I'm not at a point where I've ever needed to use one instead of


00:01:44

Harry Cook: Oh yeah,
Samuel Schuetz: the other one.
Harry Cook: yeah, yeah. Sorry. I'm gonna step away really quick for a second.
Samuel Schuetz: You're good. But yeah, thanks
Harry Cook: Whatever happened, you guys end up moving somewhere else, right?
Samuel Schuetz: Yeah.
Harry Cook: Are you happy with where you ended up?
Samuel Schuetz: Yeah.
Harry Cook: That's good.
Samuel Schuetz: Yeah.
Harry Cook: Yeah.
Samuel Schuetz: That's uh Professor Brad, Professor Bradshaw's mother-in-law lives next door to us and
Harry Cook: But look at this.
Samuel Schuetz: she's our landlord, but we're renting a house.
Harry Cook: I have I have I have two VS Code instances. Firefox Firefox on my other monitor. K9's Spotify Discord. Like I've got Steam up on another monitor. I've got all this stuff up and it's using like 16 gigs of memory and that's it. It's so nice.
Samuel Schuetz: Yeah, that's cool.
Harry Cook: It just like doesn't eat memory or CPU nearly as bad as Windows does. So, it's way nice anyway.
Samuel Schuetz: Stop.
Harry Cook: Okay. Yeah.


00:03:16

Harry Cook: So as far as this goes,
Samuel Schuetz: Yeah. Why is this?
Harry Cook: describe the recursive structure of the problem in words or math. Right? So I'm going to start let's go description do MD. Right? So the problem Yeah.
Samuel Schuetz: Yeah. But before we do that, can you help me understand
Harry Cook: Yeah.
Samuel Schuetz: um so R is just how many ups?
Harry Cook: Yeah. Or or downs. Just just how many indices it moves.
Samuel Schuetz: But but if we're at index zero,
Harry Cook: Mhm.
Samuel Schuetz: we're always Well, no, we're not. We're always on the bottom left. Right.
Harry Cook: Yep.
Samuel Schuetz: So,
Harry Cook: We always start at the bottom left.
Samuel Schuetz: I'm just talking about getting to a root.
Harry Cook: Yeah.
Samuel Schuetz: Yeah.
Harry Cook: It's going to depend how big the tree is.
Samuel Schuetz: Right. But when you're below the route to get to the route, is it still left and right or like what I like if
Harry Cook: Uh to get to the root is probably only one direction,


00:04:37

Samuel Schuetz: we're Yeah,
Harry Cook: right? It's probably only left or only right.
Samuel Schuetz: that's what I or up like if you're
Harry Cook: Yeah, only up. So, yeah.
Samuel Schuetz: here, but you're you have the direction you're faced in. So you just have to switch and then you move two. But is that right? Like is that because I don't I want to make sure we are on the same page with the problem, you know?
Harry Cook: Yeah. So, I think that's what I'm that's what I'm trying to do with writing out the problem here.
Samuel Schuetz: Yeah.
Harry Cook: The problem is we are a robot tasked with retrieving a book. ISBN there is
Samuel Schuetz: Yeah.
Harry Cook: a cost to rotate which is what's it called?
Samuel Schuetz: Um cost per rotation.
Harry Cook: Cost per rotation, cost to travel, move cost per distance, and a cost to scan, a title cost per scan.
Samuel Schuetz: Yeah.
Harry Cook: Our goal is to
Samuel Schuetz: Okay. Are you doing?
Harry Cook: retrieve the requested book with the minimum cost total for minimum cost total of cost per rotation.


00:06:28

Samuel Schuetz: Mhm.
Harry Cook: move cost per distance and cost per scan.
Samuel Schuetz: Yeah.
Harry Cook: So aim is to minimize the total distance.
Samuel Schuetz: Ghost. Oh.
Harry Cook: total number of locations and the number of scans although not necessarily right.
Samuel Schuetz: Okay, I'm going to copy. Can you send what you have?
Harry Cook: Um yeah,
Samuel Schuetz: Actually, when we're done.
Harry Cook: let me actually let me make this into a GitHub repository and
Samuel Schuetz: When we're done.
Harry Cook: share it with you because this uvit starts a git repository.
Samuel Schuetz: Okay.
Harry Cook: So I think I just need to add a remote.
Samuel Schuetz: Okay. Yeah,
Harry Cook: So this is
Samuel Schuetz: let's do it.
Harry Cook: me. Let's make this private. Let's create this.
Samuel Schuetz: So, this is robot robot EST. I'm working on assignment with my class name. Please
Harry Cook: Oh my gosh. What's your your Sam shoots something something, All right.
Samuel Schuetz: Yeah.
Harry Cook: If I want to share this with you.
Samuel Schuetz: Yeah.


00:08:44

Samuel Schuetz: Here, I'll send it in the chat here in the Google Meet. Okay, it's in the Google Meet chat window.
Harry Cook: Okay, I'm just allowing myself to add collaborators. There we go. Add people. See, it's not in the chat. There it is. See, Schuetz77. Save. Okay, there we go. Okay, you should get an invite to this repository.
Samuel Schuetz: I haven't gotten it yet. Oh, there it is.
Harry Cook: Okay, perfect. I was about to send it in the in the chat.
Samuel Schuetz: Okay.
Harry Cook: All right, you got it.
Samuel Schuetz: Yeah.
Harry Cook: Okay.
Samuel Schuetz: Okay, we're back there. Our goal is to achieve. So, what are all the ways we can incur costs? Let's put that down here.
Harry Cook: Yeah, that's here, right?
Samuel Schuetz: That's it. Huh.
Harry Cook: Mhm. Yeah.
Samuel Schuetz: A cost to scan a title. What does that mean?
Harry Cook: Uh that's in the second to last paragraph.


00:11:01

Harry Cook: Once a robot arrives at the index corresponding to the tree route. Here, let me Is that big enough or
Samuel Schuetz: Yeah. Yeah, I see it here.
Harry Cook: Okay.
Samuel Schuetz: Once the robot arrives at the index corresponding to the tree route, it scans the QR code on the bin. greater than the scanned bin once the robot arrives at the index corresponding to the tree route. So even if the So even if the ISBN if you look at my screen for a second,
Harry Cook: Mhm.
Samuel Schuetz: let's just ask this because I'm still a little blurry.
Harry Cook: Okay.
Samuel Schuetz: So, you're starting here, but if our ISBN was here, we'd hit it on the way up, but we still have to go to route.
Harry Cook: Mhm.
Samuel Schuetz: Is that right?
Harry Cook: Um.
Samuel Schuetz: Even if even if this was the one we're looking for
Harry Cook: Yeah. Yeah. Because because I think basically the goal is we don't like the goal is
Samuel Schuetz: systematic, you have to start.
Harry Cook: that we're building a binary search tree for the robot to traverse and each node in the tree corresponds to a physical location on the bookshelf.


00:12:32

Samuel Schuetz: Mhm. Right.
Harry Cook: But the bookshelf isn't structured like a binary search tree. The bookshelf is just like a list,
Samuel Schuetz: I'm right.
Harry Cook: you know? It's just an array. But we're building a binary search tree.
Samuel Schuetz: It's a It's just a flat list of bins
Harry Cook: Yeah. Yeah. But we're building the binary search tree from that list so that the robot knows what the optimal search
Samuel Schuetz: to optimally search.
Harry Cook: route is.
Samuel Schuetz: Yeah, got it. So, but that said, I mean, we have a list. We still have a list and we could we're not
Harry Cook: Uh-huh.
Samuel Schuetz: traversing up the tree. We're just going to the node in the list. We're going like the robots we have a flat list of buckets. The robot goes to the node and based
Harry Cook: Mhm.
Samuel Schuetz: on the shape of the tree that's a that's a particular cost. I guess every variation of the tree will have a different could have a different cost to get to the root node, right?


00:13:47

Harry Cook: Yeah, I think so.
Samuel Schuetz: because that would just depend on shape which depends and we're we're testing out all sorts of different shapes.
Harry Cook: Yeah.
Samuel Schuetz: Okay. So, let's just walk through this. So, robot starts at bin zero facing this way and then it faces right. It rotates one, moves five units to five. So that's one, two, three, four, five. So units is just how many h however many levels you have to go up to get to root from zero.
Harry Cook: Yep.
Samuel Schuetz: And it could be no no uh levels because and that would mean zero is true.
Harry Cook: Heat.
Samuel Schuetz: If target is less than five it already what does this mean? Do you understand this?
Harry Cook: Uh, sorry. Okay.
Samuel Schuetz: If target is less than five, it is already facing negative. Okay. Yeah. So, it always has to go to root. But in this case, say this is our our target,
Harry Cook: Mhm.
Samuel Schuetz: you'd still have to go up five and Wait a minute.


00:15:30

Samuel Schuetz: This is confusing me. If target is less than five, it is already facing negative. I thought we were facing positive to get to five.
Harry Cook: Yeah.
Samuel Schuetz: Okay. So if I say our target is four and your explain the cost to get there step by step. That's way too long. Okay, whatever. Cost one is rotation. So, we're saying rotation seven move to route is distance five. So, and we're saying that that cost per move is two. So, that's 10. Scan QR code on bid five. Target is less than four or less than five. So search proceeds to cost facing currently. Okay. So we were facing positive. Now we have to switch to negative.
Harry Cook: Yeah.
Samuel Schuetz: That makes sense.
Harry Cook: Mhm.
Samuel Schuetz: Okay. So it's just explaining it kind of weird. rotate to negative and then you have to scan you have to do a scan at the bin. So here we do one last scan to make sure and then that last scan scan target bin.


00:17:48

Samuel Schuetz: That's where you determine if it's a match or it's less than or greater than. Okay. What is this? Oh, you have to return. You have to return.
Harry Cook: Yeah. Yeah. Because you have to go back to the desk.
Samuel Schuetz: Where? Where's that? Here. Is that right
Harry Cook: I think that's in the summary, right? Um, if the robot discovers that the scanned bin has the target ISBN,
Samuel Schuetz: here?
Harry Cook: the robot ensures that it is facing the negative direction and then moves back to index zero to deliver the book.
Samuel Schuetz: Okay. And that's part of your cost.
Harry Cook: Mhm.
Samuel Schuetz: Sure. I was facing. So negative and positive direction just apply to up or down or wait. So cuz Okay, here's why I'm confused. Here's what I'm confused with Harry.
Harry Cook: Mhm.
Samuel Schuetz: This part the robot ensures that it's facing a negative direction. But say we're say our target was Oh, this is a bad example.


00:19:28

Harry Cook: Say target. Say target was four and you jumped back to five or you jump from five to three, right? Go back.
Samuel Schuetz: Okay.
Harry Cook: Imagine you go to the root, right?
Samuel Schuetz: The five. This one.
Harry Cook: Yep. You go to the root and then you jump all the way back to three,
Samuel Schuetz: Yeah.
Harry Cook: right?
Samuel Schuetz: Okay. So,
Harry Cook: Because that's what that's what our let's say our target was four,
Samuel Schuetz: our target was three.
Harry Cook: but you still somehow just jumped back to three. We're just making things up, right?
Samuel Schuetz: Okay. But we're here.
Harry Cook: So you you started No, you started at the root, right? So,
Samuel Schuetz: Yeah.
Harry Cook: so you start at zero.
Samuel Schuetz: Yep. You go to route.
Harry Cook: Now you go to the root, you go to five.
Samuel Schuetz: Yep. That's
Harry Cook: Somehow it thinks that you should go to three to see if that's where the book is. So you jump all the way over to three.


00:20:10

Samuel Schuetz: Oh, but you don't you have to go through the four to get to three.
Harry Cook: There is, but you don't have to scan the four.
Samuel Schuetz: You don't.
Harry Cook: No, because we're trying to avoid like minimal scans.
Samuel Schuetz: Well, what's the point of jumping somewhere if you don't scan? You can't know where you are.
Harry Cook: Well, you have to jump. Yeah. So, that's the point is that you're you're you're making kind of like greedy guesses, right?
Samuel Schuetz: Okay.
Harry Cook: You start at five and you just have to kind of guess and say maybe I go to three and see if that's right.
Samuel Schuetz: Okay.
Harry Cook: And you go straight to three because again, like this is a flat array, right? It's not a binary search tree.
Samuel Schuetz: Yeah. But but you But a binary but it is a flat array but we're using a binary search pattern to traverse the array.
Harry Cook: If scans are really expensive, then we don't want to scan each layer. We might sometimes want to jump a layer or two,


00:21:16

Samuel Schuetz: Okay.
Harry Cook: right?
Samuel Schuetz: And and if we're not scanning, what the hell would we do then? If we're jumping to three, why what's the point? Like what what do we do at three if we're not going to scan
Harry Cook: We scan at three, but we didn't scan at four, right? Like we just went through four. Does that make sense? Or not really.
Samuel Schuetz: sort of I I I don't think I'm not confused about the scan part. just like if we're say we're say say our target was like over on this side like our targets
Harry Cook: Yeah.
Samuel Schuetz: actually here
Harry Cook: Yeah. Mhm.
Samuel Schuetz: um and we have to move back to zero.
Harry Cook: Mhm.
Samuel Schuetz: So that means we have to switch to the negative direction.
Harry Cook: Yep.
Samuel Schuetz: Um, what's not clear to me is how negative direction works with up or down because we still have to go up and back down, right? Or is this where I'm getting confused?
Harry Cook: I think this is where you're getting confused because you're thinking about the structure of the library as a binary search tree.


00:22:36

Samuel Schuetz: Okay,
Harry Cook: So the binary search tree,
Samuel Schuetz: but here we're back to the array.
Harry Cook: yeah, here we're back to the array. So the binary search tree is just our way to store instructions to the robot, right?
Samuel Schuetz: Okay.
Harry Cook: The robot's not actually moving in any binary search tree kind of way.
Samuel Schuetz: Right.
Harry Cook: So if the robot jumps up to the root and then goes a little bit past it,
Samuel Schuetz: A robot's just a way to the binary search tree is just a way to pick what we want in a way that's better than scanning
Harry Cook: scanning every book.
Samuel Schuetz: everybody. Yeah.
Harry Cook: Yep.
Samuel Schuetz: Okay.
Harry Cook: Yeah. Yep.
Samuel Schuetz: So, we're Yeah.
Harry Cook: That's it.
Samuel Schuetz: So, we we're like say we're all the way at the bottom. We're all the way here. The biggest, right? This is the It's not necessarily the biggest element.
Harry Cook: Sure, but just pretend it is.
Samuel Schuetz: Um, yeah. So, so we would just go, we would switch direction.


00:23:38

Harry Cook: Yeah.
Samuel Schuetz: But but I guess I'm I'm I'm still confused on when you would only have to switch directions once no matter what position you're in to get back to zero.
Harry Cook: at most. Yeah,
Samuel Schuetz: Is that right at most?
Harry Cook: because you might already be facing towards zero at most. Once. switch. Yeah. To get back.
Samuel Schuetz: Okay. Okay, that's not too bad then.
Harry Cook: Yeah. Yep.
Samuel Schuetz: Okay, I think that clears me up.
Harry Cook: Yeah.
Samuel Schuetz: And I'll probably make one of those a learning log since it took so long.
Harry Cook: Yeah.
Samuel Schuetz: Um, okay. So, I got it. So, back to you. Whatever you
Harry Cook: Awesome. So, This is just what I have so far. This is this is here part one. Describe the recursive structure of the program in words or math.
Samuel Schuetz: Mhm.
Harry Cook: So, we're actually going to skip past that and we're going to go to part one.


00:24:43

Harry Cook: Work the first three provided test cases and confirm that you get the same numbers. If your hand calculation disagrees with the test, sort that out right now. Everything after this depends on you having the cost model right.
Samuel Schuetz: So, we're doing part part one.
Harry Cook: Yep. planning your solution. So, let's grab these tests.
Samuel Schuetz: Does he have them provided
Harry Cook: They're right here. Oh,
Samuel Schuetz: test?
Harry Cook: am I I'm not sharing that screen.
Samuel Schuetz: Oh,
Harry Cook: Sorry.
Samuel Schuetz: I can see I can see it though. I'm I see the assignment.
Harry Cook: Okay. Yeah. So,
Samuel Schuetz: Optimal BST cases.
Harry Cook: yep. Frequencies, rotation, move, scan, optimal cost, optimal tree. This is a little hard to read.
Samuel Schuetz: What does the 50 bin cost? Yeah, this is a little bit
Harry Cook: Okay. So I think this is frequencies five rotation three
Samuel Schuetz: creepy.
Harry Cook: move one scan two
Samuel Schuetz: Oh yeah. So those are our costs.


00:26:17

Samuel Schuetz: 312 is our costs associated.
Harry Cook: uh three is the number of rotations I think I'm not sure let me Okay.
Samuel Schuetz: It's probably cost is my guess. That's that's probably our what we're passing in for the for the move co the rotation cost the move cost and the scan cost and these are optimal BST cases. So this is the solution. So it tells us optimal cost is 10. We can't know that the optimal cost is 10 Unless we have the associated costs, right?
Harry Cook: I don't
Samuel Schuetz: Like here, let me share my screen because like this guy, I'm just looking at this. How could we know the optimal cost in the optimal tree if we don't have the rotation cost, move cost, and scan cost? We want to be able to.
Harry Cook: Yeah.
Samuel Schuetz: So these must be what? These must be the costs for each rotation cost is three. But then what is so this is frequencies. Oh, so here we're not passing in an array. We're pass like this is just has the optimal location.


00:28:21

Samuel Schuetz: Okay.
Harry Cook: for frequencies rotation move scan cost tree in optimal best cases assert cost equals
Samuel Schuetz: So, what's Yeah.
Harry Cook: o op optimal cost backtracking given frequencies cost per rotation Okay, so that's the cost per rotation, right? So rotation is cost per rotation which is three.
Samuel Schuetz: Yeah.
Harry Cook: Move cost per distance one cost per
Samuel Schuetz: But what's confusing what's confusing here
Harry Cook: scan two.
Samuel Schuetz: what's confusing is that you have a frequencies array but he doesn't give you the sorted I guess it just all of them start with 0 1 2 3 4 so the sorted array would be 0 1 2 3 4 he doesn't give you that Uh,
Harry Cook: I guess this tree is empty zero empty.
Samuel Schuetz: oh, let me see your screen. See,
Harry Cook: Am I not sharing?
Samuel Schuetz: you are. You are.
Harry Cook: Okay.
Samuel Schuetz: I just wasn't looking at it.
Harry Cook: So this is the tree.
Samuel Schuetz: Yeah.
Harry Cook: It's empty root zero on the left empty on the
Samuel Schuetz: Yep.


00:29:36

Harry Cook: right.
Samuel Schuetz: Yeah. It's just zero.
Harry Cook: So we're at zero. Okay. So we're just checking. This is the cost I think.
Samuel Schuetz: No, that's the frequency array. So since there's only there's only zero in this binary search tree,
Harry Cook: Uh
Samuel Schuetz: there's one node and it's five frequency.
Harry Cook: Mhm.
Samuel Schuetz: And then the second one would be 43. So zero gets the frequency of four and one gets this frequency of three for the second one. That's on row nine. And then the third one down is also just two elements in the tree because it only has two frequencies, four and 30. So zero would get frequency 4 and one would get frequency 30. And since it's a nested tupole. Yeah. So it's it's always uh root, left, right. I think for the for these vid uh right. Is that right? Root, left, right. I can't hear you.
Harry Cook: Sorry, I'm just like thinking very hard.
Samuel Schuetz: It must be zero.


00:31:01

Samuel Schuetz: So if we go to the row.
Harry Cook: Ah, okay. Okay,
Samuel Schuetz: Yeah.
Harry Cook: hold up. I've got it. So this is this is the number of requests indexed by book. So there's five requests for zero I think.
Samuel Schuetz: In a day. In an average day. Yeah. That's a frequency.
Harry Cook: So move rotation cost is three. Move cost is one.
Samuel Schuetz: Yeah,
Harry Cook: Scan cost is two. Optimal cost is 10 because you're at zero. Zero is the only thing in there.
Samuel Schuetz: you have to Yep.
Harry Cook: So you scan it,
Samuel Schuetz: You have to switch direction.
Harry Cook: which costs two.
Samuel Schuetz: Yep.
Harry Cook: You don't have to switch directions because you're already there. So you scan it,
Samuel Schuetz: Oh.
Harry Cook: which costs two, and hand it over, which is also free because you don't have to turn around and you don't have to move. So it's 10 because it's five times just the
Samuel Schuetz: Oh.


00:31:51

Harry Cook: scan cost.
Samuel Schuetz: Where where is that? What's What is that called when you do
Harry Cook: What is what called?
Samuel Schuetz: or where does it talk about? Oh, where does it talk about frequency coming into our equation here? That's the old assignment,
Harry Cook: Um,
Samuel Schuetz: right?
Harry Cook: an array of expected bin frequencies for the day are given as part of the problem input.
Samuel Schuetz: But
Harry Cook: So, four three So,
Samuel Schuetz: See f
Harry Cook: we're expecting a cost of four for this and three for this. I'm a little bit hard.
Samuel Schuetz: need to know the total frequency of all indexes in the span tree. So there's the right So you don't have to switch direction if you're at route. is the robot must start at bin zero
Harry Cook: Okay.
Samuel Schuetz: facing in the negative direction to receive an ISBN
Harry Cook: H Okay.
Samuel Schuetz: and cost.
Harry Cook: No, I get it. Okay. Can you still see my screen?
Samuel Schuetz: Yeah.
Harry Cook: I think it's actually like root, left,


00:33:52

Samuel Schuetz: Yeah.
Harry Cook: right.
Samuel Schuetz: Yeah.
Harry Cook: Yeah. Okay.
Samuel Schuetz: Yeah.
Harry Cook: I was I was misreading it as root, left, right, which is which is why I was getting tripped up. So, root,
Samuel Schuetz: Yeah.
Harry Cook: left, right. And same thing here.
Samuel Schuetz: So if we go Yeah.
Harry Cook: Your root is zero.
Samuel Schuetz: Yep.
Harry Cook: Left there's nothing. Right. There's another tree which is one with nothing and nothing.
Samuel Schuetz: Right. Yep. So if you go to row 11, which has three elements,
Harry Cook: Mhm. Visit one time.
Samuel Schuetz: you have zero,
Harry Cook: Vision one time. Vis one time.
Samuel Schuetz: nothing on the left.
Harry Cook: There's your root.
Samuel Schuetz: Yeah.
Harry Cook: One thing on the right,
Samuel Schuetz: And nothing on that left.
Harry Cook: which has nothing on the left and one thing on the right.
Samuel Schuetz: Yeah. Yep.
Harry Cook: So it's root one child on the right, one child on the right.
Samuel Schuetz: But I'm still confused how we got cost 10 there on the first one.


00:34:41

Harry Cook: Okay, you move to the root. You're already there, right? The route is zero. That's where you're at.
Samuel Schuetz: Okay. So, it costed nothing.
Harry Cook: You're expecting that book.
Samuel Schuetz: It costed nothing to get to the room.
Harry Cook: It costs nothing.
Samuel Schuetz: Yeah.
Harry Cook: Yep. Somebody requests the book five times. You scan it. That costs two. Each scan costs two. So 2 * 5 because there's five times the book is requested gives us 10.
Samuel Schuetz: Yeah. But that's frequency isn't how many times someone is requesting it. Frequency is just how often that gets searched for.
Harry Cook: It's the expected expected frequencies for the day and this is the
Samuel Schuetz: Yeah.
Harry Cook: optimal cost if that frequency is matched. Right?
Samuel Schuetz: Okay.
Harry Cook: Like of course if if we end up with something different than these frequencies, we're going to end up with something else. But
Samuel Schuetz: But yeah, frequency just helps you write this same shape because you're trying to get the things that have the most frequency closer to the root.


00:35:48

Harry Cook: yeah. Yeah.
Samuel Schuetz: But I don't So you did five times two or
Harry Cook: Um I actually have to run I have a Yeah.
Samuel Schuetz: what?
Harry Cook: Five time two because five frequency times two cost because you just have to scan the book.
Samuel Schuetz: two cost for and that's scan cost.
Harry Cook: Yep. Because you don't have to turn around. You're already at the route. You don't have to move anywhere. You're already at the route. But you do have to scan the book to make sure it's the right book, which costs two each time that you scan it. And scan it five times
Samuel Schuetz: But why? I don't understand why you'd be scanning route five times.
Harry Cook: because you're expecting that people are going to ask for it five times. And every time somebody asks for it, you have to confirm that you have the right book.
Samuel Schuetz: Yeah. Okay. So, I guess um optimal cost is is what? Because that's a number, but it doesn't have a target.


00:36:49

Samuel Schuetz: It doesn't have a target node you're after.
Harry Cook: So, if you have one book in your library,
Samuel Schuetz: It's it's to traverse the whole tree.
Harry Cook: no, this is if you have one book in your library and you're expecting to need to retrieve that book five
Samuel Schuetz: Yeah.
Harry Cook: times, what does the tree look like that will get you the optimal cost of 10 for a day work, which is five retrievalss of your only book.
Samuel Schuetz: Yeah.
Harry Cook: And that's your optimal tree.
Samuel Schuetz: That's your only tree possible.
Harry Cook: Yes, it's true. But it's also the optimal tree.
Samuel Schuetz: Yeah. Um got
Harry Cook: I got to get going though because I've got a meeting in like 20 minutes. Not a meeting, but I have office hours. So,
Samuel Schuetz: all right.
Harry Cook: I'm going to let you go, but uh I think I will try and look over this and try and understand it a little better and then maybe next time we meet,
Samuel Schuetz: Okay.
Harry Cook: we can both be a little bit more up to speed on what's going on.
Samuel Schuetz: Yeah,
Harry Cook: But,
Samuel Schuetz: I agree.
Harry Cook: okay, cool. Well,
Samuel Schuetz: Okay.
Harry Cook: I think we we made some progress.
Samuel Schuetz: All right.
Harry Cook: We'll have to meet again.
Samuel Schuetz: Yeah.
Harry Cook: You have a picture of my schedule, right?
Samuel Schuetz: Um. Yep.
Harry Cook: Okay. Okay. Yeah, just let me know a little bit in advance so that I can check and make sure that it works.
Samuel Schuetz: Okay.
Harry Cook: But I probably don't need um I will be
Samuel Schuetz: Do you want to meet later today or tomorrow?
Harry Cook: tied up today until probably about 9,
Samuel Schuetz: Okay. So,
Harry Cook: so probably tomorrow.
Samuel Schuetz: tomorrow.
Harry Cook: Yeah.
Samuel Schuetz: Okay. Cool.
Harry Cook: All right. Thanks, Sam.
Samuel Schuetz: All right,
Harry Cook: See you.
Samuel Schuetz: see you later. Thank you.
Harry Cook: Bye.
Samuel Schuetz: Bye.


Transcription ended after 00:38:34

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

