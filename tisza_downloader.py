from tisza_scraper.tisza_scraper import get_shoes
from utils.html_util import get_html_content
from utils.tisza_util import construct_filter_url


urls = [
    "https://www.tiszacipo.hu/bolt/kifutok/compakt-kifuto/",
    "https://www.tiszacipo.hu/bolt/kifutok/compakt-delux-kifutok/",
    "https://www.tiszacipo.hu/bolt/kifutok/comfort/",
    "https://www.tiszacipo.hu/bolt/kifutok/derby-kifutok/",
    "https://www.tiszacipo.hu/bolt/kifutok/sport-kifutok/",
    "https://www.tiszacipo.hu/bolt/kifutok/alfa-kifuto/",
    "https://www.tiszacipo.hu/bolt/kifutok/public-kifutok/",
    "https://www.tiszacipo.hu/kollekcio/budapest/"
]



def download_shoes_by_size(size):
    result = []
    for url in urls:
        result += get_shoes(get_html_content(construct_filter_url(url, size)), size)
    return result

