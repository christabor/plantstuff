"""Data fetching."""
import requests

from pyquery import PyQuery as Pq

from plantstuff.scraper_utils.decorators import cache_html


def get_dom(directory=None):
    """Create a new function with a directory specified."""
    @cache_html(directory=directory)
    def get(url):
        """Get html and dom object."""
        data = requests.get(url).content
        dom = Pq(data)
        return data, dom
    return get
