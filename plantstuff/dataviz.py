"""Graphing data."""

from pprint import pprint as ppr

import pygraphviz as pgv

from bokeh.plotting import figure, output_file, show

from plantstuff.sources.monrovia import (
    get_companion_plant_monrovia, load_monrovia_data,
)

# data = load_monrovia_data()
# names = [d['name'] for d in data]
# colors = [d['detail'].get('flower_color') for d in data]

# ppr(zip(names, colors))


def make_companion_plant_graph():
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


make_companion_plant_graph()
