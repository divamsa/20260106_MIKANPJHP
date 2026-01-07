#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from docx2pdf import convert
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 convert_single.py <docx_file>")
    sys.exit(1)

file = sys.argv[1]

if not os.path.exists(file):
    print(f'File not found: {file}')
    sys.exit(1)

print(f'Converting {file} to PDF...')
try:
    convert(file)
    print(f'✓ Successfully converted {file}')
except Exception as e:
    print(f'✗ Error converting {file}: {e}')
    sys.exit(1)


