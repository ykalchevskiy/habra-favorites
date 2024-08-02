from scrapy.exceptions import CloseSpider
from scrapy.spiders import Spider

from ..loaders import FavoriteItemLoader


class FavoritesSpider(Spider):
    handle_httpstatus_list = [404]
    name = 'favorites'

    def __init__(self, username, *args, **kwargs):
        super(FavoritesSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = []
        self._username = username

    def start_requests(self):
        self.allowed_domains = [self.settings['HABR_DOMAIN']]
        self.start_urls = [
            url.format(base_url=self.settings['HABR_DOMAIN'], user=self._username) for url in [
                'https://{base_url}/ru/users/{user}/bookmarks/articles/',
                'https://{base_url}/ru/users/{user}/bookmarks/news/',
            ]
        ]
        for requests in super(FavoritesSpider, self).start_requests():
            yield requests

    def parse(self, response, **kwargs):
        if response.status == 404:
            msg = 'There is no such user.'
            self.logger.error(msg)
            raise CloseSpider(msg)

        yield from response.follow_all(response.css('[data-test-id=pagination-next-page]'), self.parse)

        posts = response.css('article.tm-articles-list__item')
        for post in posts:
            l = FavoriteItemLoader(selector=post, response=response)

            l.add_xpath('id_', '@id')

            l.add_css('ref', 'a.tm-title__link::attr(href)')
            l.add_css('title', 'a.tm-title__link span::text')
            l.add_css('author', 'a.tm-user-info__username::text')
            l.add_xpath('datetime', '//time/@datetime')

            l.add_css('rating', '.tm-votes-meter__value_rating::text')
            l.add_css('rating_all', '.tm-votes-meter__value_rating::attr(title)')
            l.add_css('rating_up', '.tm-votes-meter__value_rating::attr(title)')
            l.add_css('rating_down', '.tm-votes-meter__value_rating::attr(title)')
            l.add_css('views', '.tm-icon-counter__value::text')
            l.add_css('count', '.bookmarks-button__counter::text')
            l.add_css('comments', '.tm-article-comments-counter-link__value::text')

            yield l.load_item()
