import scrapy


# This package
from scrapers.formatters import (
    labelize,
    maybe_lower,
)


# TODO - not done!


class PerennialsComPlants(scrapy.Spider):

    name = 'perennials_com'
    ROOT_URL = 'http://www.perennials.com'
    start_urls = [
        'http://www.perennials.com/results.html',
    ]

    def parse_grid(self, response):
        """Parse cols and rows for grid of results."""
        for row in response.css('.row-fluid.text-left'):
            for plant in row.css('.fixsearchsmall'):
                url = plant.css('a::attr(href)').extract_first()
                yield response.follow(url, callback=self.parse_plant_details)

    def parse_plant_details(self, response):
        """Parse cols and rows for grid of results."""
        title = response.css('.page-title h1 .plant-name')
        features = response.css('.fieldgroup.group-features .content .field')
        chars_groups = response.css(
            '.fieldgroup.group-characteristics .content .field')
        needs_group = response.css('.fieldgroup.group-needs .content .field')

        def extract_group(container):
            vals = {}
            for field in container:
                item = ' '.join(field.css('.field-item::text').extract())
                label = field.css(
                    '.field-label-inline-first::text').extract_first()
                if item is None or label is None:
                    continue
                item, label = item.strip(), label.strip()
                item = item.replace('\n', '').replace('  ', ' ')
                label = labelize(label)

                if label == 'light_requirement':
                    item = item.split(' to ')
                if label in [
                    'soil_fertility_requirement',
                    'soil_ph_category',
                    'bloom_time',
                ]:
                    item = item.split('  ')
                if label in [
                    'foliage_colors',
                    'hardiness_zones', 'uses',
                ]:
                    item = [x.lower() for x in item.split(' ')]
                if isinstance(item, list):
                    item = [token.strip() for token in item if token.strip()]
                vals[label] = item
            return vals

        yield {
            'url': response.url,
            'genus': maybe_lower(title.css(
                '.genus-species .genus em::text').extract_first()),
            'species': maybe_lower(title.css(
                '.genus-species .species em::text').extract_first()),
            'variety': ' '.join(
                title.css('.series-variety span strong::text').extract() +
                title.css('.series-variety .variety::text').extract()
            ),
            'common_name': title.css(
                '.common-name::text').extract_first(),
            'features': extract_group(features),
            'characteristics': extract_group(chars_groups),
            'needs': extract_group(needs_group),
        }

    def pagination(self, response):
        """Extract the pagination range for a given category."""
        last_page = response.css(
            '.item-list ul li.pager-item a::text').extract()
        last_page = last_page[-1]
        last_page = int(last_page.strip())
        # Normally we would start at 1, but provenwinners
        # has funky pagination where the url offset is different
        # than the displayed text.
        return 0, last_page

    def parse(self, response):
        """Parse the response."""
        pages = response.css('.paging .item-list ul.pages')
        rel_url = pages.css(
            'li a::attr(href)').extract_first().split('?')[0:-1]
        rel_url = ''.join(rel_url)
        first, last = self.pagination(response)
        for page_num in range(first, last):
            yield response.follow('{}?page={}'.format(rel_url, page_num),
                                  callback=self.parse_grid)
