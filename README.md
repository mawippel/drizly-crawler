# Drizly Web Crawler

Beers' characteristics Web Crawler. Extracting from [Drizly](https://drizly.com/) website.

## Intro
Its main goal is to retrieve the beers characteristics, given a certain beer style. It crawls all the beers in all pages until it reaches the end.

<img src='./assets/beerchars.png'>

## Setup
```
# Create python venv
python3.7 -m venv .venv

# Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## Running the Crawler

To run the crawler you must pass the category's endpoint as an argument to the python script. An example is shown below:

```python
python .\drizly_crawler.py /beer/ale/ipa/c15
```

In this example, the seed of the crawler will be the `https://drizly.com/beer/ale/ipa/c15` page. When the end of the page is reached, it jumps to the next page and all the crawling process runs again, until all the pages for this beer style are crawled.

<a href="https://www.buymeacoffee.com/marcelowippel" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>