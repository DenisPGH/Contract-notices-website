from scrapy import Spider

class MyDemoSpider(Spider):

    handle_httpstatus_list = [404,403,400]
    print('start')
    name = 'spider'
    dict_={}
   # allowed_domains = ["e-licitatie.ro",]
    #start_urls = ['http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1']
    start_urls = ['http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/']


    def parse(self, response,**kwargs):


        print(self.name)
        print(response)
        print(**kwargs)
        for title in response.css('.u-items-list__content'):
            #yield {'title': title.css('::text').get()}
            dict_= {'title': title.css('::text').get()}
            print(f"this: {dict_['title']}")

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)

    print('stop')
    print(dict_)


