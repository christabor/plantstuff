# -*- coding: utf-8 -*-

"""Items that are meant to be used either directly or indirectly
as database records.

For scrapy models, see documentation in:
https://doc.scrapy.org/en/latest/topics/items.html
"""

import scrapy


class Plant(scrapy.Item):
    """Plant DB item."""

    name = scrapy.Field()
    latin_name = scrapy.Field()
    cultivar = scrapy.Field()
    botanical_name = scrapy.Field()

    hardiness_zone = scrapy.Field()
    spread = scrapy.Field()
    pruning = scrapy.Field()
    light_needs = scrapy.Field()
    plant_type = scrapy.Field()
    growth_rate = scrapy.Field()
