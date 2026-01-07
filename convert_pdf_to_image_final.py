#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
import pdfplumber
import os

def pdf_to_image_final(pdf_path, output_dir='public/images'):
    """PDFを画像に変換し、Works Staff Companyの部分を正確に削除"""
    # 出力ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)
    
    # PDFファイルを開く（pypdfium2で画像化）
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[0]
    bitmap = page.render(scale=2.0)
    pil_image = bitmap.to_pil()
    
    width, height = pil_image.size
    
    print(f'Image size: {width} x {height}')
    
    # pdfplumberでテキストの位置を取得
    with pdfplumber.open(pdf_path) as pdf_plumber:
        page_plumber = pdf_plumber.pages[0]
        
        # ページのサイズを取得
        page_width = page_plumber.width
        page_height = page_plumber.height
        
        print(f'PDF page size: {page_width} x {page_height}')
        
        # すべての単語を取得
        words = page_plumber.extract_words()
        
        # "Works", "Staff", "Company"を含む単語の座標を取得
        target_texts = ['Works', 'Staff', 'Company']
        y_positions = []
        
        for word in words:
            text = word.get('text', '').strip()
            if text in target_texts:
                # PDF座標系を確認
                pdf_y_top = word.get('top', 0)
                pdf_y_bottom = word.get('bottom', 0)
                
                # スケールファクターを計算
                scale_y = height / page_height
                
                # pdfplumberのtopは上からの距離なので、そのままスケール
                image_y_top = pdf_y_top * scale_y
                image_y_bottom = pdf_y_bottom * scale_y
                
                y_positions.extend([image_y_top, image_y_bottom])
                print(f'Found "{text}" at PDF Y: {pdf_y_top:.1f}-{pdf_y_bottom:.1f}, Image Y: {image_y_top:.1f}-{image_y_bottom:.1f}')
        
        if y_positions:
            # 最小Y座標と最大Y座標を取得
            min_y = min(y_positions)
            max_y = max(y_positions)
            
            # テキストの位置から下部を削除（テキストより上は残す）
            # テキストの少し上から画像の最下部までを削除
            margin_top = 20  # テキストの少し上から
            delete_top = max(0, int(min_y - margin_top))
            delete_bottom = height  # 画像の最下部まで
            
            print(f'Deleting region: Y={delete_top} to Y={delete_bottom} (height: {delete_bottom - delete_top}px)')
            print(f'This removes {((height - delete_top) / height * 100):.1f}% from bottom')
            
            # 該当領域をghostwhiteで塗りつぶす
            draw = ImageDraw.Draw(pil_image)
            draw.rectangle(
                [(0, delete_top), (width, delete_bottom)],
                fill='ghostwhite'
            )
        else:
            # テキストが見つからない場合は、下部30%を削除
            print('Text coordinates not found, removing bottom 30%')
            delete_height = int(height * 0.30)
            draw = ImageDraw.Draw(pil_image)
            draw.rectangle(
                [(0, height - delete_height), (width, height)],
                fill='ghostwhite'
            )
    
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
        pdf_to_image_final(pdf_file)
    else:
        print(f'File not found: {pdf_file}')
