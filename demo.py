# -*- coding: utf-8 -*-
__editor__ = 0x5010

from alidayu import api, appinfo

appkey = "appkey"
secret = "secret"
req = api.AlibabaAliqinFcSmsNumSendRequest()
req.set_app_info(appinfo(appkey, secret))

req.sms_type = "normal"
req.rec_num = "手机号"
req.sms_template_code = "模板代码"
req.sms_free_sign_name = "验证名字"
req.sms_param = {"code": "模板代码和内容"}
resp = req.getResponse()
print(resp)

