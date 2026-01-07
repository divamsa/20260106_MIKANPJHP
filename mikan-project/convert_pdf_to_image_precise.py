#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
import pdfplumber
import os

def pdf_to_image_precise(pdf_path, output_dir='public/images'):
    """PDFを画像に変換し、Works Staff Companyの部分を正確に削除"""
    # 出力ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)
    
    # PDFファイルを開く（pypdfium2で画像化）
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[0]
    bitmap = page.render(scale=2.0)
    pil_image = bitmap.to_pil()
    
    # PDFのページサイズを取得
    page_width = page.get_width()
    page_height = page.get_height()
    
    # pdfplumberでテキストの位置を取得
    with pdfplumber.open(pdf_path) as pdf_plumber:
        page_plumber = pdf_plumber.pages[0]
        
        # すべての文字を取得
        chars = page_plumber.chars
        
        # "Works Staff Company"を含む文字の座標を取得
        works_y_positions = []
        staff_y_positions = []
        company_y_positions = []
        
        for char in chars:
            text = char.get('text', '')
            if 'Works' in text or 'Staff' in text or 'Company' in text:
                # PDF座標系から画像座標系に変換
                # PDFは左下が原点、画像は左上が原点
                pdf_y = char.get('top', 0)
                # 画像の高さに合わせてスケール
                scale_factor = pil_image.height / page_height
                image_y = pdf_y * scale_factor
                
                if 'Works' in text:
                    works_y_positions.append(image_y)
                elif 'Staff' in text:
                    staff_y_positions.append(image_y)
                elif 'Company' in text:
                    company_y_positions.append(image_y)
        
        # すべてのY座標を統合
        all_y_positions = works_y_positions + staff_y_positions + company_y_positions
        
        if all_y_positions:
            # 最小Y座標と最大Y座標を取得
            min_y = min(all_y_positions)
            max_y = max(all_y_positions)
            
            # 少し余裕を持たせて削除領域を設定
            margin = 30  # ピクセル単位のマージン
            delete_top = max(0, int(min_y - margin))
            delete_bottom = min(pil_image.height, int(max_y + margin))
            
            print(f'Found text at Y positions: {min_y:.1f} - {max_y:.1f}')
            print(f'Deleting region: {delete_top} - {delete_bottom}')
            
            # 該当領域をghostwhiteで塗りつぶす
            draw = ImageDraw.Draw(pil_image)
            draw.rectangle(
                [(0, delete_top), (pil_image.width, delete_bottom)],
                fill='ghostwhite'
            )
        else:
            # テキストが見つからない場合は、下部20%を削除
            print('Text not found, removing bottom 20%')
            delete_bottom = int(pil_image.height * 0.20)
            draw = ImageDraw.Draw(pil_image)
            draw.rectangle(
                [(0, pil_image.height - delete_bottom), (pil_image.width, pil_image.height)],
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
        pdf_to_image_precise(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


