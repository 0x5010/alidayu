__editor__ = 0x5010
'''
Created by auto_sdk on 2016.04.13
'''
from ..base import RestApi


class AreasGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None

    def getapiname(self):
        return 'taobao.areas.get'
