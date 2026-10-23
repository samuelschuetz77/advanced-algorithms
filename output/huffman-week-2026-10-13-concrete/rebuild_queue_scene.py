"""Replace video 4's vague priority-queue bowl scene."""
import asyncio
import json
import math
import subprocess

import edge_tts
from PIL import Image, ImageDraw

from rebuild_prefix import R, F, BG, INK, ft, put, seconds, stamp

PURPLE='#785FBD'
HEADLINE='Take the minimum twice, one at a time.'
NARRATION=('Your Project Two queue lets us peek at the minimum and remove that node. '
           'Take the weight-four tree first. The heap rearranges, so weight six becomes '
           'the new minimum. Remove that tree next. The queue is not fully sorted. '
           'Join four and six into a weight-ten tree, then insert it.')

def bubble(d,x,y,value,active=False):
    r=51
    d.ellipse((x-r,y-r,x+r,y+r),fill=PURPLE if active else 'white',outline=PURPLE,width=4)
    put(d,str(value),x,y-26,38,'white' if active else INK)

def frame(p):
    im=Image.new('RGB',(1280,720),BG);d=ImageDraw.Draw(im)
    d.rectangle((0,0,1280,12),fill=PURPLE)
    d.text((74,50),'ASSIGNMENT PARTS 2–3 · CONCEPTS',font=ft(22,True),fill=PURPLE)
    d.text((1134,50),'02 / 08',font=ft(20,True),fill='#53606D')
    d.text((74,125),HEADLINE,font=ft(49,True),fill=INK)
    stage=min(4,int(p*5))
    if stage==0:
        put(d,'peek_min() finds the lightest',640,270,30,INK)
        for x,y,v in [(370,410,11),(540,390,4),(720,430,8),(900,375,6)]:
            bubble(d,x,y,v,v==4)
        put(d,'minimum: 4',640,515,29,PURPLE)
    elif stage==1:
        put(d,'remove the weight-4 tree',640,270,31,INK)
        for x,y,v in [(430,410,11),(630,390,6),(830,425,8)]:
            bubble(d,x,y,v,v==6)
        put(d,'heap rearranges → new minimum: 6',640,515,29,PURPLE)
    elif stage==2:
        put(d,'remove the weight-6 tree',640,270,31,INK)
        bubble(d,520,400,11)
        bubble(d,760,400,8,True)
        put(d,'two separate removals: 4, then 6',640,515,29,PURPLE)
    elif stage==3:
        put(d,'join the two removed trees',640,270,31,INK)
        bubble(d,490,405,4)
        put(d,'+',640,375,43,PURPLE)
        bubble(d,790,405,6)
        put(d,'new tree has weight 10',640,515,30,PURPLE)
    else:
        put(d,'insert the new weight-10 tree',640,270,31,INK)
        for x,y,v in [(420,400,11),(640,400,8),(860,400,10)]:
            bubble(d,x,y,v,v==8)
        put(d,'minimum now: 8',640,515,29,PURPLE)
    d.rectangle((0,608,1280,720),fill=INK)
    f=ft(23);lines=[];line=''
    for word in NARRATION.split():
        candidate=(line+' '+word).strip()
        if line and d.textbbox((0,0),candidate,font=f)[2]>1120:
            lines.append(line);line=word
        else:line=candidate
    if line:lines.append(line)
    y=630+(3-len(lines))*11
    for line in lines:d.text((75,y),line,font=f,fill='#F9F9F7');y+=29
    return im

async def speak():
    await edge_tts.Communicate(NARRATION,'en-US-AvaNeural').save(str(R/'audio'/'04-02.mp3'))

def render_clip():
    audio=R/'audio'/'04-02.mp3';target=R/'clips'/'04-02.mp4'
    length=seconds(audio)+.65;count=math.ceil(length*6)
    cmd=[F,'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','6','-i','-','-i',str(audio),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-ar','24000','-t',str(length),str(target)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    for j in range(count):proc.stdin.write(frame(j/max(1,count-1)).tobytes())
    proc.stdin.close();error=proc.stderr.read().decode(errors='replace')
    if proc.wait():raise RuntimeError(error)
    return target

def main():
    story_path=R/'storyboard.json';story=json.loads(story_path.read_text(encoding='utf-8'))
    asyncio.run(speak())
    render_clip()
    clips=[R/'clips'/f'04-{i:02d}.mp4' for i in range(1,9)]
    manifest=R/'clips'/'04-concat-revised.txt'
    manifest.write_text(''.join("file '"+c.as_posix()+"'\n" for c in clips),encoding='utf-8')
    final=R/'04 - Use the Tree as a Codec.mp4'
    subprocess.run([F,'-y','-loglevel','error','-f','concat','-safe','0','-i',str(manifest),'-c','copy','-movflags','+faststart',str(final)],check=True)
    story[3]['beats'][1]={'headline':HEADLINE,'visual':{'kind':'two_removals'},'narration':NARRATION}
    elapsed=0;subs=[]
    for i,(clip,beat) in enumerate(zip(clips,story[3]['beats']),1):
        end=elapsed+seconds(clip)
        subs.append(f"{i}\n{stamp(elapsed)} --> {stamp(end)}\n{beat['narration']}\n\n")
        elapsed=end
    (R/'04 - Use the Tree as a Codec.srt').write_text(''.join(subs),encoding='utf-8')
    story_path.write_text(json.dumps(story,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Wrote {final} ({elapsed:.1f} seconds)')

if __name__=='__main__':main()
