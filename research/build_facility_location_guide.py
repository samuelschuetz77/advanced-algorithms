from pathlib import Path
from math import log2
from itertools import combinations
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT

OUT = Path(__file__).with_name('facility-location-professional-primer.pdf')
W, H = 612, 792
NAVY = HexColor('#152536')
BLUE = HexColor('#166588')
TEAL = HexColor('#087c79')
GRAY = HexColor('#576574')
PALE = HexColor('#edf4f6')
GOLD = HexColor('#d49835')
RED = HexColor('#b14f45')

BODY = ParagraphStyle('Body', fontName='Helvetica', fontSize=10.7, leading=16.2, textColor=NAVY, spaceAfter=0, allowWidows=0, allowOrphans=0)
SMALL = ParagraphStyle('Small', parent=BODY, fontSize=9.4, leading=14.0)
CAPTION = ParagraphStyle('Caption', parent=BODY, fontName='Helvetica-Oblique', fontSize=9.5, leading=13.6, textColor=GRAY)

# Every module occupies two pages. The first establishes the concept; the
# second contains an explanatory vector figure, interpretation, and transfer task.
MODULES = [
dict(title='A precise question before an algorithm',
core='A facility location instance names possible sites, clients, the cost of opening each site, and the cost of serving each client from each site. A solution chooses open sites and gives every client one open site. We seek the feasible solution with the least total cost. This is the uncapacitated facility location problem, abbreviated UFL. The adjective uncapacitated says there is no numerical limit on how many clients one open site can serve.',
exact='The decision version adds a budget B and asks whether any feasible solution costs at most B. That yes-or-no question is the form used in NP-completeness proofs. The optimization version asks for the minimum cost; a search solver also returns the sites and assignments. Keep these three outputs distinct throughout the project.',
worked='If sites A and B cost 4 and 3 to open, opening A alone costs at least 4 before any client is served. Opening both costs 7 before assignments. A low connection cost is useful only after its facility is paid for.',
pitfall='The word optimal describes an objective, not a unique named variant. State the costs, constraints, and budget before claiming a complexity result.',
figure='Three versions of the same underlying instance',
nodes=[['Instance: sites, clients, costs'],['Decision: cost <= B?', 'Search: return a feasible plan'],['Optimization: find minimum cost']],
edges=[(0,1),(0,2),(1,3),(2,3)],
read='The input is shared. The required output changes what a solver must return and how a proof is stated.',
task='For a hospital siting proposal, identify one client, one candidate site, an opening cost, and a service cost.',
answer='A client may be a demand neighborhood; a site may be a candidate clinic; rent is opening cost; travel burden is service cost.'),
dict(title='Sets and membership',
core='Discrete mathematics starts with collections of individually identifiable objects. Let F be the finite set of candidate facilities and C the finite set of clients. Write i in F when i is a candidate facility and j in C when j is a client. A proposed open set S must satisfy S subseteq F. The empty set is generally infeasible when C is nonempty, since no client could be assigned.',
exact='A set records membership, not order or repetition. {A,B} and {B,A} are the same open set. A list such as [A,A,B] must not be counted as a different configuration. If |F|=m, then F has 2^m subsets, including the empty set. This count is the first source of exponential growth.',
worked='For F={A,B,C}, the eight subsets are {}, {A}, {B}, {C}, {A,B}, {A,C}, {B,C}, and {A,B,C}. With at least one client, only seven can be feasible open sets.',
pitfall='The client set and facility set may contain objects at the same physical coordinates, but their mathematical roles remain different.',
figure='The power set of three candidate sites',
nodes=[['F = {A, B, C}'],['Open none','Open one'],['Open two','Open all three']],
edges=[(0,1),(0,2),(1,3),(2,3),(2,4),(3,4)],
read='Each branch changes membership in S. There are eight subsets, including the empty subset.',
task='List the subsets of {A,B} and identify which are feasible when one client must be assigned.',
answer='The subsets are {}, {A}, {B}, {A,B}; the three nonempty sets can support an assignment.'),
dict(title='Functions and assignment maps',
core='A solution needs more than an open set. It also needs an assignment function sigma from clients to facilities. For every j in C, sigma(j) must belong to S. The notation sigma(j) means the site selected to serve client j. A function assigns exactly one output to each input; it does not require different clients to have different outputs.',
exact='Writing sigma:C -> S makes the domain and allowed codomain visible. If the model permitted split demand, sigma would no longer describe the whole solution; we would need fractional assignment variables. Here each client is assigned whole to one facility. This modeling decision makes verification straightforward.',
worked='With S={A,B} and clients 1,2,3, the map sigma(1)=A, sigma(2)=B, sigma(3)=B is valid. The map sigma(3)=C is invalid if C is closed, even when C is a candidate in F.',
pitfall='Do not confuse “site exists in F” with “site is open in S.” The verifier must check the latter.',
figure='A valid client to open site map',
nodes=[['Clients 1, 2, 3'],['1 -> A','2 -> B','3 -> B'],['Open sites A and B']],
edges=[(0,1),(0,2),(0,3),(1,4),(2,4),(3,4)],
read='Several clients may use B. Uncapacitated means that alone does not violate feasibility.',
task='If S={A}, can a certificate assign client 2 to B?',
answer='No. B must be open before it can serve a client.'),
dict(title='Numbers, units, and the cost matrix',
core='For each site i, f_i is its nonnegative opening cost. For each site-client pair (i,j), c_ij is its nonnegative service cost. The rectangular matrix c has one row per facility and one column per client. It need not be symmetric: facilities and clients play different roles. Units must be compatible before opening and service costs can be added.',
exact='A realistic interpretation might make f_i annualized dollars and c_ij annualized transport dollars for client j. If service cost is instead distance in kilometers, multiplying by a cost rate or demand weight may be needed. An arbitrary weighted objective is mathematically legal, but its operational meaning should be explicit.',
worked='Our running instance uses f_A=4, f_B=3, f_C=5 and c rows A=(1,4,5,7), B=(4,1,2,5), C=(7,5,2,1). These small values are teaching data, not field measurements.',
pitfall='A matrix of straight-line distances should not be described as travel time on a road network.',
figure='Running example cost matrix',
matrix=[['','1','2','3','4'],['A','1','4','5','7'],['B','4','1','2','5'],['C','7','5','2','1']],
read='Rows are candidate facilities; columns are clients. Opening costs A=4, B=3, C=5 are additional.',
task='Which site serves client 4 cheapest if all three are open?',
answer='C has service cost 1 for client 4.'),
dict(title='Building the objective one term at a time',
core='The total cost of a feasible pair (S,sigma) is the sum of opening costs over S plus the sum of service costs for all clients. In symbols: cost(S,sigma)=sum(i in S) f_i + sum(j in C) c_[sigma(j),j]. The two sums represent different operational decisions. Opening too few sites may raise travel cost; opening too many may waste fixed expense.',
exact='If S is fixed and there are no capacities or other coupling constraints, each client can independently choose its cheapest open site. Thus the best possible cost for a given S is g(S)=sum(i in S) f_i + sum(j in C) min(i in S) c_ij. The minimum expression simplifies exact enumeration, but it does not remove the 2^m choices of S.',
worked='For S={A,B}, opening costs sum to 7. The four minimum service costs are 1,1,2,5, totaling 9. Hence g({A,B})=16.',
pitfall='The cheapest assignment for one fixed S is not necessarily the globally cheapest choice of S.',
figure='Two terms that create the tradeoff',
nodes=[['Choose open set S'],['Pay fixed opening cost','Assign each client'],['Add service costs'],['Total = opening + service']],
edges=[(0,1),(0,2),(2,3),(1,4),(3,4)],
read='The site choice affects both sides: it determines what is paid to open and which service options exist.',
task='Compute the opening-cost part of S={B,C}.',
answer='f_B+f_C=3+5=8.'),
dict(title='A complete positive example',
core='An example should specify all the data needed to check it, not just a picture of dots. In the running instance, take S={B,C}. Assign client 1 to B, clients 2 and 3 to B, and client 4 to C. Every assigned site belongs to S. The opening cost is 3+5=8; the service costs are 4+1+2+1=8; the total is 16.',
exact='This example is useful even though it is not the optimum. It demonstrates how to score a certificate and how a decision budget works. Under budget B=16 it is a yes-certificate; under budget B=15 it is not. A no answer for B=15 cannot be established merely by showing this one plan costs 16; it requires ruling out every cheaper plan.',
worked='The certificate can be written as ({B,C}, {1:B,2:B,3:B,4:C}). A verifier checks membership, completeness, nonnegative input costs, and the computed total. This is exactly the kind of example the five-minute presentation needs.',
pitfall='A displayed plan is a feasible upper bound on optimum; it is not proof that no better plan exists.',
figure='Certificate for a budget of 16',
nodes=[['Open B and C'],['1->B: 4','2->B: 1','3->B: 2','4->C: 1'],['Opening 8 + service 8 = 16']],
edges=[(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5)],
read='This explicit certificate makes both feasibility and arithmetic independently checkable.',
task='Does the same certificate prove a yes answer for budget 15?',
answer='No. Its cost is 16; another certificate might still satisfy budget 15.'),
dict(title='A negative example and the logical asymmetry',
core='A candidate that fails is easy to refute. Suppose S={A} but client 4 is assigned to C. The assignment is invalid because C is closed. Or suppose every client uses A: the plan is feasible, but its cost is 4+(1+4+5+7)=21. It fails a budget of 16. Both failures are local checks.',
exact='The claim “there is a solution at most B” has an existential quantifier: one good certificate suffices. The claim “there is no solution at most B” has a universal burden over all candidates. This asymmetry is central to the intuitive difference between checking a proposed answer and finding one.',
worked='For our three-site instance, evaluating all seven nonempty S gives costs 21,15,20,16,17,16,17 in the order A,B,C,AB,AC,BC,ABC. Therefore the optimum is 15 at S={B}. This conclusion uses complete enumeration, not just inspection of a single assignment.',
pitfall='Do not claim a budget is impossible from one failed candidate; show a lower bound or exhaustive proof.',
figure='All seven nonempty open sets in the running instance',
bars=[('A',21),('B',15),('C',20),('AB',16),('AC',17),('BC',16),('ABC',17)],
read='The lowest bar is B at cost 15. The tiny instance permits complete verification of optimality.',
task='Why does the {A} certificate fail B=16?',
answer='Its cost is 21, greater than 16; that says nothing by itself about other open sets.'),
dict(title='What a verifier actually receives',
core='For the decision formulation, a verifier receives an instance, a budget B, and a proposed certificate (S,sigma). It first checks that S is a subset of F and is nonempty if clients exist. Next it checks that sigma assigns exactly one open facility to every client. Finally it adds costs and compares the total with B. None of these steps searches for an alternative plan.',
exact='Represent S as a Boolean array of length m and sigma as n facility indices. An implementation can validate all indices and sum costs in O(m+n) time once the cost matrix is available for O(1) lookup. Reading the entire matrix is O(mn), which is still polynomial in the encoded input size. Arithmetic complexity also depends on the bit length of the numeric costs.',
worked='A certificate with S={B} and all four clients assigned to B has cost 3+(4+1+2+5)=15. The verifier accepts it at B=15 and rejects it at B=14.',
pitfall='A fast verifier for a proposed solution does not imply a fast exact optimizer.',
figure='Verifier pipeline',
nodes=[['Instance, B, certificate'],['Check sites and assignments'],['Sum opening and service'],['Compare total to B'],['Accept or reject']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='Each arrow is a finite, direct computation; there is no branch over all possible open sets.',
task='What does the verifier return if a client is missing from sigma?',
answer='Reject: the certificate does not assign every client.'),
dict(title='Input size and polynomial time',
core='Let m=|F| and n=|C|. An explicit cost matrix contains mn entries, so an algorithm that reads all costs already takes time proportional to mn. Complexity must be measured against the encoded input length, not merely against the number of clients. A number with many digits also takes space and time to read; treating huge integers as one constant-size operation can hide work.',
exact='A bound such as O(mn+m+n) is polynomial. The expression 2^m is exponential in m. An algorithm may be practical for small m and still have exponential worst-case growth. Conversely a polynomial guarantee alone does not promise useful performance at every real-world scale.',
worked='At m=20 there are 1,048,576 open sets; at m=40 there are about 1.10 trillion. Doubling m squares the 2^m count. The number of clients changes evaluation cost but not the number of facility subsets.',
pitfall='“Fast” in complexity theory usually means polynomially bounded, not necessarily constant time or fast on a particular machine.',
figure='Exponential growth in site configurations',
bars=[('5',32),('10',1024),('15',32768),('20',1048576),('25',33554432)],
logbars=True,
read='The vertical axis is logarithmic: each additional five sites multiplies the count by 32.',
task='How many subsets exist for six sites?',
answer='2^6=64, including the empty set.'),
dict(title='The obvious exhaustive search',
core='A direct exact algorithm loops over all nonempty subsets S of F. For each S, it pays the opening costs and assigns every client to its cheapest site in S. It records the minimum-cost result. This searches 2^m-1 open sets. A straightforward implementation scans at most m sites for each of n clients, so the work is O(2^m mn), ignoring input parsing and arithmetic bit costs.',
exact='One can enumerate assignments explicitly too: each of n clients could choose one of |S| open sites, producing |S|^n maps for a fixed S. That is unnecessary for basic UFL because clients do not compete for capacity. Choosing the cheapest open site separately for each client collapses that inner search to polynomial time.',
worked='At m=3, S runs through the seven nonempty subsets shown earlier. For S={B,C}, each client compares two service costs. At m=25, over 33 million subsets already demand evaluation, so brute force is a baseline rather than a large-instance plan.',
pitfall='Do not count m^n assignments as unavoidable for the uncapacitated model; exploit independent nearest-open assignment.',
figure='Subset enumeration and cheapest open assignment',
nodes=[['All 2^m subsets'],['Skip empty S'],['For each S: sum f_i'],['For each client: min c_ij over S'],['Keep lowest total']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='The exponential part is the facility-subset loop. The inner scoring pass is polynomial.',
task='What changes in the inner step if facilities have capacities?',
answer='Client assignments become coupled; selecting the cheapest open site for each client may overload a facility.'),
dict(title='A small exact algorithm as ground truth',
core='For teaching and testing, a short exhaustive solver is valuable. It defines a reference result against which a heuristic or optimization library can be checked on small inputs. Enumerate every nonempty bit mask of length m, compute its open sites, and evaluate g(S). Break ties deterministically, for example by lexicographic site names, so tests remain repeatable.',
exact='For each S, compute service[j]=min(c[i,j] for i in S). Save the best assignment along with the cost. A result that returns only a number is less useful for the course project: the user and the verifier need the actual sites and client assignments. Preserve enough information to reconstruct the plan.',
worked='On the running instance, exhaustive evaluation returns S={B}, assignments 1:B,2:B,3:B,4:B, and total 15. The fact that client 4 pays 5 illustrates why a single central facility may still win: opening another site costs more than it saves.',
pitfall='A reference solver is only a reliable oracle on cases small enough to enumerate completely.',
figure='Reference solver data path',
nodes=[['Bit mask 001 -> A'],['Bit mask 010 -> B'],['Bit mask 011 -> A,B'],['Score each candidate'],['Best cost and witness']],
edges=[(0,3),(1,3),(2,3),(3,4)],
read='Masks encode open sets. The solver stores a witness, not just a winning score.',
task='What result should a test compare besides the total cost?',
answer='Check feasibility of the returned open set and every client assignment.'),
dict(title='From intuition to NP membership',
core='The decision problem belongs to NP because a yes instance has a certificate of polynomial length: an open/closed bit for each facility and one assigned site index per client. A deterministic verifier can check feasibility and the budget in polynomial time. This claim concerns yes certificates. It does not say an algorithm can find them quickly.',
exact='To be fully formal, encode costs and B as finite rational or integer values with finite bit lengths. The certificate length is O(m+n log m) bits under a natural indexing scheme. Summing a polynomial number of bounded-length input values remains polynomial in the encoded input size.',
worked='The budget-15 running instance has certificate ({B}, [B,B,B,B]). An observer can audit the certificate without knowing how it was found. That separation is precisely why the decision version is useful in complexity theory.',
pitfall='NP means nondeterministic polynomial time; the shorthand “hard problems whose answers are easy to check” is incomplete and can mislead.',
figure='Certificate length versus search space',
nodes=[['m site bits + n assignments'],['Polynomial-size certificate'],['Polynomial-time verification'],['Potentially 2^m site subsets']],
edges=[(0,1),(1,2),(0,3)],
read='A compact witness may exist even while a direct search over possible witnesses is enormous.',
task='Does rejecting one certificate establish a no instance?',
answer='No. Another certificate might pass.'),
dict(title='What a reduction must establish',
core='To prove target problem T is NP-hard, start with a source problem already known to be NP-hard and transform every source instance x into an instance r(x) of T in polynomial time. The core logical condition is x is yes if and only if r(x) is yes. This is stronger than making a vaguely similar example.',
exact='The direction matters. A polynomial algorithm for T, combined with the transformer r, would solve the source problem in polynomial time. Therefore the target is at least as hard as the source under that reduction. Reducing T to the source would establish a different relationship and does not by itself prove T hard.',
worked='For facility location, a clean route is Set Cover to general UFL. If the final-project rules require starting from 3SAT, one can compose a documented 3SAT-to-Set-Cover reduction with Set-Cover-to-UFL. The chain and both correctness proofs must be shown, rather than merely naming them.',
pitfall='A reduction proves hardness of a carefully specified variant. Changing metric, capacity, or cost assumptions afterward can invalidate the proof.',
figure='Reduction direction and solver consequence',
nodes=[['Known hard source x'],['Polynomial map r'],['Facility instance r(x)'],['Hypothetical fast solver for facility'],['Fast solver for source']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='The transformation points from the known hard problem to the problem whose hardness is being established.',
task='Which way must the arrow point to prove facility location NP-hard?',
answer='From a known NP-hard problem into facility location.'),
dict(title='Set Cover as a bridge',
core='A Set Cover instance has a universe U of elements, a family of subsets S_1,...,S_m, and a limit k. It asks whether at most k of the subsets together contain every element of U. The facility analogy is direct: each candidate facility stands for a subset, and each client stands for an element needing coverage.',
exact='The reduction must price uncovered elements so that an inexpensive facility plan corresponds to a true cover. In a simple nonmetric construction, opening each facility costs 1; serving an element from a set containing it costs 0, and serving it from a set missing it costs a penalty M greater than k. A facility plan of total cost at most k then uses at most k sites and cannot afford any uncovered element.',
worked='Let U={a,b,c}; S_1={a,b}, S_2={b,c}, S_3={a}. With k=2, opening facilities 1 and 2 serves every client at zero connection cost and pays opening cost 2. With k=1, no single listed subset covers U.',
pitfall='This simple construction uses arbitrary nonmetric service costs. Do not silently call it a proof for metric UFL.',
figure='Set Cover elements become facility clients',
nodes=[['Universe a, b, c'],['S1 = {a,b}','S2 = {b,c}','S3 = {a}'],['Facilities 1, 2, 3'],['Clients a, b, c']],
edges=[(0,1),(0,2),(0,3),(1,4),(2,4),(3,4),(4,5)],
read='The incidence relation tells which facility can serve which client at low cost.',
task='Why must M exceed k in the threshold-k construction?',
answer='One uncovered client would otherwise fit within the budget and break the equivalence.'),
dict(title='A complete nonmetric hardness argument',
core='Take Set Cover (U, {S_i}, k). Create one facility per subset and one client per universe element. Set every opening cost to 1. Let connection cost be 0 for membership and M=k+1 for nonmembership. Ask if the facility instance has a solution of cost at most B=k. The transformation creates a matrix of size m|U| and is polynomial.',
exact='If a cover of at most k sets exists, open those facilities and connect each element to a containing set. Total cost equals the number of opened sets, at most k. Conversely, if a facility plan costs at most k, no client can pay M=k+1, so every client is served by an opened set containing its element. Its open facilities therefore form a cover of at most k sets. Both directions are required.',
worked='The proof also shows why the decision threshold matters. Without B=k, the construction would still encode a cost tradeoff but would not directly express the Set Cover yes/no answer.',
pitfall='This establishes NP-hardness for general UFL. To call the decision variant NP-complete, combine it with the polynomial verifier.',
figure='Both directions of the reduction',
nodes=[['Set cover <= k'],['Open corresponding sites'],['Facility cost <= k'],['Every low-cost client is covered'],['Open sites form set cover']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='The forward and reverse implications close the logical loop.',
task='What fails if M is set to zero for nonmembers?',
answer='A noncover could connect uncovered elements for free, so a facility yes instance need not imply a set cover.'),
dict(title='Metric costs require a separate proof',
core='In metric UFL, connection costs reflect distances obeying a triangle inequality. The 0-or-M matrix in the previous proof is not generally a metric. A metric reduction can instead use a graph-derived distance structure; one published lecture construction gives cost 1 for incidence and cost 3 otherwise, plus unit opening costs. It shows metric UFL remains NP-hard via Set Cover with an adjusted threshold.',
exact='The metric assumption is useful for approximation guarantees because distances behave geometrically. It does not make the exact problem easy. The report separates general UFL hardness from metric UFL hardness so that a claim about one variant is never borrowed without proof for the other.',
worked='In a metric, d(a,c) <= d(a,b)+d(b,c). If an intended “far” edge has cost 100 while two intermediate legs cost 1 each, the proposed distances violate the triangle inequality. Such a table cannot represent shortest-path distances.',
pitfall='When preparing a formal final-project proof, confirm which facility variant the instructor accepts and show the specific reduction chain.',
figure='Triangle inequality as a consistency test',
nodes=[['Point A'],['Point B'],['Point C'],['Direct A-C <= A-B + B-C']],
edges=[(0,1),(1,2),(0,3),(2,3)],
read='A metric cannot make the direct route more costly than a route through an intermediate point.',
task='Can distances AB=1, BC=1, AC=4 be metric?',
answer='No; 4 exceeds 1+1.'),
dict(title='Integer programming as a second language',
core='Define binary y_i=1 if site i opens and binary x_ij=1 if client j is assigned to site i. Minimize sum_i f_i y_i + sum_i sum_j c_ij x_ij. For every client j require sum_i x_ij=1. For every pair (i,j) require x_ij<=y_i. These two constraints say every client gets one site and closed sites serve nobody.',
exact='The formulation is equivalent to the combinatorial model when all variables are binary. It makes operational constraints easy to add, such as a maximum number of open sites or capacities. But adding constraints defines a new variant. For example sum_i y_i<=k changes the feasible set and may change the best plan.',
worked='For S={B}, set y_B=1, y_A=y_C=0. Set x_Bj=1 for all four clients, and every other x to zero. The objective evaluates to 15. Setting x_C4=1 while y_C=0 violates x_C4<=y_C.',
pitfall='A solver status, objective value, and certificate should all be checked; a mathematical model can be implemented incorrectly.',
figure='Variables and constraints in the integer model',
nodes=[['y_i: open site?','x_ij: assign client?'],['sum_i x_ij = 1','x_ij <= y_i'],['Minimize opening + service']],
edges=[(0,2),(1,2),(0,3),(1,3),(2,4),(3,4)],
read='The linking inequality x_ij<=y_i encodes the “no service from a closed site” rule.',
task='What constraint is violated when one client is assigned to two sites?',
answer='Its assignment sum is 2 rather than 1.'),
dict(title='Relaxation, lower bounds, and proof gaps',
core='If binary variables are allowed to take values anywhere from 0 to 1, the integer program becomes a linear-programming relaxation. Its feasible region includes every integer solution, so its optimum cannot exceed the integer optimum in a minimization problem. The LP objective is a lower bound, not usually a deployable plan: opening 0.4 of a clinic is not a literal site decision.',
exact='A feasible integer plan gives an upper bound; an LP solution gives a lower bound. The difference between these bounds can measure how much optimality remains unproved for an exact solver. Rounding turns a fractional solution into an integer one, but naive independent rounding can leave clients unserved or create excessive cost.',
worked='If an LP gives 13 and a feasible plan costs 15, the true optimum lies in [13,15]. Our exhaustive toy calculation establishes the exact value 15, but the LP lower bound alone would not.',
pitfall='Do not report a fractional LP objective as if it were the cost of a valid physical deployment.',
figure='Bounds around the unknown optimum',
bars=[('LP lower',13),('True optimum',15),('Feasible upper',16)],
read='The unknown optimum is trapped between a rigorous lower bound and a checked feasible upper bound.',
task='If lower bound is 24 and a feasible plan costs 24, what is proven?',
answer='The plan is optimal because no solution can cost below 24.'),
dict(title='Local improvement and its limits',
core='A practical heuristic can start from a feasible open set, then try opening one closed site, closing one open site, or swapping an open site with a closed one. After each proposed move, recompute the best assignments and total cost. Accept an improving move and repeat until none of the chosen move types improves cost.',
exact='This process terminates when every accepted move strictly reduces cost over a finite set of open sets. Its final result is locally optimal for the chosen neighborhood, not necessarily globally optimal. A two-site coordinated change may improve cost even when every one-site move appears harmful.',
worked='Starting from S={A}, cost 21, adding B gives 16; closing A then leaves S={B} at 15. The path reaches the global toy optimum. A different instance can trap the same local rule away from optimum.',
pitfall='A heuristic result is an upper bound on the true optimum. Without a proof, do not attach a worst-case approximation factor.',
figure='An improving local search path',
nodes=[['Start {A}: 21'],['Add B -> {A,B}: 16'],['Close A -> {B}: 15'],['No improving move']],
edges=[(0,1),(1,2),(2,3)],
read='Each accepted move lowers the objective. The stopping condition is defined by the neighborhood examined.',
task='Could a swap move help when no add or close move does?',
answer='Yes; it changes two membership bits together.'),
dict(title='Approximation needs a proved ratio',
core='For a minimization problem, an alpha-approximation algorithm guarantees cost(output)<=alpha times OPT for every instance in its stated class. The ratio is a theorem about the algorithm and assumptions, not a performance observation on a few examples. Metric UFL has a large literature of constant-factor approximation algorithms; one classic greedy approach by Jain, Mahdian, and Saberi has a 1.61 guarantee.',
exact='A ratio of 1.61 means the algorithmic cost is at most 61 percent above optimum in the worst case covered by the theorem. It does not say it is always 61 percent worse. A reported ratio from an experiment, cost(heuristic)/cost(exact), is informative only on instances where exact OPT is known.',
worked='If OPT=100 and a 1.61-approximation returns cost 140, it satisfies the guarantee. A return of 162 would contradict the theorem or signal that the instance violates its assumptions or the implementation is wrong.',
pitfall='Do not transfer a metric guarantee to arbitrary nonmetric service costs.',
figure='Approximation guarantee versus an observed result',
bars=[('OPT',100),('Observed',140),('1.61 bound',161)],
read='The guarantee is an upper ceiling on algorithm cost relative to the unknown optimum, not a prediction.',
task='If OPT=80, what cost ceiling does a 1.61 guarantee imply?',
answer='128.8 in real-valued units; integer cost would be at most 128 if the bound is strict by integrality.'),
dict(title='Capacities alter feasibility',
core='A capacitated variant gives each site a maximum load u_i and each client a demand d_j. An assignment is feasible only if, for each open site i, the total demand of clients assigned there is at most u_i. This single addition couples assignments: client j taking capacity at one site may force another client elsewhere.',
exact='The earlier formula g(S)=opening costs plus independent per-client minima no longer computes the best feasible assignment for a fixed S. The subproblem is now constrained. Capacity can represent beds, warehouse throughput, server load, or response teams, but the unit and time horizon must match demand.',
worked='Suppose B has capacity 2 and four clients each have demand 1. The all-to-B solution from the running toy instance becomes infeasible, even though its cost is 15. Opening an additional site may be necessary.',
pitfall='Calling a capacitated problem “UFL” without qualification can produce the wrong verifier and search count.',
figure='Capacity makes assignments compete',
nodes=[['Open B, capacity 2'],['Client 1: demand 1','Client 2: demand 1'],['Client 3: demand 1','Client 4: demand 1'],['Only two can use B']],
edges=[(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5)],
read='Once B fills, the remaining clients must use another open site. Assignment choices are coupled.',
task='What new check belongs in a capacitated verifier?',
answer='Sum demand assigned to each site and compare it with that site’s capacity.'),
dict(title='Other facility variants',
core='Several names describe different problems. In k-median, choose exactly k sites and minimize total client distance. In k-center, choose k sites and minimize the maximum client distance. In UFL, the number of sites is chosen indirectly by opening costs. Covering variants require every client to be within a radius or served by a qualifying set.',
exact='These models can select different sites on the same map. A network serving dense demand cheaply may have low total distance but leave one remote client far away. The k-center objective places that worst-served client at the center of attention. Selecting the variant is a policy choice before it is an algorithm choice.',
worked='Consider ten clients near city A and one remote client near B. A total-distance objective may prefer a site near A; a maximum-distance objective may justify the remote site if the worst distance dominates. Opening costs can instead make the second site too expensive.',
pitfall='Do not mix a k-center radius statement with a UFL sum-of-costs verifier.',
figure='Objectives can prioritize different outcomes',
nodes=[['Same candidates and clients'],['UFL: opening + sum service','k-median: choose k, sum distance','k-center: choose k, max distance'],['Different optimal site sets']],
edges=[(0,1),(0,2),(0,3),(1,4),(2,4),(3,4)],
read='The data may be identical while the objective and constraints produce different answers.',
task='Which variant directly limits the worst client distance?',
answer='k-center.'),
dict(title='Spatial data is a model, not a map decoration',
core='For a real application, candidate sites and demand points need provenance and compatible geography. A coordinate is not automatically a travel cost. Euclidean distance, road-network time, shipping cost, and expected response delay lead to different c_ij matrices. Administrative boundaries, inaccessible roads, and operating hours may change feasibility.',
exact='The cost model should state the time horizon and units. Demand weights can scale service costs: sum_j w_j c_[sigma(j),j]. That gives populous clients more weight but can hide poor service in sparse areas. If equity matters, report distributional metrics alongside the chosen objective, such as maximum delay or a high percentile.',
worked='If one neighborhood represents 1,000 requests per year and another represents 10, multiplying each travel cost by request volume models annual travel burden. It does not automatically model emergency severity or fairness.',
pitfall='For military or public-sector examples, use public or synthetic locations unless authorized data and operational assumptions are available.',
figure='From raw geography to an auditable cost matrix',
nodes=[['Candidate coordinates'],['Demand locations'],['Travel network and units'],['c_ij cost matrix'],['Optimization and audit']],
edges=[(0,2),(1,2),(2,3),(3,4)],
read='The cost matrix is a derived input. Its assumptions should be documented independently of the solver.',
task='Name one reason straight-line distance could misrank two candidate sites.',
answer='A river crossing, road closure, or mountain route can change actual travel time.'),
dict(title='Uncertainty and robustness',
core='Real demand and travel costs are not fixed with perfect knowledge. A deterministic model chooses one estimated matrix and solves it exactly; that can still be the wrong operational decision when the estimates shift. Scenario analysis evaluates the same site plan under several plausible demand or cost settings.',
exact='A robust formulation might minimize worst-case cost over a defined uncertainty set, or penalize variance and failure risk. Those choices require a defensible set of scenarios and a precise objective. “Robust” is not a generic improvement; it can raise nominal cost to reduce exposure to bad cases.',
worked='A depot near an occasionally flooded bridge may look best in normal travel times. A closure scenario can make its service costs much higher. Compare the chosen plan with an alternative under both scenarios before recommending deployment.',
pitfall='Do not present a single optimized cost as a forecast of real performance without uncertainty and data-quality analysis.',
figure='One site plan under multiple scenarios',
bars=[('Normal',15),('Peak demand',21),('Road closure',34),('Alternate plan',24)],
read='Scenario scores reveal sensitivity. The bars are illustrative and not empirical estimates.',
task='What information is needed before calling the alternate plan robust?',
answer='Its cost under the same scenarios and the decision rule for balancing them.'),
dict(title='Testing a solver without confusing tests with proof',
core='Use tiny hand-checkable instances to test syntax and logic: one client, one facility, ties, zero opening cost, a closed-site assignment, and an infeasible capacity case if capacities are modeled. For small random instances, compare the candidate solver with exhaustive enumeration and independently verify its returned certificate.',
exact='Tests can find bugs but cannot prove correctness for all instances. Conversely, a correctness argument about the mathematical algorithm does not guarantee a particular implementation indexes the matrix correctly. Keep separate checks for input validation, feasibility, cost recomputation, and claimed optimality.',
worked='A useful regression test is the running 3-by-4 matrix: optimum 15 at {B}. Another test changes f_B from 3 to 30; the expected solution should change. If the result remains {B}, inspect whether opening costs are included.',
pitfall='Do not test a solver only against its own cost function; independent recomputation is stronger.',
figure='Layered testing of a facility solver',
nodes=[['Input validation'],['Certificate verifier'],['Tiny exact oracle'],['Random differential tests'],['Scale experiments']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='Each layer addresses a different failure mode, from malformed data to large-instance behavior.',
task='Which test would catch assignment to a closed site?',
answer='The independent certificate verifier.'),
dict(title='The five minute presentation',
core='The Friday deliverable is a short slide presentation, not this full research guide. The class must leave able to create an instance, verify a proposed solution, understand the name, and describe exhaustive search. A practical structure is one slide for the problem, two example slides, one verifier slide, and one brute-force slide. Each slide should carry one main claim.',
exact='Use the running toy instance for a yes example and a changed budget or invalid assignment for a second example. Show both opening and service arithmetic. State the decision threshold B explicitly. When explaining search, say “2^m possible open sets, each scored in O(mn) by choosing the cheapest open site for each client” and identify the modeling assumptions behind that shortcut.',
worked='At a spoken pace, five minutes permits only a few equations. The report gives the depth needed to answer questions; the slides should preserve the rubric’s four required demonstrations.',
pitfall='Do not try to deliver fifty pages orally or put the entire reduction proof on a five-minute slide.',
figure='Five-slide narrative aligned to the rubric',
nodes=[['1. Define UFL'],['2. Example A'],['3. Example B'],['4. Verify certificate'],['5. Enumerate and count']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='The long guide supports understanding; the short deck shows the class exactly what the rubric asks for.',
task='What is the one sentence takeaway for the final slide?',
answer='Trying every open-site subset takes 2^m cases, even though checking one candidate is polynomial.'),
dict(title='A final audit of the problem choice',
core='Before claiming the topic in the class discussion, use the exact name “Uncapacitated Facility Location” and confirm no classmate has claimed the same problem. Decide whether the intended variant is general or metric. For the Friday explanation, the general decision problem is easy to define, exemplify, and verify. For the later final project, the chosen proof route and approximation requirement need attention.',
exact='The class instructions say the later NP-hardness proof should reduce from 3SAT, subset sum, or graph coloring. A documented chain from 3SAT through Set Cover to general UFL may work if the instructor permits composed reductions; confirm this before relying on it. The current report gives the Set-Cover-to-UFL step fully and labels the metric step separately.',
worked='The practical application can be siting clinics, depots, servers, or other assets using public or synthetic demand data. The exact objective must remain measurable: opening cost plus aggregate service cost. A later approximation solver can then be evaluated against exact small-instance results or rigorous lower bounds.',
pitfall='Topic interest is a starting point; a named variant, a valid reduction, and measurable solution quality make it a viable project.',
figure='Decision path from interest to defensible project',
nodes=[['Interest: site placement'],['Name variant and model'],['Confirm unique claim'],['Prove verifier and hardness'],['Implement and assess quality']],
edges=[(0,1),(1,2),(2,3),(3,4)],
read='Each gate makes the next phase concrete. The assignment is only Part 1 of a longer project.',
task='What detail should be posted when claiming the topic?',
answer='The specific problem name and variant, rather than only “optimal facility location.”')
]

SOURCES = [
('Course assignment', 'Final Project Part 1 - Pick and Present a Problem, local Canvas transcription, 2026-09-28. Due 2026-10-02.'),
('MIT 6.854 notes', 'Approximation Algorithms, Notes 20, Facility Location. https://courses.csail.mit.edu/6.854/21/Notes/n20-approx.html'),
('Northeastern lecture', 'Facility Location lecture notes, Set Cover reduction and metric construction. https://www.ccs.neu.edu/home/rraj/Courses/7880/F09/Lectures/FacLocFiltering.pdf'),
('Byrka and Aardal', 'An optimal bifactor approximation algorithm for the metric uncapacitated facility location problem, 2007. https://arxiv.org/abs/cs/0703010'),
('Jain, Mahdian, Saberi', 'A New Greedy Approach for Facility Location Problems, STOC 2002. doi:10.1145/509907.510012'),
]

def para(c, text, x, y, width=472, style=BODY):
    p = Paragraph(text.replace('<=', '&lt;=').replace('->', '&#8594;'), style)
    _, h = p.wrap(width, 1000)
    p.drawOn(c, x, y-h)
    return y-h

def header(c, number, section=None):
    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(70, 754, 'FACILITY LOCATION   |   PROFESSIONAL PRIMER')
    c.setStrokeColor(HexColor('#cddce0'))
    c.line(70, 743, 542, 743)
    if section:
        c.setFillColor(GRAY)
        c.setFont('Helvetica', 8)
        c.drawRightString(542, 754, section.upper())
    c.setFillColor(GRAY)
    c.setFont('Helvetica', 8)
    c.drawString(70, 37, 'Advanced Algorithms  |  Research companion to the five minute presentation')
    c.drawRightString(542, 37, str(number))

def page_title(c, kicker, title):
    c.setFillColor(TEAL)
    c.setFont('Helvetica-Bold', 9)
    c.drawString(70, 714, kicker.upper())
    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 20)
    c.drawString(70, 681, title)

def label_para(c, label, content, y):
    c.setFillColor(BLUE)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(70, y, label.upper())
    return para(c, content, 70, y-9)-21

def box(c, text, y, title='WHY THIS MATTERS'):
    p = Paragraph(text.replace('<=', '&lt;='), SMALL)
    _, h = p.wrap(436, 1000)
    ht=h+40
    c.setFillColor(PALE); c.roundRect(70,y-ht,472,ht,7,fill=1,stroke=0)
    c.setFillColor(TEAL); c.setFont('Helvetica-Bold',9)
    c.drawString(88,y-18,title)
    p.drawOn(c,88,y-31-h)
    return y-ht-16

def flow(c, spec, x=78, y=319, w=456, h=290):
    rows=spec['nodes']
    index={}; count=0
    for ri,row in enumerate(rows):
        for ci,s in enumerate(row):
            index[count]=(ri,ci,s,len(row)); count+=1
    centers={}
    for k,(ri,ci,s,n) in index.items():
        cx=x+w*(ci+1)/(n+1)
        cy=y+h-(ri+0.55)*h/len(rows)
        centers[k]=(cx,cy)
    c.setStrokeColor(HexColor('#94aeba')); c.setLineWidth(1.35)
    for a,b in spec.get('edges',[]):
        if a not in centers or b not in centers: continue
        ax,ay=centers[a]; bx,by=centers[b]
        c.line(ax,ay-20,bx,by+20)
    for k,(ri,ci,s,n) in index.items():
        cx,cy=centers[k]
        bw=min(190,w/n-20)
        c.setFillColor(PALE if ri in (0,len(rows)-1) else white)
        c.setStrokeColor(TEAL if ri in (0,len(rows)-1) else HexColor('#8aacba'))
        c.roundRect(cx-bw/2,cy-21,bw,42,6,fill=1,stroke=1)
        lines=[]; words=s.split(); line=''
        for word in words:
            test=(line+' '+word).strip()
            if len(test)>25 and line: lines.append(line); line=word
            else: line=test
        if line: lines.append(line)
        c.setFillColor(NAVY); c.setFont('Helvetica-Bold' if ri==0 else 'Helvetica',8.2)
        for li,line in enumerate(lines[:3]):
            c.drawCentredString(cx,cy+6-li*10,line)

def bars(c, spec, x=84,y=331,w=440,h=265):
    vals=spec['bars']; mx=max(v for _,v in vals); log=spec.get('logbars',False)
    c.setStrokeColor(HexColor('#8aa4ae')); c.line(x,y,x,y+h); c.line(x,y,x+w,y)
    n=len(vals); gap=w/n; bw=min(gap*0.55,54)
    for i,(name,val) in enumerate(vals):
        frac=(log2(val+1)/log2(mx+1)) if log else val/mx
        bh=frac*(h-40)
        bx=x+gap*i+(gap-bw)/2
        c.setFillColor(TEAL if val==min(v for _,v in vals) else BLUE)
        c.rect(bx,y,bw,bh,fill=1,stroke=0)
        c.setFillColor(NAVY); c.setFont('Helvetica-Bold',8)
        c.drawCentredString(bx+bw/2,y+bh+8,f'{val:,}')
        c.setFont('Helvetica',8.5); c.drawCentredString(bx+bw/2,y-17,name)
    if log:
        c.setFillColor(GRAY); c.setFont('Helvetica-Oblique',8)
        c.drawString(x+2,y+h+6,'Logarithmic height')

def matrix(c, spec, x=100,y=337,w=410,h=245):
    data=spec['matrix']; nr=len(data); nc=len(data[0]); cw=w/nc; ch=h/nr
    for r,row in enumerate(data):
        for col,value in enumerate(row):
            xx=x+col*cw; yy=y+(nr-r-1)*ch
            c.setFillColor(PALE if r==0 or col==0 else white)
            c.setStrokeColor(HexColor('#9eb8bf'))
            c.rect(xx,yy,cw,ch,fill=1,stroke=1)
            c.setFillColor(NAVY); c.setFont('Helvetica-Bold' if r==0 or col==0 else 'Helvetica',12)
            c.drawCentredString(xx+cw/2,yy+ch/2-4,value)

def figure_page(c, m, page, idx):
    header(c,page,f'figure {idx}')
    page_title(c,f'Figure {idx} of {len(MODULES)}',m['title'])
    c.setFillColor(GRAY); c.setFont('Helvetica-Oblique',10)
    c.drawString(70,648,m['figure'])
    c.setStrokeColor(HexColor('#d9e6e9')); c.roundRect(70,308,472,312,8,stroke=1,fill=0)
    if 'matrix' in m: matrix(c,m)
    elif 'bars' in m: bars(c,m)
    else: flow(c,m)
    y=291
    y=label_para(c,'Read the figure',m['read'],y)
    y=label_para(c,'Try it',m['task'],y)
    y=box(c,m['answer'],y+3,'ANSWER GUIDE')
    if y<56: raise ValueError(f'Figure page {page} overflows to {y}')
    c.showPage()

def content_page(c,m,page,idx):
    header(c,page,f'module {idx}')
    page_title(c,f'Module {idx} of {len(MODULES)}',m['title'])
    y=644
    y=label_para(c,'Core idea',m['core'],y)
    y=label_para(c,'Exact statement',m['exact'],y)
    y=label_para(c,'Worked example',m['worked'],y)
    y=box(c,m['pitfall'],y+3,'CHECK THE ASSUMPTION')
    if y<62: raise ValueError(f'Content page {page} overflows to {y}')
    c.showPage()

def cover(c):
    c.setFillColor(NAVY); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(HexColor('#68d1ca')); c.rect(70,661,65,5,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',32)
    c.drawString(70,607,'Facility Location')
    c.drawString(70,565,'from First Principles')
    c.setFont('Helvetica',16); c.setFillColor(HexColor('#d8e8ec'))
    c.drawString(70,521,'A professional primer for Advanced Algorithms')
    c.setFont('Helvetica',11)
    for n,s in enumerate([f'{2*len(MODULES)} learning pages across {len(MODULES)} modules', f'{len(MODULES)} original vector diagrams and charts',
                          'Formal definitions, examples, verification, search, hardness, and modeling',
                          'Research companion for the Friday 2 October 2026 presentation']):
        c.drawString(70,443-n*27,s)
    c.setFillColor(HexColor('#9edbd5')); c.setFont('Helvetica-Bold',9)
    c.drawString(70,125,'WORKING PROBLEM: UNCAPACITATED FACILITY LOCATION')
    c.setFillColor(HexColor('#d8e8ec')); c.setFont('Helvetica',9)
    c.drawString(70,101,'General decision variant for the introductory hardness proof; metric variant labeled separately.')
    c.showPage()

def orientation(c):
    header(c,2,'reader orientation')
    page_title(c,'How to use this guide','Start with the model')
    y=637
    y=label_para(c,'Purpose','This guide is a learning companion for a five minute class presentation on a chosen NP-complete facility-location variant. It begins with sets, functions, costs, and quantifiers; works through two fully checkable examples; then develops verification, brute force, NP membership, a Set Cover reduction, integer programming, heuristics, approximation, and real-world modeling. The Friday rubric asks for the problem, two examples, a verifier, and an exhaustive-search count. Modules 1-10 directly support that presentation.',y)
    y=label_para(c,'Working formulation','The main model is uncapacitated facility location with arbitrary nonnegative opening and service costs. In decision form, the question is whether the total can be at most a budget B. The simple Set Cover reduction in Modules 14-15 applies to the general, nonmetric variant. Metric distances require a separate construction; this distinction is made explicitly in Module 16.',y)
    y=label_para(c,'What to verify yourself','Recompute the 3-site, 4-client cost table in Modules 4-7. Trace one complete certificate through Module 8. Explain why the exhaustive search has 2^m site subsets in Module 10. Then state both directions of the reduction in Module 15 without looking. These checks reveal understanding more reliably than recognizing a definition.',y)
    y=box(c,'Notation: F is the set of candidate facilities; C is the set of clients; S is the set of open facilities; f_i is the cost to open i; c_ij is the cost of serving client j from i; sigma(j) is the site assigned to j; B is the decision budget; m=|F| and n=|C|.',y+3,'SYMBOLS USED THROUGHOUT')
    if y<60: raise ValueError(f'Orientation overflows to {y}')
    c.showPage()

def references(c,page):
    header(c,page,'sources and next steps')
    page_title(c,'Further reading','Sources and claim boundaries')
    y=637
    y=label_para(c,'Primary and course sources','The definitions, formulation, and approximation context are grounded in the sources below. The small numerical examples and all figures in this guide were constructed for explanation. They are not empirical siting results.',y)
    for name,detail in SOURCES:
        y=label_para(c,name,detail,y)
    y=box(c,'For the later project proof, establish an accepted chain from one of the course-approved sources (3SAT, subset sum, or graph coloring) to the exact named facility variant. The Set Cover to general UFL step is given in Modules 14-15. The Friday presentation needs the problem, two examples, verifier, and brute-force count.',y+3,'NEXT PROJECT GATE')
    if y<60: raise ValueError(f'References overflow to {y}')
    c.showPage()

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
    c.setTitle('Facility Location from First Principles')
    c.setAuthor('Advanced Algorithms research companion')
    cover(c); orientation(c)
    for idx,m in enumerate(MODULES,1):
        content_page(c,m,idx*2+1,idx)
        figure_page(c,m,idx*2+2,idx)
    references(c,2*len(MODULES)+3)
    c.save()
    print(f'Wrote {OUT} with {2*len(MODULES)+3} pages and {len(MODULES)} figures')

if __name__=='__main__': main()
