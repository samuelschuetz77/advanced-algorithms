from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'advanced-algorithms-2026-10-22' / 'common'))
import pipeline

if __name__ == '__main__':
    import json
    import storyboard
    pipeline.configure(HERE)
    from concurrent.futures import ThreadPoolExecutor
    def warm_audio(beat):
        words=pipeline.parse_narration(beat['narration'])
        result=pipeline.synth(' '.join(w['spoken'] for w in words))
        print('Audio ready:',beat['id'],flush=True)
        return result
    with ThreadPoolExecutor(max_workers=5) as pool:
        list(pool.map(warm_audio,storyboard.BEATS))
    tl = pipeline.prepare(storyboard.BEATS)
    (HERE/'prepared.json').write_text(json.dumps(tl, indent=1),encoding='utf-8')
    print('Prepared duration:',sum(b['dur'] for b in tl),flush=True)
    if len(sys.argv) > 1 and sys.argv[1] == 'prepare':
        raise SystemExit(0)
    results = pipeline.render_all(tl, workers=6)
    pipeline.assemble(tl,results,HERE/'Chapter 6 - Two Lessons in Ten Minutes.mp4',HERE/'work')
    pipeline.write_srt(tl,HERE/'Chapter 6 - Two Lessons in Ten Minutes.srt')
