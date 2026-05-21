#!/usr/bin/env python3
import requests
import json
import time

API_KEY = ""  # Semantic Scholar不需要API key也能使用基本功能

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Research Bot)',
}

print("正在使用Semantic Scholar API搜索谢赛宁的论文...")

base_url = "https://api.semanticscholar.org/graph/v1"

try:
    # 搜索作者
    author_search_url = f"{base_url}/author/search"
    params = {
        'query': 'Saining Xie',
        'limit': 5
    }
    
    response = requests.get(author_search_url, headers=headers, params=params, timeout=30)
    data = response.json()
    
    print(f"搜索结果: {json.dumps(data, indent=2)}")
    
    if 'data' in data and len(data['data']) > 0:
        author = data['data'][0]
        author_id = author.get('authorId')
        
        print(f"\n找到作者:")
        print(f"  姓名: {author.get('name')}")
        print(f"  机构: {author.get('affiliation', 'N/A')}")
        print(f"  论文数: {author.get('paperCount', 'N/A')}")
        print(f"  引用数: {author.get('citationCount', 'N/A')}")
        print(f"  H-index: {author.get('hIndex', 'N/A')}")
        
        # 获取作者的论文
        papers_url = f"{base_url}/author/{author_id}/papers"
        params = {
            'limit': 500,
            'fields': 'title,year,authors,citationCount,url,externalIds,publicationVenue'
        }
        
        all_papers = []
        offset = 0
        
        while True:
            params['offset'] = offset
            response = requests.get(papers_url, headers=headers, params=params, timeout=30)
            papers_data = response.json()
            
            if 'data' not in papers_data or len(papers_data['data']) == 0:
                break
            
            all_papers.extend(papers_data['data'])
            
            if 'next' not in papers_data:
                break
            
            offset = papers_data['next']
            time.sleep(1)
        
        publications = []
        print(f"\n论文总数: {len(all_papers)}")
        
        for i, paper in enumerate(all_papers, 1):
                title = paper.get('title', 'N/A')
                year = paper.get('year', 'N/A')
                citations = paper.get('citationCount', 0)
                authors_list = paper.get('authors', [])
                authors_str = ', '.join([a.get('name', '') for a in authors_list[:5]])
                
                # 尝试找到arXiv ID
                external_ids = paper.get('externalIds', {})
                arxiv_id = external_ids.get('ArXiv', None)
                
                pub_info = {
                    'title': title,
                    'year': year,
                    'authors': authors_str,
                    'citations': citations,
                    'url': paper.get('url'),
                    'arxiv_id': arxiv_id,
                    'externalIds': external_ids,
                    'paperId': paper.get('paperId')
                }
                publications.append(pub_info)
                
                print(f"\n{i}. {title}")
                print(f"   年份: {year}")
                print(f"   引用数: {citations}")
                if arxiv_id:
                    print(f"   arXiv: https://arxiv.org/abs/{arxiv_id}")
                print(f"   Semantic Scholar: {paper.get('url')}")
        
        # 保存数据
        result = {
            'author': author,
            'author_id': author_id,
            'publications': publications,
            'total_papers': len(papers_data.get('data', []))
        }
        
        with open('saining_xie_papers.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"\n所有论文信息已保存到 saining_xie_papers.json")
        
        # 生成下载列表
        arxiv_links = [p for p in publications if p.get('arxiv_id')]
        print(f"\n找到 {len(arxiv_links)} arXiv论文")
        
        with open('arxiv_download_list.txt', 'w') as f:
            for paper in arxiv_links:
                arxiv_url = f"https://arxiv.org/pdf/{paper['arxiv_id']}"
                f.write(f"{arxiv_url}\t{paper['title']}\n")
        
        print("arXiv PDF下载链接已保存到 arxiv_download_list.txt")
        
    else:
        print("未找到作者信息")
        
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()