# bing-bg-downloader

When I used [BING](https://cn.bing.com/?mkt=zh-CN) search engine, I found its backgroud was so beautiful, so I decide to download its background image.

# Usage
```bash
git clone <this repo>
cd bing-bg-downloader

# If you want to setup a timer to download  bg everyday
# Note: Only support Linux timer so far.
./scripts/setup-timer.sh

# Or, you can run the download script manually
python3 ./src/downloader.py
```

# Requirements
Python >= 3.5
