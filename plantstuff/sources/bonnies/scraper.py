"""Scraper for bonnies nursery page."""

from plantstuff.core.cache import cache_json
from plantstuff.core import fetch

URL = 'https://bonnieplants.com'

get_dom = fetch.get_dom(directory='../../data/bonnies')
