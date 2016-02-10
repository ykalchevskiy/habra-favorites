# coding: utf-8
from datetime import datetime, timedelta
import re

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

from .items import FavoriteItem


DATETIME_FORMAT = '{:%Y-%m-%d %H:%M}'
DATETIME_TODAY = re.compile(ur'сегодня в (?P<hour>\d+):(?P<minute>\d+)', re.U)
DATETIME_YESTERDAY = re.compile(ur'вчера в (?P<hour>\d+):(?P<minute>\d+)', re.U)
DATETIME_COMMON = re.compile(
    ur'(?P<day>\d+) (?P<month>\w+)\s?(?P<year>\d+)? в (?P<hour>\d+):(?P<minute>\d+)',
    re.UNICODE
)
MONTHS = (u'января', u'февраля', u'марта', u'апреля', u'мая', u'июня',
          u'июля', u'августа', u'сентября', u'октября', u'ноября', u'декабря')
MONTH_CODE = dict(zip(MONTHS, xrange(1, 13)))
NOW = datetime.today()
RATING_REGEX = re.compile(ur'Всего (\d+): ↑([\.\d]+) и ↓([\.\d]+)', re.U)


def _convert_values_to_int(dct):
    for k, v in dct.iteritems():
        dct[k] = int(v)


def process_comments(value):
    try:
        return int(value)
    except ValueError:
        return 0


def process_datetime(value):
    u"""
    >>> PSEUDO_NOW = NOW.replace(hour=17, minute=27)

    >>> process_datetime(u'25 ноября 1991 в 07:07')
    '1991-11-25 07:07'

    >>> process_datetime(u'1 января 1970 в 00:00')
    '1970-01-01 00:00'

    >>> process_datetime(u'8 мая в 17:27')  #doctest: +ELLIPSIS
    '201...-05-08 17:27'

    >>> process_datetime(u'сегодня в 17:27') == DATETIME_FORMAT.format(PSEUDO_NOW)
    True

    >>> process_datetime(u'вчера в 17:27') == DATETIME_FORMAT.format(PSEUDO_NOW - timedelta(days=1))
    True
    """
    value = value.strip()
    m = DATETIME_COMMON.match(value)
    if m:
        dt = m.groupdict()
        if not dt['year']:
            dt['year'] = NOW.year
        dt['month'] = MONTH_CODE[dt['month']]
        _convert_values_to_int(dt)
        return DATETIME_FORMAT.format(datetime(**dt))

    m = DATETIME_YESTERDAY.match(value)
    if m:
        dt = m.groupdict()
        _convert_values_to_int(dt)
        return DATETIME_FORMAT.format(NOW.replace(**dt) - timedelta(1))

    m = DATETIME_TODAY.match(value)
    if m:
        dt = m.groupdict()
        _convert_values_to_int(dt)
        return DATETIME_FORMAT.format(NOW.replace(**dt))
    return '?'


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


def process_views(value):
    try:
        return int(value)
    except ValueError:
        if value.endswith('k'):
            return int(value.rstrip('k').replace(',', '')) * 1000
        else:
            return None


class FavoriteItemLoader(ItemLoader):
    default_item_class = FavoriteItem
    default_output_processor = TakeFirst()

    id__in = MapCompose(process_id_)
    datetime_in = MapCompose(process_datetime)
    rating_in = MapCompose(process_rating)
    rating_all_in = MapCompose(process_rating_all(1))
    rating_up_in = MapCompose(process_rating_all(2))
    rating_down_in = MapCompose(process_rating_all(3))
    views_in = MapCompose(process_views)
    count_in = MapCompose(int)
    comments_in = MapCompose(process_comments)
