from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from my_scrapy.my_scrapy.spiders.notices import TestSpider, NoticeSpider

process = CrawlerProcess(get_project_settings())
process.crawl(NoticeSpider) # here have to change the name to NoticeSpider
process.start()