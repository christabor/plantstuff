from pprint import pprint as ppr

import json
import os

from collections import defaultdict

from plantstuff.core.cache import cache_json
from plantstuff.core.utils import get_dom

LETTERS = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
MONROVIA_URL = 'http://www.monrovia.com/plant-catalog/plants/{plant_info}'


def get_letter_search_results_monrovia(letter, start):
    """Scrape all plant data."""
    # ONLY HANDLES PAGE 1 OF RESULTS!
    url = ('http://www.monrovia.com/plant-catalog/search/?'
           'common_name={letter}&'
           'start_page={start}&botanical_name=&'
           'sort_by=common_name&cold_zone={zone}')
    return get_dom(url.format(start=start, letter=letter, zone=8))


def get_all_letter_search_results_monrovia():
    """Scrape all plant data, up to a number of search result pages,
    per letter."""
    for letter in LETTERS:
        # Defaults from 1-11
        for page in range(1, 12):
            get_letter_search_results_monrovia(letter, page)


@cache_json
def get_plants_grid_urls_letter_results_monrovia(letter, start):
    """Return the grid of plant urls."""
    url_base = 'http://www.monrovia.com/plant-catalog/plants/'
    page, dom = get_letter_search_results_monrovia(letter, start)
    urls = []
    print(letter, start)
    plants = dom.find('.plants-grid').find('.list-plant')
    for plant in plants:
        if plant.find('a') is not None:
            name = plant.find(
                'a').text.replace(' ', '_').lower()
            link = plant.find('a').get('href')
            info = link.replace(url_base, '')
            data = dict(name=name, link=link, info=info)
            urls.append(data)
    ppr(urls)
    return urls


@cache_json
def get_plants_grid_all_letters_results_monrovia():
    """Return the grid of plant urls."""
    all_data = defaultdict(list)
    for letter in LETTERS:
        for page in range(1, 12):
            res = get_plants_grid_urls_letter_results_monrovia(letter, page)
            all_data[letter].append(res)
    return all_data


# def get_info(info):
#     """Get plant info."""
#     data, dom = get_dom(GARDEN_ORG_URL.format(plant_info=info))
#     tables = dom.find('#ngabody').find('table')
#     dfs = pd.read_html(str(tables))
#     for table in dfs:
#         for data in table.values:
#             print(data)
#             print('-----')


@cache_json
def get_monrovia_info(info):
    """Get plant info."""
    url = MONROVIA_URL.format(plant_info=info)
    raw_data, dom = get_dom(url)
    details = dom.find('#Detail').find('.attribute')
    overview = dom.find('#Overview').find('.attribute')
    data = {}

    def get_section(els):
        d = {}
        for detail in els:
            children = detail.getchildren()
            if len(children) == 2:
                k, v = children
            else:
                # Uses a image in this section
                k, _, v = children
            if v.text is None:
                # Wrapped in a link.
                v = v.find('a')
            d[k.text.lower().replace(' ', '_').replace(':', '')] = v.text
        return d

    data['overview'] = get_section(overview)
    data['detail'] = get_section(details)
    data['url'] = url
    data['name'] = info.split('/')[1]
    # ppr(data)
    return data


def load_monrovia_data():
    """Get all companion plant references and the plants they correspond to."""
    data = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('.json'):
            p_data = open(file, 'r').read()
            p_data = json.loads(p_data)
            if 'url' in p_data and 'name' in p_data:
                data.append(p_data)
    return data


@cache_json
def get_companion_plant_monrovia():
    """Get all companion plant references and the plants they correspond to."""
    relationships = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('.json'):
            p_data = open(file, 'r').read()
            p_data = json.loads(p_data)
            if not isinstance(p_data, dict):
                continue
            if p_data.get('detail') is not None:
                companions = p_data['detail'].get('companion_plants')
                if companions is not None:
                    companions = [
                        c.strip().lower() for c in companions.split(';')
                        if c.strip()
                    ]
                    for comp in companions:
                        name = str(p_data['name'])
                        relationships.append((name, str(comp)))
    return relationships


# def get_usda_info(symbol):
#     """Get plant info."""
#     data = get_dom(USDA_URL.format(symbol=symbol))
#     dom = Pq(data)


@cache_json
def get_all_plants_from_all_letters_all_pages_n_monrovia():
    """Get all plant details for all letters A_Z for all page search results
    up to N (default 12, see other functions).
    """
    all_data = []
    data = get_plants_grid_all_letters_results_monrovia()
    for letter, results in data.items():
        for page in results:
            for plant in page:
                plant_info = get_monrovia_info(plant['info'])
                all_data.append(plant_info)
    return all_data


if __name__ == '__main__':
    # get_info('231023/Golden-Euonymus-Euonymus-japonicus-Aureo-Marginata')
    # get_usda_info('EUJA8')
    # get_monrovia_info('1143/golden-euonymus/')
    # get_monrovia_info('5159/ivory-silk-japanese-tree-lilac/')
    # get_monrovia_info('335/goldmound-spirea/')
    # get_all_letter_search_results_monrovia()
    # get_companion_plant_monrovia()
    # make_companion_plant_graph()
    get_all_plants_from_all_letters_all_pages_n_monrovia()
