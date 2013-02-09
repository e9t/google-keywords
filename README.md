Get Google Keywords
=================================

### Preparation
- Windows: Install [NLTK](http://nltk.org/install.html) 
- Mac OS X:

		pip install nltk
    
### Configure settings

    vi settings.py

- TARGET: Either 'news' or 'blog'
- QUERYLIST: List of queries
- HTMLPATH: Path to save html files. (Paths should end with a slash)
- KEYWORDPATH = 'data/keywords/'
- NCRAWLPAGES: Number of search pages to crawl from Google
- DELIMS: Delimiters for parsing words in HTML page
- TODAY: Date for analysis

### Run

In order to get search results for `data mining`, run

    python main.py data mining

or set `QUERYLIST=['data', 'mining']` in `settings.py`, and run

    python main.py

### Results
If `HTMLPATH='data/html/'` and `KEYWORDPATH='data/keywords/` in `settings.py`, the search results and keywords are stored in the 'data' folder as below.

    data/
        ├── html/
        │   ├── data_mining/
        │   └── data_mining-20120907.json
        └── keywords/
            └── keywords-data_mining.json

- **data/html/data_mining/**: This folder contains the raw HTML files. File names are marked with a timestamp.
- **data/html/data_mining-20120907.json**: This file contains th `url`, `desc`(description), `crawled_time`, `title` extracted from the raw HTML files. Below is an example.

        [
          {
            "url": "http://smartdatacollective.com/timoelliott/101486/analytics-world-news-big-data-cool-3d-analytics", 
            "desc": "Themos Kalafatis has worked as a consultant for , Text Mining, Information Extraction and Data Quality for over a decade. More \u00bb ", 
            "crawled_time": "20120907_192648",
            "page_no": 1,
            "title": "Scary Big Data, Cool 3D Analytics and More"
          },
          ...
        ]

- **data/keywords/keywords-data_mining.json**: This file contains the most frequent keywords. An example is shown below.

        ["data", 23],
        ["mining", 19],
        ["analytics", 3],
        ["app", 3],
        ["big", 2],
        ["mayo", 2],
        ["companies", 2],
        ["3d", 2],
        ["ehr", 2],
        ["datamining", 2],
        ["partner", 2],
        ["nlp", 1],
        ["desktops", 1],
        ["office", 1],
        ["advisory", 1]
        ...

### Authors
2012 LG-SNU Smart TV Project Team
(Created Sep. 2012)
