import json,torch,whisper
from pathlib import Path
torch.set_num_threads(2)
t=json.loads(Path('timeline.json').read_text(encoding='utf-8'))
m=whisper.load_model('small.en')
results=[]
for idx in (6,27,28,43):
    b=t[idx]
    heard=m.transcribe(b['audio'],language='en',fp16=False)['text']
    results.append({'beat':b['id'],'expected':b['plain'],'heard':heard})
    print(b['id'],heard,flush=True)
Path('audio-qa.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
