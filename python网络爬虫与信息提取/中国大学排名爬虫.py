import requests
from bs4 import BeautifulSoup
import bs4

#获取url的信息。输出url的内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return""

#将页面放到list列表中(ulist)
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

#将ulist里面的信息打印出来。num表示打印多少条信息
def printUnivList(ulist, num):
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
	print(tplt.format("排名","学校名称","总分",chr(12288)))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0],u[1],u[2],chr(12288)))
		
#调用主函数
def main():
    #将大学信息放到列表中。这个列表叫uinfo
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
main()


