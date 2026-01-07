#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image
import os

def extract_individual_works(pdf_path, output_dir='public/images/works'):
    """Works.pdfから各作品の個別画像を抽出"""
    os.makedirs(output_dir, exist_ok=True)
    
    pdf = pdfium.PdfDocument(pdf_path)
    
    # 作品とページ、位置のマッピング
    # 各作品の位置を推定して切り出す
    works_config = [
        # ページ1の作品
        {'name': '断らない_ある市役所の実践', 'page': 0, 'crop': (0, 0, 1.0, 0.25)},
        {'name': '迷える女性たちの家', 'page': 0, 'crop': (0, 0.25, 1.0, 0.4)},
        {'name': 'この国で生きてゆく', 'page': 0, 'crop': (0, 0.4, 1.0, 0.55)},
        {'name': 'すべてのものが幸福にしかなれない處', 'page': 0, 'crop': (0, 0.55, 1.0, 0.7)},
        {'name': 'だからあんな不思議な絵を', 'page': 0, 'crop': (0, 0.7, 1.0, 0.85)},
        {'name': '人生で美しいとは何か', 'page': 0, 'crop': (0, 0.85, 1.0, 1.0)},
        # ページ2の作品
        {'name': '美は喜び_河井寬次郎', 'page': 1, 'crop': (0, 0, 1.0, 0.5)},
        {'name': '知っていますか_ハンセン病問題', 'page': 1, 'crop': (0, 0.5, 1.0, 1.0)},
    ]
    
    for config in works_config:
        page = pdf[config['page']]
        bitmap = page.render(scale=2.0)
        pil_image = bitmap.to_pil()
        
        width, height = pil_image.size
        left = int(config['crop'][0] * width)
        top = int(config['crop'][1] * height)
        right = int(config['crop'][2] * width)
        bottom = int(config['crop'][3] * height)
        
        # 画像を切り出し
        cropped = pil_image.crop((left, top, right, bottom))
        
        output_path = os.path.join(output_dir, f"{config['name']}.png")
        cropped.save(output_path, 'PNG', optimize=True)
        print(f'✓ Extracted {config["name"]} to {output_path}')
    
    print(f'\n✓ Extracted {len(works_config)} individual work images')

if __name__ == '__main__':
    pdf_file = '../Works.pdf'
    if os.path.exists(pdf_file):
        extract_individual_works(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


