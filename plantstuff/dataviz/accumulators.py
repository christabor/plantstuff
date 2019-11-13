"""Dynamic accumulator mineral distribution visualizer.

The notion of a dynamic accumulator is heavily contested (in permaculture),
but it is an interesting concept.

This provides a visualization to quickly
see the distribution of minerals and plants.
"""
import csv

from pathlib import Path

from collections import defaultdict

import pygraphviz as pgv


def get_accumulators():
    """Visualize the distribution of minerals from a csv.

    Data source credits:
        http://www.waldeneffect.org/blog/List_of_dynamic_accumulators/
        http://www.waldeneffect.org/dynamic.xls
    """
    # Just download it and convert to csv:
    csv_filepath = '../manual_data/Walden_Dynamic_Accumulators.csv'
    with open(Path(csv_filepath)) as csvfile:
        plants_reader = csv.reader(csvfile, delimiter=',')
        cols = None
        rows = []
        for i, row in enumerate(plants_reader):
            if i == 0:
                cols = row
            else:
                rows.append(row)
        return [
            dict(zip(cols, plant)) for plant in rows
        ]


def clamp_fontsize(size):
    scale = 10 * size
    return min(scale, 100)


def visualize_concentrated():
    """Show the plants based on which has the most minerals."""
    accumulators = get_accumulators()
    graph = pgv.AGraph()
    non_mineral_cols = ['Common Name', 'Scientific Name', 'Notes']
    distribution_counts = defaultdict(list)
    for plant in accumulators:
        label = f"{plant['Common Name']}\n({plant['Scientific Name']})"
        for column, value in plant.items():
            if column in non_mineral_cols:
                continue
            if value == 'x':
                distribution_counts[label].append(column)
    for plant_name, counts in distribution_counts.items():
        relative_size = clamp_fontsize(len(counts))

        graph.add_node(plant_name, shape='box', fontsize=relative_size)
    graph.draw('dynamic-accumulators-concentration.png', prog='circo')


def visualize_distribution():
    """Visualize connections between all plants and all minerals."""
    accumulators = get_accumulators()
    graph = pgv.AGraph()
    non_mineral_cols = ['Common Name', 'Scientific Name', 'Notes']
    minerals = [
        col for col in accumulators[0].keys()
        if col not in non_mineral_cols
    ]
    # Add the initial nodes before connecting them.
    for mineral_name in minerals:
        graph.add_node(mineral_name, color='green', shape='box')
    for plant in accumulators:
        label = f"{plant['Common Name']}\n({plant['Scientific Name']})"
        for column, value in plant.items():
            if column in non_mineral_cols:
                continue
            if value == 'x':
                graph.add_edge(column, label)
    graph.draw('dynamic-accumulators.png', prog='circo')


visualize_concentrated()
