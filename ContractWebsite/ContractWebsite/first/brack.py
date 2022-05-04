   # # Save data and set current user to last updated by fields
    # def form_valid(self, form):
    #     object = form.save(commit=False)
    #     object.last_updated_by = self.request.user.get_full_name()
    #     object.last_updated_by_id = self.request.user
    #
    #     return super(EditUsers, self).form_valid(form)

    # def get_queryset(self):
    #     criteria1 = Q(owner=self.request.user)
    #     criteria2 = Q(organizationmembers__member=self.request.user)
    #     criteria3 = Q(organizationmembers__organization_admin=1)
    #     org_list = UserModel.objects. \
    #         filter(criteria1 | (criteria2 & criteria3)).distinct()

        # if org_list.count() != 0:
        #     return org_list
        # else:
        #     raise Http404('You don\'t have permissions!')
    #template_name_suffix = '_update_form'
   # success_url = reverse_lazy('admins')
    # def get_context_object_name(self, obj):
    #     print(obj)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_profil = UserModel.objects.get(id=self.object.id)
    #     print(user_profil.id)
    #     context['user'] = user_profil
    #     return context


    # def post(self, request, *args, **kwargs):
    #     user_for_edit=UserModel.objects.get(username=self.object.username)
    #     print(user_for_edit)


# class FormEditUser(forms.ModelForm):
#     class Meta:
#         model=UserModel
#         fields='__all__'
#
# class EditUsers(auth_mixin.LoginRequiredMixin,views.UpdateView):
#     model = UserModel
#     form_class = FormEditUser
#     template_name = 'edit_user.html'
#
#     def get_object(self, queryset=None):
#         pk = self.kwargs.get(self.pk_url_kwarg)
#         print(pk)

# class MyDateFilter(filters_rest.filters.DateFilter):
#     date = filters_rest.DateFromToRangeFilter()
#
#
#     # class Meta:
#     #     model = Notice
    #     fields = ['id','date','tender_name']


# class FormSearch(forms.ModelForm):
#
#     class Meta:
#         model=Notice
#         fields=('id','date','tender_name')

   # def get_form_class(self):
   #     # widgets = {
   #     #     'date': DatePickerInput(),
   #     # }
   #     return forms


   # def get(self, request, format=None):
   #     """
   #     Return a list of all users.
   #     """
   #     notice = [simple.tender_name for simple in Notice.objects.all()]
   #     return Response(notice)


   # queryset = Notice.objects.all()
   # filter_backends = [filters.SearchFilter]
   # search_fields = ['tender_name','id','date']
   # filterset_fields=['tender_name','id','date']
   # filterset_fields=SearchSerializer


# class SearchSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField()
#     class Meta:
#         model = Notice
#         fields = ('id','date','tender_name')


   # last_user=DateModel.objects.all().last()
   # print(last_user.end_date)
   # here start scrapy


   # #queryset = Notice.objects.all()
   # def get_queryset(self):
   #     filter_val = self.request.GET.get('filter')
   #     new_context = Notice.objects.filter()
   #     return new_context
   # def get_context_data(self, **kwargs):
   #     context = super(LogedPage, self).get_context_data(**kwargs)
   #     context['form'] = self.request.GET.get('filter', 'give-default-value')
   #     return context


   # first_name = forms.CharField(max_length=25, )
   # last_name = forms.CharField(max_length=30)
   # email = forms.EmailField(
   #     Null=True,
   # )
   #
   #
   # def save(self, commit=True):
   #     user = super().save(commit=commit)
   #     profile = Profile(
   #         first_name=self.cleaned_data['first_name'],
   #         last_name=self.cleaned_data['last_name'],
   #         picture=self.cleaned_data['picture'],
   #         born=self.cleaned_data['born'],
   #         user=user,
   #     )
   #
   #     if commit:
   #         profile.save()
   #         wait_user = WaitingUser(
   #             first_name=self.cleaned_data['first_name'],
   #             last_name=self.cleaned_data['last_name'],
   #             id=profile.pk,
   #
   #         )
   #         wait_user.save()
   #     return user


""" NOTICES.PY """
#os.environ['DJANGO_SETTINGS_MODULE'] = 'ContractWebsite.settings'



# class NoticesSpider(scrapy.Spider):
#     #user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
#     #coockie="isCompact=true; culture=en-US; _HttpSessionID=35E93C04EB154DDBB374AACA43484AD2; sysNoticeTypeIds=null"
#     #handle_httpstatus_list = [404, 403, 400]
#     name = 'notices'
#     allowed_domains = ['e-licitatie.ro']
#     #allowed_domains = ['quotes.toscrape.com']
#     #start_urls = ['https://www.e-licitatie.ro/views/common/notices/common/service.min.js?_=1651054814609']
#     #start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']
#     start_urls=['http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/']
#
#
#     def parse(self, response,**kwargs):
#         #strrr=response.css("div.u-items-list__item_properties::text").extract()
#         #strrr=response.css('span.ng-binding::text').extract()
#         #strrr=response.xpath('/html/body/div[1]/div/div[2]/div/div[5]/div[9]/div[2]/div[1]/div').extract()
#         print()
#         print()
#         print()
#         #strrr=response.css('#container-sizing > div.u-items-list > div.u-items-list__content').getall()
#         #strrr=response.css('.u-items-list__content').extract()
#         #strrr=response.xpath('//*[@id="container-sizing"]/div[9]/div[2]').get()
#         #date=json.loads(response.body)
#         print(response.body)
#         #strrr=date
#         #print(f"=====D E N I S L A V==={str(strrr)}")
#         print()
#         print()
#         print()
#
#         # with open("test.txt", "w") as outfile:
#         #     outfile.write(str(strrr))
#         # # #pass
#         # yield {'=====D E N I S L A V':str(strrr)}
#
#         # for title in response.css('.u-items-list__content'):
#         #     dict_ = {'title': title.css('::text').get()}
#         #     print(f"this: {dict_['title']}")
#         #     yield {'title': title.css('::text').get()}

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
# from scrapy.http import request
# from scrapy.http.request.form import FormRequest
# from scrapy.http import FormRequest


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


""" 28.04.2022"""
# class NoticesSpider(scrapy.Spider):
#     name = 'notices'
#     #allowed_domains = ['e-licitatie.ro']
#     #start_urls=['http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/']
#
#     def start_requests(self):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
#         cookies = {'cookie-key': 'culture=en-US; isCompact=true; _HttpSessionID=5BF1B10EBD394BD8B5B99ED472BD854E; sysNoticeTypeIds=null'}
#         yield scrapy.Request(
#             url='http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/',
#             method='POST',
#             headers=headers,
#             cookies=cookies,
#             callback=self.parse,
#         )
#
#     def parse(self, response,**kwargs):
#
#         print("S T A R T")
#         print("S T A R T")
#         print("S T A R T")
#         print("S T A R T")
#         print()
#         print()
#         print(response.body)
#         print()
#         print()
#         print()


# class NoticeSpider(scrapy.Spider):
#     name = 'notices'
#     # allowed_domains = ['e-licitatie.ro']
#     #start_urls=['http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/']
#     start_urls=['http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1']
#
#     def parse(self, response, **kwargs):
#
#         url='http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/'
#         my_value=response.css('strong.ng-binding').get()
#         #my_value=response.xpath('/html/body/div[1]/div/div[2]/div/div[5]/div[9]/div[2]/div[1]/div/div/div[2]/h2/a/span').extract()
#         yield {'=========D E N I S L A V':my_value}




# class NoticeSpider(scrapy.Spider):
#     name = "notices"
#     start_urls = ["http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1"]
#     headers = {
#     'Accept': 'application / json, text / plain, * / *',
#     'Accept - Encoding': 'gzip, deflate',
#     'Accept - Language': 'en - US, en;q = 0.9',
#     'Authorization': 'Bearer null',
#     'Cache - Control': 'no - cache',
#     'Connection': 'keep - alive',
#     'Content - Length': '101',
#     'Content - Type': 'application / json;charset = UTF - 8',
#    ' Cookie': 'culture = en - US;isCompact = true;_HttpSessionID = 5BF1B10EBD394BD8B5B99ED472BD854E;sysNoticeTypeIds = null',
#     'Culture': 'en - US',
#     'Host': 'www.e - licitatie.ro',
#     'HttpSessionID': 'null',
#     'Origin': 'http: // www.e - licitatie.ro',
#     'Pragma': 'no - cache',
#     'Referer': 'http: // www.e - licitatie.ro / pub / notices / contract - notices / list / 2 / 1RefreshToken: null',
#     'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
#     }
#
#     def parse(self, response,**kwargs):
#         yield scrapy.Request(
#             url="http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/",
#             callback=self.parse,
#             headers=self.headers
#         )
#
#     # def parse_json(self, response):
#     #     data = response.json() # Newer version of Scrapy come with shortcut to get JSON data
#     #
#     #     for i,school in enumerate(data):
#     #         school_code = school["itSchoolCode"]
#     #         yield scrapy.Request(
#     #             f"https://directory.ntschools.net/api/System/GetSchool?itSchoolCode={school_code}",
#     #             callback=self.parse_school,
#     #             headers=self.headers,
#     #             dont_filter=True # Many schools have the same code, same page, but listed more than once
#     #         )
#
#     # def parse_school(self, response):
#     #     data = response.json() # Newer version of Scrapy come with shortcut to get JSON data
#     #     yield {
#     #         "name": data["name"],
#     #         "telephoneNumber": data["telephoneNumber"],
#     #         "mail": data["mail"],
#     #         "physicalAddress": data["physicalAddress"]["displayAddress"],
#     #         "postalAddress": data["postalAddress"]["displayAddress"],
#     #     }


""" 30.04.2022"""

   # PAYLOAD={
   #     "sysNoticeTypeIds": [],
   #     "sortProperties": [],
   #     "pageSize": 100,
   #     "hasUnansweredQuestions": False,
   #     "pageIndex": 0
   # }

""" 05.05.2022"""
# class TestSpider(scrapy.Spider):
#     """ Test spider for crawling from test url"""
#     name = 'test'
#     start_urls = ['https://quotes.toscrape.com/']
#
#     def parse(self, response,**kwargs):
#         items = NoticeItem()
#         Notice_all = response.xpath('//div/div/div/span[1]')
#         for single_notice in Notice_all:  # extracting data
#             data=[['2022-04-30'],['a'],[f"deni{random.randint(0,10)}"],["c"],['d'],['e'],[20],['g']]
#             items['Notice'] = single_notice.css('::text').extract()
#             items['date'] = data[0]
#             items['notice_number']=data[1]
#             items['tender_name']=data[2]
#             items['procedure_state']=data[3]
#             items['contract_type']=data[4]
#             items['type_of_procurement']=data[5]
#             items['estimated_value']=data[6]
#
#             # if not in db django store it!!!!
#             if data[2][0] not in N.objects.values_list('tender_name', flat=True).distinct():
#                 new_notice = N(
#                     date=data[0][0],
#                     notice_number=data[1][0],
#                     tender_name=data[2][0],
#                     procedure_state=data[3][0],
#                     contract_type=data[4][0],
#                     type_of_procurement=data[5][0],
#                     estimated_value=data[6][0],
#                 )
#                 new_notice.save()
#             yield items


   # start_urls = [" http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"]
   # headers_others = {
   #     'Accept': 'application/json, text/plain, */*',
   #     'Accept-Encoding': 'gzip, deflate',
   #     'Accept-Language': 'en-US,en;q=0.9',
   #     'Authorization': 'Bearer null',
   #     'Cache-Control': 'no-cache',
   #     'Connection': 'keep-alive',
   #     'Content-Length': '101',
   #     'Content-Type': 'application/json;charset=UTF-8',
   #     'Cookie': 'culture=en-US; isCompact=true; _HttpSessionID=5BF1B10EBD394BD8B5B99ED472BD854E; sysNoticeTypeIds=null',
   #     'Culture': 'en-US',
   #     'Host': 'www.e-licitatie.ro',
   #     'HttpSessionID': 'null',
   #     'Origin': 'http://www.e-licitatie.ro',
   #     'Pragma': 'no-cache',
   #     'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1RefreshToken: null',
   #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
   # }
   # headers = {
   #     'Content-Type': 'application/json; charset=UTF-8',
   #     #'Content-Type': 'application/x-www-form-urlencoded',
   # }

   # PAYLOAD = {
   #     "sysNoticeTypeIds": [],
   #     "sortProperties": [],
   #     "pageSize": 5,
   #     "hasUnansweredQuestions": False,
   #     "startPublicationDate": "2022-05-01T06:14:48.809Z",
   #     "startTenderReceiptDeadline": f"{str(last_time_request.start_date)}T06:14:48.810Z",
   #     "sysProcedureStateId": 2,
   #     "pageIndex": 0,
   #     "endTenderReceiptDeadline": f"{str(last_time_request.end_date)}T21:00:00.000Z"
   # }


   # request=scrapy.Request(url=' http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/',
   #                method='POST',
   #                callback=self.parse,
   #                headers=self.headers,
   #                body=json.dumps(PAYLOAD),
   #                )


   # yield {
   #
   #     'name':data['cNoticeId']
   # }


   # print(f"Content type====={response.headers.getlist('Content-Type')}")
   # print(f"CSS====={response.css('.ng-binding')}")
   # pattern = r"data="
   # print(f"SCTIPT 1====={response.css('script')}")
   # print(f"XPATH====={response.xpath('script').re(pattern)}")
   # javascript=response.css('script').get()
   # print(f"SCTIPT GET====={response.css('script').get()}")
   # data = chompjs.parse_js_object(javascript)
   # data=chompjs.parse(javascript)
   # print(f"====DATA==={data}")
   # print(f"SCTIPT TEXT====={response.css('script::text')}")
   # print(f"DECODE====={response.body.decode(response.encoding)}")
   # print(f"===META====={response.meta}")
   # print(f"===CB====={response.cb_kwargs}")
   # print(f"===HEADERS====={response.headers}")
   # print(f"===FLAGS====={response.flags}")
   # print(f"===URL====={response.url}")
   # print(f"===protocol====={response.protocol}")
   # print(f"===BODY====={response.text}")
   # print(f"PROBE TIME PRINT ======  {PAYLOAD['startTenderReceiptDeadline']}")
   # patt=r'property name="eurLexEuropaLink"'
   # javascript = response.css('script::text').get(patt)
   # javascript = response.css('#container-sizing > script:nth-child(4)').get()
   # javascript = response.xpath('//*[@id="container-sizing"]/script[2]').get()
   # xml = lxml.etree.tostring(js2xml.parse(javascript), encoding='unicode')
   # selector = Selector(text=xml)
   # for_print=selector.css('name="config"').get()
   # print(f"====JS2XML===={for_print}")
   # print(f"====XML===={xml}")

# from chompjs import chompjs
# import js2xml
# import lxml.etree
# from parsel import Selector