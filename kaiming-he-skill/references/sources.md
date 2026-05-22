# 语料来源

> **衍生与致谢**：本 skill 是第三方开源 skill **K-Dense-AI / mimeographs 的 kaiming-he**（<https://lobehub.com/zh/skills/k-dense-ai-mimeographs-kaiming-he>）的**升级修改版本**。原版以人物百科 / 履历 / 第三方复述为主要语料（被剔除部分见下文第三节）；本版完整重写，改以下列一手来源与何恺明本人作品为据。

本 skill 的内容来自下面这些来源。分两层：**方法论一手来源**（决定"怎么做研究"那部分）和**何恺明本人作品**（决定"战绩为证"那部分）。本地路径相对项目根目录 `kaiming_he_science_taste/`。

---

## 一、方法论一手来源

| 来源 | 说明 | 本地文件 |
|------|------|---------|
| 谢赛宁 × 张小珺 七小时访谈（2026 春节，纽约） | 方法论的原始出处。谢赛宁对何恺明工作方式的第一手观察。 | —（音频/播客） |
| 涌现 Voke Flow《如何训练你的 Research Taste？从何恺明的方法论谈起》（JigmeDorje，2026-05-14） | 提出"优化视角"解读框架（Loss Function→Gradient→SGD→Taste）。 | `如何训练你的Research_Taste_从何恺明的方法论谈起.md` |
| 本项目综述《何恺明科研方法论：如何训练你的 Research Taste》 | 综合访谈、微信文章与论文核对后的方法论总结，本 skill 的主蓝本。 | `何恺明科研方法论：如何训练你的Research_Taste.md` |
| 30 篇微信公众号文章合集 | 讲座回顾、获奖感言、人物报道、论文解读等佐证材料。 | `搜索结果_何恺明方法论相关文章.md` |

> 口径提醒：上述"优化视角"是谢赛宁的观察 + 涌现作者的解读框架，不是何恺明本人提出的理论。归因细节见 `methodology.md` 顶部与 `quotes.md`。

---

## 二、何恺明本人作品（战绩为证）

### 论文语料
本地 `kaiming_he_papers/` 收录其约 76 篇论文 PDF（清单见 `kaiming_he_papers/papers_list.json`）。`research-style.md` 中所有 arXiv ID 均对齐此语料。代表作：

- **架构/归一化**：PReLU·He 初始化 (1502.01852)、ResNet (1512.03385)、Identity Mappings/ResNet v2 (1603.05027)、ResNeXt (1611.05431, 一作谢赛宁)、FPN (1612.03144)、Group Norm (1803.08494)、Transformers without Normalization (2503.10622)
- **检测/分割**：SPPnet (1406.4729)、Faster R-CNN (1506.01497)、Mask R-CNN (1703.06870)、Focal Loss/RetinaNet (1708.02002)、PointRend (2003.13678)
- **自监督/生成**：Non-local (1711.07971)、Rethinking ImageNet Pre-training (1811.08883)、MoCo (1911.05722)、SimSiam (2011.10566)、MAE (2111.06377)、ViTDet (2203.16527)、l-DAE (2401.14404)、Mean Flows (2505.13447)、Fractal Generative Models (2502.17437)、Image Generators are Generalist Vision Learners (2604.20329)
- **工程实用**：Accurate, Large Minibatch SGD (1706.02677)

### 公开表达（讲座/访谈）
- MIT News 专访《Creating a common language》(news.mit.edu, 2025) —— AI 作为科学通用语言。
- 讲座《Towards End-to-End Generative Modeling》、《Deep Learning Day: Generative Modeling》、NeurIPS 2024 keynote —— 识别/生成对称、生成模型作为通用求解器、端到端主张（讲座内容在本 skill 中按"大意转述"处理）。

---

## 三、相比原版被剔除的来源

原第三方 skill 的语料里混入了大量非一手、低信息量来源，已剔除，不再作为"何恺明思想"的依据：

- 人物词条/百科：Wikipedia、百度百科、Grokipedia、HandWiki
- 简介/索引页：Google Scholar、GitHub profile、MIT/CSAIL/Princeton 介绍页、ACM/DBLP、X(Twitter)、学生个人主页
- 第三方教程：Medium、Towards Data Science、plainenglish 等复述 He 初始化公式的博客

理由：这些页面要么是"被引数/履历"，要么是他人复述，无法支撑关于何恺明**思想与方法论**的论断。本 skill 只以一手访谈、他本人作品、以及经核对的项目综述为据。
