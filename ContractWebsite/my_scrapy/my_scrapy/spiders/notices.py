import json
import random
import re

import scrapy
from  scrapy import FormRequest
from ..items import  NoticeItem

import os
import sys
sys.path.insert(0, 'C:\\Users\\Owner\\Desktop\\Test-Website\\Contract-notices-website\\ContractWebsite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ContractWebsite.settings')
import django
django.setup()


from ContractWebsite.first.models import Notice as N
from ContractWebsite.visual.models import DateModel
from chompjs import chompjs
import js2xml
import lxml.etree
from parsel import Selector

class TestSpider(scrapy.Spider):
    """ Test spider for crawling from test url"""
    name = 'test'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response,**kwargs):
        items = NoticeItem()
        Notice_all = response.xpath('//div/div/div/span[1]')
        for single_notice in Notice_all:  # extracting data
            data=[['2022-04-30'],['a'],[f"deni{random.randint(0,10)}"],["c"],['d'],['e'],[20],['g']]
            items['Notice'] = single_notice.css('::text').extract()
            items['date'] = data[0]
            items['notice_number']=data[1]
            items['tender_name']=data[2]
            items['procedure_state']=data[3]
            items['contract_type']=data[4]
            items['type_of_procurement']=data[5]
            items['estimated_value']=data[6]

            # if not in db django store it!!!!
            if data[2][0] not in N.objects.values_list('tender_name', flat=True).distinct():
                new_notice = N(
                    date=data[0][0],
                    notice_number=data[1][0],
                    tender_name=data[2][0],
                    procedure_state=data[3][0],
                    contract_type=data[4][0],
                    type_of_procurement=data[5][0],
                    estimated_value=data[6][0],
                )
                new_notice.save()
            yield items




class NoticeSpider(scrapy.Spider):
    """
    this should be main spider,
    but couldn't find the right solution for crawling the items from the website
    """
    name = "notices"
    start_urls = ["http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1"]
    #start_urls = [" http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"]
    headers_others = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer null',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '101',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'culture=en-US; isCompact=true; _HttpSessionID=5BF1B10EBD394BD8B5B99ED472BD854E; sysNoticeTypeIds=null',
        'Culture': 'en-US',
        'Host': 'www.e-licitatie.ro',
        'HttpSessionID': 'null',
        'Origin': 'http://www.e-licitatie.ro',
        'Pragma': 'no-cache',
        'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1RefreshToken: null',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
    }
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        #'Content-Type': 'application/x-www-form-urlencoded',
    }
    def parse(self,response,**kwargs):
        last_time_request=DateModel.objects.all().last() # got the last gived data period for using in crawl

        PAYLOAD={
                "sysNoticeTypeIds": [],
                "sortProperties": [],
                "pageSize": 5,
                "hasUnansweredQuestions": False,
                "startPublicationDate": "2022-05-01T06:14:48.809Z",
                "startTenderReceiptDeadline": f"{str(last_time_request.start_date)}T06:14:48.810Z",
                "sysProcedureStateId": 2,
                "pageIndex": 0,
                "endTenderReceiptDeadline": f"{str(last_time_request.end_date)}T21:00:00.000Z"
        }

        request=scrapy.Request(url=' http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/',
                       method='POST',
                       callback=self.parse,
                       headers=self.headers,
                       body=json.dumps(PAYLOAD),
                       )


        #print(f"Content type====={response.headers.getlist('Content-Type')}")
        #print(f"CSS====={response.css('.ng-binding')}")
        pattern = r"data="
        print(f"SCTIPT 1====={response.css('script')}")
        print(f"XPATH====={response.xpath('script').re(pattern)}")
        # javascript=response.css('script').get()
        # print(f"SCTIPT GET====={response.css('script').get()}")
        # data = chompjs.parse_js_object(javascript)
        # data=chompjs.parse(javascript)
        # print(f"====DATA==={data}")
        print(f"SCTIPT TEXT====={response.css('script::text')}")
        #print(f"DECODE====={response.body.decode(response.encoding)}")
        #print(f"===META====={response.meta}")
        #print(f"===CB====={response.cb_kwargs}")
        #print(f"===HEADERS====={response.headers}")
        #print(f"===FLAGS====={response.flags}")
        #print(f"===URL====={response.url}")
        #print(f"===protocol====={response.protocol}")
        #print(f"===BODY====={response.text}")
        #print(f"PROBE TIME PRINT ======  {PAYLOAD['startTenderReceiptDeadline']}")
        patt=r'property name="eurLexEuropaLink"'
        javascript = response.css('script::text').get(patt)
        #javascript = response.css('#container-sizing > script:nth-child(4)').get()
        #javascript = response.xpath('//*[@id="container-sizing"]/script[2]').get()
        xml = lxml.etree.tostring(js2xml.parse(javascript), encoding='unicode')
        selector = Selector(text=xml)
        # for_print=selector.css('name="config"').get()
        # print(f"====JS2XML===={for_print}")
        print(f"====XML===={xml}")













