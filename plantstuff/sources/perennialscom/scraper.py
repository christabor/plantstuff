import requests

from pyquery import PyQuery as Pq

from plantstuff.core.cache import cache_html, cache_json

URL = 'http://www.perennials.com/plants/{plant}.html'

# @cache_html(directory='../../data/perennialscom')


def get_dom(url):
    """Get html and dom object."""
    data = requests.get(url).content
    dom = Pq(data)
    return data, dom


# @cache_json(directory='../../data/plantsdb')
def guess_plant():
    """Download api data by plant symbol for ALL plants."""
    content, dom = get_dom(
        'http://www.perennials.com/results_alphabet.html?'
        'start=0&letter={letter}'.format(letter='A')
    )
    urls = []


if __name__ == '__main__':
    guess_plant()
