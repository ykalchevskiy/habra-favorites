BOT_NAME = 'habra_favorites'

FEED_EXPORTERS = {
    'html': 'favorites.exporters.HtmlItemExporter',
}

ITEM_PIPELINES = {
    'favorites.pipelines.FavoriteItemPipeline': 100,
}

SPIDER_MODULES = ['favorites.spiders']
