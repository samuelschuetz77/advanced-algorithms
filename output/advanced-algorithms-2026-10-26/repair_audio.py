from pathlib import Path
import json
import render
import pipeline,storyboard

if __name__=='__main__':
    pipeline.configure(render.HERE)
    old=json.loads((render.HERE/'prepared.json').read_text(encoding='utf-8'))
    tl=pipeline.prepare(storyboard.BEATS)
    assert len(old)==len(tl)
    changed=[i+1 for i,(a,b) in enumerate(zip(old,tl)) if a['narration']!=b['narration']]
    assert changed==[28],changed
    (render.HERE/'prepared.json').write_text(json.dumps(tl,indent=1),encoding='utf-8')
    tl=render.timeline()
    targets=set(changed)
    for sec in (14,19,24):
        targets.add(max(i+1 for i,b in enumerate(tl) if b['section']==sec))
    result={int(k):v for k,v in json.loads((render.HERE/'render-results.json').read_text()).items()}
    result.update(pipeline.render_all(tl,only=targets,workers=4))
    (render.HERE/'render-results.json').write_text(json.dumps(result),encoding='utf-8')
    print('Repaired frames:',targets,flush=True)
