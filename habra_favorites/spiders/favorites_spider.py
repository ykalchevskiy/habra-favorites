from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import BaseSpider

from habra_favorites.loaders import FavoriteItemLoader


class HabraFavoritesSpider(BaseSpider):
    allowed_domains = ['habrahabr.ru']
    name = 'habra_favorites'

    def __init__(self, username=None, *args, **kwargs):
        super(HabraFavoritesSpider, self).__init__(*args, **kwargs)
        self.base_url = 'http://' + self.allowed_domains[0]
        self.start_urls = [
            '{base_url}/users/{user}/favorites/'.format(
                base_url=self.base_url,
                user=username,
            )
        ]

    def parse(self, response):
        sel = Selector(response)

        next_urls = sel.xpath('//a[@id="next_page"]/@href').extract()
        for url in next_urls:
            yield Request(self.base_url + url, self.parse)

        posts = sel.xpath('//div[contains(concat(" ", @class, " "), " post ")]')
        for post in posts:
            l = FavoriteItemLoader(selector=post)

            l.add_xpath('id_', '@id')
            l.add_xpath('ref', './/a[@class="post_title"]/@href')
            l.add_xpath('title', './/a[@class="post_title"]/text()')

            l.add_xpath('rating', './/span[@class="score"]/text()')
            l.add_xpath('rating_all', './/span[@class="score"]/@title')
            l.add_xpath('rating_up', './/span[@class="score"]/@title')
            l.add_xpath('rating_down', './/span[@class="score"]/@title')
            l.add_xpath('views', './/div[@class="pageviews"]/text()')
            l.add_xpath('count', './/div[@class="favs_count"]/text()')
            l.add_xpath('comments', './/div[@class="comments"]//span[@class="all"]/text()')

            yield l.load_item()
