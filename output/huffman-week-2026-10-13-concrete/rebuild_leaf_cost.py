"""Replace the unexplained leaf-cost ending of video 3."""
import asyncio
import json
import math
import subprocess

import edge_tts
from PIL import Image, ImageDraw

from rebuild_prefix import R, F, BG, INK, ft, put, seconds, stamp

GREEN = '#179889'
SCRIPT = [
 ('The weights add to forty-four.', 'weight_sum', "You're right: four plus six plus eight plus eleven plus fifteen is forty-four. These weights count how often the letters appear. They do not yet count bits."),
 ('Multiply by each code\'s length.', 'weighted_lengths', "P and Q have three-bit codes. R, S, and T have two-bit codes. Multiply each letter's weight by the number of bits in its code."),
 ('The message takes ninety-eight bits.', 'weighted_total', "Four times three plus six times three plus eight times two plus eleven times two plus fifteen times two equals ninety-eight bits. That is the total encoded message length."),
 ('The merge sum checks the answer.', 'merge_total', "The merge weights also add to ninety-eight: ten plus eighteen plus twenty-six plus forty-four. This gives us a second way to check the bit count."),
]

def picture(i,p):
    headline,kind,narration=SCRIPT[i-10]
    im=Image.new('RGB',(1280,720),BG);d=ImageDraw.Draw(im)
    d.rectangle((0,0,1280,12),fill=GREEN)
    d.text((74,50),'READING 4.4 · PRACTICE EXAMPLE',font=ft(22,True),fill=GREEN)
    d.text((1134,50),f'{i:02d} / 13',font=ft(20,True),fill='#53606D')
    d.text((74,125),headline,font=ft(52,True),fill=INK)
    if kind=='weight_sum':
        put(d,'4 + 6 + 8 + 11 + 15',640,325,48,INK,mono=True)
        if p>.45: put(d,'= 44 letter occurrences',640,420,40,GREEN)
    elif kind=='weighted_lengths':
        rows=[('P','4','3'),('Q','6','3'),('R','8','2'),('S','11','2'),('T','15','2')]
        active=min(4,int(p*5))
        d.text((135,290),'letter',font=ft(28,True),fill='#53606D')
        d.text((445,290),'times used',font=ft(28,True),fill='#53606D')
        d.text((805,290),'bits each time',font=ft(28,True),fill='#53606D')
        for j,(letter,weight,bits) in enumerate(rows):
            y=345+j*46
            if j==active:d.rounded_rectangle((115,y-3,1160,y+43),radius=10,fill='#DDF1EC')
            d.text((160,y),letter,font=ft(31,True),fill=GREEN if j==active else INK)
            d.text((500,y),weight,font=ft(31,True),fill=GREEN if j==active else INK)
            d.text((875,y),bits,font=ft(31,True),fill=GREEN if j==active else INK)
    elif kind=='weighted_total':
        put(d,'4×3 + 6×3 + 8×2 + 11×2 + 15×2',640,310,36,INK,mono=True)
        if p>.4:put(d,'12 + 18 + 16 + 22 + 30',640,390,38,INK,mono=True)
        if p>.72:put(d,'= 98 bits for the message',640,480,38,GREEN)
    else:
        put(d,'10 + 18 + 26 + 44',640,340,48,INK,mono=True)
        if p>.45:put(d,'= 98',640,435,50,GREEN)
    d.rectangle((0,608,1280,720),fill=INK)
    f=ft(23);lines=[];line=''
    for word in narration.split():
        candidate=(line+' '+word).strip()
        if line and d.textbbox((0,0),candidate,font=f)[2]>1120:
            lines.append(line);line=word
        else:line=candidate
    if line:lines.append(line)
    y=630+(3-len(lines))*11
    for line in lines:d.text((75,y),line,font=f,fill='#F9F9F7');y+=29
    return im

async def speak(i,narration):
    await edge_tts.Communicate(narration,'en-US-AvaNeural').save(str(R/'audio'/f'03-{i:02d}.mp3'))

async def speak_all():
    await asyncio.gather(*(speak(i,row[2]) for i,row in enumerate(SCRIPT,10)))

def new_clip(i):
    audio=R/'audio'/f'03-{i:02d}.mp3';target=R/'clips'/f'03-{i:02d}.mp4'
    length=seconds(audio)+.65;count=math.ceil(length*6)
    cmd=[F,'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','6','-i','-','-i',str(audio),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-ar','24000','-t',str(length),str(target)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    for j in range(count):proc.stdin.write(picture(i,j/max(1,count-1)).tobytes())
    proc.stdin.close();error=proc.stderr.read().decode(errors='replace')
    if proc.wait():raise RuntimeError(error)
    return target

def old_clip(i):
    source=R/'clips'/f'03-{i:02d}.mp4';target=R/'clips'/f'03-{i:02d}-v13.mp4'
    overlay=R/'slides'/f'03-{i:02d}-counter.png'
    im=Image.new('RGBA',(1280,720));d=ImageDraw.Draw(im)
    d.rectangle((1100,25,1280,100),fill=BG)
    d.text((1134,50),f'{i:02d} / 13',font=ft(20,True),fill='#53606D')
    im.save(overlay)
    subprocess.run([F,'-y','-loglevel','error','-i',str(source),'-i',str(overlay),'-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-map','0:a','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','copy',str(target)],check=True)
    return target

def main():
    story_path=R/'storyboard.json';story=json.loads(story_path.read_text(encoding='utf-8'))
    prior=[b['narration'] for b in story[2]['beats'][:9]]
    asyncio.run(speak_all())
    clips=[old_clip(i) for i in range(1,10)]+[new_clip(i) for i in range(10,14)]
    manifest=R/'clips'/'03-concat-v13.txt'
    manifest.write_text(''.join("file '"+c.as_posix()+"'\n" for c in clips),encoding='utf-8')
    final=R/'03 - Build One Huffman Tree.mp4'
    subprocess.run([F,'-y','-loglevel','error','-f','concat','-safe','0','-i',str(manifest),'-c','copy','-movflags','+faststart',str(final)],check=True)
    lines=prior+[row[2] for row in SCRIPT];elapsed=0;subs=[]
    for i,(clip,narration) in enumerate(zip(clips,lines),1):
        end=elapsed+seconds(clip);subs.append(f'{i}\n{stamp(elapsed)} --> {stamp(end)}\n{narration}\n\n');elapsed=end
    (R/'03 - Build One Huffman Tree.srt').write_text(''.join(subs),encoding='utf-8')
    story[2]['beats']=story[2]['beats'][:9]+[{'headline':h,'visual':{'kind':k},'narration':n} for h,k,n in SCRIPT]
    story_path.write_text(json.dumps(story,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Wrote {final} ({elapsed:.1f} seconds)')

if __name__=='__main__':main()
