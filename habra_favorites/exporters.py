# coding: utf-8
import os

from scrapy.contrib.exporter import JsonItemExporter


class HtmlItemExporter(JsonItemExporter):

    TEMPLATE = 'base.html'

    def __init__(self, file_, **kwargs):
        super(HtmlItemExporter, self).__init__(file_, **kwargs)
        self.file.seek(0)
        self.file.truncate()
        with open(os.path.join(os.path.dirname(__file__), 'templates', self.TEMPLATE)) as f:
            self.file_start, self.file_finish = f.read().split('// ITEMS')

    def start_exporting(self):
        self.file.write(self.file_start)

    def finish_exporting(self):
        self.file.write(self.file_finish)
