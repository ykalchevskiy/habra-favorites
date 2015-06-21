# Scrapy settings
BOT_NAME = 'favorites'

FEED_EXPORTERS = {
    'html': 'habra_favorites.exporters.HtmlItemExporter',
}

ITEM_PIPELINES = {
    'habra_favorites.pipelines.FavoriteItemPipeline': 100,
}

SPIDER_MODULES = ['habra_favorites.spiders']

# Project settings
HABRA_FAVORITES_DOMAINS = ['habrahabr.ru', 'geektimes.ru', 'megamozg.ru']
