"""Companion plant visualization tools."""
import sys
from collections import Counter
from pprint import pprint as ppr

import pygraphviz as pgv

from plantstuff.sources.monrovia.scraper import (
    get_companion_plant_monrovia,
    load_monrovia_data,
)


def wordcloud(detail_key='plant_type'):
    """Return a counter of details for a given key useful for creating word clouds."""
    data = load_monrovia_data()
    return Counter([
        w['detail'][detail_key].lower() for w in data
        if detail_key in w['detail']
    ])


def make_companion_plant_graph():
    """Create a companion plant graph from parsed data."""
    relationships = get_companion_plant_monrovia()
    g = pgv.AGraph()
    seen = []
    for (start, end) in relationships:
        if len(end) > 50:
            continue
        if start not in seen:
            g.add_node(start)
            seen.append(start)
        if end not in seen:
            g.add_edge(start, end)
            seen.append(end)

    g.draw('companion-plants.png', prog='circo')


if __name__ == '__main__':
    if '--companion' in sys.argv:
        make_companion_plant_graph()
    if '--wordcloud' in sys.argv:
        ppr(wordcloud())
