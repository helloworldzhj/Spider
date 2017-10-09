import requests
url = "https://www.amazon.cn/图书/dp/B01M8L5Z3Y/ref=sr_1_1?ie=UTF8&qid=1504334793&sr=8-1&keywords=极简"
try:
	kv = {'user-agent':'Mozilla/5.0'}#伪装一个浏览器。这样亚马逊就不会拒绝我的访问
	r = requests.get(url,headers=kv)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.text[1000:2000])
except:
	print('爬取失败')