import scrapy

# TODO: THIS SITE USES JS TO RENDER EVERYTHING;
# https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash


class PlantLustTypeCategoryScraper(scrapy.Spider):
    """Scrapes any plant 'type' category page."""

    def parse_single_page(self, response):
        """Parse a single page for a plant."""
        list_of_species = response.css(
            '#mw-pages .div-col ul li a::text').extract()
        yield dict(
            name=list_of_species[0].strip().split(' ')[0],
            species=[
                name.strip() for name in list_of_species
                if '[' not in name and ']' not in name
            ],
        )

    def pagination(self, response):
        """Return pagination.

        Plantlust is nice, it tells exactly how many pages there are total
        right in the DOM.
        """
        page_links = response.css(
            '.searchpage__pagination li a::text').extract()
        indices = [int(page) for page in page_links if page.strip() != '...']
        raise Exception
        return range(0, indices + 1)

    def follow_page_links(self, response):
        """Follow the link for each plant item on a results page."""
        heading_link_css = (
            '.searchpage__results .plant__name_cont h2 a::attr(href)'
        )
        links = response.css(heading_link_css).extract()
        for url in links:
            yield response.follow(url, callback=self.parse_single_page)

    def parse(self, response):
        """Parse the response."""
        for page in self.pagination(response):
            url = response.urljoin('&page=' + page)
            yield response.follow(url, callback=self.follow_page_links)


class CactusSucculentScraper(PlantLustTypeCategoryScraper):
    """Get all plants in the cactus/succulent category."""

    name = 'plantlust_cactus_succulents'

    start_urls = [
        'https://plantlust.com/search/#/attribute=Plant+Type&val=aroid',
    ]
