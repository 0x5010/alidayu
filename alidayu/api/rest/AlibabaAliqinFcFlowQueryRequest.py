__editor__ = 0x5010
'''
Created by auto_sdk on 2016.03.30
'''
from ..base import RestApi


class AlibabaAliqinFcFlowQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.out_id = None

    def getapiname(self):
        return 'alibaba.aliqin.fc.flow.query'
