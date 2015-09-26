class FavoriteItemPipeline(object):

    def __init__(self):
        self.fields = ['rating', 'rating_all', 'rating_up', 'rating_down']

    def process_item(self, item, _spider):
        for field in self.fields:
            if field not in item:
                item[field] = None
        return item
