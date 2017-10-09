import requests
import time

def GetHTML(url,times):
	try:
		for i in range(100):
			r = requests.get(url,timeout = 10)
			r.raise_for_status()
			#r.encoding=r.apparent_encoding
			#return r.text
	except:
		print("Error")

def GetTime(url,times):
	start = time.time()
	GetHTML(url,times)
	end = time.time()
	print("共需要时间"+str(end - start)+"s")

def main():
	url = input("URL:")
	times = int(input("times:"))
	GetTime(url,times)
	
if __name__=="__main__":
	main()




