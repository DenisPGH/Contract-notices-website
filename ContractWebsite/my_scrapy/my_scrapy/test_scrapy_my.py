import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,bg;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1',
    'Content-Type': 'application/json;charset=UTF-8',
}

json_data = {
    'sysNoticeTypeIds': [
        2,
    ],
    'sortProperties': [],
    'pageSize': 5,
    'hasUnansweredQuestions': False,
    'startPublicationDate': '2022-04-04T14:01:43.389Z',
    'startTenderReceiptDeadline': '2022-05-04T14:01:43.389Z',
    'sysProcedureStateId': 2,
    'pageIndex': 0,
}

response = requests.post('http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/', headers=headers, json=json_data, verify=False)
print(response.text)