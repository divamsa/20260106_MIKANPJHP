#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image
import os
import sys

def pdf_to_image(pdf_path, output_dir='public/images'):
    """PDFを画像に変換"""
    # 出力ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)
    
    # PDFファイルを開く
    pdf = pdfium.PdfDocument(pdf_path)
    
    # 最初のページを画像に変換
    page = pdf[0]  # 最初のページ（0-indexed）
    bitmap = page.render(scale=2.0)  # 高解像度でレンダリング
    
    # PIL Imageに変換
    pil_image = bitmap.to_pil()
    
    # ファイル名を生成
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(output_dir, f'{base_name}.png')
    
    # 画像を保存
    pil_image.save(output_path, 'PNG', optimize=True)
    
    print(f'✓ Converted {pdf_path} to {output_path}')
    
    return output_path

if __name__ == '__main__':
    pdf_file = '../表紙.pdf'
    if os.path.exists(pdf_file):
        pdf_to_image(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


