#!/usr/bin/env python3
"""Validate this repository's manifest, skill discovery, and local references."""
import json
import re
from pathlib import Path
from check_links import check_links
root = Path(__file__).resolve().parents[1]
plugins = list((root/'plugins').iterdir())
assert plugins, 'No plugins found'
count = 0
for plugin in plugins:
    manifest = json.loads((plugin/'.codex-plugin/plugin.json').read_text())
    assert manifest['name'] == plugin.name
    assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
    assert manifest['description'] and manifest['author']['name']
    assert manifest['skills'] == './skills/'
    for field in ('displayName','shortDescription','longDescription','developerName','category'):
        assert manifest['interface'][field]
    for field in ('mcpServers','apps'):
        assert field not in manifest, 'Skills-only release must not imply a bundled connection'
    skills = sorted((plugin/'skills').iterdir())
    assert skills, 'No skills found'
    for skill in skills:
        text = (skill/'SKILL.md').read_text()
        match = re.match(r'^---\n(.*?)\n---\n',text,re.S)
        assert match, f'Missing frontmatter: {skill.name}'
        # This package uses simple scalar name/description metadata.
        header = dict(line.split(': ',1) for line in match[1].splitlines())
        assert set(header) == {'name','description'}
        assert header['name'] == skill.name and len(skill.name) < 64
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',skill.name)
        assert 0 < len(header['description']) <= 1024
        assert '[TODO:' not in text
        guide_links = re.findall(r'https://github.com/outset-vtt/compendium-authoring-guide[^)\s]*', text)
        for link in guide_links:
            assert re.match(r'https://github.com/outset-vtt/compendium-authoring-guide/(?:blob|tree)/v' + re.escape(manifest['version']) + r'(?:/|$)', link), 'Pin guide references to the matching release: ' + link
        count += 1
check_links()
print(f'Validated {len(plugins)} plugin and {count} skills.')
