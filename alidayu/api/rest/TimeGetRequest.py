__editor__ = 0x5010
'''
Created by auto_sdk on 2016.03.28
'''
from ..base import RestApi


class TimeGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return 'taobao.time.get'
