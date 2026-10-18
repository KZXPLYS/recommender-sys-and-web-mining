# Local datasets

The data files are excluded from Git. Obtain them from the course-provided source and place them in this directory without renaming them.

| File | Used by |
| --- | --- |
| `fantasy_10000.json.gz` | HW1 book-rating experiments |
| `beer_50000.json` | HW1 and HW2 beer-review experiments |
| `amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz` | HW2 recommendation experiments |

The local folder also contains `young_adult_20000.json.gz`, `book_images_5000.json`, and `book_descriptions_50000.json`; the current runners do not use these files.

The beer data uses Python-literal records; the runners read them with `ast.literal_eval`. The fantasy data is gzip-compressed JSON lines, and the Amazon data is a gzip-compressed TSV.
