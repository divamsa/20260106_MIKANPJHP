#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
from PIL import Image
import pdfplumber
import os

def analyze_works_pdf(pdf_path):
    """Works.pdfの構造を分析して、各番組と画像の対応関係を表示"""
    pdf_pdfium = pdfium.PdfDocument(pdf_path)
    pdf_plumber = pdfplumber.open(pdf_path)
    
    # 全作品リスト
    works_list = [
        {'title': '断らない ある市役所の実践', 'page': 0, 'search': '断らない'},
        {'title': '迷える女性たちの家', 'page': 0, 'search': '迷える女性'},
        {'title': 'この国で生きてゆく ～大阪 外国ルーツの子どもたち', 'page': 0, 'search': 'この国で生きてゆく'},
        {'title': 'すべてのものが幸福にしかなれない處 ～京都・五条坂 河井寬次郎家の人々', 'page': 0, 'search': 'すべてのものが幸福'},
        {'title': 'だからあんな不思議な絵を 〜夭折の画家・有元利夫と家族〜', 'page': 0, 'search': 'だからあんな不思議'},
        {'title': '人生で美しいとは何か 彫刻家・舟越保武と子どもたち', 'page': 0, 'search': '人生で美しい'},
        {'title': '美は喜び 河井寬次郎 住める哲学', 'page': 1, 'search': '美は喜び'},
        {'title': '知っていますか？ ハンセン病問題', 'page': 1, 'search': '知っていますか'},
    ]
    
    print("=== Works PDF Analysis ===\n")
    
    for work in works_list:
        page_plumber = pdf_plumber.pages[work['page']]
        words = page_plumber.extract_words()
        
        # 該当テキストを探す
        target_words = []
        for word in words:
            if work['search'] in word.get('text', ''):
                target_words.append(word)
        
        if target_words:
            first_word = target_words[0]
            print(f"【{work['title']}】")
            print(f"  ページ: {work['page'] + 1}")
            print(f"  テキスト位置: top={first_word.get('top', 0):.1f}, bottom={first_word.get('bottom', 0):.1f}")
            print(f"  ページ高さ: {page_plumber.height:.1f}")
            print(f"  相対位置: {first_word.get('top', 0) / page_plumber.height * 100:.1f}% from top")
            print()
    
    # 各ページの画像を保存して確認
    output_dir = 'public/images/works_analysis'
    os.makedirs(output_dir, exist_ok=True)
    
    for page_num in range(len(pdf_pdfium)):
        page = pdf_pdfium[page_num]
        bitmap = page.render(scale=2.0)
        pil_image = bitmap.to_pil()
        output_path = os.path.join(output_dir, f'page_{page_num + 1}_full.png')
        pil_image.save(output_path, 'PNG', optimize=True)
        print(f"Saved full page {page_num + 1} to {output_path}")
    
    pdf_plumber.close()
    print("\n=== Analysis Complete ===")

if __name__ == '__main__':
    pdf_file = '../Works.pdf'
    if os.path.exists(pdf_file):
        analyze_works_pdf(pdf_file)
    else:
        print(f'File not found: {pdf_file}')


