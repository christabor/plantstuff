"""Scraper for springhills nursery page."""

from plantstuff.scraper_utils import fetch
from plantstuff.scraper_utils import normalize
from plantstuff.scraper_utils.decorators import to_json

# 'a' is for all, not an alphabetical letter
URL = 'https://www.springhillnursery.com/category/{section}/a'

ALL_SECTIONS = [
    'perennial_plants',
    'flowering_fast_growing_trees',
    'shrubs_hedges',
    'vines_climbers',
    'flower_bulbs',
    'rose_plants',
    'edibles',
    'annuals',
]
get_dom = fetch.get_dom(directory='../../data/springhills')


@to_json(directory='../../data/springhills')
def get_all_detail_links_for_all_categories():
    """Get all available links for each category.."""
    links = {}
    for section in ALL_SECTIONS:
        links[section] = get_detail_links_for_category(section)
    return links


@to_json(directory='../../data/springhills')
def get_detail_links_for_category(section):
    """Get all available links for a category.."""
    url = URL.format(section=section)
    _, dom = get_dom(url)
    links = []
    tiles = dom.find('.category_page_products ul li section .prodthumb_name a')
    for tile in tiles:
        if tile is None:
            continue
        links.append(dict(
            url=url,
            category=section,
            name=tile.text.strip().lower(),
            link=tile.get('href'),
        ))
    return links


@to_json(directory='../../data/springhills')
def get_plant_details(url):
    """Get details of a plant."""
    _, dom = get_dom(url)
    info = dom.find('.product_info')
    list_a = info.find('.info_list_A li')
    list_b = info.find('.info_list_B li')
    items = {}

    def _get_list(items, lst):
        for item in lst:
            try:
                title, val = item.text_content().split(':')
            except ValueError:
                continue
            title = normalize.clean_key(title)
            if 'restricted' in title:
                items[title] = [
                    l.upper() for l in normalize.clean(val).split(' ')
                ]
            else:
                items[title] = normalize.clean(val)
    _get_list(items, list_a)
    _get_list(items, list_b)
    return items


@to_json(directory='../../data/springhills')
def get_all_plant_details():
    """Get details of ALL plants."""
    details = []
    categories = get_all_detail_links_for_all_categories()
    for category, plants in categories.items():
        for plant in plants:
            url = 'https://www.springhillnursery.com' + plant['link']
            details.append(dict(
                category=category,
                detail_url=url,
                detail=get_plant_details(url),
                name=plant['name'],
            ))
    return details


if __name__ == '__main__':
    get_all_detail_links_for_all_categories()
    get_all_plant_details()
