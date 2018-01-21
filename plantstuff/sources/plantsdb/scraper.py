from collections import namedtuple

import requests

from pyquery import PyQuery as Pq

from plantstuff.core.cache import cache_html, cache_json

API_URL = 'https://plantsdb.xyz/search?symbol={symbol}'
USDA_PLANTLIST_URL = (
    'https://www.plants.usda.gov/java/downloadData?'
    'fileName=plantlst.txt&static=true'
)


@cache_html(directory='../../data/plantsdb')
def get_dom(url):
    """Get html and dom object."""
    data = requests.get(url).content
    dom = Pq(data)
    return data, dom


@cache_json(directory='../../data/plantsdb')
def get_all_data_from_usda_plants():
    """Download all the symbol/plant data."""
    raw = requests.get(USDA_PLANTLIST_URL).content.split('\n')
    # labels are like:
    # "Symbol","Synonym Symbol","Scientific Name with Author",
    # "Common Name","Family"
    rows = raw[1:]
    data = []
    for row in rows:
        try:
            symb, syn, name, common, family = row.replace('"', '').split(',')
            data.append(dict(
                symbol=symb,
                synonym_symbol=syn,
                name_and_author=name,
                common_name=common,
                family=family,
            ))
        except ValueError:
            data.append(row.replace('"', '').split(','))
    return data


@cache_json(directory='../../data/plantsdb')
def get_data_by_symbol(symbol):
    """Download api data by plant symbol"""
    res = requests.get(API_URL.format(symbol=symbol))
    if res.status_code == 200:
        return res.json()


@cache_json(directory='../../data/plantsdb')
def get_all_data_by_symbol():
    """Download api data by plant symbol for ALL plants."""
    refdata = get_all_data_from_usda_plants()
    raw = []
    for row in refdata:
        if 'symbol' in row:
            data = get_data_by_symbol(row['symbol'])
            raw.append(data)
    return raw


if __name__ == '__main__':
    get_all_data_by_symbol()
