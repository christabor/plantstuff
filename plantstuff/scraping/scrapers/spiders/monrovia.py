from string import ascii_uppercase

import scrapy

# TODO - not done!


class MonroviaAlpahbetical(scrapy.Spider):
    name = "monrovia"
    root_url = 'https://www.monrovia.com'

    def start_requests(self):
        """Dynamically generate urls."""
        for letter in list(ascii_uppercase):
            yield scrapy.Request(
                '{}/plant-catalog/search?botanical_name={}'
                '&sort_by=botanical_name'.format(self.root_url, letter))

    def parse(self, response):
        """Parse the response."""
        for plant in response.css('.list-plant'):
            spans = plant.css('span').extract()
            details = [
                s.replace('<span>', '').replace('</span>', '').strip()
                for s in spans if not any([
                    'Add to' not in s,
                    'Buy Online' not in s,
                    'Item #' not in s,
                ])
            ]
            yield {
                'url': plant.css('a::attr(href)').extract_first(),
                'name': plant.css('span::text').extract_first(),
                'details': details,
            }
