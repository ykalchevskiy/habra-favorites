import os

from scrapy.exporters import JsonItemExporter


class HtmlItemExporter(JsonItemExporter):

    TEMPLATE = 'base.html'

    def __init__(self, file_, **kwargs):
        super(HtmlItemExporter, self).__init__(file_, **kwargs)
        self.file.seek(os.SEEK_SET)
        self.file.truncate()
        with open(os.path.join(os.path.dirname(__file__), 'templates', self.TEMPLATE), encoding='utf-8') as f:
            self.file_start, self.file_finish = f.read().split('// ITEMS')

    def start_exporting(self):
        self.file.write(self.file_start.encode('utf-8'))

    def finish_exporting(self):
        self.file.write(self.file_finish.encode('utf-8'))
