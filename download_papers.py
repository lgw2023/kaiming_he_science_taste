#!/usr/bin/env python3
import requests
import os
import re
import time
from urllib.parse import unquote

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

download_dir = 'saining_xie_papers'
os.makedirs(download_dir, exist_ok=True)

print(f"论文将下载到目录: {download_dir}")

arxiv_links = [
    ('2504.13129', 'Science-T2I: Addressing Scientific Illusions in Image Synthesis'),
    ('2512.15699', 'FrontierCS: Evolving Challenges for Evolving Intelligence'),
    ('2506.17450', 'BlenderFusion: 3D-Grounded Visual Editing and Generative Compositing'),
    ('2512.16922', 'Next-Embedding Prediction Makes Strong Vision Learners'),
    ('2501.09732', 'Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps'),
    ('2506.11928', 'LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?'),
    ('2406.18533', 'On Scaling Up 3D Gaussian Splatting Training'),
    ('2410.03051', 'AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark'),
    ('2409.19429', 'Fast Encoding and Decoding for Implicit Video Representation'),
]

success_count = 0
failed_count = 0

for arxiv_id, title in arxiv_links:
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    
    # 清理标题用于文件名
    clean_title = re.sub(r'[^\w\s-]', '', title)
    clean_title = re.sub(r'[-\s]+', '-', clean_title)
    filename = f"{arxiv_id}_{clean_title[:50]}.pdf"
    filepath = os.path.join(download_dir, filename)
    
    print(f"\n正在下载: {title}")
    print(f"  arXiv ID: {arxiv_id}")
    print(f"  URL: {pdf_url}")
    
    try:
        response = requests.get(pdf_url, headers=headers, timeout=60, stream=True)
        
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            print(f"  ✓ 下载成功: {filename}")
            success_count += 1
        else:
            print(f"  ✗ 下载失败: HTTP {response.status_code}")
            failed_count += 1
        
        time.sleep(2)
        
    except Exception as e:
        print(f"  ✗ 下载失败: {e}")
        failed_count += 1
        time.sleep(2)

print(f"\n下载完成!")
print(f"  成功: {success_count} 篇")
print(f"  失败: {failed_count} 篇")
print(f"  文件保存在: {download_dir}/")

if success_count > 0:
    print(f"\n下载的文件列表:")
    for f in os.listdir(download_dir):
        if f.endswith('.pdf'):
            size_mb = os.path.getsize(os.path.join(download_dir, f)) / (1024 * 1024)
            print(f"  {f} ({size_mb:.2f} MB)")