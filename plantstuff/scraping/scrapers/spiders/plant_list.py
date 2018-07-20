"""Spiders for theplantlist.org."""

import csv

# Third-party
import scrapy

# This package
from scrapers.formatters import (
    labelize,
)


class GroupSpider(scrapy.Spider):
    """General spider for all major plant groups."""

    name = 'plantlist'
    ROOT_URL = 'http://www.theplantlist.org'

    def parse_csv(self, response):
        """Convert the csv response into a list of dicts."""
        cr = csv.reader(response.body.splitlines(), delimiter=',')
        cr = list(cr)
        headers = [labelize(item) for item in cr[0]]
        rows = cr[1:]
        yield {response.meta['_ours']['family']: [
            dict(zip(headers, [labelize(field) for field in row]))
            for row in rows
        ]}

    def get_species_csv_list(self, response):
        """Download and parse out the csv list contents."""
        url = response.css('section p.clear a::attr(href)').extract_first()
        yield response.follow(url,
                              callback=self.parse_csv,
                              meta={'_ours': response.meta['_ours']})

    def get_species(self, url, meta):
        """Get the link to the csv species list."""
        return scrapy.Request('{}{}'.format(self.ROOT_URL, url),
                              callback=self.get_species_csv_list,
                              meta={'_ours': meta})

    def start_requests(self):
        """Determine which category starting url to run."""
        cats = {
            'angiosperms': 'A',
            'gymnosperms': 'G',
            'bryophytes': 'B',
            'pteridophytes': 'P',
        }
        if not hasattr(self, 'category'):
            self.category = 'pteridophytes'
        if self.category not in cats.keys():
            raise ValueError('Invalid category! Choose from: {}'.format(
                ', '.join(cats.keys())
            ))
        url = '{}/1.1/browse/{}'.format(self.ROOT_URL, cats[self.category])
        yield scrapy.Request(url)

    def parse(self, response):
        """Get the list of families for each major group."""
        for family in response.css('#nametree li'):
            url = family.css('a::attr(href)').extract_first()
            group = response.css('.bread .majorgroup::text').extract_first()
            family = family.css('a i::text').extract_first()
            meta = dict(
                group=group.lower(),
                family=family.lower(),
                genera_url=url,
            )
            yield self.get_species(url, meta)
