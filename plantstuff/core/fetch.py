"""Data fetching."""
from pyquery import PyQuery as Pq
import requests

from plantstuff.core.cache import cache_html


def get_dom(directory=None):
    """Create a new function with a directory specified."""
    @cache_html(directory=directory)
    def get(url):
        """Get html and dom object."""
        data = requests.get(url).content
        dom = Pq(data)
        return data, dom
    return get
