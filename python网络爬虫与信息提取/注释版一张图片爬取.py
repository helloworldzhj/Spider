import requests
import os

url = "http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C302%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C310/sign=8800a2e3b3119313c743ffb855036fa7/1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg"
#需要保存的图片的网址，注意在url链接的最后要是图片的***.jpg之类的
root = 'C:/Users/Administrator/Desktop/pics/'
#保存图片的目录文件夹
path = root + url.split('/')[-1]
#保存的图片的名字
try:
	if not os.path.exists(root):
		os.mkdir(root)
	#如果文件夹不存在就会创建一个文件夹。
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
		#以写的格式打开这个文件
			f.write(r.content)
			#然后我就把图片的东西写进去
			f.close()
			#关闭这个文件
			print('save successfully')
			#告诉系统我保存好了
	else:
		print('it has been saved')
		#如果之前已经保存过了我就说‘已经保存过了’
except:
	print('defeat')
	#如果出现错误我就说出问题了。