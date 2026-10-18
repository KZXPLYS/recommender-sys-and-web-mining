# Recommender Sys & Web Mining

A learning portfolio exploring review-based prediction, feature engineering, model evaluation, and collaborative filtering with Python and scikit-learn.

本项目整理了两次课程作业的实现与实验入口，展示从评论特征建模到推荐系统的学习过程。函数名称保留课程接口，方便继续运行原有作业。

## Projects

| Project | Methods | Evaluation |
| --- | --- | --- |
| [HW1: Review prediction](HWs/HW1/) | Linear regression; calendar feature encoding; balanced logistic regression; ranking by predicted probability | MSE, balanced error rate (BER), precision@K |
| [HW2: Classification & recommendation](HWs/HW2/) | Feature ablation; regularization selection; Jaccard item similarity; item-based rating prediction; shrinkage toward the global mean | Validation/test BER, rating MSE |

### HW1 · Review prediction

- Compare review-length and date features for predicting book ratings.
- Compare one-hot calendar features against numeric weekday/month features.
- Predict positive beer reviews and examine ranking precision.
- Explore additional sensory-rating and ABV features.

Implementation: [homework1.py](HWs/HW1/homework1.py) · Experiments: [hw1_runner.ipynb](HWs/HW1/hw1_runner.ipynb)

### HW2 · Classification & recommendation

- Predict whether beer ABV exceeds 7 using style, review scores, and text length.
- Select regularization using validation BER and compare feature ablations.
- Find similar products using reviewer-set Jaccard similarity.
- Predict ratings with item-centered collaborative filtering and a global-mean blend.

Implementation: [homework2.py](HWs/HW2/homework2.py) · Experiments: [hw2_runner.ipynb](HWs/HW2/hw2_runner.ipynb)

## Download the data / 下载数据

1. Open [Project datasets](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/tag/datasets-v1).
2. Expand **Assets** and click the data filenames, or use the [direct download links](datasets/README.md).
3. Save the downloaded files in the project-root `datasets/` folder, next to `HWs/`. Keep the original filenames and do not extract `.gz` files.

打开上面的下载页，在 **Assets** 中点击数据文件名，下载后放入根目录 `datasets/`。HW1 需要 fantasy 和 beer 数据；HW2 需要 beer 和 Amazon 数据。完整清单及直接下载链接见 [datasets/README.md](datasets/README.md)。

**Download ZIP / git clone includes code only.** Release data must be downloaded separately; the two “Source code” attachments are not datasets.

## Run locally

From the project directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

Download the six original data files from [Project datasets](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/tag/datasets-v1) and place them in `datasets/`, as described in [the data guide](datasets/README.md). Open `HWs/HW1/hw1_runner.ipynb` or `HWs/HW2/hw2_runner.ipynb` and execute the setup cells in order. HW1 calls its question functions at the end; HW2 defines several optional `testQ*` functions whose calls are commented out. Uncomment or call them to run the corresponding experiments.

Dependencies are currently unpinned; a reproducible environment lock should be recorded after a successful full run.

## Repository layout

```text
recommender-sys-and-web-mining/
├── HWs/                    # Homework implementations and experiments
│   ├── HW1/
│   └── HW2/
├── archive/templates/      # Original course scaffolds, not runnable solutions
├── datasets/               # Data download guide; files in Releases
└── requirements.txt
```

## Results and limitations

This cleanup preserves the executable logic of both solution modules. Notebook outputs were cleared because they included stale errors and local debugging output. No model scores are claimed as newly verified results: the current Python environment lacks the numerical dependencies needed for a full run.

These are educational experiments. Some HW1 metrics are calculated on the same data used for fitting; HW1 Q4 uses a held-out split. In HW2, the supplied runner derives the category vocabulary from the entire beer dataset before training. Document these choices when interpreting or presenting scores.

## 中文说明

- 优先阅读本页了解项目，再查看 Python 实现与运行笔记本。
- 未完成的课程模板已移到 `archive/templates/`，不作为可运行成果。
- 完整数据集已作为 GitHub Releases 附件提供下载；下载后放入本地 `datasets/`。缓存和原始文件备份不上传。
- 本地原文件备份位于 `.local-backup/`，用于需要时恢复。
- GitHub 代码仓库用来展示源码；个人网站可以链接到这里，或增加项目介绍页。网站接入方式需根据现有网站仓库确定。
