#!/usr/bin/env python3
"""Check repository-relative Markdown file links outside fenced examples."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', 'node_modules', 'dist', '__pycache__'}
def check_links():
    checked = 0
    for path in ROOT.rglob('*.md'):
        if SKIP.intersection(path.relative_to(ROOT).parts):
            continue
        fence = None
        for line in path.read_text().splitlines():
            marker = re.match(r'^\s*(`{3,}|~{3,})', line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                continue
            if fence:
                continue
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', line):
                url = urlsplit(target)
                if url.scheme or not url.path:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.exists():
                    raise ValueError(f'{path.relative_to(ROOT)}: broken or external local link: {target}')
                checked += 1
    print(f'Checked {checked} repository-relative Markdown links.')
if __name__ == '__main__':
    check_links()
