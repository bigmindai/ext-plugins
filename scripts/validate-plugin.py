#!/usr/bin/env python3
"""Validate the shipped plugin's local dependency graph and metadata (no network)."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'bigmind'
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def local_target(source, value, boundary):
    target = (source.parent / unquote(value.split('#', 1)[0])).resolve()
    check(target.is_relative_to(boundary), f'{source.relative_to(ROOT)}: path escapes package: {value}')
    check(target.exists(), f'{source.relative_to(ROOT)}: missing target: {value}')
    return target

manifests = list(PLUGIN.glob('.*-plugin/plugin.json'))
check(len(manifests) == 3, 'Expected Claude, Codex and Cursor manifests')
versions = set()
for file in manifests:
    data = json.loads(file.read_text())
    versions.add(data.get('version'))
    check(data.get('name') == 'bigmind', f'{file}: wrong plugin name')
    check(bool(re.fullmatch(r'\d+\.\d+\.\d+', data.get('version', ''))), f'{file}: invalid version')
    # Manifest paths resolve against the plugin root, not the manifest directory.
    for key in ('skills', 'mcpServers', 'logo'):
        if key in data:
            local_target(PLUGIN / 'manifest', data[key], PLUGIN)
    for key in ('composerIcon', 'logo'):
        if key in data.get('interface', {}):
            local_target(PLUGIN / 'manifest', data['interface'][key], PLUGIN)
check(len(versions) == 1, 'Platform manifest versions differ')
json.loads((PLUGIN / '.mcp.json').read_text())

skills = list((PLUGIN / 'skills').glob('*/SKILL.md'))
names = set()
for file in skills:
    text = file.read_text()
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    check(match is not None, f'{file}: missing frontmatter')
    if not match:
        continue
    fields = dict(re.findall(r'^(name|description):\s*(.+)$', match.group(1), re.M))
    name = fields.get('name', '')
    check(name == file.parent.name and bool(re.fullmatch(r'[a-z0-9-]{1,64}', name)), f'{file}: invalid skill name')
    check(name not in names, f'{file}: duplicate skill name')
    names.add(name)
    check(bool(fields.get('description')), f'{file}: missing description')
    check(not re.search(r'\[(?:TODO|INSERT|PLACEHOLDER)\]', text), f'{file}: unfinished scaffold')

# Catch broken references, package-external dependencies and stranded guides.
referenced = set()
for file in [ROOT / 'README.md', *PLUGIN.rglob('*.md')]:
    for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
            continue
        boundary = ROOT if file == ROOT / 'README.md' or file == PLUGIN / 'README.md' else PLUGIN
        referenced.add(local_target(file, link, boundary))
for file in (PLUGIN / 'references').glob('*.md'):
    check(file.resolve() in referenced, f'Unlinked shared guide: {file.name}')
for file in skills:
    check(file.resolve() in referenced, f'Skill missing from catalog: {file.parent.name}')

for file in (ROOT / '.agents/plugins/marketplace.json', ROOT / '.cursor-plugin/marketplace.json'):
    data = json.loads(file.read_text())
    for plugin in data['plugins']:
        source = plugin['source']
        path = source['path'] if isinstance(source, dict) else source
        local_target(ROOT / 'marketplace', path, ROOT)

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Validated {len(skills)} skills, {len(manifests)} synchronized manifests, assets, marketplaces and local references.')
