#!/usr/bin/env python3
import requests
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
}

download_dir = 'saining_xie_all_papers'
os.makedirs(download_dir, exist_ok=True)

print("=" * 70)
print("下载谢赛宁(Saining Xie)的所有arXiv论文")
print("=" * 70)

# Load complete papers data
with open('saining_xie_complete_papers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

papers = data['papers']

# Filter papers with arXiv ID
arxiv_papers = [p for p in papers if p.get('arxiv_id')]
arxiv_papers.sort(key=lambda x: x.get('citations', 0) or 0, reverse=True)

print(f"\n总论文数: {len(papers)}")
print(f"arXiv论文数: {len(arxiv_papers)}")

# Check already downloaded
already_downloaded = []
to_download = []

for paper in arxiv_papers:
    arxiv_id = paper['arxiv_id']
    clean_title = re.sub(r'[^\w\s-]', '', paper['title'])
    clean_title = re.sub(r'[-\s]+', '-', clean_title)
    filename = f"{arxiv_id}_{clean_title[:50]}.pdf"
    filepath = os.path.join(download_dir, filename)
    
    if os.path.exists(filepath):
        already_downloaded.append({
            'paper': paper,
            'filename': filename,
            'size': os.path.getsize(filepath)
        })
    else:
        to_download.append({
            'paper': paper,
            'filename': filename,
            'filepath': filepath
        })

print(f"\n已下载: {len(already_downloaded)} 篇")
print(f"待下载: {len(to_download)} 篇")

def download_paper(item):
    paper = item['paper']
    filepath = item['filepath']
    arxiv_id = paper['arxiv_id']
    
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    
    try:
        response = requests.get(pdf_url, headers=headers, timeout=60, stream=True)
        
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            size_mb = os.path.getsize(filepath) / (1024 * 1024)
            return {
                'success': True,
                'arxiv_id': arxiv_id,
                'title': paper['title'],
                'filename': os.path.basename(filepath),
                'size_mb': size_mb,
                'citations': paper.get('citations', 0)
            }
        else:
            return {
                'success': False,
                'arxiv_id': arxiv_id,
                'error': f'HTTP {response.status_code}'
            }
    except Exception as e:
        return {
            'success': False,
            'arxiv_id': arxiv_id,
            'error': str(e)
        }

print("\n开始下载...")
print("=" * 70)

success_count = len(already_downloaded)
failed_count = 0
downloaded_papers = []

# Download in parallel (max 5 concurrent)
max_workers = 5
batch_size = 20

for i, item in enumerate(to_download, 1):
    result = download_paper(item)
    
    if result['success']:
        downloaded_papers.append(result)
        success_count += 1
        print(f"[{success_count}/{len(arxiv_papers)}] ✓ {result['title'][:50]}")
        print(f"    arXiv: {result['arxiv_id']}, Size: {result['size_mb']:.2f}MB")
    else:
        failed_count += 1
        print(f"[✗] {item['paper']['title'][:50]}")
        print(f"    Error: {result['error']}")
    
    time.sleep(2)

print("\n" + "=" * 70)
print("下载完成!")
print("=" * 70)

print(f"\n成功下载: {success_count} 篇")
print(f"下载失败: {failed_count} 篇")

# Summary
print("\n已下载的论文:")
print("=" * 70)

all_downloaded = already_downloaded + [{'paper': d, 'filename': d['filename']} for d in downloaded_papers]

for i, item in enumerate(already_downloaded, 1):
    paper = item['paper']
    size_mb = item['size'] / (1024 * 1024)
    citations = paper.get('citations', 0) or 0
    print(f"{i:2}. {paper['title'][:60]}")
    print(f"    arXiv: {paper['arxiv_id']}, 引用数: {citations}, Size: {size_mb:.2f}MB")

for i, item in enumerate(downloaded_papers, len(already_downloaded)+1):
    print(f"{i:2}. {item['title'][:60]}")
    print(f"    arXiv: {item['arxiv_id']}, 引用数: {item['citations']}, Size: {item['size_mb']:.2f}MB")

# Save download summary
summary = {
    'total_papers': len(papers),
    'arxiv_papers': len(arxiv_papers),
    'success': success_count,
    'failed': failed_count,
    'already_downloaded': len(already_downloaded),
    'newly_downloaded': len(downloaded_papers),
    'downloaded_files': [os.path.join(download_dir, d['filename']) for d in already_downloaded] + [d['filepath'] for d in downloaded_papers if d['success']]
}

with open('download_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"\n下载摘要已保存到 download_summary.json")
print(f"所有PDF文件在: {download_dir}/")

# Calculate total size
total_size = sum(item['size'] for item in already_downloaded) + sum(item['size_mb'] * 1024 * 1024 for item in downloaded_papers if item['success'])
print(f"\n总下载大小: {total_size / (1024*1024):.2f} MB ({total_size / (1024*1024*1024):.2f} GB)")