from utils.soup_playwright import get_soup_pw



url = 'https://books.toscrape.com/'

if __name__ == '__main__':
    soup = get_soup_pw(url)
