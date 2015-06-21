from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider

from ..loaders import FavoriteItemLoader


class FavoritesSpider(Spider):
    handle_httpstatus_list = [404]
    name = 'favorites'

    def __init__(self, domain, username, *args, **kwargs):
        super(FavoritesSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = []
        self._domain = domain
        self._username = username

    def start_requests(self):
        all_domains = self.settings['HABRA_FAVORITES_DOMAINS']
        self.allowed_domains = all_domains if self._domain == 'all' else [self._domain]
        self.start_urls = ['http://{base_url}/users/{user}/favorites/'.format(
            base_url=domain,
            user=self._username,
        ) for domain in self.allowed_domains]
        for requests in super(FavoritesSpider, self).start_requests():
            yield requests

    def parse(self, response):
        if response.status == 404:
            msg = 'There is no such user.'
            self.logger.error(msg)
            raise CloseSpider(msg)

        sel = Selector(response)

        next_urls = sel.xpath('//a[@id="next_page"]/@href').extract()
        for url in next_urls:
            yield Request(response.urljoin(url), self.parse)

        posts = sel.xpath('//div[contains(concat(" ", @class, " "), " post ")]')
        for post in posts:
            l = FavoriteItemLoader(selector=post)

            l.add_xpath('id_', '@id')
            l.add_xpath('ref', './/a[@class="post_title"]/@href')
            l.add_xpath('title', './/a[@class="post_title"]/text()')
            l.add_xpath('datetime', './/div[@class="published"]/text()')

            l.add_xpath('rating', './/span[@class="score"]/text()')
            l.add_xpath('rating_all', './/span[@class="score"]/@title')
            l.add_xpath('rating_up', './/span[@class="score"]/@title')
            l.add_xpath('rating_down', './/span[@class="score"]/@title')
            l.add_xpath('views', './/div[@class="pageviews"]/text()')
            l.add_xpath('count', './/div[@class="favs_count"]/text()')
            l.add_xpath('comments', './/div[@class="comments"]//span[@class="all"]/text()')

            yield l.load_item()
