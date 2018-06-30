"""Utilities for working with and understanding the db schema."""
import importlib
import inspect
import os
import pkgutil

import pygraphviz as pgv

from plantstuff import schema


def get_all_schemas():
    """Get all schema classes for the schema module."""
    pkg_dir = os.path.dirname(schema.__file__)
    mapping = {}
    for (module_loader, mod_name, is_pkg) in pkgutil.iter_modules([pkg_dir]):
        if mod_name not in ['schema_testing', 'graph_schema']:
            module = importlib.import_module(mod_name)
            members = inspect.getmembers(module)
            members = [
                (name, obj) for (name, obj) in members
                if inspect.isclass(obj) and obj.__module__ == mod_name
            ]
            mapping[mod_name] = members
    return mapping


def get_model_fields(cls_obj):
    """Extract the raw data from the mode cls."""
    return [
        (k, v) for k, v in cls_obj.__dict__.items() if not k.startswith('_')
    ]


def make_schema_graph():
    """Make a visualization of all the schema classes and their fields.

    This does NOT follow any relationships defined in the schemas.

    See https://www.graphviz.org/doc/info.
    """
    data = get_all_schemas()
    graph = pgv.AGraph(directed=True, splines='curved')
    for pkg, klasses in data.items():
        for (cls_name, cls_obj) in klasses:
            graph.add_node(cls_name,
                           fillcolor='#B8EAC6',
                           style='filled',
                           fontsize=30 if cls_name == 'Plant' else 16,
                           shape='folder')
            subgraph = graph.add_subgraph([cls_name], name=cls_name)
            for field, _ in get_model_fields(cls_obj):
                uniq_label = '{}:{}'.format(cls_name, field)
                subgraph.add_node(uniq_label,
                                  label=field,
                                  fontsize=14,
                                  shape='tab')
                subgraph.add_edge(cls_name, uniq_label,
                                  color='#cccccc',
                                  shape='note')

    graph.layout()
    graph.draw('graph_schema.png', prog='circo')


if __name__ == '__main__':
    make_schema_graph()
