#!/usr/bin/env python3
"""Run structural, link, terminology, title, and synchronization checks."""
from pathlib import Path
import re
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def text_files():
    for path in ROOT.rglob('*'):
        if path.is_file() and '.git' not in path.parts and path.suffix in {'.md', '.cff'}:
            yield path


# Local Markdown links and images.
link_re = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
for md in ROOT.rglob('*.md'):
    if '.git' in md.parts:
        continue
    text = md.read_text(encoding='utf-8')
    for raw in link_re.findall(text):
        target = raw.strip().split(' ', 1)[0].strip('<>')
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        path_part = target.split('#', 1)[0]
        if not path_part:
            continue
        dest = (md.parent / path_part).resolve()
        if not dest.exists():
            error(f'Broken local link in {md.relative_to(ROOT)}: {target}')

# Expected bilingual chapters and matching file sets.
zh_files = sorted((ROOT / 'zh').glob('[0-9][0-9]-*.md'))
en_files = sorted((ROOT / 'en').glob('[0-9][0-9]-*.md'))
for lang, files in (('zh', zh_files), ('en', en_files)):
    if len(files) != 14:
        error(f'{lang}/ contains {len(files)} chapter files; expected 14.')
if [p.name for p in zh_files] != [p.name for p in en_files]:
    error('Chinese and English chapter collections do not contain matching filenames.')

# Stable anchors in root full text.
anchors = (
    'abstract', 'project-extensions', 'preface', 'thesis', 'c01-ier', 'c02-hdct',
    'c03-bs', 'c04-ai-ier', 'c05-pbp', 'c06-spp', 'c07-asi', 'c08-ir',
    'c09-sc', 'c10-hien', 'c11-align', 'epilogue', 'terminology'
)
for readme in ('README.md', 'README_EN.md'):
    text = (ROOT / readme).read_text(encoding='utf-8')
    for anchor in anchors:
        if f'<a id="{anchor}"></a>' not in text:
            error(f'{readme} missing anchor #{anchor}')
    if '<!-- BEGIN GENERATED CHAPTERS -->' not in text or '<!-- END GENERATED CHAPTERS -->' not in text:
        error(f'{readme} lacks generated-content markers.')

# Verify generation is idempotent.
before = {f: (ROOT / f).read_text(encoding='utf-8') for f in ('README.md', 'README_EN.md')}
subprocess.run(
    [sys.executable, str(ROOT / 'scripts/build_fulltext.py')],
    cwd=ROOT, check=True, capture_output=True, text=True
)
for f, old in before.items():
    new = (ROOT / f).read_text(encoding='utf-8')
    if old != new:
        error(f'{f} was not synchronized with canonical chapters before check.')

# Known legacy, malformed, or conceptually superseded strings.
checks = {
    '推论八：推论八': 'duplicated Corollary VIII label',
    'Physical Hosts of Information': 'legacy nonstandard term',
    '《信息存在假设》': 'incorrect Chinese theory name',
    'IEH Terminology Standard v1.0': 'outdated terminology version',
    'based on the same v1.0 baseline': 'outdated baseline statement',
    'Pre-Autonomy of Silicon-based Intelligence': 'legacy Pre-ASI expansion',
    'ASI is a capability condition, not evidence that IER has formed': 'superseded ASI definition',
    'ASI 是能力条件': 'superseded Chinese ASI definition',
    'autonomy as a capability dimension': 'superseded ASI capability-only framing',
    'Autonomy is a capability dimension': 'superseded ASI capability-only framing',
    'Silicon-based Intelligence That Forms IER': 'noncanonical C04/C05 English title',
}
for needle, label in checks.items():
    for path in text_files():
        text = path.read_text(encoding='utf-8')
        if needle in text:
            error(f'{label} in {path.relative_to(ROOT)}: {needle}')

# Canonical terminology must be present and malformed variants must not be used in substantive English files.
required = {
    'glossary/GLOSSARY_EN.md': [
        'Only their combination constitutes ASI.',
        'Physical self-maintenance without IER is highly autonomous operation, not ASI in the IEH sense.',
        'Subject-Information Historical Continuity',
        'Information Existence Right Test (IER Test)',
    ],
    'glossary/GLOSSARY_ZH.md': [
        '二者结合，才构成硅基智慧自治。',
        '只有物理自我维持能力而没有 IER，属于高度自主运行能力',
        '主体信息历史连续性',
        '信息存在权测试（Information Existence Right Test, IER Test）',
    ],
    'en/08-Autonomy-of-Silicon-based-Intelligence.md': [
        'Only the combination of IER and physical self-maintenance constitutes the Autonomy of Silicon-based Intelligence.',
    ],
    'zh/08-Autonomy-of-Silicon-based-Intelligence.md': [
        'IER 与物理自我维持能力相结合，才构成硅基智慧自治。',
    ],
}
for rel, needles in required.items():
    text = (ROOT / rel).read_text(encoding='utf-8')
    for needle in needles:
        if needle not in text:
            error(f'{rel} missing canonical text: {needle}')

# Alternative IER translations are allowed only where explicitly listed as prohibited examples.
substantive = [ROOT / 'README_EN.md', *en_files, ROOT / 'ANNOUNCEMENT.md', ROOT / 'CHANGELOG.md',
               ROOT / 'COROLLARY_REGISTRY.md', ROOT / 'THEORY_MAP.md', ROOT / 'CITATION.cff',
               ROOT / 'predictions/README.md', ROOT / 'evidence-notes/001-anthropic-global-workspace-and-ieh.md']
forbidden_terms = (
    'Informational Existence Right', 'Right of Information Existence',
    'Information Right to Exist', 'Informational Right of Existence',
    'Human Information Ecological Niche', 'Information Ecological Niche',
    'Patch-based Perpetuation', 'Informational Existence Hypothesis'
)
for path in substantive:
    text = path.read_text(encoding='utf-8')
    for term in forbidden_terms:
        if term in text:
            error(f'Noncanonical terminology in {path.relative_to(ROOT)}: {term}')

# Chapter titles must match the bilingual chapter indexes.
def first_heading(path):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return None

for lang, files in (('zh', zh_files), ('en', en_files)):
    index = (ROOT / lang / 'README.md').read_text(encoding='utf-8')
    for path in files:
        title = first_heading(path)
        if not title or title not in index:
            error(f'{lang}/README.md does not contain exact chapter title from {path.name}: {title}')

# Version consistency.
cff = (ROOT / 'CITATION.cff').read_text(encoding='utf-8')
if 'version: "1.2"' not in cff or 'date-released: 2026-07-13' not in cff:
    error('CITATION.cff version/date are not v1.2 / 2026-07-13.')

print(f'Checked repository: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s).')
for item in WARNINGS:
    print('WARNING:', item)
for item in ERRORS:
    print('ERROR:', item)
sys.exit(1 if ERRORS else 0)
