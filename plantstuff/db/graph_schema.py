"""Describing the core schema in terms of a graph.

This is meant to be used in conjunction with graph rendering software,
or generated as a stand-alone image.

The goal is to visually edit and inspect the graph but store it as a
structured text format for easier retrieval and version control.
"""

import pygraphviz as pgv

core_schema = u"""
digraph plantdb {
    RANKDIR=LR;
    plant -> taxonomy;
    taxonomy -> division;
}
"""


graph = pgv.AGraph()
graph.render(core_schema)
graph.draw('plantdb_graph_schema.png', prog='circo')
