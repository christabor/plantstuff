"""Functions that map scraped schemas to the new format for ingestion.

Why? This makes writing scrapers and other tools independent of the db,
so there is no need to normalize it there. Instead, we scrape or otherwise
retrieve data in its native schema, then normalize it here.

This layer of indirection also makes it easier to change things up in case
the schema needs to change.
"""


def map_daves_data(plant_chunk):
    """Map data to the new format.

    Args:
        plant_chunk (dict): The plant specific data.

    Returns:
        dict: The new data, formatted to fit the schema. Any missing fields
        will simply be None.
    """


def map_monrovia_data(plant_chunk):
    """Map data to the new format.

    Args:
        plant_chunk (dict): The plant specific data.

    Returns:
        dict: The new data, formatted to fit the schema. Any missing fields
        will simply be None.
    """
    mappings = {
        'overview::light_needs': 'growth_requirements::aspect',
        'detail::plant_type': 'ecology::duration',
    }
    newdata['growth_requirements']['aspect'] = plant_chunk['overview']['light_needs']
    newdata['growth_requirements']['aspect'] = plant_chunk['overview']['light_needs']
    return newdata


def map_usda_data(plant_chunk):
    """Map data to the new format.

    Args:
        plant_chunk (dict): The plant specific data.

    Returns:
        dict: The new data, formatted to fit the schema. Any missing fields
        will simply be None.
    """


def map_uconn_data(plant_chunk):
    """Map data to the new format.

    Args:
        plant_chunk (dict): The plant specific data.

    Returns:
        dict: The new data, formatted to fit the schema. Any missing fields
        will simply be None.
    """


def map_wikipedia_data(plant_chunk):
    """Map data to the new format.

    Args:
        plant_chunk (dict): The plant specific data.

    Returns:
        dict: The new data, formatted to fit the schema. Any missing fields
        will simply be None.
    """


def map_springhills_data(plant_chunk):
    """Map data to the new format.

    Args:
        plant_chunk (dict): The plant specific data.

    Returns:
        dict: The new data, formatted to fit the schema. Any missing fields
        will simply be None.
    """
