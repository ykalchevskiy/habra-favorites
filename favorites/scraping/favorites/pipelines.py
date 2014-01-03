class FavoriteItemPipeline(object):

    def process_item(self, item, spider):
        fields = ['rating', 'rating_all', 'rating_up', 'rating_down']
        for field in fields:
            if field not in item:
                item[field] = None
        return item
