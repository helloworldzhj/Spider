import requests
url = "https://item.jd.com/5181386.html"
try:
	r = requests.get(url,timeout=30)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(r.text[:1000])
except:
	print('爬取失败')