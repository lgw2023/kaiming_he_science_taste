#!/usr/bin/env python3
import requests
import json
import xml.etree.ElementTree as ET
import time

headers = {'User-Agent': 'Mozilla/5.0 (compatible; Research Bot)'}

print("=" * 70)
print("从DBLP获取完整论文列表")
print("=" * 70)

try:
    # Get DBLP XML
    dblp_url = "https://dblp.org/pid/126/0960.xml"
    response = requests.get(dblp_url, headers=headers, timeout=30)
    
    root = ET.fromstring(response.content)
    
    dblp_papers = []
    for r in root.findall('r'):
        # Can be inproceedings, article, etc.
        for child in r:
            if child.tag in ['inproceedings', 'article', 'incollection', 'book']:
                title_elem = child.find('title')
                title = title_elem.text if title_elem is not None else 'N/A'
                
                year_elem = child.find('year')
                year = year_elem.text if year_elem is not None else 'N/A'
                
                authors = []
                for author_elem in child.findall('author'):
                    if author_elem.text:
                        authors.append(author_elem.text)
                authors_str = ', '.join(authors[:5])
                
                venue_elem = child.find('booktitle') or child.find('journal')
                venue = venue_elem.text if venue_elem is not None else 'N/A'
                
                ee_elem = child.find('ee')
                url = ee_elem.text if ee_elem is not None else None
                
                doi = None
                if url and 'doi.org' in url:
                    doi = url.split('doi.org/')[-1]
                
                dblp_papers.append({
                    'title': title,
                    'year': year,
                    'authors': authors_str,
                    'venue': venue,
                    'type': child.tag,
                    'url': url,
                    'doi': doi,
                    'source': 'DBLP'
                })
    
    print(f"\nDBLP论文总数: {len(dblp_papers)}")
    
    for i, paper in enumerate(dblp_papers[:15], 1):
        print(f"{i}. {paper['title']} ({paper['year']})")
        print(f"   Venue: {paper['venue']}")
    
    with open('dblp_full_papers.json', 'w', encoding='utf-8') as f:
        json.dump({
            'author': 'Saining Xie',
            'pid': '126/0960',
            'total': len(dblp_papers),
            'papers': dblp_papers
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\nDBLP完整数据已保存到 dblp_full_papers.json")
    
except Exception as e:
    print(f"DBLP错误: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("从OpenAlex获取完整论文列表")
print("=" * 70)

try:
    # OpenAlex author ID
    author_id = "A5102416863"
    
    print(f"\n作者ID: {author_id}")
    
    # Get works with pagination
    works_url = "https://api.openalex.org/works"
    
    all_works = []
    cursor = "*"
    
    while cursor:
        params = {
            'filter': f'author.id:{author_id}',
            'per_page': 200,
            'cursor': cursor
        }
        
        response = requests.get(works_url, headers=headers, params=params, timeout=30)
        data = response.json()
        
        if 'results' in data:
            all_works.extend(data['results'])
            print(f"已获取 {len(all_works)} 篇论文...")
        
        # Get next cursor
        if 'meta' in data and 'next_cursor' in data['meta']:
            cursor = data['meta']['next_cursor']
        else:
            break
        
        time.sleep(0.3)
    
    print(f"\nOpenAlex论文总数: {len(all_works)}")
    
    openalex_papers = []
    for work in all_works:
        title = work.get('title', 'N/A')
        year = work.get('publication_year', 'N/A')
        
        authors = []
        for authorship in work.get('authorships', []):
            author_name = authorship.get('author', {}).get('display_name', '')
            if author_name:
                authors.append(author_name)
        authors_str = ', '.join(authors[:5])
        
        cited_by = work.get('cited_by_count', 0)
        
        venue = 'N/A'
        location = work.get('primary_location')
        if location:
            source = location.get('source')
            if source:
                venue = source.get('display_name', 'N/A')
        
        doi = work.get('doi')
        
        # Check for arXiv
        arxiv_id = None
        for loc in work.get('locations', []):
            source = loc.get('source')
            if source and source.get('display_name') == 'arXiv e-Print archive':
                landing_page = loc.get('landing_page_url', '')
                if 'arxiv.org/abs/' in landing_page:
                    arxiv_id = landing_page.split('/abs/')[-1]
        
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
    
    # Sort by citations
    openalex_papers.sort(key=lambda x: x.get('citations', 0), reverse=True)
    
    for i, paper in enumerate(openalex_papers[:15], 1):
        print(f"{i}. {paper['title']} ({paper['year']})")
        print(f"   引用数: {paper['citations']}, Venue: {paper['venue']}")
        if paper.get('arxiv_id'):
            print(f"   arXiv: {paper['arxiv_id']}")
    
    with open('openalex_full_papers.json', 'w', encoding='utf-8') as f:
        json.dump({
            'author_id': author_id,
            'total': len(openalex_papers),
            'papers': openalex_papers
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\nOpenAlex完整数据已保存到 openalex_full_papers.json")
    
except Exception as e:
    print(f"OpenAlex错误: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("合并所有数据源")
print("=" * 70)

all_papers = []

# Load DBLP
try:
    with open('dblp_full_papers.json', 'r', encoding='utf-8') as f:
        dblp = json.load(f)
        all_papers.extend(dblp.get('papers', []))
        print(f"DBLP: {len(dblp.get('papers', []))} papers")
except:
    pass

# Load OpenAlex
try:
    with open('openalex_full_papers.json', 'r', encoding='utf-8') as f:
        openalex = json.load(f)
        all_papers.extend(openalex.get('papers', []))
        print(f"OpenAlex: {len(openalex.get('papers', []))} papers")
except:
    pass

# Load arXiv
try:
    with open('arxiv_papers.json', 'r', encoding='utf-8') as f:
        arxiv = json.load(f)
        all_papers.extend(arxiv.get('papers', []))
        print(f"arXiv: {len(arxiv.get('papers', []))} papers")
except:
    pass

# Deduplicate
unique_papers = []
seen_titles = {}

for paper in all_papers:
    title_key = paper['title'].lower().strip()
    
    if title_key not in seen_titles:
        seen_titles[title_key] = paper
        unique_papers.append(paper)
    else:
        # Merge data from different sources
        existing = seen_titles[title_key]
        if paper.get('citations') and not existing.get('citations'):
            existing['citations'] = paper.get('citations')
        if paper.get('arxiv_id') and not existing.get('arxiv_id'):
            existing['arxiv_id'] = paper.get('arxiv_id')
        if paper.get('doi') and not existing.get('doi'):
            existing['doi'] = paper.get('doi')

# Sort by citations
unique_papers.sort(key=lambda x: (x.get('citations', 0) or 0, int(x.get('year', 0) or 0)), reverse=True)

print(f"\n去重后总数: {len(unique_papers)} 篇论文")

# Save merged
with open('saining_xie_complete_papers.json', 'w', encoding='utf-8') as f:
    json.dump({
        'author': 'Saining Xie',
        'total': len(unique_papers),
        'papers': unique_papers,
        'sources': ['DBLP (144)', 'OpenAlex (122)', 'arXiv (83)']
    }, f, ensure_ascii=False, indent=2)

print(f"\n所有数据已合并保存到 saining_xie_complete_papers.json")

# Statistics
venues = {}
years = {}
for p in unique_papers:
    v = p.get('venue', 'Unknown')
    venues[v] = venues.get(v, 0) + 1
    y = p.get('year', 'Unknown')
    years[y] = years.get(y, 0) + 1

print("\n按会议/期刊统计 (Top 10):")
for v, c in sorted(venues.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  {v}: {c} papers")

print("\n按年份统计:")
for y, c in sorted(years.items(), reverse=True)[:10]:
    print(f"  {y}: {c} papers")

# Create complete arXiv download list
arxiv_download_list = []
for paper in unique_papers:
    if paper.get('arxiv_id'):
        arxiv_download_list.append({
            'arxiv_id': paper['arxiv_id'],
            'title': paper['title'],
            'year': paper['year'],
            'citations': paper.get('citations', 0)
        })

print(f"\n可下载的arXiv论文: {len(arxiv_download_list)} 篇")

with open('complete_arxiv_download_list.txt', 'w') as f:
    f.write("# 谢赛宁(Saining Xie) arXiv论文下载列表\n")
    f.write("# 格式: URL\t标题\t年份\t引用数\n\n")
    for paper in arxiv_download_list:
        pdf_url = f"https://arxiv.org/pdf/{paper['arxiv_id']}"
        f.write(f"{pdf_url}\t{paper['title']}\t{paper['year']}\t{paper.get('citations', 0)}\n")

print(f"完整下载列表已保存到 complete_arxiv_download_list.txt")

# Create top papers list
print("\n" + "=" * 70)
print("Top 20 高引用论文")
print("=" * 70)

for i, paper in enumerate(unique_papers[:20], 1):
    citations = paper.get('citations', 0) or 'N/A'
    print(f"{i}. {paper['title']} ({paper['year']})")
    print(f"   引用数: {citations}")
    print(f"   Venue: {paper.get('venue', 'N/A')}")
    if paper.get('arxiv_id'):
        print(f"   arXiv: {paper['arxiv_id']}")
    print()