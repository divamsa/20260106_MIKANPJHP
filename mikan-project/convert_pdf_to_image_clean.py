#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
import os

def pdf_to_image_clean(pdf_path, output_dir='public/images'):
    """PDFを画像に変換し、下部のWorks Staff Companyの部分を削除"""
    # 出力ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)
    
    # PDFファイルを開く
    pdf = pdfium.PdfDocument(pdf_path)
    
    # 最初のページを画像に変換
    page = pdf[0]  # 最初のページ（0-indexed）
    bitmap = page.render(scale=2.0)  # 高解像度でレンダリング
    
    # PIL Imageに変換
    pil_image = bitmap.to_pil()
    
    # 画像のサイズを取得
    width, height = pil_image.size
    
    # 下部の20%程度を白で塗りつぶす（Works Staff Companyの部分を削除）
    # 下部から20%の領域を白で塗りつぶす
    draw = ImageDraw.Draw(pil_image)
    fill_height = int(height * 0.20)  # 下部20%
    draw.rectangle([(0, height - fill_height), (width, height)], fill='ghostwhite')
    
    # ファイル名を生成
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(output_dir, f'{base_name}.png')
    
    # 画像を保存
    pil_image.save(output_path, 'PNG', optimize=True)
    
    print(f'✓ Converted {pdf_path} to {output_path} (cleaned)')
    
    return output_path

if __name__ == '__main__':
    pdf_file = '../表紙.pdf'
    if os.path.exists(pdf_file):
        pdf_to_image_clean(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


