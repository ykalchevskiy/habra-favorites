# coding: utf-8
from datetime import datetime
import re

from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from .items import FavoriteItem

RATING_REGEX = re.compile(r'Всего (\d+): ↑([.\d]+) и ↓([.\d]+)', re.U)


def urljoin(url, loader_context):
    response = loader_context.get('response')
    return response.urljoin(url)


def process_datetime(value):
    return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d %H:00')


def process_rating(value):
    try:
        return int(value)
    except ValueError:
        try:
            return -int(value.lstrip('–'))
        except ValueError:
            return None


def process_rating_all(group):
    def process(value):
        m = RATING_REGEX.match(value)
        if m:
            # it may be a float, but we cast to an int it anyway http://habrahabr.ru/post/110174/
            try:
                return int(m.group(group))
            except ValueError:
                return float(m.group(group))
    return process


def process_views(value):
    try:
        return int(value)
    except ValueError:
        if value.endswith('K'):
            return int(float(value.rstrip('K').replace(',', '')) * 1000)
        else:
            return None


class FavoriteItemLoader(ItemLoader):
    default_item_class = FavoriteItem
    default_output_processor = TakeFirst()

    id__in = MapCompose(int)
    ref_in = MapCompose(urljoin)
    datetime_in = MapCompose(process_datetime)
    rating_in = MapCompose(process_rating)
    rating_all_in = MapCompose(process_rating_all(1))
    rating_up_in = MapCompose(process_rating_all(2))
    rating_down_in = MapCompose(process_rating_all(3))
    views_in = MapCompose(process_views)
    count_in = MapCompose(int)
    comments_in = MapCompose(int)
