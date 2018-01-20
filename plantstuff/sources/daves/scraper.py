import requests

from pyquery import PyQuery as Pq

from plantstuff.core.cache import cache_html, cache_json

LETTERS = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
DAVES_URL = 'http://davesgarden.com/guides/pf/go/{plant_id}/'
DAVES_URL_BY_SPECIES = (
    'http://davesgarden.com/guides/pf/tools/names.php?z=species'
)


@cache_html(directory='../../data/daves')
def get_dom(url):
    """Get html and dom object."""
    data = requests.get(url).content
    dom = Pq(data)
    return data, dom


@cache_json(directory='../../data/daves')
def get_all_species_links_on_page(url):
    data, dom = get_dom(url)
    table = dom.find('.tableguides.table-responsive > table a')
    links = []
    for link in table:
        if link is None or link.text is None:
            continue
        links.append(dict(
            name=link.text.strip().lower(),
            url=DAVES_URL_BY_SPECIES + link.get('href')
        ))
    return links


@cache_json(directory='../../data/daves')
def get_all_species_links_on_page_all_pages():
    # This is hard-coded on their site, for now.
    per_page = 40
    curr_offset = 0
    # This is hard-coded and brittle, but it works for now.
    total_pages = 619
    data = []
    while curr_offset < total_pages * per_page:
        url = '{}&offset={}'.format(DAVES_URL_BY_SPECIES, curr_offset)
        data.append(dict(
            offset=curr_offset,
            data=get_all_species_links_on_page(url),
        ))
        curr_offset += per_page
    return data


if __name__ == '__main__':
    get_all_species_links_on_page_all_pages()
