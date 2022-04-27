import json

import scrapy


class NoticesSpider(scrapy.Spider):
    #user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
    #coockie="isCompact=true; culture=en-US; _HttpSessionID=35E93C04EB154DDBB374AACA43484AD2; sysNoticeTypeIds=null"
    #handle_httpstatus_list = [404, 403, 400]
    name = 'notices'
    allowed_domains = ['e-licitatie.ro']
    #allowed_domains = ['quotes.toscrape.com']
    #start_urls = ['https://www.e-licitatie.ro/views/common/notices/common/service.min.js?_=1651054814609']
    #start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']
    start_urls=['http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/']


    def parse(self, response,**kwargs):
        #strrr=response.css("div.u-items-list__item_properties::text").extract()
        #strrr=response.css('span.ng-binding::text').extract()
        #strrr=response.xpath('/html/body/div[1]/div/div[2]/div/div[5]/div[9]/div[2]/div[1]/div').extract()
        print()
        print()
        print()
        #strrr=response.css('#container-sizing > div.u-items-list > div.u-items-list__content').getall()
        #strrr=response.css('.u-items-list__content').extract()
        #strrr=response.xpath('//*[@id="container-sizing"]/div[9]/div[2]').get()
        #date=json.loads(response.body)
        print(response.body)
        #strrr=date
        #print(f"=====D E N I S L A V==={str(strrr)}")
        print()
        print()
        print()

        # with open("test.txt", "w") as outfile:
        #     outfile.write(str(strrr))
        # # #pass
        # yield {'=====D E N I S L A V':str(strrr)}

        # for title in response.css('.u-items-list__content'):
        #     dict_ = {'title': title.css('::text').get()}
        #     print(f"this: {dict_['title']}")
        #     yield {'title': title.css('::text').get()}




# class NoticesSpider(scrapy.Spider):
#     name = "notices"
#     start_urls = [
#             'http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/',
#         ]
#
#     def parse(self, response,**kwargs):
#         print(response.css('items'))
#         for quote in response.css("items"):
#              yield {
#                 'text': quote.css("s").extract_first(),
#                 }

#


# import scrapy
#
#
# class QuotesSpider(scrapy.Spider):
#     name = "notices"
#
#     def start_requests(self):
#         urls = [
#             'http://www.e-licitatie.ro',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response,**kwargs):
#         #page = response.url.split("/")[-2]
#         page = response.css['items']
#         filename = f'quotes-{page}.html'
#         dictionary={"1":page}
#         with open("test.json", "w") as outfile:
#             json.dump(dictionary, outfile)
#         # with open(filename, 'wb') as f:
#         #     f.write(response.body)
#         # self.log(f'Saved file {filename}')



from scrapy.http import request
from scrapy.http.request.form import FormRequest
from scrapy.http import FormRequest


# class CodeSpider(scrapy.Spider):
#     name = 'code'
#     allowed_domains = ['code.comcom']
#     start_urls = ['https://technet.rapaport.com/HTTP/JSON/RetailFeed/GetDiamonds.aspx']
#
#     def start_requests(self):
#         form_data = {"request":{"header":{"raplink_access_key":"e7d7d61946804c579d02dab565371113","domain":"www.sarvadajewels.com"},"body":{"search_type":"white","shapes":["round"],"size_from":0.1,"size_to":100,"color_from":"D","color_to":"M","clarity_from":"IF","clarity_to":"I1","cut_from":"Excellent","cut_to":"Poor","polish_from":"Excellent","polish_to":"Poor","symmetry_from":"Excellent","symmetry_to":"Poor","labs":[],"fancy_colors":[],"price_total_from":0,"price_total_to":7428404930,"page_number":2,"page_size":"60","sort_by":"price","sort_direction":"asc","currency_code":"INR"}}}
#         request_body = json.dumps(form_data)
#         yield scrapy.Request('https://technet.rapaport.com/HTTP/JSON/RetailFeed/GetDiamonds.aspx',
#                             method="POST",
#                             body=request_body,
#                             headers={'Content-Type': 'application/x-www-form-urlencoded'},callback=self.parse )
#
#     def parse(self, response,**kwargs):
#         yield json.loads(response.text)
