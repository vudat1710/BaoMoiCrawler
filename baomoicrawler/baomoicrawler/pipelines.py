# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from baomoicrawler.exporters import JsonItemExporter
import json, codecs
from scrapy.exceptions import CloseSpider

class BaomoicrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open("data_week_temp.json", 'w', encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, indent=4) + ",\n"
        self.file.write(line)
        return item
