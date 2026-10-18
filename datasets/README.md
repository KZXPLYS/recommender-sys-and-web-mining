# Datasets

Download all six original data files from [Project datasets](https://github.com/KZXPLYS/recommender-sys-and-web-mining/releases/tag/datasets-v1). Save them in this `datasets/` folder without changing their names. Keep `.gz` files compressed; the notebooks read them directly.

The data files are hosted as GitHub Release assets because several exceed the size limits for ordinary repository files. Cloning the repository or downloading its source ZIP does **not** include these assets; download them separately.

| File | Used by |
| --- | --- |
| `fantasy_10000.json.gz` | HW1 book-rating experiments |
| `beer_50000.json` | HW1 and HW2 beer-review experiments |
| `amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz` | HW2 recommendation experiments |
| `young_adult_20000.json.gz` | Additional local dataset; not used by the current runners |
| `book_images_5000.json` | Additional local dataset; not used by the current runners |
| `book_descriptions_50000.json` | Additional local dataset; not used by the current runners |

The beer data uses Python-literal records; the runners read them with `ast.literal_eval`. The fantasy data is gzip-compressed JSON lines, and the Amazon data is a gzip-compressed TSV.

完整数据下载见上方链接。将六个文件放在此目录即可；无需解压 `.gz` 文件。代码仓库只保存本说明，原始数据在 Releases 中单独下载。
