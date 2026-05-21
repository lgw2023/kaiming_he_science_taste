#!/usr/bin/env python3
from scholarly import scholarly
import json
import time

print("正在搜索谢赛宁(Saining Xie)的Google Scholar页面...")

try:
    search_query = scholarly.search_author('Saining Xie')
    author = next(search_query)
    
    print(f"\n找到作者: {author['name']}")
    print(f"机构: {author.get('affiliation', 'N/A')}")
    print(f"总引用数: {author.get('citedby', 'N/A')}")
    print(f"H-index: {author.get('hindex', 'N/A')}")
    
    author_filled = scholarly.fill(author)
    
    print(f"\n论文总数: {len(author_filled.get('publications', []))}")
    
    publications = []
    for pub in author_filled.get('publications', [])[:50]:
        pub_filled = scholarly.fill(pub)
        
        title = pub_filled.get('bib', {}).get('title', 'N/A')
        year = pub_filled.get('bib', {}).get('pub_year', 'N/A')
        authors = pub_filled.get('bib', {}).get('author', 'N/A')
        citations = pub_filled.get('num_citations', 0)
        
        pub_info = {
            'title': title,
            'year': year,
            'authors': authors,
            'citations': citations,
            'bib': pub_filled.get('bib', {})
        }
        publications.append(pub_info)
        
        print(f"\n{len(publications)}. {title}")
        print(f"   年份: {year}")
        print(f"   引用数: {citations}")
        
        time.sleep(2)
    
    with open('saining_xie_papers.json', 'w', encoding='utf-8') as f:
        json.dump({
            'author': author_filled,
            'publications': publications
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n所有论文信息已保存到 saining_xie_papers.json")
    
except Exception as e:
    print(f"错误: {e}")
    print("\n可能遇到反爬虫限制，建议稍后再试或手动访问页面")