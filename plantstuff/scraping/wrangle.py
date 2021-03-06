"""Data to wrangle together disparate sources."""

import json
import subprocess

from plantstuff.scraper_utils.decorators import to_json

DATA_SOURCES = [
    'daves',
    'monrovia',
    'plantsdb',
    'uconn',
    'springhills',
]


def get_shell(cmd):
    """Get return stdout from a shell command."""
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    return proc.stdout.read()


def search_files(plant_name, filetype=None):
    """Try to build a set of info from all known sources of data."""
    # Try each variation of spaces, as a sort of fuzzy search.
    # Kind of lame, but it sort of works.
    res = get_shell('ag "{} " -l data/'.format(plant_name)).split('\n')
    if filetype is not None:
        res = [f for f in res if f.endswith(filetype)]
    return list(set(res))


def search_all_json(dossier, token):
    """Try to build a set of info from all known sources of json data."""
    for source in DATA_SOURCES:
        dossier[source] = {}
    files = search_files(token, filetype='.json')
    # Db is recreated and very large. TODO: better organize/conventions.
    # _all_ typically means a group of combined datasets,
    # which is very large and redundant - TODO: also make this better.
    files = [f for f in files if '_db' not in f and '_all_' not in f]
    for file in files:
        # File format is data/<source>/fname
        source = file.split('/')[1]
        if source not in dossier:
            continue
        with open(file, 'r') as data:
            dossier[source][file] = json.loads(data.read())
    return dossier


@to_json()
def search_all_json_by_name(plant_name):
    """Try to build a set of info from all known sources of json data."""
    dossier = {'given': plant_name.lower()}
    return search_all_json(dossier, '{}'.format(plant_name))


@to_json()
def search_all_json_by_code(code):
    """Try to build a set of info from all known sources of json data."""
    dossier = {'given': code}
    return search_all_json(dossier, code)


if __name__ == '__main__':
    # search_files('alder')
    # search_all_json_by_name('alder')
    search_all_json_by_name('echinacea')
    # search_all_json_by_code('ABJA')
