#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import time
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

url = "https://scholar.google.com/citations?user=Y2GtJkAAAAAJ&hl=en"

print("正在尝试访问Google Scholar...")
try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"响应状态码: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        papers = []
        
        for item in soup.select('.gsc_a_tr'):
            title_elem = item.select_one('.gsc_a_at')
            if title_elem:
                title = title_elem.text.strip()
                link = title_elem.get('href', '')
                
                authors_elem = item.select_one('.gsc_a_t .gsc_a_as')
                authors = authors_elem.text.strip() if authors_elem else ''
                
                year_elem = item.select_one('.gsc_a_y')
                year = year_elem.text.strip() if year_elem else ''
                
                citations_elem = item.select_one('.gsc_a_c')
                citations = citations_elem.text.strip() if citations_elem else '0'
                
                paper_info = {
                    'title': title,
                    'link': link,
                    'authors': authors,
                    'year': year,
                    'citations': citations
                }
                papers.append(paper_info)
        
        print(f"\n找到 {len(papers)} 篇论文")
        
        for i, paper in enumerate(papers[:10], 1):
            print(f"\n{i}. {paper['title']}")
            print(f"   作者: {paper['authors']}")
            print(f"   年份: {paper['year']}")
            print(f"   引用数: {paper['citations']}")
        
        with open('saining_xie_papers.json', 'w', encoding='utf-8') as f:
            json.dump(papers, f, ensure_ascii=False, indent=2)
        
        print(f"\n所有论文信息已保存到 saining_xie_papers.json")
        
    else:
        print("访问被拒绝，可能需要使用其他方法")
        print("建议方案:")
        print("1. 使用 arXiv API 查找谢赛宁的论文")
        print("2. 手动访问页面并复制论文列表")
        
except Exception as e:
    print(f"错误: {e}")
    print("\n建议使用其他方法获取论文信息")