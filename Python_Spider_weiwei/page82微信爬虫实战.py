#!/usr/bin/env python
#-*-coding:utf-8-*-

http://weixin.sogou.com/weixin?type=2&query=%E7%89%A9%E8%81%94%E7%BD%91&ie=utf8&s_from=input&_sug_=y&_sug_type_=&w=01019900&sut=2121&sst0=1506690658520&lkt=1%2C1506690658419%2C1506690658419

http://weixin.sogou.com/weixin?query=%E7%89%A9%E8%81%94%E7%BD%91&_sug_type_=&sut=2121&lkt=1%2C1506690658419%2C1506690658419&s_from=input&_sug_=y&type=2&sst0=1506690658520&page=2&ie=utf8&w=01019900&dr=1

type	类型
query	关键词
page	页码


import re
#导入正则表达式库
import urllib.request
import time
import urllib.error

#模拟成浏览器
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
opener = urllib.request.build.opener()
opener.addheaders = [headers]
#将opener安装为全局
urllib.request.install_opener(opener)
#设置一个列表listurl存储文章网址列表
listurl = []
#自定义函数，功能为使用代理服务器
def use_proxy(proxy_addr,url):
	#建立异常处理机制
	try:
		import urllib.request
		proxy = urllib.request.ProxyHandler({'http':proxy_addr})
		opener  urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
		urllib.requestinstall_opener(opener)
		data = urllib.request.urlopen(url).read().decode('utf-8')
		return data
	except urllib.error.URLError as e:
























