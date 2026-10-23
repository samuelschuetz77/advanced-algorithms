"""Patch the BANANA video's ending from its saved clips."""
import asyncio
import json
import math
import re
import subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

R = Path(__file__).resolve().parent
F = imageio_ffmpeg.get_ffmpeg_exe()
BG, INK, ORANGE, RED = '#FAF9F6', '#172331', '#E76F51', '#B93D48'
SCRIPT = [
 ('Equal-length bytes have clear boundaries.', 'ascii_bytes', 'Here is BANANA in eight-bit ASCII bytes. Every letter takes eight digits, so we know where to cut: after each group of eight. You do not need to memorize these codes.'),
 ('A bad short code can be ambiguous.', 'prefix_bad', 'Suppose A is zero, N is zero one, and B is one. Now zero one could mean N, or A followed by B. The zero at the start of N is already A. That is the problem.'),
 ('Our short labels avoid that problem.', 'prefix_good', 'With our actual labels, zero finishes A. If the first bit is one, read another: one zero is N, and one one is B. No complete label starts another label. That is the prefix-free rule.'),
 ('This is what Huffman encoding is about.', 'final', 'That is what Huffman encoding is about: give common letters shorter labels, keep every label readable, and send fewer bits overall.'),
]

def ft(size, bold=False, mono=False):
    name = 'consola.ttf' if mono else 'arialbd.ttf' if bold else 'arial.ttf'
    return ImageFont.truetype(str(Path('C:/Windows/Fonts') / name), size)

def put(d, s, x, y, size=35, color=INK, bold=True, mono=False):
    f = ft(size, bold, mono)
    w = d.textbbox((0,0), s, font=f)[2]
    d.text((x-w/2,y), s, font=f, fill=color)

def picture(idx, p):
    headline, kind, narration = SCRIPT[idx-12]
    im = Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(im)
    d.rectangle((0,0,1280,12), fill=ORANGE)
    d.text((74,50),'START WITH ONE WORD',font=ft(22,True),fill=ORANGE)
    d.text((1134,50),f'{idx:02d} / 15',font=ft(20,True),fill='#53606D')
    d.text((74,125),headline,font=ft(51,True),fill=INK)
    if kind=='ascii_bytes':
        codes=['01000010','01000001','01001110','01000001','01001110','01000001']
        active=min(5,int(p*6))
        for j,(letter,code) in enumerate(zip('BANANA',codes)):
            x=83+j*188; focus=j==active
            d.rounded_rectangle((x,330,x+170,460),radius=18,fill=ORANGE if focus else 'white',outline=ORANGE,width=3)
            put(d,letter,x+85,342,39,'white' if focus else INK)
            put(d,code,x+85,404,22,'white' if focus else INK,mono=True)
        if p>.75: put(d,'6 groups of 8 = 48 bits',640,520,30,ORANGE)
    elif kind=='prefix_bad':
        for j,(x,s) in enumerate([(180,'A = 0'),(515,'N = 01'),(850,'B = 1')]):
            d.rounded_rectangle((x,310,x+250,405),radius=20,fill='white',outline=RED if j<2 else '#6E7A84',width=4)
            put(d,s,x+125,331,39,INK,mono=True)
        if p>.25:
            d.ellipse((320,326,380,390),outline=RED,width=6)
            d.ellipse((651,326,688,390),outline=RED,width=6)
        if p>.45:
            put(d,'01  →  N',405,465,34,INK,mono=True)
            put(d,'0 | 1  →  A B',884,465,34,INK,mono=True)
        if p>.7:
            d.ellipse((608,455,672,519),outline=RED,width=7)
            d.line((616,511,664,463),fill=RED,width=7)
    elif kind=='prefix_good':
        for x,code,letter in [(140,'0','A'),(515,'10','N'),(890,'11','B')][:max(1,math.ceil(p*3))]:
            d.rounded_rectangle((x,335,x+250,455),radius=24,fill='white',outline=ORANGE,width=4)
            put(d,code,x+70,365,43,ORANGE,mono=True)
            put(d,'→',x+135,365,38,'#6E7A84')
            put(d,letter,x+195,365,43,INK)
            d.ellipse((x+30,344,x+110,445),outline=ORANGE,width=4)
        if p>.8: put(d,'A finished label never starts another label.',640,520,29,ORANGE)
    else:
        for j,(label,count) in enumerate([('same 2 bits each',12),('short A code',9)]):
            y=340+j*125;d.text((130,y),label,font=ft(28,True),fill=INK)
            for k in range(count):
                x=430+k*55;d.rounded_rectangle((x,y,x+42,y+54),radius=8,fill=ORANGE if j else '#A5ADB5')
            if j==0 or p>.45: d.text((1110,y),str(count),font=ft(40,True),fill=ORANGE if j else INK)
    d.rectangle((0,608,1280,720),fill=INK)
    f=ft(23); lines=[]; line=''
    for word in narration.split():
        candidate=(line+' '+word).strip()
        if line and d.textbbox((0,0),candidate,font=f)[2]>1120:
            lines.append(line);line=word
        else: line=candidate
    if line:lines.append(line)
    y=630+(3-len(lines))*11
    for line in lines:
        d.text((75,y),line,font=f,fill='#F9F9F7');y+=29
    return im

def seconds(path):
    run=subprocess.run([F,'-hide_banner','-i',str(path)],capture_output=True,text=True)
    m=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',run.stderr)
    if not m: raise RuntimeError(f'No duration: {path}')
    return int(m[1])*3600+int(m[2])*60+float(m[3])

async def speak(i, narration):
    await edge_tts.Communicate(narration,'en-US-AvaNeural').save(str(R/'audio'/f'01-{i:02d}.mp3'))

async def speak_all():
    await asyncio.gather(*(speak(i,row[2]) for i,row in enumerate(SCRIPT,12)))

def new_clip(i):
    audio=R/'audio'/f'01-{i:02d}.mp3'; target=R/'clips'/f'01-{i:02d}.mp4'
    length=seconds(audio)+.65;count=math.ceil(length*6)
    cmd=[F,'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','6','-i','-','-i',str(audio),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-ar','24000','-t',str(length),str(target)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    for j in range(count):proc.stdin.write(picture(i,j/max(1,count-1)).tobytes())
    proc.stdin.close();error=proc.stderr.read().decode(errors='replace')
    if proc.wait():raise RuntimeError(error)
    return target

def old_clip(i):
    source=R/'clips'/f'01-{i:02d}.mp4';target=R/'clips'/f'01-{i:02d}-v15.mp4'
    overlay=R/'slides'/f'01-{i:02d}-counter.png'
    im=Image.new('RGBA',(1280,720));d=ImageDraw.Draw(im)
    d.rectangle((1100,25,1280,100),fill=BG)
    d.text((1134,50),f'{i:02d} / 15',font=ft(20,True),fill='#53606D')
    im.save(overlay)
    subprocess.run([F,'-y','-loglevel','error','-i',str(source),'-i',str(overlay),'-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-map','0:a','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','copy',str(target)],check=True)
    return target

def stamp(t):
    n=round(t*1000)
    return f'{n//3600000:02d}:{n//60000%60:02d}:{n//1000%60:02d},{n%1000:03d}'

def main():
    story_path=R/'storyboard.json'; story=json.loads(story_path.read_text(encoding='utf-8'))
    old_lines=[b['narration'] for b in story[0]['beats'][:11]]
    asyncio.run(speak_all())
    clips=[old_clip(i) for i in range(1,12)]+[new_clip(i) for i in range(12,16)]
    manifest=R/'clips'/'01-concat-v15.txt'
    manifest.write_text(''.join("file '"+c.as_posix()+"'\n" for c in clips),encoding='utf-8')
    final=R/'01 - BANANA - One Word, Fewer Bits.mp4'
    subprocess.run([F,'-y','-loglevel','error','-f','concat','-safe','0','-i',str(manifest),'-c','copy','-movflags','+faststart',str(final)],check=True)
    lines=old_lines+[row[2] for row in SCRIPT];elapsed=0;subs=[]
    for i,(c,narration) in enumerate(zip(clips,lines),1):
        end=elapsed+seconds(c);subs.append(f'{i}\n{stamp(elapsed)} --> {stamp(end)}\n{narration}\n\n');elapsed=end
    (R/'01 - BANANA - One Word, Fewer Bits.srt').write_text(''.join(subs),encoding='utf-8')
    story[0]['beats']=story[0]['beats'][:11]+[{'headline':h,'visual':{'kind':k},'narration':n} for h,k,n in SCRIPT]
    story_path.write_text(json.dumps(story,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Wrote {final} ({elapsed:.1f} seconds)')

if __name__=='__main__':main()
