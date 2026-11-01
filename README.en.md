
# Beyond Automation: Notes on Embodied Intelligence

[中文](README.md) · **English**

From deep learning to reinforcement learning and robot tasks, these notes document concepts, mathematical derivations, and the learning process.

**Markdown supports source reading, forks, and collaborative editing. PDFs provide typeset editions for reading, downloading, and printing.**

## Courses and resources behind these notes

- rl-xihu: Notes on *Mathematical Principles of Reinforcement Learning*, a course by Shiyu Zhao at Westlake University.
- deep_learning: Notes from a deep learning course, covering foundational algorithms such as KNN and MLP.
- rl-algorithms: Notes based on OpenAI's open-source *Spinning Up* resource, covering algorithms such as TRPO, PPO, and SAC.

## Reading roadmap

Follow the solid arrows on the cover, or enter at a topic that matches your background. For a task-first approach, start with the embodied intelligence overview, then revisit the foundations as needed.

The [editable cover and roadmap (PPTX)](reading-roadmap.pptx) sits beside this README: slide 1 is Chinese and slide 2 is English. After saving edits, run `python scripts/export_reading_roadmap.py` to update both covers.

## Course materials

Use the links below to read or download the materials.

The originals preserve the author's own wording and learning process. The English editions are edited for English-speaking learners and contributors. PDFs are the existing original-language editions.

| No. | Topic | Original notes | English Markdown | PDF (original) | Coverage |
| :---: | --- | :---: | :---: | :---: | --- |
| 1 | K-Nearest Neighbors | [MD](deep_learning/KNN.md) | [English](deep_learning/KNN.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/deep_learning/KNN.pdf) | Instance-based learning, classification and regression, neighbor count, and distance |
| 2 | Multilayer Perceptrons | [MD](deep_learning/mlp.md) | [English](deep_learning/mlp.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/deep_learning/mlp.pdf) | Forward propagation, backpropagation, gradient updates, and momentum |
| 3 | Westlake University Reinforcement Learning Notes | [MD](rl-xihu/西湖大学强化学习.md) | [English](rl-xihu/西湖大学强化学习.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/rl-xihu/%E8%A5%BF%E6%B9%96%E5%A4%A7%E5%AD%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0.pdf) | Bellman equations, value iteration, MC, TD, DQN, policy gradients, and Actor-Critic |
| 4 | Technical Routes in Embodied Intelligence | [LaTeX](thought_on_embodied_robot/roadmap_for_embodied_tech.tex) | — | [PDF](https://acsg999.github.io/advanced-automation-notes/thought_on_embodied_robot/roadmap_for_embodied_tech.pdf) | Task modeling, VLA, force and touch, world models, system integration, and evaluation |
| 5 | TRPO: Trust Region Policy Optimization | [MD](rl-algorithms/TRPO_handnote.md) | [English](rl-algorithms/TRPO_handnote.en.md) | [PDF](https://acsg999.github.io/advanced-automation-notes/rl-algorithms/TRPO_handnote.pdf) | KL divergence, surrogate advantage, natural policy gradients, Fisher information, conjugate gradients, and backtracking line search |

## Reading

- **Study**: download a PDF and follow its contents. Equations, images, and explanatory notes are retained from the source.
- **Review and editing**: open the MD and use GitHub's source view, diffs, and history to follow changes.

## Contributing

Feel free to fork this repository, clarify concepts, correct equations, improve figures and references, or share questions encountered while studying.

These are learning notes. To report a conceptual or derivation issue, identify the topic and location in [Issues](https://github.com/AcSg999/advanced-automation-notes/issues).

## Rebuilding PDFs

Install **Python 3.9+, Pandoc 3.9+, and XeLaTeX** (TeX Live or MiKTeX), with SimSun, SimHei, Times New Roman, and Consolas fonts. The Python build script uses only the standard library.

Blockquote formatting requires the LaTeX packages `tcolorbox` and `pdfcol`.

Run from the repository root:

```bash
# Pass a Markdown path; create or replace the PDF beside the source like：
python scripts/build_pdfs.py rl-algorithms/TRPO_handnote.md

# Absolute paths also work; quote paths containing spaces like：
python scripts/build_pdfs.py "deep_learning/mlp.md"

# The embodied intelligence notes keep their native LaTeX build script
python thought_on_embodied_robot/build_pdf.py
```

Each run converts one file; no registration in the script is needed. The PDF is saved beside its Markdown source. The cover uses the first Markdown heading, falling back to the filename. Temporary build directories live under `.build/pdf/` in this repository; the terminal prints their creation and removal paths. Temporary files are removed when the run ends; errors and layout warnings appear in the terminal.

