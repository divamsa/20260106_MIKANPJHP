#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from docx2pdf import convert
import sys
import os
import time

files = ['Company.docx', 'Staff.docx', 'Works.docx', '表紙.docx']

for file in files:
    if os.path.exists(file):
        print(f'Converting {file} to PDF...')
        try:
            # 少し待機してから変換（Wordの準備時間を確保）
            time.sleep(1)
            convert(file)
            print(f'✓ Successfully converted {file}')
            # 変換間隔を空ける
            time.sleep(2)
        except Exception as e:
            print(f'✗ Error converting {file}: {e}')
            # エラーが発生した場合も少し待機
            time.sleep(2)
    else:
        print(f'✗ File not found: {file}')

print('Conversion complete!')
