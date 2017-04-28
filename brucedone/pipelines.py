# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class BrucedonePipeline(object):
    def _init_(self):
        self.file = codecs.open('brucedone.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        return item
