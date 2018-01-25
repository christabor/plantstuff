"""Scraper for university of connecticut horticulture page."""
from plantstuff.core import fetch
from plantstuff.core.cache import cache_json, cached


get_dom = fetch.get_dom(directory='../../data/wikipedia')


def clean(text):
    """Heading and list text needs to be cleaned up."""
    if not isinstance(text, (str, unicode)):
        return
    text = text.replace('  ', ' ')
    return text.replace('\n', '').replace('\r', '').strip()


def get_plants_for_species(item):
    """Get list of plants for a species."""
    @cached('species_list_{}.json'.format(item['name']),
            directory='../../data/wikipedia')
    def get():
        def table(dom):
            # We need to switch to table format - the wikipedia articles
            # are inconsistent.
            rows = dom.find('.mw-parser-output .wikitable tr')
            headings = [h.text.strip() for h in rows[0]]
            for row in rows[1:]:
                row_data = {}
                tds = row.findall('td')
                if tds is None:
                    continue
                for i, td in enumerate(tds):
                    try:
                        row_data[headings[i]] = td.text or None
                    except IndexError:
                        continue
                data.append(row_data)

        data = []
        url = 'https://en.wikipedia.org{}'.format(item['link'])
        _, dom = get_dom(url)
        # Try to be specific, but broaden scope if none found.
        if 'bamboo' in item['name']:
            table(dom)
        else:
            links = dom.find('.mw-parser-output ul li a')
            if not links:
                links = dom.find('.mw-parser-output ol li a')
            if not links:
                links = dom.find('.mw-parser-output li a')
            if links:
                for link in links:
                    if link.text is None:
                        continue
                    # Reference links embedded within the lists.
                    if any([
                        # External link is invalid
                        link.get('href', '').startswith('http'),
                        # Anchors, invalid link
                        link.get('href', '').startswith('#'),
                        # Not real links/text
                        link.text.startswith('['),
                        link.text == '^',
                        link.text.startswith('\\'),
                    ]):
                        continue
                    data.append(dict(name=link.text, link=link.get('href')))
            else:
                table(dom)
        return data
    return get()


@cache_json(directory='../../data/wikipedia')
def get_all_plant_species_lists():
    """Get ALL the lists of plants by species for all species."""
    data = []
    url = 'https://en.wikipedia.org/wiki/Category:Lists_of_plant_species'
    _, dom = get_dom(url)
    links = dom.find('.mw-category ul li a')
    for link in links:
        data.append(dict(name=link.text, link=link.get('href')))
    return data


if __name__ == '__main__':
    species = get_all_plant_species_lists()
    for item in species:
        get_plants_for_species(item)
