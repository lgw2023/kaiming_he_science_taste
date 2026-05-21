#!/usr/bin/env python3
import json
import os
from datetime import datetime

# Load all data
with open('saining_xie_complete_papers.json', 'r') as f:
    papers_data = json.load(f)

with open('download_report.json', 'r') as f:
    download_data = json.load(f)

# Generate markdown report
report = f"""# 谢赛宁(Saining Xie)学术研究论文汇总报告

生成日期: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

---

## 📊 总览

| 统计项 | 数量 |
|--------|------|
| **总论文数** | {papers_data['total']} 篇 |
| **arXiv论文** | {download_data['arxiv_papers']} 篇 |
| **已下载PDF** | {download_data['downloaded']} 篇 |
| **总下载大小** | {download_data['total_size_mb']:.2f} MB |

---

## 🎯 数据来源

1. **DBLP** - 143篇论文（计算机科学权威数据库）
2. **OpenAlex** - 122篇论文（开放学术图谱，包含引用数）
3. **arXiv** - 83篇预印本（直接API查询）

---

## 🏆 Top 30 高引用论文

"""

# Add top papers
papers_with_citations = [p for p in papers_data['papers'] if p.get('citations')]
papers_with_citations.sort(key=lambda x: x['citations'], reverse=True)

for i, p in enumerate(papers_with_citations[:30], 1):
    arxiv_link = f"https://arxiv.org/abs/{p['arxiv_id']}" if p.get('arxiv_id') else ''
    doi_link = f"https://doi.org/{p['doi']}" if p.get('doi') else ''
    
    report += f"""### {i}. {p['title']}

- **年份**: {p['year']}
- **引用数**: {p['citations']}
- **作者**: {p.get('authors', 'N/A')}
- **发表地**: {p.get('venue', 'N/A')}
"""

    if arxiv_link:
        report += f"- **arXiv**: [{p['arxiv_id']}]({arxiv_link})\n"
    if doi_link:
        report += f"- **DOI**: [链接]({doi_link})\n"
    
    report += "\n"

# Year statistics
report += """---

## 📅 年份分布

"""

years = {}
for p in papers_data['papers']:
    y = str(p.get('year', 'Unknown'))
    years[y] = years.get(y, 0) + 1

for y, c in sorted(years.items(), reverse=True)[:15]:
    report += f"| {y} | {c} 篇 |\n"

# Venue statistics
report += """---

## 📚 主要发表会议/期刊 (Top 15)

"""

venues = {}
for p in papers_data['papers']:
    v = p.get('venue', 'Unknown')
    if v != 'Unknown' and v != 'N/A' and not v.startswith('CoRR'):
        venues[v] = venues.get(v, 0) + 1

for v, c in sorted(venues.items(), key=lambda x: x[1], reverse=True)[:15]:
    report += f"| {v[:50]} | {c} 篇 |\n"

# Downloaded files list
report += """---

## 📥 已下载的PDF文件清单

"""

downloaded_papers = download_data['papers']
downloaded_papers.sort(key=lambda x: x.get('citations', 0), reverse=True)

for i, d in enumerate(downloaded_papers[:50], 1):
    if d.get('title'):
        report += f"{i}. `{d['filename']}` ({d['size']/(1024*1024):.2f}MB)\n"
        report += f"   - {d['title'][:80]}\n"
        if d.get('citations'):
            report += f"   - arXiv: {d['arxiv_id']}, 引用数: {d['citations']}\n"
        report += "\n"

# Research topics
report += """---

## 🔬 主要研究领域

根据论文标题分析，谢赛宁的主要研究方向包括：

1. **深度学习架构** - ResNeXt, ConvNeXt等经典网络架构
2. **自监督学习** - MoCo, MAE等自监督方法
3. **视觉表示学习** - 视觉特征提取与表征学习
4. **3D视觉** - 点云理解、三维场景理解
5. **视频理解** - 时空特征学习
6. **扩散模型** - DiT等生成模型
7. **神经架构搜索** - NAS相关研究
8. **边缘检测** - HED等经典工作

---

## 📖 经典论文简介

### MoCo (Momentum Contrast)
- **引用数**: 11,911
- 开创性的自监督视觉表示学习方法，为后续对比学习研究奠定了基础

### ResNeXt
- **引用数**: 11,789
- 改进了ResNet架构，引入分组卷积，在保持准确率的同时降低计算成本

### ConvNeXt
- **引用数**: 6,858
- 将现代Transformer设计思想融入卷积网络，证明纯CNN架构仍有巨大潜力

### HED (Holistically-Nested Edge Detection)
- **引用数**: 3,115
- 深度监督的经典应用，提出多层次边缘检测方法

---

## 📁 文件位置

- **论文数据库**: `saining_xie_complete_papers.json`
- **PDF文件**: `saining_xie_all_papers/` (77篇) + `saining_xie_papers/` (9篇)
- **下载报告**: `download_report.json`
- **本报告**: `README.md`

---

## 🔗 相关链接

- [Google Scholar](https://scholar.google.com/citations?user=Y2GtJkAAAAAJ)
- [DBLP](https://dblp.org/pid/126/0960)
- [OpenAlex](https://openalex.org/A5102416863)

---

*本报告由自动化脚本生成，数据来源于DBLP、OpenAlex和arXiv API*
"""

# Save report
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(report)

print("完整报告已生成: README.md")
print(f"报告长度: {len(report)} 字符")
print()

# Also create a simple text list for easy reference
with open('paper_list.txt', 'w', encoding='utf-8') as f:
    f.write(f"谢赛宁(Saining Xie)论文列表 ({len(papers_data['papers'])}篇)\n")
    f.write("=" * 70 + "\n\n")
    
    papers_sorted = sorted(papers_data['papers'], 
                          key=lambda x: (x.get('citations', 0) or 0, int(x.get('year', 0) or 0)), 
                          reverse=True)
    
    for i, p in enumerate(papers_sorted, 1):
        f.write(f"{i}. {p['title']}\n")
        f.write(f"   年份: {p['year']}, 引用数: {p.get('citations', 'N/A')}\n")
        if p.get('arxiv_id'):
            f.write(f"   arXiv: https://arxiv.org/abs/{p['arxiv_id']}\n")
        f.write("\n")

print("论文列表已生成: paper_list.txt")