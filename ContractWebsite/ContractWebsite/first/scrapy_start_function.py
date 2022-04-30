import scrapy
from scrapy.crawler import CrawlerProcess
# class TestSpider(scrapy.Spider):
#     name = 'test'
from my_scrapy.my_scrapy.spiders.notices import TestSpider

if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(TestSpider)
  process.start()
  # pass