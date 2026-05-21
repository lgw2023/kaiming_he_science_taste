#!/usr/bin/env python3
import requests
import json
import time
import xml.etree.ElementTree as ET

headers = {'User-Agent': 'Mozilla/5.0 (compatible; Research Bot)'}

print("=" * 60)
print("方法1: DBLP API")
print("=" * 60)

try:
    # DBLP search for author
    search_url = "https://dblp.org/search/author/api"
    params = {'q': 'Saining Xie', 'format': 'json'}
    
    response = requests.get(search_url, headers=headers, params=params, timeout=30)
    data = response.json()
    
    if 'hit' in data and len(data['hit']) > 0:
        author_url = data['hit'][0]['info']['url']
        author_pid = data['hit'][0]['info']['url'].split('/')[-1]
        
        print(f"\n找到作者: {data['hit'][0]['info']['text']}")
        print(f"DBLP URL: {author_url}")
        print(f"PID: {author_pid}")
        
        # Get author's publications
        pubs_url = f"https://dblp.org/pid/{author_pid}.json"
        response = requests.get(pubs_url, headers=headers, timeout=30)
        pubs_data = response.json()
        
        dblp_papers = []
        for pub in pubs_data.get('publications', []):
            title = pub.get('title', 'N/A')
            year = pub.get('year', 'N/A')
            authors = pub.get('authors', [])
            authors_str = ', '.join([a.get('name', '') for a in authors[:5]])
            venue = pub.get('venue', 'N/A')
            type_pub = pub.get('type', 'N/A')
            doi = pub.get('doi', None)
            url_pub = pub.get('url', None)
            
            dblp_papers.append({
                'title': title,
                'year': year,
                'authors': authors_str,
                'venue': venue,
                'type': type_pub,
                'doi': doi,
                'url': url_pub,
                'source': 'DBLP'
            })
        
        print(f"\nDBLP论文总数: {len(dblp_papers)}")
        
        for i, paper in enumerate(dblp_papers[:10], 1):
            print(f"{i}. {paper['title']} ({paper['year']})")
        
        with open('dblp_papers.json', 'w', encoding='utf-8') as f:
            json.dump({
                'author': data['hit'][0]['info'],
                'pid': author_pid,
                'total': len(dblp_papers),
                'papers': dblp_papers
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\nDBLP数据已保存到 dblp_papers.json")
        
except Exception as e:
    print(f"DBLP错误: {e}")

print("\n" + "=" * 60)
print("方法2: OpenAlex API")
print("=" * 60)

try:
    # OpenAlex search
    search_url = "https://api.openalex.org/authors"
    params = {'search': 'Saining Xie'}
    
    response = requests.get(search_url, headers=headers, params=params, timeout=30)
    data = response.json()
    
    if 'results' in data and len(data['results']) > 0:
        author = data['results'][0]
        author_id = author['id']
        
        print(f"\n找到作者: {author['display_name']}")
        print(f"OpenAlex ID: {author_id}")
        print(f"works_count: {author.get('works_count', 'N/A')}")
        print(f"cited_by_count: {author.get('cited_by_count', 'N/A')}")
        print(f"h_index: {author.get('summary_stats', {}).get('h_index', 'N/A')}")
        
        # Get works
        works_url = "https://api.openalex.org/works"
        params = {
            'filter': f'author.id:{author_id.split("/")[-1]}',
            'per_page': 200,
            'sort': 'cited_by_count:desc'
        }
        
        all_works = []
        page = 1
        
        while True:
            params['page'] = page
            response = requests.get(works_url, headers=headers, params=params, timeout=30)
            works_data = response.json()
            
            if 'results' not in works_data or len(works_data['results']) == 0:
                break
            
            all_works.extend(works_data['results'])
            
            if len(works_data['results']) < 200:
                break
            
            page += 1
            time.sleep(0.5)
        
        openalex_papers = []
        for work in all_works:
            title = work.get('title', 'N/A')
            year = work.get('publication_year', 'N/A')
            authors = work.get('authorships', [])
            authors_str = ', '.join([a['author']['display_name'] for a in authors[:5]])
            cited_by = work.get('cited_by_count', 0)
            venue = work.get('primary_location', {}).get('source', {}).get('display_name', 'N/A')
            doi = work.get('doi', None)
            
            # Check for arXiv
            locations = work.get('locations', [])
            arxiv_id = None
            for loc in locations:
                if loc.get('source', {}).get('display_name') == 'arXiv':
                    arxiv_url = loc.get('landing_page_url', '')
                    if 'arxiv.org/abs/' in arxiv_url:
                        arxiv_id = arxiv_url.split('/abs/')[-1]
            
            openalex_papers.append({
                'title': title,
                'year': year,
                'authors': authors_str,
                'citations': cited_by,
                'venue': venue,
                'doi': doi,
                'arxiv_id': arxiv_id,
                'source': 'OpenAlex'
            })
        
        print(f"\nOpenAlex论文总数: {len(openalex_papers)}")
        
        for i, paper in enumerate(openalex_papers[:10], 1):
            print(f"{i}. {paper['title']} ({paper['year']}) - {paper['citations']} citations")
        
        with open('openalex_papers.json', 'w', encoding='utf-8') as f:
            json.dump({
                'author': author,
                'total': len(openalex_papers),
                'papers': openalex_papers
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\nOpenAlex数据已保存到 openalex_papers.json")
        
except Exception as e:
    print(f"OpenAlex错误: {e}")

print("\n" + "=" * 60)
print("方法3: arXiv API (直接查询)")
print("=" * 60)

try:
    import urllib.parse
    
    # arXiv API query
    query = urllib.parse.quote('au:"Xie Saining" OR au:"Saining Xie"')
    arxiv_url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=100"
    
    response = requests.get(arxiv_url, headers=headers, timeout=30)
    
    # Parse XML
    root = ET.fromstring(response.content)
    
    arxiv_papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        
        authors = []
        for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
            name = author.find('{http://www.w3.org/2005/Atom}name').text
            authors.append(name)
        
        authors_str = ', '.join(authors[:5])
        
        # Get arXiv ID
        id_url = entry.find('{http://www.w3.org/2005/Atom}id').text
        arxiv_id = id_url.split('/abs/')[-1]
        
        # Get year from published date
        published = entry.find('{http://www.w3.org/2005/Atom}published').text
        year = published[:4]
        
        # Get summary
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
        
        arxiv_papers.append({
            'title': title,
            'year': year,
            'authors': authors_str,
            'arxiv_id': arxiv_id,
            'summary': summary[:200] + '...' if len(summary) > 200 else summary,
            'source': 'arXiv'
        })
    
    print(f"\narXiv论文总数: {len(arxiv_papers)}")
    
    for i, paper in enumerate(arxiv_papers[:10], 1):
        print(f"{i}. {paper['title']} ({paper['year']})")
        print(f"   arXiv: {paper['arxiv_id']}")
    
    with open('arxiv_papers.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total': len(arxiv_papers),
            'papers': arxiv_papers
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\narXiv数据已保存到 arxiv_papers.json")
    
except Exception as e:
    print(f"arXiv错误: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("合并所有数据源")
print("=" * 60)

# Merge all papers
all_papers = []

# Load from files
try:
    with open('dblp_papers.json', 'r', encoding='utf-8') as f:
        dblp = json.load(f)
        all_papers.extend(dblp.get('papers', []))
    print(f"DBLP: {len(dblp.get('papers', []))} papers")
except:
    pass

try:
    with open('openalex_papers.json', 'r', encoding='utf-8') as f:
        openalex = json.load(f)
        all_papers.extend(openalex.get('papers', []))
    print(f"OpenAlex: {len(openalex.get('papers', []))} papers")
except:
    pass

try:
    with open('arxiv_papers.json', 'r', encoding='utf-8') as f:
        arxiv = json.load(f)
        all_papers.extend(arxiv.get('papers', []))
    print(f"arXiv: {len(arxiv.get('papers', []))} papers")
except:
    pass

# Deduplicate by title similarity
unique_papers = []
seen_titles = set()

for paper in all_papers:
    title_lower = paper['title'].lower().strip()
    # Simple dedup
    if title_lower not in seen_titles:
        seen_titles.add(title_lower)
        unique_papers.append(paper)

# Sort by citations (OpenAlex) or year
unique_papers.sort(key=lambda x: (x.get('citations', 0) or 0, x.get('year', 0) or 0), reverse=True)

print(f"\n去重后总数: {len(unique_papers)} papers")

# Save merged data
with open('saining_xie_all_papers.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total': len(unique_papers),
        'papers': unique_papers,
        'sources': ['DBLP', 'OpenAlex', 'arXiv', 'Semantic Scholar']
    }, f, ensure_ascii=False, indent=2)

print(f"\n所有数据已合并保存到 saining_xie_all_papers.json")

# Generate download list for all arXiv papers
arxiv_download_list = []
for paper in unique_papers:
    if paper.get('arxiv_id'):
        arxiv_download_list.append({
            'arxiv_id': paper['arxiv_id'],
            'title': paper['title'],
            'year': paper['year']
        })

print(f"\n找到 {len(arxiv_download_list)} arXiv论文可下载")

with open('all_arxiv_download_list.txt', 'w') as f:
    for paper in arxiv_download_list:
        f.write(f"https://arxiv.org/pdf/{paper['arxiv_id']}\t{paper['title']}\n")

print(f"所有arXiv下载链接已保存到 all_arxiv_download_list.txt")