"""Finalize a ten-minute timeline, render QA frames, then render and mux."""
from pathlib import Path
import sys,json,subprocess,math
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'advanced-algorithms-2026-10-22'/'common'))
import pipeline
import storyboard

NAME='Chapter 6 - Two Lessons in Ten Minutes'

def timeline():
    tl=json.loads((HERE/'prepared.json').read_text(encoding='utf-8'))
    assert len(tl)==len(storyboard.BEATS)
    for b,new in zip(tl,storyboard.BEATS):
        b['topic']=new['topic']
        b['dur']=round(b['dur']*30)/30
    remaining=18000-sum(round(b['dur']*30) for b in tl)
    assert 0<=remaining<=900, 'Unexpected pacing: revise narration rather than pad.'
    # Brief thinking time after the proof, path comparison, and final paper task.
    targets=[max(i for i,b in enumerate(tl) if b['section']==sec) for sec in (14,19,24)]
    for j,i in enumerate(targets):
        frames=remaining//(len(targets)-j)
        tl[i]['dur']+=frames/30
        tl[i]['pause_len']+=frames/30
        tl[i]['reading_hold']=frames/30
        remaining-=frames
    start=0
    for b in tl:
        b['start']=start/30
        start+=round(b['dur']*30)
    assert start==18000
    (HERE/'timeline.json').write_text(json.dumps(tl,indent=1),encoding='utf-8')
    return tl

def qa(tl):
    from PIL import Image,ImageDraw
    picks=[]
    for sec in (1,3,4,7,11,13,17,18,19,21,22,23):
        i=next(i for i,b in enumerate(tl) if b['section']==sec and (sec!=4 or b.get('predict')))
        t=min(tl[i]['dur']-.2,tl[i]['audio_dur']*.7)
        picks.extend(pipeline.snap(tl,i+1,[t],HERE/'snaps'))
    board=Image.new('RGB',(1920,4*405),'#dce4e8')
    draw=ImageDraw.Draw(board)
    for k,p in enumerate(picks):
        im=Image.open(p).convert('RGB'); im.thumbnail((640,360))
        x=(k%3)*640;y=(k//3)*405
        board.paste(im,(x,y));draw.text((x+10,y+365),Path(p).name,fill='black')
    board.save(HERE/'snaps'/'contact-sheet.jpg')
    # Small playable draft for inspecting transitions and typography.
    listing=[]
    for p in picks:
        listing.append("file '%s'\nduration 2" % Path(p).as_posix())
    listing.append("file '%s'" % Path(picks[-1]).as_posix())
    (HERE/'snaps'/'preview.txt').write_text('\n'.join(listing),encoding='utf-8')
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(HERE/'snaps'/'preview.txt'),'-vf','scale=854:480,fps=30,format=yuv420p','-c:v','libx264','-preset','fast',str(HERE/'Draft - visual check.mp4')],check=True)

def assemble(tl,results):
    work=HERE/'work';work.mkdir(exist_ok=True)
    pipeline.build_audio(tl,work/'narration.wav')
    lines=[];last=None
    for i in range(len(tl)):
        for p,n in results[i]:
            lines.append("file '%s'\noption framerate 30\nduration %.9f" % (Path(p).as_posix(),n/30))
            last=p
    lines.append("file '%s'\noption framerate 30" % Path(last).as_posix())
    (work/'frames.txt').write_text('\n'.join(lines),encoding='utf-8')
    chapters=[';FFMETADATA1','title=Chapter 6 - Two Lessons in Ten Minutes']
    starts=[b for b in tl if b['part']==1]
    for i,b in enumerate(starts):
        end=starts[i+1]['start'] if i+1<len(starts) else 600
        chapters.extend(['[CHAPTER]','TIMEBASE=1/1000',f"START={round(b['start']*1000)}",f'END={round(end*1000)}',f"title={b['topic']}"])
    (work/'chapters.txt').write_text('\n'.join(chapters),encoding='utf-8')
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(work/'frames.txt'),'-i',str(work/'narration.wav'),'-i',str(work/'chapters.txt'),'-map','0:v','-map','1:a','-map_metadata','2','-map_chapters','2','-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','fast','-crf','18','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-c:a','aac','-b:a','192k','-t','600','-movflags','+faststart',str(HERE/(NAME+'.mp4'))],check=True)
    pipeline.write_srt(tl,HERE/(NAME+'.srt'))

if __name__=='__main__':
    pipeline.configure(HERE)
    tl=timeline()
    if len(sys.argv)>1 and sys.argv[1]=='qa':
        qa(tl)
    elif len(sys.argv)>1 and sys.argv[1]=='assemble':
        results={int(k):v for k,v in json.loads((HERE/'render-results.json').read_text()).items()}
        assemble(tl,results)
    else:
        results=pipeline.render_all(tl,workers=6)
        (HERE/'render-results.json').write_text(json.dumps(results),encoding='utf-8')
        print('Frames complete. Encoding final video.',flush=True)
        assemble(tl,results)
        print('DONE:',HERE/(NAME+'.mp4'),flush=True)
