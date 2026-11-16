import render,pipeline,json

if __name__=='__main__':
    pipeline.configure(render.HERE)
    tl=render.timeline()
    targets={i+1 for i,b in enumerate(tl) if b['section'] in (1,9,11,12,13,15,24)}
    results={int(k):v for k,v in json.loads((render.HERE/'render-results.json').read_text()).items()}
    results.update(pipeline.render_all(tl,only=targets,workers=6))
    (render.HERE/'render-results.json').write_text(json.dumps(results),encoding='utf-8')
    print('Revised diagrams complete; encoding.',flush=True)
    render.assemble(tl,results)
    print('DONE',flush=True)
