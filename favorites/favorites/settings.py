BOT_NAME = 'habra_favorites'

ITEM_PIPELINES = {
    'favorites.pipelines.FavoriteItemPipeline': 100,
}

SPIDER_MODULES = ['favorites.spiders']
