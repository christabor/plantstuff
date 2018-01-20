"""Scraping utils."""

import hashlib
import json

from functools import wraps

from pyquery import PyQuery as Pq


def cache_json(directory=None):
    """Cache dict/list data as a json file."""
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            url = args[0] if len(args) > 0 else ''
            fname = func.__name__ + '_'.join(url)
            hash = hashlib.md5(fname).hexdigest()
            fname = 'cached_{}_{}.json'.format(func.__name__, hash)
            try:
                fpath = fname
                if directory is not None:
                    fpath = '{}/{}'.format(directory, fname)
                with open(fpath, 'r') as jsondata:
                    data = json.loads(jsondata.read())
                    print('using cached JSON! {}'.format(fname))
                    return data
            except IOError:
                data = func(*args)
                with open(fpath, 'w') as jsondata:
                    jsondata.write(json.dumps(data, indent=4))
                return data
        return inner
    return outer


def cache_html(directory=None):
    """Decorator to cache html file and load pyquery object from it."""
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            url = args[0]
            fname = func.__name__ + '_'.join(url)
            hash = hashlib.md5(fname).hexdigest()
            fname = 'cached_{}_{}.html'.format(func.__name__, hash)
            fpath = fname
            if directory is not None:
                fpath = '{}/{}'.format(directory, fname)
            try:
                with open(fpath, 'r') as html:
                    data = html.read()
                    dom = Pq(data)
                    print('using cached HTML! {}'.format(fname))
                    return data, dom
            except IOError:
                data, dom = func(url)
                with open(fpath, 'w') as html:
                    html.write(data)
                return data, dom
        return inner
    return outer
