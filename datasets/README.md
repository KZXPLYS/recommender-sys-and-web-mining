# Download datasets / 数据下载

The complete original files are available in [Project datasets](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/tag/datasets-v1), under **Assets**. This folder in the code repository contains instructions; the large data files are hosted as Release attachments.

## How to download / 下载步骤

1. Click a filename in the table below to download it directly, or open the release page and expand **Assets**.
2. Save the files in this `datasets/` folder at the project root, alongside `HWs/`.
3. Keep filenames unchanged. **Do not unzip the `.gz` files**: the notebooks read them directly.
4. Open `HWs/HW1/hw1_runner.ipynb` or `HWs/HW2/hw2_runner.ipynb`, then run the cells from top to bottom.

点击下表文件名即可下载。把文件放入项目根目录的 `datasets/`，不要放到 `HWs/` 或各作业文件夹里，也不要解压 `.gz` 文件。只运行 HW1 时下载 fantasy 和 beer；运行 HW2 时下载 beer 和 Amazon；要保留全部数据则下载六个文件。

**Cloning the repository or choosing Code → Download ZIP does not download the data.** The release's “Source code (zip)” and “Source code (tar.gz)” attachments also contain only code. Choose the six named data assets below.

## Files / 文件清单

| Download | Used by | Size |
| --- | --- | --- |
| [fantasy_10000.json.gz](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/download/datasets-v1/fantasy_10000.json.gz) | HW1 | 3.6 MiB |
| [beer_50000.json](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/download/datasets-v1/beer_50000.json) | HW1 + HW2 | 58.3 MiB |
| [amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/download/datasets-v1/amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz) | HW2 | 184.1 MiB |
| [young_adult_20000.json.gz](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/download/datasets-v1/young_adult_20000.json.gz) | Additional dataset / 当前实验未使用 | 5.0 MiB |
| [book_images_5000.json](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/download/datasets-v1/book_images_5000.json) | Additional dataset / 当前实验未使用 | 168.9 MiB |
| [book_descriptions_50000.json](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/download/datasets-v1/book_descriptions_50000.json) | Additional dataset / 当前实验未使用 | 99.3 MiB |

## Expected local layout / 下载后的目录

```text
recommender-sys-and-web-mining/
├── HWs/
│   ├── HW1/
│   └── HW2/
└── datasets/
    ├── README.md
    ├── fantasy_10000.json.gz
    ├── beer_50000.json
    ├── amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz
    ├── young_adult_20000.json.gz
    ├── book_images_5000.json
    └── book_descriptions_50000.json
```

The beer data uses Python-literal records, read with `ast.literal_eval`; the fantasy data is gzip-compressed JSON lines, and the Amazon data is a gzip-compressed TSV. Local data files remain ignored by Git because their downloadable copies are in Releases.
