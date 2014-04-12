# coding: utf-8
import re

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

from .items import FavoriteItem


RATING_REGEX = re.compile(ur'Всего (\d+): ↑([\.\d]+) и ↓([\.\d]+)', re.UNICODE)


def process_comments(value):
    try:
        return int(value)
    except ValueError:
        return 0


def process_id_(value):
    return int(value.split('_')[-1])


def process_rating(value):
    try:
        return int(value)
    except ValueError:
        try:
            return -int(value.lstrip(u'–'))
        except ValueError:
            return None


def process_rating_all(group):
    def process(value):
        m = RATING_REGEX.match(value)
        if m:
            # it may be float but we cast to int it anyway http://habrahabr.ru/post/110174/
            try:
                return int(m.group(group))
            except ValueError:
                return float(m.group(group))
    return process


class FavoriteItemLoader(ItemLoader):
    default_item_class = FavoriteItem
    default_output_processor = TakeFirst()

    id__in = MapCompose(process_id_)
    rating_in = MapCompose(process_rating)
    rating_all_in = MapCompose(process_rating_all(1))
    rating_up_in = MapCompose(process_rating_all(2))
    rating_down_in = MapCompose(process_rating_all(3))
    views_in = MapCompose(int)
    count_in = MapCompose(int)
    comments_in = MapCompose(process_comments)
