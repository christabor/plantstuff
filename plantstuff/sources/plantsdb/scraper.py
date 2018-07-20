"""Plantsdb.xyz "scraper"."""

from collections import defaultdict

import requests

from plantstuff.core import fetch
from plantstuff.core.decorators import to_json

API_URL = 'https://plantsdb.xyz/search?symbol={symbol}'
USDA_PLANTLIST_URL = (
    'https://www.plants.usda.gov/java/downloadData?'
    'fileName=plantlst.txt&static=true'
)
get_dom = fetch.get_dom(directory='../../data/plantsdb')


@to_json(directory='../../data/plantsdb')
def get_usda_options():
    """Download all the options from USDA advanced form."""
    url = 'https://plants.usda.gov/adv_search.html'
    data, dom = get_dom(url)
    sels = dom.find('#advqry').find('select')
    data = defaultdict(list)
    for sel in sels:
        name = sel.get('name').lower().replace(' ', '')
        for opt in sel.findall('option'):
            data[name].append(opt.text)
    from pprint import pprint as ppr
    ppr(data)
    return data


@to_json(directory='../../data/plantsdb')
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


@to_json(directory='../../data/plantsdb')
def get_data_by_symbol(symbol):
    """Download api data by plant symbol."""
    res = requests.get(API_URL.format(symbol=symbol))
    if res.status_code == 200:
        return res.json()


@to_json(directory='../../data/plantsdb')
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
    # get_all_data_by_symbol()
    get_usda_options()
