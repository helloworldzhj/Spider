#!/usr/bin/env python
#-*-coding:utf-8-*-

'''import threading
class A(threading.Thread):
	def __init__(self):
		#初始化线程
		threading.Thread.__init__(self)
	def run(self):
		#该线程要执行的程序内容
		for i in range(10):
			print('i\'m threading A')
class B(threading.Thread):
	def __init__(self):
		# 初始化线程
		threading.Thread.__init__(self)

	def run(self):
		# 该线程要执行的程序内容
		for i in range(10):
			print('i\'m threading B')
t1 = A()
t1.start()
t2 = B()
t2.start()

我们可以看到输出结果中，ab是混在一起的，所以AB是并行执法的。
以上我们给出了多线程的简单实例，再接下来的项目中。我们还需要用到队列中的一些基础知识。
队列是一种典型的数据结构，其特点是先进先出，就像排队一样，队列的功能非常好实现，我们通过导入queue模块来实现对应的功能。导入后可以通过queue.Queue()实例化一个队列对象并且通过队列对象的put（）方法实现将一个数据入队列的操作，每次入完队列后，可以通过task_done()方法表示该次入队列任务完成，如果要出队列，则可以通过队列对象的get方法实现，下面是一个例子'''

import queue#先导入queue模块
a = queue.Queue()#导入后可以通过以下代码创建一个队列a
a.put('hello')#可以通过put将对应的数据传入队列中，如下所示，我们将字符串数据hello传入队列a中
a.task_done()#这句代码表示该次入队列任务完成。
print(a.get())#对于传入的数据，这句话可以取出来
a.put('python')#顺序输出对应的结果
print(a.get())
a.put('123')
print(a.get())
a.put('456')
print(a.get())
a.put('789')
print(a.get())






























