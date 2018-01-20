"""Graphing data."""

from collections import Counter
from pprint import pprint as ppr

from pandas import Series
from tinydb import Query, TinyDB

from plantstuff import utils

db = TinyDB('../../data/monrovia/monrovia_plant_db.json')


def backfill():
    raw = utils.get_all_plants_from_all_letters_all_pages_n_monrovia()
    for item in raw:
        print('inserting,', item)
        db.insert(item)


# res = db.all()
# print(res)
Plant = Query()

# trees = db.search(Plant.detail.plant_type == 'Tree')
# gray_green_trees = db.search((Plant.detail.plant_type == 'Perennial') & (Plant.detail.foliage_color == 'Gray-green'))

# fast = db.search(Plant.detail.growth_rate == 'Fast')

# def get(res, key=None):
#     return sorted(set([d[key] if key is not None else d for d in res]))

# # ppr(get(gray_green_trees, key='name'))
# # ppr(get(trees, key='name'))
# ppr(get(fast, key='name'))


def count_all_of_key(section='detail', key=None):
    if key is None:
        return []
    return [
        d[section].get(key)
        for d in db.all() if d[section].get(key) is not None
    ]


def count_all_keys_of(section='detail'):
    # A throwaway record used to get keys
    if section == 'detail':
        _ = db.search(Plant.detail.blooms == 'Spring')[0]
    else:
        _ = db.search(Plant.overview.light_needs == 'Full Sun')[0]

    for attr in _[section].keys():
        counts = count_all_of_key(attr)
        s = Series(counts)
        vc = s.value_counts()
        vc = vc.sort_index()
        print('~' * 80)
        print(attr.upper() + '~' * 80)
        print('~' * 80)
        print(vc)
        print('~' * 80)
        # vc.plot(kind='bar')
        # print(Counter(counts))


def get_x_like(key, val):
    return [(r[val], r.get(key, {}))
            for r in db.all() if val in r[key]]


def get_name_like(val):
    return [(r['name'], r.get('detail', {}))
            for r in db.all() if val in r['name']]


def repl():
    while True:
        query = raw_input('Enter a plant to search: ')
        res = get_name_like(query)
        for val in res:
            print()


if __name__ == '__main__':
    repl()
