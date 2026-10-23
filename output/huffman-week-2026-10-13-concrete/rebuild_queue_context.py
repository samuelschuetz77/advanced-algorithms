"""Insert Project 2 vocabulary and its Huffman roles into video 4."""
import asyncio
import json
import math
import subprocess

import edge_tts
from PIL import Image, ImageDraw

from rebuild_prefix import R, F, BG, INK, ft, put, seconds, stamp

PURPLE='#785FBD'
SCENES=[
 ('Two Project Two tools have different jobs.','graph_queue_roles',
  'The assignment reuses two things you built in Project Two. The Graph holds the Huffman tree, with zero or one on each edge. The priority queue chooses which current trees to join next.'),
 ('A priority queue chooses what goes next.','pq_role',
  "Your learning log calls it a line where the most important item goes next. Here, each item is one current tree. Its priority is that tree's total frequency, and the smallest weight goes next."),
 ('A min-heap makes the minimum quick.','heap_role',
  'Project Two implements the queue with a min-heap. Each parent weighs no more than its children, so the root is the minimum. The whole heap is not sorted. After a removal, it rearranges to restore that rule.'),
 ('The locator tells us where a key is.','locator_role',
  "Your locator dictionary maps each tree's unique key to its position in the heap array. When two heap entries swap, their locator positions change too. It helps remove or update a known key. The heap, not the locator, chooses the minimum."),
]

def caption(d,narration):
    d.rectangle((0,608,1280,720),fill=INK)
    f=ft(23);lines=[];line=''
    for word in narration.split():
        candidate=(line+' '+word).strip()
        if line and d.textbbox((0,0),candidate,font=f)[2]>1120:
            lines.append(line);line=word
        else:line=candidate
    if line:lines.append(line)
    if len(lines)>3:
        f=ft(21);lines=[];line=''
        for word in narration.split():
            candidate=(line+' '+word).strip()
            if line and d.textbbox((0,0),candidate,font=f)[2]>1120:
                lines.append(line);line=word
            else:line=candidate
        if line:lines.append(line)
    y=630+(3-len(lines))*11
    for line in lines:d.text((75,y),line,font=f,fill='#F9F9F7');y+=29

def card(d,box,label,sub,active=False):
    d.rounded_rectangle(box,radius=24,fill=PURPLE if active else 'white',outline=PURPLE,width=4)
    x=(box[0]+box[2])/2
    put(d,label,x,box[1]+22,36,'white' if active else INK)
    put(d,sub,x,box[1]+80,26,'white' if active else PURPLE)

def frame(i,p):
    headline,kind,narration=SCENES[i-2]
    im=Image.new('RGB',(1280,720),BG);d=ImageDraw.Draw(im)
    d.rectangle((0,0,1280,12),fill=PURPLE)
    d.text((74,50),'ASSIGNMENT PARTS 2–3 · CONCEPTS',font=ft(22,True),fill=PURPLE)
    d.text((1134,50),f'{i:02d} / 12',font=ft(20,True),fill='#53606D')
    d.text((74,125),headline,font=ft(48,True),fill=INK)
    if kind=='graph_queue_roles':
        card(d,(145,332,585,477),'Graph','stores the joined tree',p<.5)
        if p>.35:card(d,(695,332,1135,477),'Priority queue','chooses the next trees',p>=.5)
    elif kind=='pq_role':
        put(d,'current tree weights',640,275,29,INK)
        values=[(230,4),(455,11),(680,6),(905,8)]
        for j,(x,v) in enumerate(values):
            active=(v==4 and p>.25)
            card(d,(x,335,x+145,455),str(v),'tree',active)
        if p>.65:put(d,'priority = total frequency',640,515,30,PURPLE)
    elif kind=='heap_role':
        positions=[(640,305,4),(445,440,6),(835,440,8),(340,540,11)]
        for a,b in [(0,1),(0,2),(1,3)]:
            x,y,_=positions[a];xx,yy,_=positions[b]
            d.line((x,y+30,xx,yy-30),fill='#A6A0B7',width=5)
        for x,y,v in positions:
            active=(v==4)
            r=37
            d.ellipse((x-r,y-r,x+r,y+r),fill=PURPLE if active else 'white',outline=PURPLE,width=4)
            put(d,str(v),x,y-22,34,'white' if active else INK)
        if p>.52:put(d,'only the root is guaranteed smallest',640,535,26,PURPLE)
    else:
        put(d,'heap array',375,280,29,INK)
        put(d,'locator: key → index',910,280,29,INK)
        keys=['P','Q','R','S']
        active=min(3,int(p*4))
        for j,key in enumerate(keys):
            y=330+j*62
            d.rounded_rectangle((170,y,560,y+50),radius=11,fill=PURPLE if j==active else 'white',outline=PURPLE,width=3)
            put(d,f'{j}: tree {key}',365,y+8,27,'white' if j==active else INK)
            d.rounded_rectangle((765,y,1085,y+50),radius=11,fill=PURPLE if j==active else 'white',outline=PURPLE,width=3)
            put(d,f'{key} → {j}',925,y+8,27,'white' if j==active else INK)
    caption(d,narration)
    return im

async def speak(i,narration):
    await edge_tts.Communicate(narration,'en-US-AvaNeural').save(str(R/'audio'/f'04-new{i:02d}.mp3'))

async def speak_all():
    await asyncio.gather(*(speak(i,row[2]) for i,row in enumerate(SCENES,2)))

def new_clip(i):
    audio=R/'audio'/f'04-new{i:02d}.mp3';target=R/'clips'/f'04-new{i:02d}.mp4'
    length=seconds(audio)+.65;count=math.ceil(length*6)
    cmd=[F,'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','6','-i','-','-i',str(audio),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-ar','24000','-t',str(length),str(target)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    for j in range(count):proc.stdin.write(frame(i,j/max(1,count-1)).tobytes())
    proc.stdin.close();error=proc.stderr.read().decode(errors='replace')
    if proc.wait():raise RuntimeError(error)
    return target

def shifted_clip(old,new):
    source=R/'clips'/f'04-{old:02d}.mp4';target=R/'clips'/f'04-shifted{new:02d}.mp4'
    overlay=R/'slides'/f'04-shifted{new:02d}-counter.png'
    im=Image.new('RGBA',(1280,720));d=ImageDraw.Draw(im)
    d.rectangle((1100,25,1280,100),fill=BG)
    d.text((1134,50),f'{new:02d} / 12',font=ft(20,True),fill='#53606D')
    im.save(overlay)
    subprocess.run([F,'-y','-loglevel','error','-i',str(source),'-i',str(overlay),'-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-map','0:a','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','copy',str(target)],check=True)
    return target

def main():
    story_path=R/'storyboard.json';story=json.loads(story_path.read_text(encoding='utf-8'))
    old=story[3]['beats']
    if len(old)==12 and old[1]['visual']['kind']=='graph_queue_roles':
        old=old[:1]+old[5:]
    asyncio.run(speak_all())
    clips=[shifted_clip(1,1)]+[new_clip(i) for i in range(2,6)]
    clips += [shifted_clip(i,i+4) for i in range(2,9)]
    manifest=R/'clips'/'04-concat-context.txt'
    manifest.write_text(''.join("file '"+c.as_posix()+"'\n" for c in clips),encoding='utf-8')
    final=R/'04 - Use the Tree as a Codec.mp4'
    subprocess.run([F,'-y','-loglevel','error','-f','concat','-safe','0','-i',str(manifest),'-c','copy','-movflags','+faststart',str(final)],check=True)
    fresh=[{'headline':h,'visual':{'kind':k},'narration':n} for h,k,n in SCENES]
    story[3]['beats']=old[:1]+fresh+old[1:]
    elapsed=0;subs=[]
    for i,(clip,beat) in enumerate(zip(clips,story[3]['beats']),1):
        end=elapsed+seconds(clip)
        subs.append(f"{i}\n{stamp(elapsed)} --> {stamp(end)}\n{beat['narration']}\n\n")
        elapsed=end
    (R/'04 - Use the Tree as a Codec.srt').write_text(''.join(subs),encoding='utf-8')
    story_path.write_text(json.dumps(story,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Wrote {final} ({elapsed:.1f} seconds)')

if __name__=='__main__':main()
