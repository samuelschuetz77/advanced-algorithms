"""Generate the production storyboard directly from the reviewed Markdown."""
from pathlib import Path
import re
import widgets
from scenes import scene

widgets.CONFIG.update(series='ADVANCED ALGORITHMS', title='October 26 + 28 | Chapter 6 primer')
SHORT_TITLES=['','Three path questions','Figure 6.4','Arrival and return','Nested calls','The discovery forest','Three vertex states','Four edge types','Finish order','Return-trip groups','A DAG of components','Search from d','Collect one group','Two reversals','The ordering proof','State for each pass','Reading the notes','To, from, through','Two counting passes','Compare the paths','Remove a vertex','The DFS root','Another connection','Chapter reading route','Try it on paper']
SOURCE = Path(__file__).with_name('script-combined.md')
BEATS = []
section = 0
part = 0
titles = {}
for line in SOURCE.read_text(encoding='utf-8').splitlines():
    match = re.match(r'## (\d+) . (.*)', line)
    if match:
        section = int(match[1]); part = 0; titles[section] = match[2]
    if not line.startswith('\u201c'):
        continue
    paragraph = line.strip('\u201c\u201d')
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    groups = []
    for sentence in sentences:
        if groups and len((groups[-1] + ' ' + sentence).split()) <= 32 and not groups[-1].endswith('?'):
            groups[-1] += ' ' + sentence
        else:
            groups.append(sentence)
    for narration in groups:
        part += 1
        prediction = section in (4,11,19,21) and narration.endswith('?')
        book = 'JEA 6.1 | PDF 247'
        if section == 8: book = 'JEA 6.3-6.4 | PDF 250-254'
        elif 9 <= section <= 15: book = 'JEA 6.5-6.6 | PDF 255-259'
        elif 16 <= section <= 19: book = 'Exercise 3 | PDF 263'
        elif 20 <= section <= 22: book = 'Exercise 4 | PDF 263-264'
        elif section >= 23: book = 'Chapter 6 | Reading route'
        # Cues are actual TTS word boundaries, never guessed timings.
        cued = ' '.join('[[w%d]]%s' % (i,w) for i,w in enumerate(narration.split()))
        BEATS.append(dict(id=f'{section:02d}-{part:02d}', section=section, part=part,
                          topic=SHORT_TITLES[section], narration=cued, plain=narration,
                          scene=scene, book=book, pause=5.0 if prediction else 0.0,
                          predict='Trace the picture, then explain your answer.' if prediction else ''))

