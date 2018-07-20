"""Daves garden scrapers."""
from plantstuff.core import fetch
from plantstuff.core.decorators import to_json

LETTERS = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
DAVES_URL = 'http://davesgarden.com/guides/pf/go/{plant_id}/'
DAVES_URL_BY_SPECIES = (
    'http://davesgarden.com/guides/pf/tools/names.php?z=species'
)

get_dom = fetch.get_dom(directory='../../data/daves')


@to_json(directory='../../data/daves')
def get_all_species_links_on_page(url):
    """Get all the species list on the main page."""
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


@to_json(directory='../../data/daves')
def get_all_species_links_on_page_all_pages():
    """Get all species links on all pages (paginated)."""
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


@to_json(directory='../../data/daves')
def get_real_plant_profile_link(name, ref_url):
    """Get the real profile link.

    Using all species/all pages data,
    get the actual profile id link for the plant url.
    """
    data, dom = get_dom(ref_url)
    link = dom.find('.plant-info-block > a')
    url = 'https://davesgarden.com{}'.format(link.get('href'))
    return {'ref': ref_url, 'real_url': url, 'name': name}


@to_json(directory='../../data/daves')
def get_all_plant_profile_links():
    """Get the real profile links.

    Using all species/all pages data,
    get the actual profile id link for each one.
    """
    data = []
    link_data = get_all_species_links_on_page_all_pages()
    links = []
    for link in link_data:
        links += link['data']
    for link in links:
        res = get_real_plant_profile_link(link['name'], link['url'])
        data.append(res)
    return data


if __name__ == '__main__':
    get_all_plant_profile_links()
