#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pdfplumber
import sys

files = ['表紙.pdf', 'Company.pdf', 'Staff.pdf', 'Works.pdf']

for pdf_file in files:
    print(f'\n{"="*60}')
    print(f'ファイル: {pdf_file}')
    print(f'{"="*60}\n')
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    print(f'--- ページ {i} ---')
                    print(text)
                    print()
    except Exception as e:
        print(f'エラー: {e}')


