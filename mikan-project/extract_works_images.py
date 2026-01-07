#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image
import os

def extract_works_images(pdf_path, output_dir='public/images/works'):
    """Works.pdfから各作品の画像を抽出"""
    # 出力ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)
    
    # PDFファイルを開く
    pdf = pdfium.PdfDocument(pdf_path)
    
    # 各ページを画像に変換
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        bitmap = page.render(scale=2.0)  # 高解像度でレンダリング
        
        # PIL Imageに変換
        pil_image = bitmap.to_pil()
        
        # ファイル名を生成（ページ番号は1から始まる）
        output_path = os.path.join(output_dir, f'work_{page_num + 1}.png')
        
        # 画像を保存
        pil_image.save(output_path, 'PNG', optimize=True)
        
        print(f'✓ Extracted page {page_num + 1} to {output_path}')
    
    print(f'\n✓ Extracted {len(pdf)} images from {pdf_path}')
    
    return output_dir

if __name__ == '__main__':
    pdf_file = '../Works.pdf'
    if os.path.exists(pdf_file):
        extract_works_images(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


