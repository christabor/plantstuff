"""Scraping utils."""
import hashlib
import json
import os

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


def cached(*cache_args, **cache_kwargs):
    """General-purpose.

    Allows custom filename, with function fallback.

    Load/save cached function data. Also handle data types gracefully.

    Example:
        >>> cached('myfile.json', folder=SOME_DIR)
        >>> def my_thing():
        >>>    return {'foo': 'bar'}
    """
    def outer(func, *args, **kwargs):
        folder = cache_kwargs.get('folder')
        if len(cache_args) > 0:
            name = cache_args[0]
        else:
            # Guess a resonable name.
            name = func.__name__.replace('_', '-') + '.json'

        def _inner(*args, **kwargs):
            try:
                # Allow users to specify non-existant subfolders
                # but fail gracefully.
                os.makedirs(folder)
            except Exception:
                pass
            path = '{}/{}'.format(folder, name) if folder is not None else name
            try:
                with open(path, 'r') as _cached:
                    if '.json' in name:
                        return json.loads(_cached.read())
                    else:
                        return _cached.read()
            except ValueError as exc:
                if 'No JSON object could be decoded' in str(exc):
                    return func(*args, **kwargs)
            except IOError:
                res = func(*args, **kwargs)
                if res is None:
                    return
                with open(path, 'w') as _cached:
                    if '.json' in name:
                        try:
                            to_write = json.dumps(res, indent=4)
                        # The json was invalid, skip this.
                        except TypeError:
                            return res
                    else:
                        to_write = res
                    _cached.write(to_write)
                    _cached.write('\n')
                    return res
        return _inner
    return outer
