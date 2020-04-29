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
### Notes
If you want to commit to your own github repo automatically every download, please configure as follow:
1. Git should be install on your machine correctlly;
2. Configure your repo to store your credential:
```bash
git config --local credential.helper store
```
3. Try an arbitary commmit so that your credential are stored.

Your credential may store at ./git-credentials. you can remove it if you don't need it anymore.

# Requirements
Python >= 3.5
