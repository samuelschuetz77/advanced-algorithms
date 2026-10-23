"""Concrete-first rewrite of the four narrated Huffman study videos."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

from PIL import ImageDraw

ROOT = Path(__file__).resolve().parent
ENGINE_PATH = ROOT.parent / "huffman-week-2026-10-13-revised" / "build.py"
if ENGINE_PATH.exists():
    spec = importlib.util.spec_from_file_location("huffman_video_engine", ENGINE_PATH)
    engine = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(engine)
else:
    # The earlier video set can be removed independently of this final cut.
    import rebuild_prefix
    import rebuild_leaf_cost
    import rebuild_queue_context

    class SavedClipEngine:
        visual = staticmethod(lambda *args: None)
        beat = staticmethod(lambda headline, visual, narration: {
            "headline": headline, "visual": visual, "narration": narration
        })
        @staticmethod
        def main():
            rebuild_prefix.main()
            rebuild_leaf_cost.main()
            rebuild_queue_context.main()

    engine = SavedClipEngine()
base_visual = engine.visual
beat = engine.beat

LESSONS = [
    {
        "name": "01 - BANANA - One Word, Fewer Bits",
        "tag": "START WITH ONE WORD",
        "accent": "#E76F51",
        "beats": [
            beat("Imagine sending the word BANANA.", {"kind":"message"},
                 "Imagine typing BANANA on one phone and sending it to another. The second phone must receive the exact same six letters, in the same order."),
            beat("Computers send tiny yes-or-no choices.", {"kind":"bit"},
                 "A computer can represent information with zeros and ones. One zero or one is called a bit: a tiny choice between two possibilities."),
            beat("Give each letter a two-bit label.", {"kind":"fixed"},
                 "Let's make a tiny codebook for the three letters in BANANA. These are labels we choose for this example, so there are no ASCII codes to memorize. Each label has exactly two bits."),
            beat("BANANA now takes twelve bits.", {"kind":"fixed_total"},
                 "Read across BANANA. Each of its six letters contributes two bits, so the whole word takes twelve bits."),
            beat("A appears three times.", {"kind":"banana_focus","letter":"A","count":3},
                 "Look at A. It appears in the second, fourth, and sixth positions. We have to send A's label three times."),
            beat("N appears twice.", {"kind":"banana_focus","letter":"N","count":2},
                 "N appears in the third and fifth positions. Its label is sent twice."),
            beat("B appears once.", {"kind":"banana_focus","letter":"B","count":1},
                 "B appears only at the beginning. Its label is sent just once."),
            beat("What if A had a shorter label?", {"kind":"banana_label","letter":"A","code":"0"},
                 "Because A appears most often, make its label just zero. Every A now saves one bit."),
            beat("Keep N and B distinguishable.", {"kind":"banana_two_labels"},
                 "Give N the label one zero and B the label one one. Those labels are longer, but we use them less often."),
            beat("The same word now takes nine bits.", {"kind":"bit_compare"},
                 "B uses two bits once. N uses two bits twice. A uses one bit three times. That adds up to nine bits instead of twelve."),
            beat("Can the receiver read it back?", {"kind":"decode_banana"},
                 "Yes. Read the bits from left to right: one one means B, zero means A, and one zero means N. Continue to recover BANANA."),
            beat("Equal-length bytes have clear boundaries.", {"kind":"ascii_bytes"},
                 "Here is BANANA in eight-bit ASCII bytes. Every letter takes eight digits, so we know where to cut: after each group of eight. You do not need to memorize these codes."),
            beat("A bad short code can be ambiguous.", {"kind":"prefix_bad"},
                 "Suppose A is zero, N is zero one, and B is one. Now zero one could mean N, or A followed by B. The zero at the start of N is already A. That is the problem."),
            beat("Our short labels avoid that problem.", {"kind":"prefix_good"},
                 "With our actual labels, zero finishes A. If the first bit is one, read another: one zero is N, and one one is B. No complete label starts another label. That is the prefix-free rule."),
            beat("This is what Huffman encoding is about.", {"kind":"bit_compare"},
                 "That is what Huffman encoding is about: give common letters shorter labels, keep every label readable, and send fewer bits overall.")
        ]
    },
    {
        "name": "02 - What Greedy Means",
        "tag": "READING 4.1 → 4.4",
        "accent": "#3F77B9",
        "beats": [
            beat("Imagine three files on a tape.", {"kind":"tape","items":[2,5,9]},
                 "A tape stores files in a line. These files have lengths two, five, and nine. You must pass earlier files to reach later ones."),
            beat("To read the last file, scan all three.", {"kind":"scan"},
                 "If you want the last file, you first pass the first file and the second. Then you finally read the last one."),
            beat("Short first: total cost 25.", {"kind":"costs","order":"2  →  5  →  9","costs":"2, 7, 16","total":"25"},
                 "In the order two, five, nine, the three read costs are two, seven, and sixteen. Together they total twenty-five."),
            beat("Long first: total cost 39.", {"kind":"costs","order":"9  →  5  →  2","costs":"9, 14, 16","total":"39"},
                 "Reverse the order. The read costs are now nine, fourteen, and sixteen. Together they total thirty-nine."),
            beat("Why did moving two help?", {"kind":"repeated"},
                 "The first file gets scanned on every read. A short first file is cheaper each time that repeated scan happens."),
            beat("This is a greedy choice.", {"kind":"swap","before":"9   |   2","after":"2   |   9"},
                 "Put the shorter file earlier, commit to that choice, and continue. That is a greedy method: choose a helpful step now."),
            beat("Huffman chooses two small trees.", {"kind":"pool","items":[4,6,8,11],"selected":[0,1]},
                 "Huffman has a different problem but a similar habit. Among the trees available right now, choose the two lightest."),
            beat("The new tree must go back in.", {"kind":"merge","a":4,"b":6,"sum":10},
                 "Joining weights four and six creates a tree of weight ten. Put that new tree back with the trees you have not used."),
            beat("Choose from the updated pool.", {"kind":"pool","items":[8,10,11],"selected":[0,1]},
                 "Now the available weights are eight, ten, and eleven. The next two are eight and ten. Recheck after every merge.")
        ]
    },
    {
        "name": "03 - Build One Huffman Tree",
        "tag": "READING 4.4 · PRACTICE EXAMPLE",
        "accent": "#149584",
        "beats": [
            beat("Each symbol starts as one leaf.", {"kind":"symbol_pool","items":[["P",4],["Q",6],["R",8],["S",11],["T",15]],"selected":[]},
                 "Our separate practice message has five symbols. P occurs four times, Q six, R eight, S eleven, and T fifteen."),
            beat("The two smallest are P and Q.", {"kind":"symbol_pool","items":[["P",4],["Q",6],["R",8],["S",11],["T",15]],"selected":[0,1]},
                 "P's weight is four and Q's is six. They are the two least frequent symbols, so Huffman joins them first."),
            beat("Their parent weighs ten.", {"kind":"merge","a":4,"b":6,"sum":10},
                 "Place P and Q under one new parent. Its weight is four plus six, which is ten."),
            beat("Now eight is the smallest.", {"kind":"pool","items":[8,10,11,15],"selected":[0,1]},
                 "The new tree of weight ten returns to the pool. R still weighs eight, so eight and ten leave next."),
            beat("Eight and ten make eighteen.", {"kind":"merge","a":8,"b":10,"sum":18},
                 "Join R to the P-Q tree. Their new parent weighs eighteen. It contains three original symbols."),
            beat("Next, eleven and fifteen.", {"kind":"merge","a":11,"b":15,"sum":26},
                 "The remaining weights are eleven, fifteen, and eighteen. The smallest pair is eleven and fifteen, making twenty-six."),
            beat("Finish with eighteen and twenty-six.", {"kind":"merge","a":18,"b":26,"sum":44},
                 "Two trees remain. Join them under a parent of weight forty-four. Now every symbol belongs to one tree."),
            beat("Put bits on the edges.", {"kind":"tree","tree":"practice"},
                 "Let left mean zero and right mean one. The code for a letter is the bits you pass from the top to that letter."),
            beat("Read one path: P is 010.", {"kind":"practice_path"},
                 "To reach P, go left, then right, then left. Write those edge bits in order: zero, one, zero."),
            beat("The weights add to forty-four.", {"kind":"weight_sum"},
                 "You're right: four plus six plus eight plus eleven plus fifteen is forty-four. These weights count how often the letters appear. They do not yet count bits."),
            beat("Multiply by each code's length.", {"kind":"weighted_lengths"},
                 "P and Q have three-bit codes. R, S, and T have two-bit codes. Multiply each letter's weight by the number of bits in its code."),
            beat("The message takes ninety-eight bits.", {"kind":"weighted_total"},
                 "Four times three plus six times three plus eight times two plus eleven times two plus fifteen times two equals ninety-eight bits. That is the total encoded message length."),
            beat("The merge sum checks the answer.", {"kind":"merge_total"},
                 "The merge weights also add to ninety-eight: ten plus eighteen plus twenty-six plus forty-four. This gives us a second way to check the bit count.")
        ]
    },
    {
        "name": "04 - Use the Tree as a Codec",
        "tag": "ASSIGNMENT PARTS 2–3 · CONCEPTS",
        "accent": "#785FBD",
        "beats": [
            beat("A program must build the tree first.", {"kind":"pool","items":[4,6,8,11],"selected":[0,1]},
                 "The hand trace kept finding the two smallest available weights. A program needs a way to do that repeatedly."),
            beat("Two Project Two tools have different jobs.", {"kind":"graph_queue_roles"},
                 "The assignment reuses two things you built in Project Two. The Graph holds the Huffman tree, with zero or one on each edge. The priority queue chooses which current trees to join next."),
            beat("A priority queue chooses what goes next.", {"kind":"pq_role"},
                 "Your learning log calls it a line where the most important item goes next. Here, each item is one current tree. Its priority is that tree's total frequency, and the smallest weight goes next."),
            beat("A min-heap makes the minimum quick.", {"kind":"heap_role"},
                 "Project Two implements the queue with a min-heap. Each parent weighs no more than its children, so the root is the minimum. The whole heap is not sorted. After a removal, it rearranges to restore that rule."),
            beat("The locator tells us where a key is.", {"kind":"locator_role"},
                 "Your locator dictionary maps each tree's unique key to its position in the heap array. When two heap entries swap, their locator positions change too. It helps remove or update a known key. The heap, not the locator, chooses the minimum."),
            beat("Take the minimum twice, one at a time.", {"kind":"two_removals"},
                 "Your Project Two queue lets us peek at the minimum and remove that node. Take the weight-four tree first. The heap rearranges, so weight six becomes the new minimum. Remove that tree next. The queue is not fully sorted. Join four and six into a weight-ten tree, then insert it."),
            beat("The finished tree holds the codes.", {"kind":"tree","tree":"practice"},
                 "In the finished tree, each edge carries a zero or one. A symbol's path from the top is its code."),
            beat("A map points to each letter's leaf.", {"kind":"map","items":[["P","leaf P"],["Q","leaf Q"],["R","leaf R"]]},
                 "The symbol-to-leaf map helps the program jump straight to the right leaf instead of hunting through the tree."),
            beat("To encode P, follow its path.", {"kind":"practice_path"},
                 "P's path is left, right, left, so the program emits zero, one, zero. It repeats that for each input symbol."),
            beat("To decode, reverse the direction.", {"kind":"flow","top":"010","bottom":"P"},
                 "Start at the tree's top and follow the incoming bits. Zero, one, zero ends at P, so output P."),
            beat("Keep the first test tiny.", {"kind":"flow","top":"P  Q  P","bottom":"encode → decode → P  Q  P"},
                 "Encode the short message P-Q-P, then decode those bits. The result should be P-Q-P again."),
            beat("For alternatives, ask two questions.", {"kind":"questions","items":["Same two smallest each time?","How much work repeats?"]},
                 "When comparing other methods, ask whether they choose the correct pair after every merge. Then ask how much repeated work they do.")
        ]
    }
]


def centered_text(draw, text, x, y, font, fill):
    draw.text((x-engine.width(draw,text,font)/2,y),text,font=font,fill=fill)


def bubble(draw, x, y, label, accent, filled=False, radius=45):
    draw.ellipse((x-radius,y-radius,x+radius,y+radius),fill=accent if filled else "#FFFFFF",outline=accent,width=4)
    f=engine.face(35,True)
    centered_text(draw,label,x,y-27,f,"#FFFFFF" if filled else engine.INK)


def visual(draw, info, accent, progress):
    kind=info["kind"]
    if kind=="message":
        for x in (155,925):
            draw.rounded_rectangle((x,290,x+210,535),radius=35,fill="#FFFFFF",outline=engine.INK,width=5)
            draw.rounded_rectangle((x+18,315,x+192,490),radius=14,fill="#EAEFF0")
            draw.ellipse((x+94,507,x+115,528),fill=engine.INK)
        f=engine.face(39,True)
        centered_text(draw,"BANANA",260,375,f,accent)
        if progress>.35:
            draw.line((420,410,845,410),fill=accent,width=8)
            draw.polygon([(845,410),(814,392),(814,428)],fill=accent)
        if progress>.68:
            centered_text(draw,"BANANA",1030,375,f,accent)
        else:
            centered_text(draw,"?",1030,375,f,engine.MUTED)
    elif kind=="bit":
        bubble(draw,465,410,"0",accent,progress>.25,70)
        if progress>.50:
            bubble(draw,815,410,"1",accent,True,70)
        engine.center(draw,"one bit = one choice",525,engine.face(29,True),engine.MUTED)
    elif kind in {"fixed","fixed_total"}:
        mappings=[("B","00"),("A","01"),("N","10")]
        if kind=="fixed":
            visible=max(1,math.ceil(progress*len(mappings)))
            for i,(letter,code) in enumerate(mappings[:visible]):
                x=235+i*300
                draw.rounded_rectangle((x,350,x+220,465),radius=22,fill="#FFFFFF",outline=accent,width=3)
                centered_text(draw,f"{letter}  =  {code}",x+110,385,engine.face(40,True),engine.INK)
        else:
            letters=list("BANANA")
            active=min(5,int(progress*6))
            for i,letter in enumerate(letters):
                centered_text(draw,letter,345+i*118,420,engine.face(39,True),accent if i==active else engine.INK)
            codes=["00","01","10","01","10","01"]
            for i,code in enumerate(codes):
                centered_text(draw,code,345+i*118,490,engine.face(36,True,mono=True),accent if i==active else engine.MUTED)
            if progress>.70:
                engine.center(draw,"6 letters × 2 bits = 12 bits",555,engine.face(28,True),engine.MUTED)
    elif kind=="banana_focus":
        letter=info["letter"]
        for i,ch in enumerate("BANANA"):
            x=315+i*125
            centered_text(draw,ch,x,345,engine.face(72,True),accent if ch==letter else "#A8B0B5")
        count=info["count"]
        label=f"{letter} appears {count} " + ("time" if count==1 else "times")
        engine.center(draw,label,480,engine.face(39,True),accent)
    elif kind=="banana_label":
        letter=info["letter"]
        for i,ch in enumerate("BANANA"):
            centered_text(draw,ch,315+i*125,340,engine.face(72,True),accent if ch==letter else "#A8B0B5")
        if progress>.4:
            engine.center(draw,f"{letter}  →  {info['code']}",495,engine.face(51,True),accent)
    elif kind=="banana_two_labels":
        active="N" if progress<.55 else "B"
        for i,ch in enumerate("BANANA"):
            centered_text(draw,ch,315+i*125,315,engine.face(70,True),accent if ch==active else "#A8B0B5")
        if progress>.25:
            engine.center(draw,"N  →  10",430,engine.face(43,True),accent if active=="N" else engine.MUTED)
        if progress>.58:
            engine.center(draw,"B  →  11",510,engine.face(43,True),accent)
    elif kind=="banana_counts":
        letters=list("BANANA")
        for i,letter in enumerate(letters):
            x=290+i*115
            color=accent if letter=="A" and progress>.30 else engine.INK
            centered_text(draw,letter,x,310,engine.face(65,True),color)
        counts=[("A",3),("N",2),("B",1)]
        visible=max(1,math.ceil(progress*3))
        for i,(letter,count) in enumerate(counts[:visible]):
            x=340+i*300
            centered_text(draw,f"{letter}: {count}",x,455,engine.face(43,True),accent if letter=="A" else engine.INK)
    elif kind=="short_code":
        mappings=[("A","0"),("N","10"),("B","11")]
        visible=max(1,math.ceil(progress*3))
        for i,(letter,code) in enumerate(mappings[:visible]):
            x=235+i*300
            draw.rounded_rectangle((x,340,x+220,465),radius=24,fill=accent if letter=="A" else "#FFFFFF",outline=accent,width=3)
            centered_text(draw,f"{letter} : {code}",x+110,374,engine.face(43,True),"#FFFFFF" if letter=="A" else engine.INK)
    elif kind=="bit_compare":
        for i,(label,count) in enumerate([("same 2 bits each",12),("short A code",9)]):
            y=340+i*125
            draw.text((130,y),label,font=engine.face(28,True),fill=engine.INK)
            for j in range(count):
                x=430+j*55
                draw.rounded_rectangle((x,y,x+42,y+54),radius=8,fill=accent if i==1 else "#A5ADB5")
            if progress>.45 or i==0:
                draw.text((1110,y+4),str(count),font=engine.face(40,True),fill=accent if i==1 else engine.INK)
    elif kind=="decode_banana":
        top=["11","0","10","0","10","0"]
        bottom=list("BANANA")
        visible=max(1,math.ceil(progress*6))
        for i in range(visible):
            x=205+i*158
            centered_text(draw,top[i],x,340,engine.face(52,True,mono=True),accent)
            draw.line((x,412,x,455),fill="#A4AFB4",width=4)
            centered_text(draw,bottom[i],x,465,engine.face(48,True),accent if i==visible-1 else engine.INK)
    elif kind=="prefix_zero":
        centered_text(draw,"next bit",350,320,engine.face(29,True),engine.INK)
        draw.rounded_rectangle((540,310,655,420),radius=24,fill=accent)
        centered_text(draw,"0",597,325,engine.face(57,True,mono=True),"#FFFFFF")
        draw.line((662,365,760,365),fill=accent,width=5)
        if progress>.25:
            centered_text(draw,"A",830,325,engine.face(57,True),accent)
        if progress>.6:
            engine.center(draw,"Stop. The letter is complete.",500,engine.face(29,True),engine.INK)
    elif kind=="prefix_one":
        centered_text(draw,"next bit",230,335,engine.face(27,True),engine.INK)
        draw.rounded_rectangle((360,330,465,430),radius=22,fill=accent)
        centered_text(draw,"1",412,343,engine.face(49,True,mono=True),"#FFFFFF")
        if progress>.2:
            draw.line((470,380,600,380),fill=accent,width=5)
            centered_text(draw,"read one more",730,335,engine.face(29,True),engine.INK)
        if progress>.45:
            centered_text(draw,"10  →  N",520,465,engine.face(39,True,mono=True),accent)
        if progress>.7:
            centered_text(draw,"11  →  B",850,465,engine.face(39,True,mono=True),accent)
    elif kind=="banana_tree":
        nodes={"root":(640,315,""),"A":(420,445,"A"),"inner":(855,445,""),"N":(760,550,"N"),"B":(980,550,"B")}
        edges=[("root","A","0"),("root","inner","1"),("inner","N","0"),("inner","B","1")]
        visible=max(1,math.ceil(progress*len(edges)))
        shown={"root"}
        for a,b,bit in edges[:visible]:
            x1,y1,_=nodes[a];x2,y2,_=nodes[b]
            draw.line((x1,y1,x2,y2),fill="#A0ABAE",width=5)
            centered_text(draw,bit,(x1+x2)/2,(y1+y2)/2-22,engine.face(29,True),accent)
            shown.add(b)
        for key in shown:
            x,y,label=nodes[key]
            bubble(draw,x,y,label,accent,key in {"A","N","B"},32)
    elif kind=="scan":
        vals=[2,5,9]; widths=[155,245,400]
        x=240
        active=min(2,int(progress*3))
        for i,(val,w) in enumerate(zip(vals,widths)):
            fill=accent if i<=active else "#E2E6E5"
            draw.rounded_rectangle((x,365,x+w,465),radius=13,fill=fill)
            centered_text(draw,str(val),x+w/2,386,engine.face(40,True),"#FFFFFF" if i<=active else engine.INK)
            x+=w+10
        engine.center(draw,"to reach 9, pass 2 and 5 first",520,engine.face(27,True),engine.MUTED)
    elif kind=="repeated":
        engine.center(draw,"short first",310,engine.face(34,True),engine.MUTED)
        engine.center(draw,"2  +  2  +  2",370,engine.face(53,True),accent)
        if progress>.5:
            engine.center(draw,"long first",455,engine.face(34,True),engine.MUTED)
            engine.center(draw,"9  +  9  +  9",515,engine.face(53,True),engine.INK)
    elif kind=="symbol_pool":
        items=info["items"]; selected=set(info.get("selected",[]))
        chip=178;gap=18
        x=(1280-len(items)*chip-(len(items)-1)*gap)/2
        for i,(label,value) in enumerate(items):
            focus=i in selected and progress>.35
            fill=accent if focus else "#FFFFFF"
            draw.rounded_rectangle((x,350,x+chip,480),radius=25,fill=fill,outline=accent,width=3)
            centered_text(draw,label,x+chip/2,365,engine.face(36,True),"#FFFFFF" if focus else engine.INK)
            centered_text(draw,str(value),x+chip/2,415,engine.face(42,True),"#FFFFFF" if focus else accent)
            x+=chip+gap
    elif kind=="practice_path":
        nodes=[(260,390,"44"),(500,390,"18"),(740,390,"10"),(980,390,"P")]
        bits=["0","1","0"]
        visible=max(1,math.ceil(progress*4))
        for i in range(visible):
            x,y,label=nodes[i]
            bubble(draw,x,y,label,accent,i==3,42)
            if i>0:
                prior_x=nodes[i-1][0]
                draw.line((prior_x+43,y,x-43,y),fill=accent,width=5)
                centered_text(draw,bits[i-1],(prior_x+x)/2,y-70,engine.face(40,True),accent)
        if progress>.73:
            engine.center(draw,"P = 010",520,engine.face(42,True),accent)
    elif kind=="bowl":
        draw.arc((300,320,980,570),0,180,fill=accent,width=10)
        vals=[4,6,8,11]
        for i,val in enumerate(vals):
            x=390+i*160
            focus=i<2 and progress>.45
            bubble(draw,x,395,str(val),accent,focus,44)
        if progress>.7:
            engine.center(draw,"take 4 and 6; put back 10",550,engine.face(27,True),accent)
    else:
        base_visual(draw,info,accent,progress)


engine.ROOT=ROOT
engine.LESSONS=LESSONS
engine.visual=visual

if __name__=="__main__":
    engine.main()
