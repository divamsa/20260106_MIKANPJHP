#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import time

def convert_docx_to_pdf(docx_path):
    """AppleScriptを使ってWordでdocxをPDFに変換"""
    pdf_path = docx_path.replace('.docx', '.pdf')
    abs_docx = os.path.abspath(docx_path)
    abs_pdf = os.path.abspath(pdf_path)
    
    script = f'''
    tell application "Microsoft Word"
        activate
        set docPath to POSIX file "{abs_docx}"
        open docPath
        set theActiveDoc to active document
        set pdfPath to POSIX file "{abs_pdf}"
        save as theActiveDoc file format format PDF file name pdfPath
        close theActiveDoc saving no
    end tell
    '''
    
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=120
        )
        if result.returncode == 0:
            return True, None
        else:
            return False, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

files = ['Company.docx', 'Staff.docx', 'Works.docx', '表紙.docx']

for file in files:
    if os.path.exists(file):
        print(f'Converting {file} to PDF...')
        success, error = convert_docx_to_pdf(file)
        if success:
            print(f'✓ Successfully converted {file}')
        else:
            print(f'✗ Error converting {file}: {error}')
        time.sleep(2)  # 変換間隔を空ける
    else:
        print(f'✗ File not found: {file}')

print('Conversion complete!')
