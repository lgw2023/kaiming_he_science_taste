# 语录（按出处与说话人分区）

> 纪律：**verbatim 引号只用于书面可核对的来源**（论文、MIT News 等）。讲座内容因原始字幕为自动转录、易有听写错误，一律标为"大意转述"而非逐字引用。区分"何恺明本人 / 谢赛宁转述 / 学生评价 / 经文与解读框架"。

---

## 一、何恺明本人（书面来源，可逐字核对）

**ResNet — Deep Residual Learning for Image Recognition (arXiv 1512.03385)**
> "We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions."

> "The depth of representations is of central importance for many visual recognition tasks."

**PReLU / He 初始化 — Delving Deep into Rectifiers (arXiv 1502.01852)**
> "we derive a robust initialization method that particularly considers the rectifier nonlinearities. This method enables us to train extremely deep rectified models directly from scratch."

**MIT News 专访《Creating a common language》(news.mit.edu, 2025)**
> "Science and AI are not isolated subjects. We have been approaching the same goal from different perspectives, and now we are getting together."

> "When you are in your PhD stage, there is a high wall between different disciplines and subjects, and there was even a high wall within computer science. The guy sitting next to me could be doing things that I completely couldn't understand."

---

## 二、何恺明讲座观点（大意转述，非逐字）

来自他 2024–2026 关于生成建模与端到端学习的公开演讲（见 `sources.md`）。原始为视频/自动字幕，此处为整理后的**大意**，请勿当作逐字原话：

- 识别与生成是同一枚硬币的两面：识别从复杂数据流形抽象到简单标签流形，生成是其逆过程。
- 生成模型可作为通用求解器——把问题写成"给定条件 Y 生成 X"，对 X、Y 几乎没有限制。
- 今天一步步训练扩散/自回归模型，概念上类似 AlexNet 之前"逐层训练"的时代；方向应是真正的端到端优化。

---

## 三、谢赛宁访谈中关于何恺明（2026 七小时访谈 / 涌现整理，中文）

这些是谢赛宁的话或他对何恺明的转述，引用时请注明说话人是谢赛宁：

> "恺明在我心里面就是最牛逼的研究员。"

> "他每天除了这一个问题之外，不会想任何其他的东西……他大部分的 mental cycle 都会被 allocate 到这一个具体的问题上。"

> "过分追求虚无的相（论文接收、得奖、名声、一时的称赞、物质奖励）是 research taste 不够好的原因。"

> "weaker baseline 上的提升可能是误导，没有意义，这是 research 的脚手架，不稳什么也做不出来。"

> "对 research 最重要的事情不是从 A 点通到 B 点（A 是 idea，B 是 paper），而是这个过程中你到底能找到什么样的 signal，你的 gradient 到底在哪。"

> "在这个世界上，只有人与人之间真诚的交流是重要的，也许其他都不重要。"

**谢赛宁转述何恺明的话（大意）：**
- 如果你坐在那儿凭空想出来一个 idea，它大概率不是好的——要么一万个聪明人在抢手速，要么是别人试过的烂 idea。
- （2018–2019 年前后）"我们一定需要把模型变得更大，把数据变得更大。"

---

## 四、学生与同行评价

> 张祥雨（ResNet 团队，最年轻未来科学大奖得主）："我的两位导师，尤其是我的 mentor 何恺明和我在 MSRA 的指导老师孙剑，让我们始终坚持简单和本质的原则。"

> 胡瀚（Swin Transformer，ICCV 2021 最佳论文）："正是因为有着孙剑、何恺明等在科研品味和科研素质方面的培养和训练……"

---

## 五、经文与解读框架（注意：不是何恺明的原话）

> "应无所住而生其心。"——《金刚经》

何恺明曾送给谢赛宁一本《金刚经》。"打破幻相"的读论文方法是谢赛宁的引申；"确保你的 Loss Function 定义对了，然后在你自己的路径上，诚实地做梯度下降"是涌现（JigmeDorje）借经文对何恺明方法论的概括——属于解读，不应署成何恺明本人的话。
