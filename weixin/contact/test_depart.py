from weixin.contact.get_token import GetToken
from weixin.py11 import GetLog
import pytest
import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)
# logging = GetLog()

class TestDepart:

    @classmethod
    def setup_class(cls):
        logging.info('小祥哥牛逼')
        pass
    def setup(self):
        logging.info('小祥哥牛逼')
        pass
    def test_creat(self):
        # url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        token = GetToken().get_token()
        # logging.debug(token)
        # data = {"name": "一年级一班",
        #         "parentid": 1}
        Data = {'url':'https://qyapi.weixin.qq.com/cgi-bin/department/create',
                'params':{'access_token':token},
                'json':{"name": "一年级一班",
                "parentid": 1}}

        res = requests.post(**Data)
        logging.debug(res.json())

    def test_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        token = GetToken().get_token()

        res = requests.get(url,params={'access_token':token})
        logging.debug(json.dumps(res.json(),indent=2 ))

if __name__ == '__main__':
    pytest.main('-v -c test_depart')