#coding=utf-8
#!/usr/bin/env python 

'''
模块要求：1.将给定字符串转化为列表；
          2.对列表内部每个数据进行格式化统一。
          3.对列表中的记录时间数据进行排序。
          4.将排序后的数据追加到各个新的列表中。
          5.对重复数据进行迭代删除。
          6.提取出时间最短的前三个数据，开头打印出人名，以列表的形式输出。
'''

def get_coach_data(filename):                                        # 读取文本函数，并转化为列表。函数设定一个参数filename,用来传递文本变量。
	try:                                                             # try异常处理，保护以下代码
		with open (filename) as f:                                   # 上下文本管理器。将打开的文本文件赋值给变量f。
			data = f.readline()                                      # 将文本文件读取后存入data变量中，生成新的文本。
		tmp = data.strip().split(',')                                # 返回的文本进行格式化处理 ①除去空白符 ② 使用split分割方式，赋值给变量tmp（列表）
		return (Athlete(tmp.pop(0), tmp.pop(0), tmp))                # 返回Athlete类（tmp.pop(0)...分别表示传入的三个对应参数）
	except IOError as e:                                             # except抛出异常。
		print('File err'+ str(e))                                    # 错误提示，打印log
		return(None)                             

class Athlete:                                                       # 定义一个名为Athlete的类。                                             
	def __init__(self, a_name,a_dob=None, a_times=[]):               # def __init__（self）初始化类属性。
		self.name = a_name                                           # self.name 为对象属性。
		self.dob = a_dob                                             # self.dob 为对象的另一个属性。
		self.times = a_times                                         # self.times 为对象的第三个属性。

	def top3(self):                                                  # 类Athlete的另一个方法属性。self 表示类本身 
		return (str(sorted(set([sanitize(t) for t in self            # 返回用时最短前三个 元素的列表。这里的self 用于调用类的本身。self.times
			.times]))[0:3]))                                         # = a_times = tmp = data.strip().split(',') 


def sanitize(time_string):                                           # 清洗数据函数。函数设定一个参数time_string.用来传递需要格式化处理的数据。
	if '-' in time_string:                                           # 判断如果数据中存在‘-’字符串。
		splitter = '-'                                               # 将字符串'-'赋值给splitter变量。
	elif ':' in time_string:                                         # 否则如果数据中存在':'字符串。
		splitter = ':'                                               # 将字符串':'赋值给splitter变量。
	else:                                                            # 其他情况
		return time_string                                           # 可直接返回数据
	(mins,secs) = time_string.split(splitter)                        # 使用split分割的方法，将分割的数据分别赋值给mins,secs两个变量
	return(mins+'.'+secs)                                            # 返回一个（以min . secs三部分）新组成的数据


sarah = get_coach_data ("Sarah.txt")                                 # 调用get_coach_data函数，导入数据。将值赋值给sarah变量

print (sarah.name  + "'s fastest times are: " + sarah.top3())        # 输出结果：sarah.name（sarah为类Athlete的一个对象，sarah.name表示调用类的属性，
                                                                     # 为a_name(即tmp.pop(0))）;sarah.top3() 为调用类的top3()的方法属性 
                                                                     
                                                                     




		






