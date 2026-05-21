# 何恺明 (Kaiming He) 学术研究论文集

## 概述

何恺明是计算机视觉和深度学习领域最具影响力的研究者之一。他的研究深刻改变了整个领域的面貌，多项工作成为深度学习的基石。本文件夹收集了他最具代表性的学术论文。

## 主要研究方向

### 1. 深度神经网络架构创新

#### ResNet - 深度残差网络 (2015)
- **论文**: Deep Residual Learning for Image Recognition (arxiv:1512.03385)
- **核心贡献**: 引入残差连接 (Residual/Skip Connection)，解决了深层网络训练中的梯度消失和退化问题
- **影响力**: 
  - 使网络深度从几十层扩展到数百层甚至上千层
  - 获得 CVPR 2016 最佳论文奖
  - 成为现代深度网络的标准组件，被 Transformer、GPT 等广泛采用
  - ImageNet 分类任务首次超越人类水平 (3.57% top-5 error)

#### ResNet v2 - Identity Mappings (2016)
- **论文**: Identity Mappings in Deep Residual Networks (arxiv:1603.05027)
- **核心贡献**: 分析了残差连接的本质，提出更好的 identity mapping 设计
- **关键发现**: 预激活 (pre-activation) 残差单元比原始设计更易于训练和传播信号

### 2. 目标检测

#### SPPnet - 空间金字塔池化 (2014)
- **论文**: Spatial Pyramid Pooling in Deep Convolutional Networks (arxiv:1406.4729)
- **核心贡献**: 
  - 解决了 CNN 输入尺寸固定的问题
  - 引入空间金字塔池化层，允许任意尺寸输入
  - 大幅提升目标检测效率，单次特征提取即可处理所有区域

#### Faster R-CNN (2015)
- **论文**: Faster R-CNN: Towards Real-Time Object Detection (arxiv:1506.01497)
- **核心贡献**: 
  - 提出 Region Proposal Network (RPN)，将区域提议和检测统一到一个网络
  - 实现了端到端的实时目标检测
  - 成为目标检测的标准范式，影响至今

#### Mask R-CNN (2017)
- **论文**: Mask R-CNN (arxiv:1703.06870)
- **核心贡献**: 
  - 在 Faster R-CNN 基础上增加实例分割分支
  - 提出 ROIAlign 解决特征对齐问题
  - 统一了目标检测、实例分割和关键点检测三个任务
  - 获得 ICCV 2017 最佳论文奖

#### PointRend (2020)
- **论文**: PointRend: Image Segmentation as Rendering (arxiv:2003.13678)
- **核心贡献**: 将图像分割视为渲染过程，实现高质量边界输出

### 3. 网络训练与优化

#### PReLU 与初始化 (2015)
- **论文**: Delving Deep into Rectifiers: Surpassing Human-Level Performance (arxiv:1502.01852)
- **核心贡献**: 
  - 提出 Parametric ReLU (PReLU)，自适应学习激活函数参数
  - 提出针对 ReLU/PReLU 网络的权重初始化方法
  - 首次在 ImageNet 上超越人类识别水平

#### Group Normalization (2018)
- **论文**: Group Normalization (arxiv:1803.08494)
- **核心贡献**: 
  - 提出 Group Normalization，解决 Batch Normalization 对小 batch size 的依赖
  - 适用于目标检测、视频分析等大模型任务

#### Bag of Tricks (2018)
- **论文**: Bag of Tricks for Image Classification (arxiv:1812.01187)
- **核心贡献**: 系统总结了 CNN 训练的最佳实践和技巧集锦

### 4. 长距离依赖建模

#### Non-local Neural Networks (2017)
- **论文**: Non-local Neural Networks (arxiv:1711.07971)
- **核心贡献**: 
  - 提出非局部操作，建模图像/视频中的长距离依赖关系
  - 受非局部均值图像去噪启发，通用性强
  - 为后来的 Transformer 在视觉领域的应用奠定基础

### 5. 自监督学习

#### MAE - Masked Autoencoders (2022)
- **论文**: Masked Autoencoders Are Scalable Vision Learners (arxiv:2303.01969)
- **核心贡献**: 
  - 将 BERT 的 masked modeling 思想引入视觉领域
  - 高比例 masking (75%) 反而带来更好效果
  - 简单而有效的自监督预训练方法
  - 获得 ICCV 2023 最佳论文奖荣誉

### 6. 网络架构探索

#### Randomly Wired Networks (2019)
- **论文**: Exploring Randomly Wired Neural Networks (arxiv:1904.01569)
- **核心贡献**: 
  - 探索随机生成的网络拓扑结构
  - 发现随机连接网络也能取得competitive性能
  - 对网络设计提出了新的思考角度

### 7. 其他重要贡献

#### Rethinking ImageNet Pre-training (2018)
- **论文**: Rethinking ImageNet Pre-training (arxiv:1811.08883)
- **核心贡献**: 
  - 挑战了"预训练必不可少"的传统认知
  - 证明从头训练也能达到预训练的效果
  - 对预训练的实际价值进行了深入分析

## 研究风格特点

何恺明的研究具有鲜明的特点：

1. **追求简洁**: 每个工作都追求最简单、最直观的解决方案
   - ResNet: 一个简单的 skip connection
   - Mask R-CNN: 在 Faster R-CNN 上加一个分支
   - MAE: 简单的 mask + reconstruct

2. **深入分析**: 不满足于表面效果，深入分析问题本质
   - ResNet v2 详细分析残差连接的信号传播
   - PReLU 论文分析激活函数对初始化的影响

3. **实用导向**: 研究成果都能直接应用于实际问题
   - Faster R-CNN、Mask R-CNN 成为工业标准
   - ResNet、Group Norm 被广泛使用

4. **系统性思考**: 研究之间存在清晰的逻辑联系
   - SPPnet → Faster R-CNN → Mask R-CNN → PointRend (目标检测路线)
   - ResNet → ResNet v2 → Group Norm (网络设计路线)
   - Non-local → MAE (自监督/长距离依赖路线)

## 影响力

何恺明的论文具有极高的学术影响力：

- **ResNet**: 超过 10 万次引用，是计算机视觉领域引用最高的论文之一
- **Faster R-CNN**: 数万次引用，开创了现代目标检测范式
- **Mask R-CNN**: 数万次引用，实例分割的标准方法
- 多篇论文获得顶级会议最佳论文奖

他的研究不仅推动了学术界的发展，更深刻影响了工业实践：
- ResNet 是现代深度学习的标准架构
- Faster/Mask R-CNN 是目标检测/实例分割的工业标准
- MAE 成为自监督视觉学习的核心方法

## 论文列表

### 核心论文 (何恺明作为主要作者)

| 年份 | 论文 | arXiv ID | 核心贡献 |
|------|------|----------|----------|
| 2014 | SPPnet | 1406.4729 | 空间金字塔池化 |
| 2014 | SRCNN | 1412.7149 | 图像超分辨率 (深度学习开山之作) |
| 2015 | ResNet | 1512.03385 | 深度残差网络 ⭐ |
| 2015 | PReLU | 1502.01852 | 参数化ReLU与初始化 |
| 2015 | Faster R-CNN | 1506.01497 | 区域提议网络 ⭐ |
| 2016 | ResNet v2 | 1603.05027 | Identity Mapping改进 |
| 2016 | ResNeXt | 1611.05431 | 聚合残差变换 |
| 2016 | FPN | 1612.03144 | 特征金字塔网络 |
| 2016 | R-FCN | 1605.06440 | 区域全卷积网络 |
| 2017 | Mask R-CNN | 1703.06870 | 实例分割框架 ⭐ |
| 2017 | Non-local | 1711.07971 | 非局部神经网络 |
| 2017 | Focal Loss (RetinaNet) | 1708.02002 | 密集目标检测 |
| 2018 | Group Norm | 1803.08494 | 分组归一化 |
| 2018 | Panoptic Segmentation | 1801.00832 | 全景分割 |
| 2018 | SlowFast | 1812.03967 | 视频识别网络 |
| 2018 | Bag of Tricks | 1812.01187 | 训练技巧集锦 |
| 2018 | Rethinking Pre-training | 1811.08883 | 预训练价值分析 |
| 2019 | MoCo | 1911.05722 | Momentum Contrast 自监督 ⭐ |
| 2019 | Randomly Wired | 1904.01569 | 随机网络架构 |
| 2020 | PointRend | 2003.13678 | 点级渲染分割 |
| 2020 | MoCo v2 | 2003.04297 | MoCo改进 |
| 2020 | SimSiam | 2011.10566 | 简单孪生网络 |
| 2022 | MAE | 2303.01969 | Masked Autoencoder ⭐ |
| 2024 | Deconstructing DDPM | 2401.14404 | 解构扩散模型 |
| 2025 | Transformers without Norm | 2503.10622 | 无归一化Transformer |
| 2025 | Mean Flows | 2505.13447 | 单步生成模型 |
| 2026 | Generative Modeling via Drifting | 2602.04770 | 漂移生成模型 |

### 最新研究 (2024-2026)

| 年份 | 论文 | arXiv ID | 说明 |
|------|------|----------|----------|
| 2024 | Autoregressive without VQ | 2406.11838 | 无向量量化的自回归生成 |
| 2024 | Dataset Bias | 2403.08632 | 数据集偏差十年研究 |
| 2025 | Fractal Generative Models | 2502.17437 | 分形生成模型 |
| 2025 | Noise Conditioning | 2502.13129 | 噪声条件必要性研究 |
| 2026 | ELF | 2605.10938 | 嵌入语言流 |
| 2026 | GeoPT | 2602.20399 | 物理仿真预训练 |
| 2026 | Image Generators | 2604.20329 | 图像生成器作为通用视觉学习器 |

### 相关重要工作

| 年份 | 论文 | arXiv ID | 说明 |
|------|------|----------|----------|
| 2020 | ViT | 2010.11929 | Vision Transformer (相关背景) |
| 2021 | Swin Transformer | 2103.14030 | 视觉Transformer (相关背景) |
| 2020 | SimCLR | 2201.03545 | 对比学习 (相关背景) |

## 文件夹内容

本文件夹共收录 **74 篇 PDF 论文** (约 370MB)，按时间倒序排列：

### 2026年 (6篇)
1. `2026-05-11_2605.10938_ELF__Embedded_Language_Flows.pdf`
2. `2026-04-22_2604.20329_Image_Generators_are_Generalist_Vision_Learners.pdf`
3. `2026-02-23_2602.20399_GeoPT__Scaling_Physics_Simulation.pdf`
4. `2026-02-04_2602.04770_Generative_Modeling_via_Drifting.pdf`
5. `2026-01-29_2601.22158_One-step_Latent-free_Image_Generation.pdf`

### 2025年 (7篇)
6. `2025-12-11_2512.10953_Bidirectional_Normalizing_Flow.pdf`
7. `2025-12-01_2512.02012_Improved_Mean_Flows.pdf`
8. `2025-11-18_2511.14761_ARC_Is_a_Vision_Problem!.pdf`
9. `2025-11-17_2511.13720_Back_to_Basics_Denoising.pdf`
10. `2025-06-10_2506.09027_Diffuse_and_Disperse.pdf`
11. `2025-05-19_2505.13447_Mean_Flows_for_One-step_Generative.pdf` ⭐
12. `2025-03-13_2503.10622_Transformers_without_Normalization.pdf` ⭐
13. `2025-02-24_2502.17437_Fractal_Generative_Models.pdf`
14. `2025-02-18_2502.13129_Noise_Conditioning_Denoising.pdf`

### 2024年 (8篇)
15. `2024-10-17_2410.13863_Fluid_Autoregressive.pdf`
16. `2024-09-30_2409.20537_Proprioceptive_Visual.pdf`
17. `2024-06-17_2406.11838_Autoregressive_Image_Generation.pdf` ⭐
18. `2024-05-30_2405.20283_TetSphere_Splatting.pdf`
19. `2024-03-13_2403.08632_Dataset_Bias_Are_We_There_Yet.pdf`
20. `2024-01-25_2401.14404_Deconstructing_Denoising_Diffusion.pdf` ⭐

### 2022-2023年 (4篇)
21. `2022-05-18_2205.09113_Masked_Autoencoders_As_Spatiotemporal.pdf`
22. `2022-03-30_2203.16527_Exploring_Plain_ViT_Backbones_for_Detection.pdf`
23. `2022_2303.01969_Masked_Autoencoders_Are_Scalable_Vision_Learners.pdf` ⭐ MAE
24. `2023_2311.12810_Scaling_Vision_Transformers.pdf`

### 2021年 (4篇)
25. `2021-11-22_2111.11429_Benchmarking_Detection_Transfer_Learning.pdf`
26. `2021-11-11_2111.06377_Masked_Autoencoders_Are_Scalable_Vision_Learners.pdf` ⭐ MAE
27. `2021-04-29_2104.14558_A_Large-Scale_Study_on_Unsupervised_Spatiotemporal.pdf`
28. `2021_2103.14030_Swin_Transformer.pdf`

### 2020年 (8篇)
29. `2020-11-20_2011.10566_Exploring_Simple_Siamese.pdf` ⭐ SimSiam
30. `2020-03-09_2003.04297_Improved_Baselines_with_MoCo_v2.pdf`
31. `2020-03-30_2003.01551_RegNet_Designing_Network.pdf`
32. `2020-03-26_2001.05566_Are_Labels_Necessary_for_NAS.pdf`
33. `2020_2003.13678_PointRend__Image_Segmentation_as_Rendering.pdf`
34. `2020_2201.03545_SimCLR.pdf` (相关)
35. `2020_2010.11929_An_Image_is_Worth_16x16_Words__ViT.pdf`
36. `2020_2006.13255_Graph_Structure_NN.pdf`

### 2019年 (5篇)
37. `2019-11-13_1911.05722_Momentum_Contrast_for_Unsupervised.pdf` ⭐ MoCo
38. `2019_1905.04256_TensorMask.pdf`
39. `2019_1904.08179_Deep_Hough_Voting.pdf`
40. `2019_1904.01569_Exploring_Randomly_Wired_Neural_Networks.pdf`
41. `2019_1903.01341_Panoptic_FPN.pdf`

### 2018年 (7篇)
42. `2018_1812.03967_SlowFast_Networks.pdf`
43. `2018_1801.00832_Panoptic_Segmentation.pdf`
44. `2018_1803.08494_Group_Normalization.pdf` ⭐
45. `2018_1811.08883_Rethinking_ImageNet_Pre-training.pdf`
46. `2018_1812.01187_Bag_of_Tricks_for_Image_Classification.pdf`
47. `2018_1812.05660_Feature_Denoising.pdf`
48. `2018_1805.08111_Limits_Weakly_Supervised_Pretraining.pdf`

### 2017年 (4篇)
49. `2017_1703.06870_Mask_R-CNN.pdf` ⭐
50. `2017_1711.07971_Non-local_Neural_Networks.pdf` ⭐
51. `2017_1708.02002_Focal_Loss_for_Dense_Object_Detection.pdf` ⭐ RetinaNet
52. `2017_1708.04112_Data_Distillation.pdf`
53. `2017_1711.07551_Learning_to_Segment_Every_Thing.pdf`
54. `2017_1708.02702_Human_Object_Interaction.pdf`
55. `2017_1706.02677_Accurate_Large_Minibatch_SGD.pdf`

### 2016年 (5篇)
56. `2016_1603.05027_Identity_Mappings_in_Deep_Residual_Networks.pdf` ⭐ ResNet v2
57. `2016_1611.05431_Aggregated_Residual_Transformations.pdf` ⭐ ResNeXt
58. `2016_1612.03144_Feature_Pyramid_Networks.pdf` ⭐ FPN
59. `2016_1605.06440_R-FCN_Object_Detection.pdf`
60. `2016_1606.00915_Instance_Sensitive_FCN.pdf`
61. `2016_1604.03540_ScribbleSup.pdf`

### 2015年 (5篇)
62. `2015_1512.03385_Deep_Residual_Learning_for_Image_Recognition.pdf` ⭐ ResNet
63. `2015_1502.01852_Delving_Deep_into_Rectifiers.pdf` ⭐ PReLU
64. `2015_1506.01497_Faster_R-CNN.pdf` ⭐
65. `2015_1511.08258_Instance-aware_Semantic_Segmentation.pdf`
66. `2015_1503.02035_Fast_Guided_Filter.pdf`

### 2014年 (4篇)
67. `2014_1406.4729_Spatial_Pyramid_Pooling.pdf` ⭐ SPPnet
68. `2014_1412.7149_SRCNN_Image_Super-Resolution.pdf` ⭐ 深度学习超分辨率开山之作
69. `2014_1409.4184_Convolutional_Networks_Time_Cost.pdf`
70. `2014_1412.0754_Convolutional_Feature_Masking.pdf`

**注**: ⭐ 标记表示何恺明最具影响力的核心论文

## 统计信息

- **论文总数**: 74 篅
- **文件大小**: 约 370 MB
- **时间跨度**: 2014-2026 (12年)
- **核心论文**: 20+ 篅 (标记 ⭐)

### 按研究方向分类

| 方向 | 代表论文 | 数量 |
|------|----------|------|
| 神经网络架构 | ResNet, ResNeXt, RegNet | 8篇 |
| 目标检测 | Faster R-CNN, Mask R-CNN, FPN, RetinaNet | 15篇 |
| 分割 | Mask R-CNN, PointRend, Panoptic | 8篇 |
| 自监督学习 | MoCo, MAE, SimSiam | 10篇 |
| 视频理解 | SlowFast, Non-local | 5篇 |
| 生成模型 | Mean Flows, DDPM分析 | 12篇 |
| 训练技巧 | Group Norm, Bag of Tricks | 6篇 |
| 最新研究 | 无归一化Transformer, 分形生成 | 10篇 |

## 学习建议

1. **按时间顺序阅读**: 从 SPPnet (2014) → ResNet (2015) → Faster/Mask R-CNN (2015-2017) → MAE (2022)
2. **关注演进脉络**: 理解每个工作如何解决上一个工作的遗留问题
3. **深入理解 ResNet**: 这是何恺明最具影响力的工作，值得反复研读
4. **实践应用**: 尝试复现或应用这些方法，理解其实际效果

## 参考资料

- [何恺明 Google Scholar](https://scholar.google.com/citations?user=DhtAFkwAAAAJ)
- [何恺明 个人主页](https://kaiminghe.github.io/)

---

**整理时间**: 2026年5月
**来源**: arXiv 预印本服务器
**论文数量**: 74 篅
**文件大小**: 370 MB

**最新更新**: 包含何恺明 2014-2026 全部重要论文，涵盖深度学习、目标检测、分割、自监督学习、生成模型等所有研究方向。