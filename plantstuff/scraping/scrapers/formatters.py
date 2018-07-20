# -*- coding: utf-8 -*-

"""Various utilities for formatting content"""


def labelize(item):
    if item is None:
        return
    item = item.strip().replace(' ', '_').replace('&nbsp;', '')
    return item.replace('/', '_').replace(':', '').lower()


def maybe_lower(item):
    if item is None:
        return
    return item.lower()


def tokenize(item):
    if item is None:
        return []
    return [token.strip() for token
            in item.strip().split(' ') if token.strip()]
