"""Printable graph atlas; original book crops and faithful video-data redraws."""
from pathlib import Path
import math, sys, importlib.util, json, textwrap
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/pdf'; TMP=ROOT/'tmp/pdfs'; TMP.mkdir(exist_ok=True,parents=True)
BOOK=fitz.open(ROOT/'Reading for Prep/JEA - Algorithms textbook (Erickson).pdf')
W,H=612,792; M=27; CW=W-2*M
items=[]
def book(fig,page,box,caption):
    p=BOOK[page-1]
    pix=p.get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(*box))
    path=TMP/f'figure-{fig}.png';pix.save(path)
    im=Image.open(path).convert('L'); im=ImageOps.autocontrast(im); im.save(path)
    items.append(dict(title=f'Erickson | Figure {fig}',source=f'Algorithms, printed p. {page-18}; PDF p. {page}',image=path,caption=caption))

book('5.4',210,(52,401,413,476),'These drawings encode the same two components despite different layouts. Trace actual edges, ignoring crossings without vertices. Circle each component, then choose one root per group and build search trees.')
book('5.5',211,(75,103,425,182),'Each segment or circle represents a vertex; intersections represent edges. Identify the two components without relying on spatial separation. Translate this representation into adjacency lists before running your component search.')
book('5.6',211,(117,389,382,431),'A recurrence becomes a directed dependency graph. Following arrows gives reachability, but not necessarily return paths. Identify singleton strong components, then erase arrowheads mentally and compare the resulting weak components.')
book('5.7',212,(167,67,299,192),'This grid contains directed dependencies rather than undirected roads. Determine whether any directed cycle exists. Compare forward reachability, weak connectivity, and strong connectivity before deciding which component algorithm applies here.')
book('5.8',212,(90,352,373,507),'Vertices represent legal disk configurations; edges represent single legal moves. Explore connectivity through the repeating triangular structure. Choose distant configurations and explain why a search can eventually connect those states.')
book('5.12',220,(114,263,350,366),'Depth first and breadth first searches choose different spanning trees while reaching the same component. Mark tree edges separately from original edges. Explain why changing search order cannot change membership.')
book('5.13',224,(134,184,332,276),'Treat each pixel of the chosen color as a vertex, joining side neighbors. Flood fill marks one component. Repeat from unmarked pixels, and test how allowing diagonal neighbors changes connectivity.')
book('6.1',244,(103,475,361,577),'Different starting vertices produce different directed DFS trees. A tree contains vertices reached during that search, not necessarily one strong component. Check return paths before grouping any two vertices together.')
book('6.4',247,(132,73,369,289),'Record entry and exit times while tracing the forest. Nested intervals indicate ancestry; separate intervals indicate completed branches. Use actual finish order, rather than discovery order, when preparing Kosaraju searches.')
book('6.5',248,(90,72,375,199),'Distinguish tree, forward, back, and cross edges using ancestry and active intervals. Back edges witness directed cycles. A cycle belongs inside one SCC, but overlapping cycles may form larger components.')
book('6.6',249,(193,236,308,342),'This directed acyclic graph has singleton strong components, even though many vertices remain reachable from others. Identify sources and sinks, then compare its weak components with the number of SCCs.')
book('6.8',250,(54,280,413,447),'Reverse postorder gives a topological order for this DAG. Trace several arrows in the linear arrangement. Explain why the same ordering cannot topologically sort individual vertices inside a directed cycle.')
book('6.13',256,(107,145,359,260),'The left drawing groups mutually reachable vertices; the right contracts each group. Preserve edges between different groups and remove internal edges. Explain why the resulting component graph contains no cycle.')
book('6.14',257,(69,233,432,345),'Compare the component shading with the DFS forest and active intervals. Component vertices form connected subtrees of the forest. Finishing times identify which component can be safely collected next here.')
book('6.17',259,(111,345,431,578),'The first traversal uses reversed edges; the second uses original edges in decreasing finish order. Track the component roots carefully. Already assigned vertices must never be collected into later groups.')
book('6.20',263,(151,405,352,468),'The highlighted vertices lie on every directed path between the designated endpoints. This is a path bottleneck question, not an SCC partition. Compare path counts before and after removing vertices.')
book('6.21',263,(146,532,354,617),'These highlighted vertices disconnect an undirected graph when removed. Count components before and after each deletion. Distinguish articulation points from SCCs: the graph here has undirected edges, so direction disappears.')
book('6.23',270,(135,496,329,616),'Letter labels and crossing edges complicate the picture without changing connectivity definitions. Ignore labels initially, identify singleton strong components, and verify that every directed path respects a valid topological ordering.')

BASE=ROOT/'output/advanced-algorithms-2026-10-22'
sys.path.insert(0,str(BASE/'common'))
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
metro=load('metro_atlas',BASE/'02-whatever-first-search-part-2/metrolog.py')
colony=load('colony_atlas',BASE/'01-whatever-first-search-part-1/trace_check.py')
path=load('paths_atlas',BASE/'03-class-lab-count-paths/pathlog.py')
topo=load('topo_atlas',BASE/'04-class-lab-topo-order/topolog.py')
maze=load('maze_atlas',BASE/'05-primer-preorder-postorder-cycles/mazelog.py')
classmod=load('class_atlas',ROOT/'output/advanced-algorithms-2026-10-26/trace_check.py')
def graph(title,g,caption,source,directed=True,pos=None):
    if pos is None:
        pos={v:(.5+.42*math.cos(2*math.pi*i/len(g)-math.pi/2),.5+.42*math.sin(2*math.pi*i/len(g)-math.pi/2)) for i,v in enumerate(g)}
    items.append(dict(title=title,graph=g,directed=directed,pos=pos,caption=caption,source=source))
graph('Colony | disconnected burrow',colony.graph,'The main colony and isolated burrow require separate searches. Start at S, mark everything reachable, then restart at X. Explain why revisiting marked vertices adds work but never new components.', 'Video 01: The Mole-Rat Colony | faithful data redraw',False)
graph('Metro | one connected network',metro.G,'Use either a stack or queue to explore this undirected network. Compare discovery trees while keeping component membership fixed. Every station belongs together because undirected paths connect all these vertices.', 'Video 02: The Metro Map | faithful data redraw',False)
graph('Metro | separate ferry network',metro.G2,'The ferry triangle adds a second component, not extra reachable stations from Arch. Run an outer loop across every vertex. Start another search only when its candidate root remains unmarked.', 'Video 02: The Metro Map | faithful data redraw',False)
graph('Metro | one-way tracks',metro.GD,'Following outgoing tracks from Arch cannot visit every station. That failure alone does not determine strong components. Search for directed return paths, then compare SCCs against the underlying undirected network.', 'Video 02: The Metro Map | one-way variant')
graph('Frog | stepping-stone dependencies',path.STONES,'Each arrow moves forward one or two stones, preventing directed cycles. Every strong component is therefore a singleton. Ignoring directions yields one connected component; explain why these statements coexist naturally.', 'Video 03: count_paths and the Frog | faithful data redraw')
graph('Class lab | diamond and tail',path.DIAMOND,'Two routes merge at d and continue to e. Shared descendants do not create strong connectivity without return paths. Trace finish order, reverse every arrow, and predict the singleton components.', 'Video 03: count_paths | class diamond',pos={'a':(.1,.5),'b':(.4,.85),'c':(.4,.15),'d':(.7,.5),'e':(.95,.5)})
graph('Hiking map | DAG',path.TRAIL,'Multiple uphill routes create many paths but no directed cycles. Treat each junction as its own SCC. Condensation changes nothing here; compare this result with the cyclic maze shown later.', 'Videos 03 and 06: hiking map | weights omitted for connectivity')
graph('Morning routine | class A-B-C-D graph',topo.G1,'Dependencies connect all four tasks weakly, yet none can return to an earlier task. List four singleton SCCs. Practice collecting them with both Kosaraju orientations and compare their output orders.', 'Video 04: topo_order and the Morning | original letter labels')
graph('Dinner | dependency network',topo.DINNER,'Follow dependencies from shopping through eating, then try to return. The missing return paths separate all strong components. Compare the DFS tree with SCC membership to avoid confusing these structures.', 'Video 04: topo_order and the Morning | dinner variant')
graph('Maze | directed cycles',maze.MAZE,'Trace the loops through B and E, and through C and F. Extend each loop using mutual reachability. Decide whether D or G joins either group before checking your partition.', 'Video 05: Preorder, Postorder, and Cycles | faithful data redraw')
graph('Maze | back edges removed',maze.DAG,'Removing the DFS back edges produces the lesson DAG. Recompute components rather than keeping the previous labels. Explain why removing edges can split strong components but cannot merge separate groups.', 'Video 05: Preorder, Postorder, and Cycles | DAG variant')
cp={'a':(.08,.5),'b':(.25,.88),'c':(.25,.12),'d':(.53,.12),'e':(.73,.3),'f':(.85,.75),'g':(.98,.75)}
graph('Class notes | original directed graph',classmod.CLASS_GRAPH,'Start at d and distinguish reachable vertices from vertices that can return. Circle the three strong components. Then contract them, preserving every connection between groups while discarding each internal arrow.', 'October 26 notes; Chapter 6 video | original 11-edge drawing',pos=cp)
graph('Chapter 6 video | added teaching edge',classmod.GRAPH,'The video adds arrow a to c inside an existing component. Verify that this shortcut changes some paths but leaves SCC membership unchanged. Compare with the original drawing shown earlier.', 'Chapter 6: Two Lessons in Ten Minutes | added edge a -> c',pos=cp)
rev=classmod.reverse_graph(classmod.CLASS_GRAPH)
graph('Class graph | reversed arrows',rev,'Reverse every original arrow while preserving isolated vertices and labels. Mutual reachability survives reversal, so component membership stays fixed. Only connections between components reverse; compare source and sink groups now.', 'Chapter 6 video | original class graph transposed',pos=cp)
graph('Class graph | condensation DAG',{'ABC':['DE','FG'],'DE':['FG'],'FG':[]},'Each vertex now represents an entire strong component. Two routes connect ABC to FG, but these are component routes, not counts of original graph paths. Check why no return exists.', 'Chapter 6 video | component names abbreviate vertex sets',pos={'ABC':(.12,.7),'DE':(.5,.15),'FG':(.88,.7)})
und={v:set() for v in classmod.CLASS_GRAPH}
for v,ns in classmod.CLASS_GRAPH.items():
    for n in ns:und[v].add(n);und[n].add(v)
graph('Class graph | undirected interpretation',und,'Erase directions and merge reciprocal arrows into single edges. This graph becomes one connected component. Remove f and recount; then relate the split to the number of DFS root children.', 'October 28 notes; Chapter 6 video | undirected variant',False,pos=cp)

# Preserve familiar video geometry for the principal examples.
colpos={'S':(.04,.5),'A':(.3,.88),'B':(.3,.5),'C':(.3,.12),'D':(.65,.88),'E':(.65,.5),'F':(.65,.12),'X':(.95,.75),'Y':(.95,.25)}
metpos={'Arch':(.04,.5),'Bay':(.3,.88),'Cove':(.3,.5),'Dock':(.3,.12),'East':(.65,.85),'Fort':(.65,.15),'Gate':(.95,.5)}
mazpos={'A':(.04,.5),'B':(.3,.88),'C':(.3,.12),'D':(.6,.88),'E':(.9,.88),'F':(.6,.12),'G':(.9,.12)}
dinpos={'Shop':(.04,.5),'Chop':(.23,.5),'Boil':(.42,.9),'Fry':(.42,.1),'Sauce':(.62,.5),'Plate':(.8,.5),'Eat':(.98,.5)}
for it in items:
    if it['title'].startswith('Colony'):it['pos']=colpos
    elif it['title'].startswith('Metro') and len(it['graph'])==7:it['pos']=metpos
    elif it['title'].startswith('Maze'):it['pos']=mazpos
    elif it['title'].startswith('Dinner'):it['pos']=dinpos

def wrap(s,width,font='Helvetica',size=7.5):
    lines=['']
    for word in s.split():
        trial=(lines[-1]+' '+word).strip()
        if stringWidth(trial,font,size)>width:lines.append(word)
        else:lines[-1]=trial
    return lines

def drawgraph(c,it,x,y,w,h):
    # Uniform, white nodes and dark edges; reciprocal arcs remain distinct.
    pos={v:(x+22+px*(w-44),y+16+py*(h-32)) for v,(px,py) in it['pos'].items()}
    r=15 if max(map(lambda v:len(str(v)),pos))<4 else 24
    edges={(u,v) for u,ns in it['graph'].items() for v in ns}
    done=set();c.setLineWidth(.9);c.setStrokeGray(.18);c.setFillGray(.18)
    for u,v in sorted(edges,key=str):
        if not it['directed'] and (v,u) in done:continue
        done.add((u,v));a,b=pos[u],pos[v];dx,dy=b[0]-a[0],b[1]-a[1];L=math.hypot(dx,dy)
        if L==0:continue
        bend=20 if it['directed'] and (v,u) in edges else 0
        # Route a long edge around intervening vertices; otherwise its existence
        # would be hidden behind the two shorter edges on the same line.
        for other,q in pos.items():
            if other in (u,v):continue
            t=((q[0]-a[0])*dx+(q[1]-a[1])*dy)/(L*L)
            distance=abs(dx*(q[1]-a[1])-dy*(q[0]-a[0]))/L
            if .06<t<.94 and distance<r+3:
                bend=(65 if str(u)<str(v) else 105) if it['directed'] and (v,u) in edges else 85
                break
        ctrl=((a[0]+b[0])/2-dy/L*bend,(a[1]+b[1])/2+dx/L*bend)
        if bend and not (x+8 <= ctrl[0] <= x+w-8 and y+8 <= ctrl[1] <= y+h-8):
            bend=-bend
            ctrl=((a[0]+b[0])/2-dy/L*bend,(a[1]+b[1])/2+dx/L*bend)
        def trim(p,q):
            d=math.hypot(q[0]-p[0],q[1]-p[1]);return p[0]+(q[0]-p[0])*r/d,p[1]+(q[1]-p[1])*r/d
        start=trim(a,ctrl);end=trim(b,ctrl)
        if bend:
            p=c.beginPath();p.moveTo(*start);p.curveTo(*ctrl,*ctrl,*end);c.drawPath(p)
        else:c.line(*start,*end)
        if it['directed']:
            theta=math.atan2(end[1]-ctrl[1],end[0]-ctrl[0]);p=c.beginPath();p.moveTo(*end)
            p.lineTo(end[0]-7*math.cos(theta-.42),end[1]-7*math.sin(theta-.42));p.lineTo(end[0]-7*math.cos(theta+.42),end[1]-7*math.sin(theta+.42));p.close();c.drawPath(p,fill=1,stroke=0)
    for v,(xx,yy) in pos.items():
        c.setFillGray(1);c.setStrokeGray(0);c.circle(xx,yy,r,stroke=1,fill=1);c.setFillGray(0);c.setFont('Helvetica-Bold',8 if r==24 else 10);c.drawCentredString(xx,yy-3,str(v))

def build():
    total=len(items)//2+1
    dest=OUT/'connected-components-graph-atlas.pdf'
    c=canvas.Canvas(str(dest),pagesize=(W,H));c.setTitle('Connected Components - Graph Practice Atlas');c.setAuthor('Study reference from Erickson and course lessons')
    audit=[]
    for i in range(0,len(items),2):
        page=i//2+1
        c.setFillGray(0);c.setFont('Helvetica-Bold',14);c.drawString(M,H-M-10,'CONNECTED COMPONENTS | GRAPH PRACTICE')
        c.setFont('Helvetica',7.5);c.drawString(M,H-M-24,'Circle groups. Trace arrows. Record finish order. Compare reachable sets with mutually reachable sets.')
        for j,it in enumerate(items[i:i+2]):
            top=H-77-j*342
            c.setFont('Helvetica-Bold',10);c.drawString(M,top,f'{i+j+1:02d}  {it["title"]}')
            c.setFont('Helvetica',7);c.drawString(M,top-12,it['source'])
            x,y,w,h=M+10,top-286,CW-20,261
            if 'image' in it:
                im=Image.open(it['image']);iw,ih=im.size;scale=min(w/iw,h/ih)
                c.drawImage(ImageReader(im),x+(w-iw*scale)/2,y+(h-ih*scale)/2,width=iw*scale,height=ih*scale)
            else:drawgraph(c,it,x,y,w,h)
            lines=wrap(it['caption'],CW)
            assert len(it['caption'].split())==30,(i+j+1,len(it['caption'].split()),it['caption'])
            assert len(lines)<=2,(i+j+1,lines)
            c.setFont('Helvetica',7.5);c.setFillGray(0)
            for k,line in enumerate(lines):c.drawString(M,top-304-k*10,line)
            audit.append({'panel':i+j+1,'words':30,'lines':len(lines),'font_pt':7.5,'title':it['title']})
            if j==0:c.setStrokeGray(.78);c.setLineWidth(.4);c.line(M,top-326,W-M,top-326)
        footer(c,page,total);c.showPage()
    finalpage(c,total);c.save()
    (TMP/'caption-audit.json').write_text(json.dumps(audit,indent=2))
    print(dest);print(f'{total} pages; {len(items)} images; every caption exactly 30 words, at most two lines, 7.5pt = 10px.')

def footer(c,p,total):
    c.setFont('Helvetica',7);c.setFillGray(.25);c.drawString(M,19,'Letter paper | 0.375-inch margins | Print at actual size | Grayscale friendly');c.drawRightString(W-M,19,f'{p} / {total}')

def finalpage(c,total):
    c.setFillGray(0);c.setFont('Helvetica-Bold',15);c.drawString(M,755,'BUILD THE ALGORITHMS | ONE-PAGE GUIDE')
    y=735
    sections=[
    ('Choose the connectivity question',
     'Undirected components: two vertices share a group when a path connects them. Weak components: ignore arrow directions first. Strong components: each vertex must reach the other by directed paths. A directed DFS tree is not generally an SCC. Use adjacency lists, include vertices with no outgoing edges, and keep vertex iteration order explicit for reproducible traces.'),
    ('1. Undirected components: recursive DFS, iterative DFS, or BFS',
     'Create one global visited set and an empty list of groups. Scan every vertex. For each unvisited root, create a fresh group, mark the root, and explore all unvisited neighbors, marking each when discovered. Recursion explores immediately; an explicit stack gives iterative depth-first exploration; a FIFO queue gives breadth-first exploration. When that search empties, save the group. Keep visited across roots. To find weak components, put both directions of every edge in the adjacency lists first. Each version takes O(V + E) time and O(V) auxiliary space.'),
    ('2. Kosaraju: original graph first (project orientation)',
     'First run a complete DFS forest on G. Mark a vertex on entry; append it to finish only after every outgoing neighbor has been processed. Restart at unvisited vertices until finish includes every vertex. Build GT by creating every vertex first, then adding v -> u for each u -> v. Reset visited. Scan finish backward and search GT from each still-unvisited root, collecting one fresh group per search. The resulting SCCs occur in source-to-sink topological order of G\'s component DAG. Never reverse discovery order as a substitute for finish order.'),
    ('3. Kosaraju: reversed graph first (book and October 26 lesson)',
     'Build GT, run the full finishing-order DFS on GT, reset visited, and process that finish list backward while searching G. This collects sink components first, so reverse the resulting component list if you need source-to-sink order. Both orientations give the same partition. For the class drawing the SCCs are {a,b,c}, {d,e}, and {f,g}; original-first yields that order, reversed-first yields its reverse. A finish list is append-on-exit order; popping its end processes decreasing finish time. Each orientation costs O(V + E) time and space.'),
    ('4. Iterative Kosaraju: preserve recursive return events',
     'Replace each recursive first-pass call with a stack frame containing a vertex and an iterator over its remaining neighbors. Mark a vertex before pushing its frame. Inspect the top frame: advance to the next neighbor, pushing a frame only if that neighbor is new. When the iterator is exhausted, pop that frame and append its vertex to finish. This reproduces recursive postorder without recursion-depth limits. The second pass needs only a normal reachability stack or queue because it collects vertices, not finishing times.'),
    ('5. Tarjan: a one-pass SCC alternative (Erickson 6.6)',
     'Give each newly discovered vertex an increasing index; initialize low[v] = index[v]. Push it onto a separate active-component stack and mark on_stack. For an unvisited neighbor w, recurse, then lower low[v] using low[w]. For an already discovered neighbor still on_stack, lower low[v] using index[w]; ignore edges to completed components. On return, if low[v] = index[v], pop through v and emit those vertices as one SCC. The component stack is separate from the DFS call stack. This standard variant takes O(V + E) time and O(V) auxiliary space.'),
    ('Build the component DAG, then verify',
     'Map each original vertex to its component id; use a frozenset of member ids when matching the project interface. Insert component vertices in the required order. Scan every original edge u -> v; add an edge between their component ids only when the ids differ, deduplicating repeated pairs. Check that every vertex appears exactly once, each group is mutually reachable, and the component graph is acyclic. Test an empty graph, an isolated vertex, a self-loop, a chain, one cycle, disconnected cycles, and two cycles joined by one one-way edge.'),
    ('October 28 extension: cut vertices and paths through a vertex',
     'For an undirected DFS forest, a root is a cut vertex exactly when it has at least two DFS children. A non-root v is a cut vertex when some child w has low[w] >= discovery[v], using undirected ancestor back edges and excluding the parent edge. This low value is not Tarjan\'s SCC stack rule. In a DAG with fixed endpoints s and t, count paths to v in topological order and paths from v in reverse order; their product counts s-to-t paths through v. Do not apply this counting rule directly to cyclic graphs.'),
    ]
    for title,body in sections:
        c.setFont('Helvetica-Bold',9);c.drawString(M,y,title);y-=12
        for line in wrap(body,CW,size=9.5):
            c.setFont('Helvetica',9.5);c.drawString(M,y,line);y-=11.7
        y-=9
    assert y>56,y
    c.setFont('Helvetica',6.8)
    c.drawString(M,47,'Sources: Erickson, Algorithms, Chapters 5-6; course videos dated Oct 22 and Oct 26/28; live class notes fetched Oct 29, 2026.')
    c.drawString(M,37,'Scope: relevant graph-search / connectivity figures, not every illustration in the textbook. Video panels are source-data redraws.')
    footer(c,total,total)

if __name__=='__main__':
    if '--counts' in sys.argv:
        for i,it in enumerate(items):print(i+1,len(it['caption'].split()),it['caption'])
    else:build()

