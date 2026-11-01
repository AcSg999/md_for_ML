
# 自动化之后--具身智能学习笔记

**中文** · [English](README.en.md)

从深度学习到强化学习与机器人任务，记录概念、公式推导和学习过程。

其中**Markdown 用于阅读源码、Fork 和共同完善；PDF 用于完整阅读、下载与打印。**
## 寻根溯源
- rl-xihu: 面向西湖大学赵世钰老师的《强化学习数学原理》的课程笔记。
- deep_learning: 面向深度学习课程的笔记，涵盖 KNN、MLP 等基础算法。
- rl-algorithms: 面向openai开源的spinning up的笔记，涵盖 TRPO、PPO、SAC 等算法。

## 阅读路线

从基础起步，可按图中实线顺读；已有基础可直接进入对应主题。关注机器人任务时，可先读具身智能总览，再回查所需知识。

[可编辑封面与路线图（PPTX）](reading-roadmap.pptx) 与本 README 位于同一目录，第 1 页为中文，第 2 页为英文。保存修改后，运行 `python scripts/export_reading_roadmap.py` 同步更新两张封面。

## 课程资料

点击表中链接阅读或下载。

md原稿保留作者的原始表达；英文版面向英语学习者整理，便于阅读和共同完善。PDF展示排版与表达效果。


| 序号 | 主题 | 原稿 |  Markdown.eng | PDF（原版） | 内容范围 |
| :---: | --- | :---: | :---: | :---: | --- |
| 1 | KNN：K 近邻方法 | [MD](deep_learning/KNN.md) | [English](deep_learning/KNN.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/deep_learning/KNN.pdf) | 基于实例的学习、分类与回归、邻居数量与距离 |
| 2 | MLP：多层感知机 | [MD](deep_learning/mlp.md) | [English](deep_learning/mlp.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/deep_learning/mlp.pdf) | 前向传播、反向传播、梯度更新与动量 |
| 3 | 西湖大学强化学习 | [MD](rl-xihu/西湖大学强化学习.md) | [English](rl-xihu/西湖大学强化学习.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/rl-xihu/%E8%A5%BF%E6%B9%96%E5%A4%A7%E5%AD%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0.pdf) | Bellman 方程、价值迭代、MC、TD、DQN、策略梯度与 Actor-Critic |
| 4 | 具身智能技术路线 | [LaTeX](thought_on_embodied_robot/roadmap_for_embodied_tech.tex) | — | [PDF](https://acsg999.github.io/advanced-automation-notes/thought_on_embodied_robot/roadmap_for_embodied_tech.pdf) | 任务建模、VLA、力触觉、世界模型、系统组合与评测 |
| 5 | TRPO：Trust Region Policy Optimization | [MD](rl-algorithms/TRPO_handnote.md) | [English](rl-algorithms/TRPO_handnote.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/rl-algorithms/TRPO_handnote.pdf) | KL 散度、代理优势、自然策略梯度、Fisher 信息矩阵、共轭梯度法、回溯线搜索 |


## 如何阅读

- **学习**：下载 PDF，按目录阅读；原稿中的公式、图片和补充解释保留在讲义中。
- **查阅与修改**：打开 MD，利用 GitHub 的源码、差异对比和历史记录追踪修改。


## 共同完善

欢迎fork本仓库，补充概念解释、纠正公式、改善配图与引用，也欢迎提交学习中遇到的问题。

现有笔记侧重学习记录。发现推导或概念问题时，可在 [Issues](https://github.com/AcSg999/advanced-automation-notes/issues) 中标出主题和具体位置。

## 重建 PDF

需要 **Python 3.9+、Pandoc 3.9+ 和 XeLaTeX**（TeX Live 或 MiKTeX），以及宋体、黑体、Times New Roman、Consolas 字体。Python 构建脚本只使用标准库。

引用块排版需要 XeLaTeX 的 `tcolorbox` 和 `pdfcol` 宏包。

在仓库根目录运行：

```bash
# 传入 Markdown 路径，在原目录生成或覆盖同名 PDF, 如
python scripts/build_pdfs.py rl-algorithms/TRPO_handnote.md

# 也支持绝对路径；路径含空格时加引号，如
python scripts/build_pdfs.py "deep_learning/mlp.md"

# 具身智能讲义使用原生 LaTeX，沿用独立构建脚本
python thought_on_embodied_robot/build_pdf.py
```

每次运行转换一个文件，无需在脚本中登记，PDF 放在对应 Markdown 目录下。封面标题取第一个 Markdown 标题，没有标题时使用文件名。临时编译目录位于本仓库的 `.build/pdf/` 下，终端会打印创建和删除的位置；运行结束后自动清理，报错和排版警告直接显示在终端。





