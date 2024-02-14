# main.py
import pandas as pd
from utils.util import get_soup_req, get_url


if __name__ == '__main__':
    results = []
    # pagination
    for i in range(1,6):  
        url = get_url(i)
        soup = get_soup_req(url)       
        items = soup.select('div.product')

        # parse the items
        for item in items:
            result = {
                'brand': item.select_one('h3 span').text,
                'product_name': item.select_one('h3 span.product_name').text,
                'price': item.find('span', {'itemprop':["price", 'lowPrice']}).text,
                'link': item.select_one('a.product_link')['href'],
            }
            
            # save the dictionary of result to the list results
            results.append(result)
    # create DataFrame and save to file
    df = pd.DataFrame(results)
    df.to_csv('data/results.csv', index=False)




