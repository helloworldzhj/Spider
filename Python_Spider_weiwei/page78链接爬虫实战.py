#!/usr/bin/env python
#-*-coding:utf-8-*-

import re
import urllib.request
def getlink(url):#创建了一个自定义函数getlink（url）专门富足爬取对应的url上所有的链接，再函数中，首先需要设置header信息等模拟成浏览器，
	#模拟成浏览器
	headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')#模拟成浏览器并爬取对应的网页
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	#将opener安装为全局
	urllib.request.install_opener(opener)
	file = urllib.request.urlopen(url)
	data = str(file.read())#然后需要读取该网页的源代码，
	pat = '(http?://[^\s)";]+\.(\w|/)*)'#根据需求构建好链接提取的正则表达式
	link = re.compile(pat).findall(data)#读取了源代码之后根据构建的正则表达式，通过re.compile(pat).findall(data)提取出该网页的所有链接，
	link = list(set(link))#此时提取到的链接可能有所重复，所以通过list（set（link））将对应重复的元素过滤掉
	return link#然后返回过滤后的列表。
url = "http://blog.csdn.net/"#在函数外，首先确定好要爬虫的入口链接
linklist=getlink(url)
for link in linklist:#将获取到的链接通过for循环遍历出来并打印到控制台上
	print(link[0])#后续操作。比如说把他们打印出来

其中比较关键的一点在于，正则表达式的构造不一定是固定的，需要根据自身的需求来进行调整，并且可以不断完善，
上面的正则表达式为http?://[^\s)";]+\.(\w|/)*
确定其简单版的链接为http://xxx.yyy其中xxx和yyy均代表可变化部分，根据其简单版本进行完善，首先协议部分有的是http有的是https这时候s‘可有可无然后xxx部分不可以出现空格，不可以出现双引号，也不可以出现分号，yyy部分是一些非特殊字符，可以是/符号，当然还可以继续完善。

























