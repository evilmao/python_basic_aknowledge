#coding=utf-8
#!/usr/bin/env python 

'''
模块要求：1.将给定字符串转化为列表；
          2.对列表内部每个数据进行格式化统一。
          3.对列表中的记录时间数据素进行排序。
          4.将排序后的数据追加到各个新的列表中。
          5.对重复数据进行迭代删除。
          6.提取出时间最短的前三个数据，以列表的形式输出。
'''

def get_coach_data(filename):                        # 读取文本函数，并转化为列表。函数设定一个参数filename,用来传递文本变量。
	try:                                         # try异常处理，保护以下代码
		with open (filename) as f:           # 上下文本管理器。将打开的文本文件赋值给变量f。
			data = f.readline()          # 将文本文件读取后存入data变量中，生成新的文本。
		return(data.strip().split(','))      # 对返回的文本进行格式化处理 ①除去空白符 ② 使用split分割方式，将变量data转化成列表。
	except IOError as e:                         # except抛出异常。
		print('File err'+ str(e))            # 错误提示，打印log
		return(None)                             


def sanitize(time_string):                           # 清洗数据函数。函数设定一个参数time_string.用来传递需要格式化处理的数据。
	if '-' in time_string:                       # 判断如果数据中存在‘-’字符串。
		splitter = '-'                       # 将字符串'-'赋值给splitter变量。
	elif ':' in time_string:                     # 否则如果数据中存在':'字符串。
		splitter = ':'                       # 将字符串':'赋值给splitter变量。
	else:                                        # 其他情况
		return time_string                   # 可直接返回数据
	(mins,secs) = time_string.split(splitter)    # 使用split分割的方法，将分割的数据分别赋值给mins,secs两个变量
	return(mins+'.'+secs)                        # 返回一个（以min . secs三部分）新组成的数据


sarah = get_coach_data ("Sarah.txt")
sarah_name , sarah_dob = sarah.pop(0),sarah.pop(0)   # 使用列表pop方法（返回值为列表索引对应的值，原列表元素抽离）得到对应需要输出的内容。

print (sarah_name + "'s fastest times are: " + str
(sorted(set([sanitize(t) for t in sarah]))[0:3]))




		



