#!/usr/bin/env python3
"""Check references after copying only skill folders into a Claude-style mount."""
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote

PLUGIN = Path(__file__).resolve().parents[1] / 'plugins' / 'bigmind'
errors = []
with tempfile.TemporaryDirectory(prefix='bigmind-skills-', ignore_cleanup_errors=True) as temporary:
    mount = Path(temporary).resolve() / 'mnt' / 'skills' / 'plugins'
    mount.mkdir(parents=True)
    skills = sorted((PLUGIN / 'skills').glob('*/SKILL.md'))
    for skill in skills:
        root = mount / f'60474523-d762-41f2-855f-665e261aa5ce:{skill.parent.name}'
        shutil.copytree(skill.parent, root, symlinks=True)
        for file in root.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                    continue
                target = (file.parent / unquote(link.split('#', 1)[0])).resolve()
                if not target.is_relative_to(root) or not target.is_file():
                    errors.append(f'{skill.parent.name}/{file.relative_to(root)}: unavailable reference {link}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'All local Markdown references resolve inside each of {len(skills)} isolated skill mounts.')
