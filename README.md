# kaiming-he science taste

一个 agent skill：用何恺明的科研方法论与品味（research taste）辅助机器学习 / 计算机视觉 / 深度学习的研究决策。

核心是一套"优化视角"——把做科研当成一个优化问题：先定义正确的 Loss Function（理解问题本身，而非论文数 / 影响因子），再在探索中获取真实 gradient，靠简洁、数理严谨与系统演进收敛出 taste。

## 何时触发

纠结"该做什么方向"、判断"这个 idea 好不好"、设计实验与消融、读论文判断真伪、对着 benchmark 刷点感到迷茫，或在设计网络架构时。

## 结构

```
kaiming-he-skill/
├── SKILL.md                  # skill 主体
└── references/
    ├── methodology.md        # 优化视角方法论
    ├── research-style.md     # 何恺明研究风格（以其论文为证）
    ├── anti-patterns.md      # 反模式与护栏
    ├── quotes.md             # 引述（注明口径）
    └── sources.md            # 来源与语料说明
kaiming_he_papers/            # 语料清单（papers_list.json，PDF 不入库）
```

## 衍生说明（致谢）

本 skill 是在第三方开源 skill **K-Dense-AI / mimeographs 的 kaiming-he**（<https://lobehub.com/zh/skills/k-dense-ai-mimeographs-kaiming-he>）基础上的**升级修改版本**，并非从零原创。

相比原版的主要改动：

- **重写语料根基**：原版以人物百科 / 履历 / 第三方博客复述为主要来源；本版剔除这些非一手材料，改以谢赛宁访谈、涌现《如何训练你的 Research Taste》的解读框架，以及何恺明本人约 76 篇论文语料为据（详见 `kaiming-he-skill/references/sources.md`）。
- **重构为"优化视角"方法论**：围绕 Loss Function → Gradient → SGD → Taste 这套框架重新组织，而非罗列生平与成果。
- **新增反模式与护栏**：加入"判作品不判署名"等反权威护栏，并澄清"简洁"的作用域。

## 来源口径

"优化视角"是谢赛宁访谈观察 + 涌现《如何训练你的 Research Taste》提出的解读框架，并非何恺明本人原话；研究风格部分直接以其公开论文为证。引用时请保持这一区分，详见 `kaiming-he-skill/references/sources.md`。
