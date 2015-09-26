# coding: utf-8
from scrapy.item import Item, Field


class FavoriteItem(Item):
    id_ = Field()
    ref = Field()
    title = Field()
    datetime = Field()
    author = Field()

    # Статистика
    rating = Field()  # рейтинг
    rating_all = Field()  # кол-во всех голосов
    rating_up = Field()  # кол-во голосов "за"
    rating_down = Field()  # кол-во голосов "против"
    views = Field()  # кол-во просмотров
    count = Field()  # кол-во добавлений
    comments = Field()  # кол-во комментариев
