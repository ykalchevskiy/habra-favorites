import argparse
import logging
import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import ENVVAR, get_project_settings

from . import get_version


def run_spider(args):
    username = args.username
    domain = args.domain
    file_name = args.file_name
    file_format = args.file_format

    os.environ.setdefault(ENVVAR, 'habra_favorites.settings')
    settings = get_project_settings()
    settings.set('FEED_FORMAT', file_format)
    settings.set('FEED_URI', file_name)
    settings.set('LOG_LEVEL', logging.ERROR)

    process = CrawlerProcess(settings)
    process.crawl('habra_favorites', username=username, domain=domain)
    process.start()


def parse():
    parser = argparse.ArgumentParser(
        description='Process favorites posts from Habrahabr.ru or Geektimes.ru'
    )

    parser.add_argument('username', help='Nickname')
    parser.add_argument('--version', action='version', version=get_version())
    parser.add_argument(
        '-d', '--domain',
        choices=['habrahabr.ru', 'geektimes.ru', 'megamozg.ru'],
        dest='domain',
        default='habrahabr.ru',
        help='choose DOMAIN for scrapping',
        metavar='DOMAIN',
    )
    parser.add_argument(
        '-f', '--format',
        choices=['html', 'json', 'csv', 'xml'],
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
