#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib.request
import re
def getcontent(url,page):
	#模拟成浏览器
	headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3453.400 QQBrowser/9.6.12025.400')
	opener=urllib.request.build_opener()
	opener.addheaders = [headers]
	#将opener安装为全局
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(url).read().decode("utf-8")
	#构建对应用户提取的正则表达式
	userpat = 'target="_black" title="(.*?)">'
	#构建段子内容提取的正则表达式
	contentpat='<div class="content">(.*?)</div>'
	#寻找出所有的用户
	userlist = re.compile(userpat,re.S).findall(data)
	contentlist = re.compile(contentpat,re.S).findall(data)
	x = 1
	#通过for循环遍历段子内容并将内容分别赋给对应的变量
	for content in contentlist:
		content = content.replace("\n","")
		name = "content" + str(x)
		exec(name+'=content')
		x += 1
	y = 1
	for user in userlist:
		name = "content" + str(y)
		print("用户"+str(page)+str(y)+"是："+user)
		print('内容是：')
		exec("print("+name+")")
		print("\n")
		y += 1
for i in range(1,3):
	url = "https://www.qiushibaike.com/8hr/page/"+str(i)
	getcontent(url,i)


#暂时没有实现，我个人推测的话应该是因为网页改版正则表达式变了，以后集中学习正则表达式的话我还会回来把他们解决的




























