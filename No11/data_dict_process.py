#coding=utf-8
#!/usr/bin/env python 

'''
模块要求：1.将给定字符串转化为列表；
          2.对列表内部每个数据进行格式化统一。
          3.对列表中的记录时间数据进行排序。
          4.将排序后的数据追加到各个新的列表中。
          5.对重复数据进行迭代删除。
          6.提取出时间最短的前三个数据，以列表的形式输出。
'''

def get_coach_data(filename):                                        # 读取文本函数，并转化为列表。函数设定一个参数filename,用来传递文本变量。
	try:                                                             # try异常处理，保护以下代码
		with open (filename) as f:                                   # 上下文本管理器。将打开的文本文件赋值给变量f。
			data = f.readline()                                      # 将文本文件读取后存入data变量中，生成新的文本。
			tmp = data.strip().split(',')                            # 返回的文本进行格式化处理 ①除去空白符 ② 使用split分割方式，赋值给变量tmp（列表）
		return({'Name' :tmp.pop(0),                                  # 返回一个字典. 三个键.值对对应三项需要分类的数据。 利用列表pop方法得到对应键的值
                'DOB'  :tmp.pop(0),                                  # 其中Times 键的值利用①sorted(复制升序排序方法)②set集合唯一性（去重）③sannitize
                'Times':str(sorted(set([sanitize(t)                  # 数据清洗函数④[t for t in tmp]列表推导式格式化处理生成新的列表⑤通过切片的方式[0:3] 
		      for t in tmp]))[0:3])                                  # 取出前三的数据;
                })
	except IOError as e:                                             # except抛出异常。
		print('File err'+ str(e))                                    # 错误提示，打印log
		return(None)                             


def sanitize(time_string):                                           # 清洗数据函数。函数设定一个参数time_string.用来传递需要格式化处理的数据。
	if '-' in time_string:                                           # 判断如果数据中存在‘-’字符串。
		splitter = '-'                                               # 将字符串'-'赋值给splitter变量。
	elif ':' in time_string:                                         # 否则如果数据中存在':'字符串。
		splitter = ':'                                               # 将字符串':'赋值给splitter变量。
	else:                                                            # 其他情况
		return time_string                                           # 可直接返回数据
	(mins,secs) = time_string.split(splitter)                        # 使用split分割的方法，将分割的数据分别赋值给mins,secs两个变量
	return(mins+'.'+secs)                                            # 返回一个（以min . secs三部分）新组成的数据


sarah = get_coach_data ("Sarah.txt")                                 # 调用文本读取函数。读取存有Sarah成绩数据的文本.
print (sarah["Name"]  + "'s fastest times are: " + sarah["Times"])   # 输出需要的数据：三部分组成，通过字典键——值方法。




		






