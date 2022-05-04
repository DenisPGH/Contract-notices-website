import json
import random
import re

import requests
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
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
        'Content-Type': 'application/json;charset=UTF-8',
    }

    def parse(self,response,**kwargs):
        last_time_request=DateModel.objects.all().last() # got the last gived data period for using in crawl
        json_data = {
            'sysNoticeTypeIds': [
                2,
            ],
            'sortProperties': [],
            'pageSize': 100,
            'hasUnansweredQuestions': False,
            'startPublicationDate': f'{str(last_time_request.start_date)}T14:01:43.389Z',
            #'startTenderReceiptDeadline': f'{str(last_time_request.end_date)}T14:01:43.389Z',
            'sysProcedureStateId': 2,
            'pageIndex': 0,
            "endTenderReceiptDeadline": f"{str(last_time_request.end_date)}T21:00:00.000Z"
        }

        response = requests.post('http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/',
                                 headers=self.headers,
                                 json=json_data,
                                 verify=False)
        data=response.json() #return dict
        # with open('json_test.json','w') as read:
        #     data=json.dumps(data)
        #     read.write(data)
        #print(f"======={data['items'][0]['cNoticeId']}")
        for each_items in range(len(data['items'])):
            if data['items'][each_items]["contractingAuthorityNameAndFN"] not in N.objects.values_list('tender_name', flat=True).distinct():
                new_notice = N(
                    date=data['items'][each_items]["noticeStateDate"].split('T')[0],
                    notice_number=data['items'][each_items]['noticeNo'],
                    tender_name=data['items'][each_items]["contractingAuthorityNameAndFN"],
                    procedure_state=data['items'][each_items]["sysProcedureState"]["text"],
                    contract_type=data['items'][each_items]["sysAcquisitionContractType"]["text"],
                    type_of_procurement=data['items'][each_items]["sysProcedureType"]["text"],
                    estimated_value=float(data['items'][each_items]["estimatedValueExport"].split(" ")[0].split(',')[0]),
                )
                new_notice.save()















