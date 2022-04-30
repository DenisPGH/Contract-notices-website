# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class MyScrapyItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class NoticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # only one field that it of Quote.
    Notice = scrapy.Field()
    Name = scrapy.Field()
