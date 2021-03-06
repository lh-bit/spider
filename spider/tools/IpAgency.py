#! -*- encoding:utf-8 -*-

import requests
import os
from xmlUnit.ReadXML import ReadXml


class IpAgency:
    #配置文件
    configPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\xmlUnit\\config.xml"
    readxml = ReadXml(configPath)
    #需要 xmlUnit下的 config.xml 里面两个元素的配置
    def __init__(self):
        # 代理服务器
        self.proxyHost = "http-dyn.abuyun.com"
        self.proxyPort = "9020"

        # 代理隧道验证信息
        self.proxyUser = IpAgency.readxml.get_ItemValue("proxyUser")
        self.proxyPass = IpAgency.readxml.get_ItemValue("proxyPass")
        self.proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": self.proxyHost,
            "port": self.proxyPort,
            "user": self.proxyUser,
            "pass": self.proxyPass,
        }
        self.proxies = {
            "http": self.proxyMeta,
            "https": self.proxyMeta,
        }

    def getIpProxy(self):
        return self.proxies


if __name__ == '__main__':
    # 要访问的目标页面
    ipagency = IpAgency()
    targetUrl = "http://www.baidu.com"
    resp = requests.get(targetUrl, proxies=ipagency.getIpProxy())

    print(resp.status_code)
    print(resp.text)
