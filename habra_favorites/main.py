import argparse
import os

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.utils.project import ENVVAR, get_project_settings
from twisted.internet import reactor

from . import get_version
from spiders.favorites_spider import HabraFavoritesSpider


def run_spider(args):
    username = args.username
    file_name = args.file_name
    file_format = args.file_format

    os.environ.setdefault(ENVVAR, 'habra_favorites.settings')
    settings = get_project_settings()
    settings.overrides['FEED_FORMAT'] = file_format
    settings.overrides['FEED_URI'] = file_name

    spider = HabraFavoritesSpider(username=username)
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    reactor.run()


def parse():
    parser = argparse.ArgumentParser(
        description='Process favorites posts from Habrahabr.ru'
    )

    parser.add_argument('username', help='Nickname on Habrahabr.ru')
    parser.add_argument('--version', action='version', version=get_version())
    parser.add_argument(
        '-f', '--format',
        choices=['html', 'json'],
        dest='file_format',
        default='html',
        help='choose FORMAT of the result file',
        metavar='FORMAT',
    )
    parser.add_argument(
        '-o', '--output',
        default='favorites.html',
        dest='file_name',
        help='choose NAME for the result file',
        metavar='NAME',
    )

    return parser.parse_args()


def main():
    run_spider(parse())


if __name__ == '__main__':
    main()
