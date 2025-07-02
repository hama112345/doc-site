#!/usr/bin/env python3
"""Convert all .docx files in docs_src/ to markdown in docs/ for MkDocs."""

import glob
import pathlib
import re
import subprocess
import sys

try:
    import pypandoc
except ImportError:
    sys.stderr.write("pypandoc not installed. Install with `pip install pypandoc`\n")
    sys.exit(1)

def safe_filename(name: str) -> str:
    # Remove unsafe chars and spaces -> underscore
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    return re.sub(r'\s+', '_', name)

docs_src = pathlib.Path('docs_src')
docs_dst = pathlib.Path('docs')
docs_dst.mkdir(exist_ok=True)

for docx_path in docs_src.glob('*.docx'):
    stem = docx_path.stem
    md_name = safe_filename(stem) + '.md'
    md_path = docs_dst / md_name
    print(f'Converting {docx_path} -> {md_path}')
    markdown = pypandoc.convert_file(str(docx_path), 'gfm')
    md_path.write_text(markdown, encoding='utf-8')
print('Conversion complete.')
