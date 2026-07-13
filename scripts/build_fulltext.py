#!/usr/bin/env python3
"""Build root full-text READMEs from canonical chapter files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    '00-Preface.md','01-Information-Existence-Hypothesis.md','02-Information-Existence-Right.md',
    '03-High-dimensional-Cognitive-Tools.md','04-Brain-Siliconization.md',
    '05-Silicon-based-Intelligence-Defends-IER.md','06-Patch-Based-Perpetuation.md',
    '07-Super-Prosperity-Phase.md','08-Autonomy-of-Silicon-based-Intelligence.md',
    '09-Informational-Resilience.md','10-Silicon-Cambrian.md',
    '11-Human-Informational-Ecological-Niche.md','12-AI-Alignment.md',
    '13-Epilogue-Human-Dignity.md',
]
ANCHORS = ['preface','thesis','c01-ier','c02-hdct','c03-bs','c04-ai-ier','c05-pbp','c06-spp','c07-asi','c08-ir','c09-sc','c10-hien','c11-align','epilogue']
BEGIN = '<!-- BEGIN GENERATED CHAPTERS -->'
END = '<!-- END GENERATED CHAPTERS -->'

def clean_chapter(text: str, lang: str) -> str:
    # Remove chapter-only navigation.
    text = re.split(r'\n---\n\n## Navigation\s*\n', text, maxsplit=1)[0].rstrip()
    # Remove the C06 public-draft status box from the combined full text.
    text = re.sub(
        r'\n> \*\*Document Status / 文档状态\*\*.*?\n---\n',
        '\n', text, flags=re.S
    )
    text = text.replace('../figures/', './figures/')
    return text.strip()

def generated(lang: str) -> str:
    sections=[]
    for anchor, filename in zip(ANCHORS, CHAPTERS):
        text=clean_chapter((ROOT/lang/filename).read_text(encoding='utf-8'), lang)
        sections.append(f'<a id="{anchor}"></a>\n{text}')
    return '\n\n'.join(sections)

def build(readme: str, lang: str) -> None:
    p=ROOT/readme
    text=p.read_text(encoding='utf-8')
    pre_anchor='<a id="preface"></a>'
    post_anchor='<a id="terminology"></a>'
    if BEGIN in text and END in text:
        prefix=text.split(BEGIN,1)[0].rstrip()
        suffix=text.split(END,1)[1].lstrip()
    else:
        prefix=text.split(pre_anchor,1)[0].rstrip()
        suffix=post_anchor + text.split(post_anchor,1)[1]
    out=f'{prefix}\n\n{BEGIN}\n{generated(lang)}\n{END}\n\n{suffix.lstrip()}'
    p.write_text(out.rstrip()+'\n', encoding='utf-8')

if __name__=='__main__':
    build('README.md','zh')
    build('README_EN.md','en')
    print('Built README.md and README_EN.md from canonical chapter files.')
