"""Word-synchronized diagrams for the combined primer."""
import json
import math
from pathlib import Path
from engine import *
from graphview import GraphView
from widgets import chrome, panel_card, draw_wrapped, predict_chip, tag
from trace_check import GRAPH, CLASS_GRAPH
HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'combined-trace.json').read_text(encoding='utf-8'))
SCC=json.loads((HERE/'trace.json').read_text(encoding='utf-8'))['video']
POS={'a':(140,370),'b':(320,230),'c':(290,650),'d':(640,630),'e':(850,610),'f':(1030,350),'g':(1170,350)}
COLORS={'a':BLUE,'b':BLUE,'c':BLUE,'d':GREEN,'e':GREEN,'f':ACCENT,'g':ACCENT}
TREE=DATA['figure']['parent']
FPOS={v:(155+(i%4)*175,250+(i//4)*150) for i,v in enumerate('abcdefghijklmnop')}

def word_state(ctx):
    spoken=[]; current=''
    for w in ctx.b['words']:
        if ctx.t >= w['t0']:
            spoken.append(w['disp']); current=w['disp']
    return ' '.join(spoken),current.strip('.,?:;').lower()

def point(ctx,x,y,color=ACCENT):
    # Brief eased appearance rather than continuous motion during reading.
    a=ctx.p('w0',.4)
    ctx.cv.circle(x,y,12,fill=color,a=a)

def panel(ctx,title,rows):
    panel_card(ctx,title)
    y=185
    for heading,body,color in rows:
        ctx.cv.text(1320,y,heading,30,color,True)
        y+=45
        for line in body.split('\n'):
            y+=draw_wrapped(ctx.cv,1320,y,line,31,515,INK,lead=1.25)
        y+=30

def class_graph(ctx,undirected=False,reverse=False,groups=False,remove=False):
    edges=[]; seen=set()
    for u,ns in GRAPH.items():
        for v in ns:
            if undirected:
                key=tuple(sorted((u,v)))
                if key in seen: continue
                seen.add(key)
            if reverse: u1,v1=v,u
            else: u1,v1=u,v
            bulge=45 if (u,v) in [('d','e'),('e','d'),('f','g'),('g','f')] else 0
            if (u,v)==('a','c') and not undirected: bulge=-90
            edges.append((u1,v1,bulge))
    gv=GraphView(POS,edges,directed=not undirected,r=35,label_size=36)
    spoken,current=word_state(ctx)
    rings={current:(ACCENT,1)} if current in POS else {}
    fills={v:(COLORS[v],.85) for v in POS} if groups else {}
    if ctx.b['section']==21:
        fills={v:(BLUE,.7) for v in 'abcde'}
        fills.update(f=(GREEN,.8),g=(ACCENT,.8))
    styles={}
    for u,v,_ in edges:
        color=LINE
        alpha=.8
        if current in (u,v): color=ACCENT
        if remove and 'f' in (u,v): alpha=.12
        if ctx.b['section']==21:
            parents=DATA['root_f']['parent']
            tree=parents.get(u)==v or parents.get(v)==u
            color=GREEN if tree else GRAY
            alpha=1 if tree else .35
        styles[gv.key(u,v)]=(color,4,alpha)
    gv.draw(ctx,fills=fills,rings=rings,estyle=styles,vfade={'f':.15} if remove else {})
    # Draw the extra teaching edge as dashes over a cleared line.
    if not undirected:
        eu,ev=('c','a') if reverse else ('a','c')
        pts=gv.pts(eu,ev)
        ctx.cv.poly_line(pts,(241,246,246),7)
        for k in range(0,len(pts)-8,18):
            ctx.cv.poly_line(pts[k:k+9],BLUE,3)
    ctx.cv.text(65,745,'Undirected version of the class drawing' if undirected else 'Class drawing: seven vertices, eleven original arrows',26,MUTED)
    ctx.cv.text(65,785,'Reciprocal arrows now share one undirected edge.' if undirected else 'Teaching addition: a → c (same components)',25,BLUE)
    # Visually label the additional edge, rather than implying it was in class.
    x,y=gv.mid('c','a') if reverse else gv.mid('a','c')
    ctx.cv.text(x+10,y,'+',24,BLUE,True)

def figure(ctx):
    from combined_trace_check import FIGURE
    sec=ctx.b['section']; spoken,current=word_state(ctx)
    edges=[(u,v,30 if (v,u) in [(a,b) for a,ns in FIGURE.items() for b in ns] else 0) for u,ns in FIGURE.items() for v in ns]
    gv=GraphView(FPOS,edges,directed=True,r=25,label_size=30)
    styles={}
    for u,v,_ in edges:
        tree=TREE[v]==u
        color=GREEN if tree else GRAY
        if sec==6 and (u,v)==('d','c'): color=ACCENT
        styles[(u,v)]=(color,5 if tree else 2,.95 if tree else .55)
    gv.draw(ctx,estyle=styles,rings={current:(ACCENT,1)} if current in FPOS else {})
    ctx.cv.text(65,155,'Figure 6.4 · graph and active intervals',35,INK,True)
    pre=DATA['figure']['pre']; post=DATA['figure']['post']
    order=sorted(pre,key=pre.get)
    for i,v in enumerate(order):
        y=235+i*32
        x0=800+(pre[v]-1)*12; x1=800+(post[v]-1)*12
        col=ACCENT if v==current else GREEN
        if sec==4 and v in 'hdl': col={'h':BLUE,'d':ACCENT,'l':GREEN}[v]
        grow=ctx.p('w0',.7) if sec==3 else 1
        ctx.cv.rrect(x0,y,max(x0+2,x0+(x1-x0)*grow),y+23,3,fill=mix(WHITE,col,.25),outline=col,width=2)
        ctx.cv.text(x0-20,y,v,21,INK,True,anchor='ra')
    for t in (1,6,8,9,17,22,32):
        x=800+(t-1)*12
        ctx.cv.text(x,765,str(t),19,MUTED,anchor='ma')
    ctx.cv.text(830,810,'entry → active call → return',25,INK)

def dag(ctx,shortcut=True,counts=False):
    pos={'ABC':(240,380),'DE':(640,600),'FG':(1050,380)}
    edges=[('ABC','DE'),('DE','FG')]
    if shortcut: edges.append(('ABC','FG',-85))
    gv=GraphView(pos,edges,directed=True,r=65,label_size=38)
    gv.draw(ctx,fills={'ABC':(BLUE,.85),'DE':(GREEN,.85),'FG':(ACCENT,.85)})
    ctx.cv.text(65,155,'A DAG of three components',36,INK,True)
    ctx.cv.text(200,270,'start s',30,BLUE,True)
    ctx.cv.text(1000,270,'target t',30,ACCENT,True)
    if counts:
        d=DATA['component_dag'] if shortcut else DATA['no_shortcut']
        for v,(x,y) in pos.items():
            ctx.cv.text(x,y+95,f"to {d['to'][v]}  ×  from {d['onward'][v]}",28,INK,True,anchor='ma')
        ctx.cv.text(640,775,'through = to × from',38,GREEN,True,anchor='ma')

def scene(ctx):
    cv=ctx.cv; sec=ctx.b['section']; part=ctx.b['part']
    spoken,current=word_state(ctx)
    ctx.sig.append((sec,part,spoken))
    cv.rrect(30,118,1260,915,24,fill=(241,246,246),outline=PANEL_LINE,width=2)
    if 2<=sec<=7:
        figure(ctx)
        rows={
            2:[('Two views','The arrows describe connections. The bars record the calls.',BLUE)],
            3:[('pre = entry','The recursive call begins.',BLUE),('post = return','The call has finished checking its neighbors.',GREEN)],
            4:[('Active intervals','h: [6, 17]\nd: [7, 8]\nl: [9, 16]',BLUE),('Read the picture','Nested bars show ancestry. Separate bars show calls at different times.',GREEN)],
            5:[('Discovery forest','Green edges first discover vertices. Other graph edges remain.',GREEN),('One discovery per vertex','Several incoming edges may lead to the same vertex.',BLUE)],
            6:[('new → active → finished','Active vertices are on the recursive call stack.',BLUE),('d → c','The edge returns to an active ancestor. Together with the tree path, it forms a cycle.',ACCENT)],
            7:[('Four relationships','Tree: direct child\nForward: other descendant\nBack: ancestor\nCross: separate branch',BLUE)]
        }[sec]
        if sec==4 and ctx.b.get('predict'):
            rows=[rows[0],('Predict','Which call finishes first? Is d still active when l starts?',GREEN)]
        panel(ctx,'READING FIGURE 6.4',rows)
    elif sec in (8,10,14,16,17,18,19,23):
        removed=sec==19 and ('remove' in spoken.lower() or part>=3)
        dag(ctx,shortcut=not removed,counts=sec in (18,19) and not ctx.b.get('predict'))
        rows={
            8:[('Topological order','ABC → DE → FG',BLUE),('Dependencies','If arrows point to needed values, compute those values first.',GREEN)],
            10:[('Why a DAG?','A cycle between groups would give return journeys and merge those groups.',GREEN)],
            14:[('Finish-time idea','For X → Y between components, max finish(X) > max finish(Y).',BLUE),('Two cases','Explore X first: Y finishes inside its search. Explore Y first: it finishes before X starts.',GREEN)],
            16:[('Interpretation of the notes','“to” and “from” + multiplication + removing vertices',BLUE),('Working question','How many complete paths pass through each vertex?',GREEN)],
            17:[('Fixed endpoints','to(v): paths s → v\nfrom(v): paths v → t',BLUE),('Unique split','A complete path through v has one prefix and one suffix.',GREEN)],
            18:[('Two evaluation orders','To: add incoming counts.\nFrom: add outgoing counts in reverse order.',BLUE),('Middle box','1 × 1 = 1 path through DE',GREEN)],
            19:[('Complete paths','1 without the shortcut' if removed else '2 with the shortcut',BLUE),('Through the middle','1 path through DE',GREEN),('Compare','All complete paths use DE.' if removed else 'One of two paths uses DE.',ACCENT)],
            23:[('Read in this order','6.1: bars and ancestry\n6.2–6.3: cycles and order\n6.4: memoization',BLUE),('Then connect the lessons','6.5–6.6: components\nExercises 3–4: paths and vertex removal',GREEN)]
        }[sec]
        if sec==19 and ctx.b.get('predict'):
            rows=[('Two routes','The shortcut, or the route through the middle.',BLUE),('Predict','How many routes pass through DE?',GREEN)]
        panel(ctx,'FOLLOW THE RELATIONSHIPS',rows)
    else:
        reverse=sec==13 and part==1 and 'Return' not in spoken
        remove=sec==20 and ('Remove' in spoken or part>1)
        is_undirected=20<=sec<=22 or (sec==24 and part>=2)
        class_graph(ctx,undirected=is_undirected,reverse=reverse,groups=sec in (9,12,13,15),remove=remove)
        title='UNDIRECTED VERSION' if is_undirected else ('PASS 1: REVERSED GRAPH' if reverse else 'MONDAY’S DIRECTED GRAPH')
        rows={
            1:[('Three questions','Where can a path go?\nCan it return?\nWhat does it pass through?',BLUE)],
            9:[('Return-trip groups','{a, b, c}\n{d, e}\n{f, g}',GREEN),('Strong components','Each group includes everyone who can reach one another.',BLUE)],
            11:[('Search from d','d → e → f → g',BLUE),('Compare the groups','Reachability includes {d,e} and {f,g}.',GREEN)],
            12:[('Start at f','Collect {f, g}.',ACCENT),('Then start at d','Collect {d, e}; f and g are already assigned.',GREEN)],
            13:[('Finish stack · top at right','b c a e d g f',BLUE),('Pop in the original graph','f → {f,g}\nd → {d,e}\na → {a,b,c}',GREEN)],
            15:[('Two kinds of state','Pass 1: visited while recording order.\nPass 2: assigned to components.',BLUE),('Work per pass','Each vertex and edge once: O(V + E).',GREEN)],
            20:[('Remove vertex f','All edges touching f are removed. Vertex g is then separate.',BLUE),('Cut vertex','Removing it increases the number of connected components.',GREEN)],
            21:[('DFS rooted at f','Tree children: b and g',BLUE),('Child branches','b branch: {a,b,c,d,e}\ng branch: {g}',GREEN),('Root condition','At least two DFS children → cut vertex',ACCENT)],
            22:[('Another connection','Can the child subtree reach an ancestor above this vertex?',BLUE),('Non-root condition','Some child has low[child] ≥ pre[vertex].',GREEN),('Reading note','Exercise 4(b)(ii) appears to omit “not”; use the connection argument.',ACCENT)],
            24:[('Retell the connection','Discovery → active intervals\nFinish order → evaluation\nTwo passes → components',BLUE),('Try on paper','Draw two child branches. Remove the root. Explain what remains.',GREEN)]
        }[sec]
        if sec==11 and part<=2:
            rows=[('Start at d','Follow the outgoing arrows.',BLUE),('Predict','Which vertices does this search reach?',GREEN)]
        if sec==21 and part<=2:
            rows=rows[:2]
        if sec==13:
            if part==1:
                stack_text=''
                if 'Our stack is ' in spoken:
                    suffix=spoken.split('Our stack is ',1)[1].split('Return')[0]
                    stack_text=' '.join(w.strip('.,') for w in suffix.split() if w.strip('.,') in list('BCAEDGF'))
                rows=[('Finish stack · top at right',stack_text or '(record each vertex on return)',BLUE),('Current graph','Original arrows: ready to pop.' if not reverse else 'Reversed arrows: compute finish order.',GREEN)]
            elif part==2:
                found=[]
                for letter,group in [('F','{f,g}'),('D','{d,e}'),('A','{a,b,c}')]:
                    if letter in [w.strip('.,') for w in spoken.split()]: found.append(group)
                rows=[('Pop order','f g d e a c b',BLUE),('Components collected',' → '.join(found) or '(start at f)',GREEN)]
        panel(ctx,title,rows)
    # Show one small focus marker at the actually spoken vertex.
    predict_chip(ctx)
    chrome(ctx)
