
import pandas as pd
from utils.selenium_template import bypass_sel, get_soup

filename = 'data/text_html.txt'
url = "https://www.villagehatshop.com/category/464/1/view-all.html"

soup = get_soup(url)
# soup = bypass_sel(filename)

print(soup.find('title').text)


