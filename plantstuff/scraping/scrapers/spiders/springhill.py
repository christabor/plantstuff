import scrapy


# This package
from scrapers.formatters import (
    labelize,
    tokenize,
)


class SpringHillNursery(scrapy.Spider):

    name = 'springhill'
    ROOT_URL = 'https://www.springhillnursery.com'

    def start_requests(self):
        """Determine which category starting url to run."""
        cats = [
            'perennial_plants',
            'flowering_fast_growing_trees',
            'shrubs_hedges',
            'vines_climbers',
            'flower_bulbs',
            'rose_plants',
            'edibles',
            'annuals',
        ]
        has_cat = hasattr(self, 'category')
        if has_cat and self.category not in cats:
            raise ValueError('Invalid category')
        to_fetch = cats if not has_cat else [self.category]
        for cat in to_fetch:
            self.category = cat
            url = '{}/category/{}/a'.format(self.ROOT_URL, cat)
            yield scrapy.Request(url, meta={'_ours': {'category': cat}})

    def parse_plant_details(self, response):
        """Parse plant details."""

        def extract_group(container):
            keys = [
                labelize(k) for k
                in container.css('li span strong::text').extract()
            ]
            vals = container.css('li span::text').extract()
            data = dict(zip(keys, vals))
            for k, v in data.items():
                if k == 'restricted_states':
                    data[k] = tokenize(v)
            return data

        data = {
            'url': response.url,
            'category': response.meta['_ours']['category'],
        }
        data.update(extract_group(response.css('.product_info .info_list_A')))
        data.update(extract_group(response.css('.product_info .info_list_B')))
        yield data

    def parse(self, response):
        """Parse the response."""
        for plant in response.css('.category_page_products ul li'):
            url = plant.css('.prod_thumb h2 a::attr(href)').extract()[-1]
            yield response.follow(url,
                                  callback=self.parse_plant_details,
                                  meta={'_ours': response.meta['_ours']})
