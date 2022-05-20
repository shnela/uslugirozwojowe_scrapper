# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

from openpyxl import Workbook


class ParpPipeline:
    def process_item(self, item, spider):
        logging.info(item)
        return item


class WriteToXlsx(object):
  def open_spider(self, spider):
    self.workbook = Workbook()
    self.worksheet = self.workbook.active
    self.worksheet.page_setup.fitToWidth = 1
    self.keys_initialized = False

  def close_spider(self, spider):
    filename = f'out/{spider.name}.xlsx'
    self.workbook.save(filename)

  def process_item(self, item, spider):
    if not self.keys_initialized:
      self.worksheet.append(list(item.keys()))
      self.keys_initialized = True
    vlaues = [str(value) for value in item.values()]
    self.worksheet.append(vlaues)
    return item