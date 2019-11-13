import scrapy

category_mapping = {
    'plant_species': 'Lists_of_plant_species',
    'data_deficient': 'Data_deficient_plants',
    'endemic_orchids_ecuador': 'Endemic_orchids_of_Ecuador',
}


class WikipediaCategoryScraper(scrapy.Spider):
    """Scrapes any wikipedia category page."""

    name = 'wiki_category_lists'
    ROOT_CAT_URL = 'https://en.wikipedia.org/wiki/Category:'

    def start_requests(self):
        """Determine which category starting url to run."""
        for cat, urlpart in category_mapping.items():
            self.category = cat
            url = '{}{}'.format(self.ROOT_CAT_URL, urlpart)
            yield scrapy.Request(url, meta={'_ours': {'category': cat}})

    def parse(self, response):
        """Parse the response of each list category."""
        links = set(response.css('.mw-category ul li a::attr(href)').extract())
        meta = response.meta['_ours']
        for rellink in links:
            url = response.urljoin(rellink)
            next_context = {
                'category': meta['category'],
                'sublink': rellink.replace('.', '_')
            }
            yield response.follow(url,
                                  callback=self.parse_single_list_page,
                                  meta={'_ours': next_context})

    def parse_single_list_page(self, response):
        """Parse a single page listing species for a category."""
        list_of_species = response.css(
            '#mw-content-text .div-col ul li a::text').extract()
        category = response.meta['_ours']['category']
        sublink = response.meta['_ours']['sublink']
        if not list_of_species:
            yield dict(category=category,
                       sublink=sublink, name=None, species=[])
        else:
            yield dict(
                sublink=sublink,
                category=category,
                name=list_of_species[0].strip().split(' ')[0],
                species=list(set(
                    name.strip() for name in list_of_species
                    if '[' not in name and ']' not in name
                )),
            )
