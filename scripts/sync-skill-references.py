#!/usr/bin/env python3
"""Bundle canonical guides into each independently mounted skill directory."""
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1] / 'plugins' / 'bigmind'
for skill in sorted((PLUGIN / 'skills').glob('*/SKILL.md')):
    destination = skill.parent / 'references'
    destination.mkdir(exist_ok=True)
    for source in (PLUGIN / 'references').glob('*.md'):
        (destination / source.name).write_bytes(source.read_bytes())
print('Bundled shared guides into every skill.')
