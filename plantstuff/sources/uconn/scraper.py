"""Scraper for university of connecticut horticulture page."""
from plantstuff.core import fetch
from plantstuff.core.decorators import to_json

URL = 'http://hort.uconn.edu'

get_dom = fetch.get_dom(directory='../../data/uconn')


def clean(text):
    """Heading and list text needs to be cleaned up."""
    if not isinstance(text, (str, unicode)):
        return
    text = text.replace('  ', ' ')
    return text.replace('\n', '').replace('\r', '').strip()


@to_json(directory='../../data/uconn')
def get_all_plant_profile_links():
    """Get the plant name and their detail page links."""
    content, dom = get_dom(URL + '/list.php')
    data = []
    links = dom.find('#results .result')
    for link in links:
        spans = link.findall('span')
        latin_name = spans[0]
        name = spans[1]
        url = link.get('href')
        data.append(dict(
            latin_name=latin_name.text,
            name=name.text,
            url=url
        ))
    return data


@to_json(directory='../../data/uconn')
def get_plant_details(url):
    """Get the plant details."""
    content, dom = get_dom(url)
    info = dom.find('#description')
    # Content is like:
    # <p>heading</p>
    # <ul>...</ul>
    # <p>heading</p>
    # <ul>...</ul>
    data = {'url': url, 'details': {}}
    headings = info.find('p')
    details = info.find('ul')
    for heading, detail in zip(headings, details):
        section_info = []
        title = heading.find('font')
        if title is None:
            continue
        for item in details.find('li'):
            if item is not None:
                section_info.append(clean(item.text))
        title = clean(title.text)
        data['details'][title] = section_info
    return data


@to_json(directory='../../data/uconn')
def get_all_plant_profile_details():
    """Get ALL the plant details."""
    data = []
    links = get_all_plant_profile_links()
    for link in links:
        url = '{}/{}'.format(URL, link['url'])
        details = get_plant_details(url)
        data.append(dict(
            details=details,
            name=link['name'],
            latin_name=link['latin_name'],
            url=link['url'],
        ))
    return data


if __name__ == '__main__':
    get_all_plant_profile_links()
    get_all_plant_profile_details()
