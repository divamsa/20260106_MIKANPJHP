#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image
import pdfplumber
import os

def extract_precise_works(pdf_path, output_dir='public/images/works'):
    """Works.pdfから各作品の正確な位置で画像を抽出"""
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_pdfium = pdfium.PdfDocument(pdf_path)
    pdf_plumber = pdfplumber.open(pdf_path)
    
    # 作品とテキストのマッピング
    works_config = [
        {'name': '断らない_ある市役所の実践', 'page': 0, 'text': '断らない'},
        {'name': '迷える女性たちの家', 'page': 0, 'text': '迷える女性'},
        {'name': 'この国で生きてゆく', 'page': 0, 'text': 'この国で生きてゆく'},
        {'name': 'すべてのものが幸福にしかなれない處', 'page': 0, 'text': 'すべてのものが幸福'},
        {'name': 'だからあんな不思議な絵を', 'page': 0, 'text': 'だからあんな不思議'},
        {'name': '人生で美しいとは何か', 'page': 0, 'text': '人生で美しい'},
        {'name': '美は喜び_河井寬次郎', 'page': 1, 'text': '美は喜び'},
        {'name': '知っていますか_ハンセン病問題', 'page': 1, 'text': '知っていますか'},
    ]
    
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
            if config['text'] in word.get('text', ''):
                target_word = word
                break
        
        if target_word:
            # テキスト位置から画像位置を計算
            page_height = page_plumber.height
            page_width = page_plumber.width
            
            # PDF座標系（左下が原点）から画像座標系（左上が原点）に変換
            scale_y = pil_image.height / page_height
            scale_x = pil_image.width / page_width
            
            # テキストの上から少し上まで、次の作品の前までを切り出す
            text_top = target_word.get('top', 0)
            text_bottom = target_word.get('bottom', 0)
            
            # 画像座標に変換
            image_y_top = (page_height - text_top - 50) * scale_y  # 上に50px余裕
            image_y_bottom = (page_height - text_bottom + 200) * scale_y  # 下に200px余裕
            
            # 境界チェック
            image_y_top = max(0, int(image_y_top))
            image_y_bottom = min(pil_image.height, int(image_y_bottom))
            
            # 画像を切り出し
            cropped = pil_image.crop((0, image_y_top, pil_image.width, image_y_bottom))
        else:
            # テキストが見つからない場合は全体を使用
            cropped = pil_image
        
        output_path = os.path.join(output_dir, f"{config['name']}.png")
        cropped.save(output_path, 'PNG', optimize=True)
        print(f'✓ Extracted {config["name"]} to {output_path}')
    
    pdf_plumber.close()
    print(f'\n✓ Extracted {len(works_config)} precise work images')

if __name__ == '__main__':
    pdf_file = '../Works.pdf'
    if os.path.exists(pdf_file):
        extract_precise_works(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


