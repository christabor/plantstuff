"""Scraping utils."""

import hashlib
import json

from functools import wraps

from pyquery import PyQuery as Pq


def cache_json(func):
    """Cache dict/list data as a json file."""
    @wraps(func)
    def inner(*args, **kwargs):
        url = args[0] if len(args) > 0 else ''
        fname = func.__name__ + '_'.join(url)
        hash = hashlib.md5(fname).hexdigest()
        fname = 'cached_{}_{}.json'.format(func.__name__, hash)
        try:
            with open(fname, 'r') as jsondata:
                data = json.loads(jsondata.read())
                print('using cached JSON! {}'.format(fname))
                return data
        except IOError:
            data = func(*args)
            with open(fname, 'w') as jsondata:
                jsondata.write(json.dumps(data, indent=4))
            return data
    return inner


def cache_html(func):
    """Decorator to cache html file and load pyquery object from it."""
    @wraps(func)
    def inner(*args, **kwargs):
        url = args[0]
        fname = func.__name__ + '_'.join(url)
        hash = hashlib.md5(fname).hexdigest()
        fname = 'cached_{}_{}.html'.format(func.__name__, hash)
        try:
            with open(fname, 'r') as html:
                data = html.read()
                dom = Pq(data)
                print('using cached HTML! {}'.format(fname))
                return data, dom
        except IOError:
            data, dom = func(url)
            with open(fname, 'w') as html:
                html.write(data)
            return data, dom
    return inner
