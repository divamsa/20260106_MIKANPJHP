#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image
import pdfplumber
import os

def extract_correct_works_images(pdf_path, output_dir='public/images/works'):
    """Works.pdfから各番組に対応する正確な画像を抽出"""
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_pdfium = pdfium.PdfDocument(pdf_path)
    pdf_plumber = pdfplumber.open(pdf_path)
    
    # 各番組の設定（テキスト位置から画像領域を計算）
    works_config = [
        {
            'name': '断らない_ある市役所の実践',
            'page': 0,
            'search': '断らない',
            'image_top_offset': -80,  # テキストより上80px
            'image_bottom_offset': 100,  # テキストより下100px
            'image_left': 0,
            'image_right': 1.0,  # 全幅
        },
        {
            'name': '迷える女性たちの家',
            'page': 0,
            'search': '迷える女性',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
        {
            'name': 'この国で生きてゆく',
            'page': 0,
            'search': 'この国で生きてゆく',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
        {
            'name': 'すべてのものが幸福にしかなれない處',
            'page': 0,
            'search': 'すべてのものが幸福',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
        {
            'name': 'だからあんな不思議な絵を',
            'page': 0,
            'search': 'だからあんな不思議',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
        {
            'name': '人生で美しいとは何か',
            'page': 0,
            'search': '人生で美しい',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
        {
            'name': '美は喜び_河井寬次郎',
            'page': 1,
            'search': '美は喜び',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
        {
            'name': '知っていますか_ハンセン病問題',
            'page': 1,
            'search': '知っていますか',
            'image_top_offset': -80,
            'image_bottom_offset': 100,
            'image_left': 0,
            'image_right': 1.0,
        },
    ]
    
    print("=== Extracting Work Images ===\n")
    
    for config in works_config:
        # PDFiumでページを画像化
        page_pdfium = pdf_pdfium[config['page']]
        bitmap = page_pdfium.render(scale=2.0)
        pil_image = bitmap.to_pil()
        
        # pdfplumberでテキスト位置を取得
        page_plumber = pdf_plumber.pages[config['page']]
        words = page_plumber.extract_words()
        
        # 該当テキストを探す
        target_word = None
        for word in words:
            if config['search'] in word.get('text', ''):
                target_word = word
                break
        
        if target_word:
            # テキスト位置から画像位置を計算
            page_height = page_plumber.height
            page_width = page_plumber.width
            
            # スケールファクター
            scale_y = pil_image.height / page_height
            scale_x = pil_image.width / page_width
            
            # テキストの位置（PDF座標系：左下が原点）
            text_top_pdf = target_word.get('top', 0)
            
            # 画像座標系（左上が原点）に変換
            text_top_image = (page_height - text_top_pdf) * scale_y
            
            # 画像領域を計算
            image_top = int(text_top_image + config['image_top_offset'] * scale_y)
            image_bottom = int(text_top_image + config['image_bottom_offset'] * scale_y)
            image_left = int(config['image_left'] * pil_image.width)
            image_right = int(config['image_right'] * pil_image.width)
            
            # 境界チェック
            image_top = max(0, image_top)
            image_bottom = min(pil_image.height, image_bottom)
            image_left = max(0, image_left)
            image_right = min(pil_image.width, image_right)
            
            # 画像を切り出し
            if image_bottom > image_top and image_right > image_left:
                cropped = pil_image.crop((image_left, image_top, image_right, image_bottom))
                
                output_path = os.path.join(output_dir, f"{config['name']}.png")
                cropped.save(output_path, 'PNG', optimize=True)
                print(f"✓ {config['name']}")
                print(f"  Text position: {text_top_pdf:.1f} (PDF), {text_top_image:.1f} (Image)")
                print(f"  Image area: top={image_top}, bottom={image_bottom}, height={image_bottom-image_top}")
                print(f"  Saved to: {output_path}\n")
            else:
                print(f"✗ {config['name']}: Invalid crop area\n")
        else:
            print(f"✗ {config['name']}: Text not found\n")
    
    pdf_plumber.close()
    print("=== Extraction Complete ===")

if __name__ == '__main__':
    pdf_file = '../Works.pdf'
    if os.path.exists(pdf_file):
        extract_correct_works_images(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


