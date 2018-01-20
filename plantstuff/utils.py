"""Scraping utils."""

import requests

from pyquery import PyQuery as Pq

from plantstuff.core.cache import cache_html

GARDEN_ORG_URL = 'https://garden.org/plants/view/{plant_info}/'
USDA_URL = 'https://plants.usda.gov/core/profile?symbol={symbol}'
UCONN_URL = 'http://hort.uconn.edu/search.php'
PLANTS_DB_URL = 'https://plantsdb.xyz/search'
PERENNIALS_URL = 'http://www.perennials.com/plants/{plant}.html'
DAVES_URL = 'https://davesgarden.com/guides/pf/go/{plant_id}/'


@cache_html
def get(url):
    """Get html and dom object."""
    data = requests.get(url).content
    dom = Pq(data)
    return data, dom
