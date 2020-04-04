from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
DEFAULT_URL = "https://www.worldometers.info/coronavirus"

def parse_page(url= DEFAULT_URL, headers = DEFAULT_HEADERS):
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    parsed_page = soup(html, "html.parser")
    return parsed_page
