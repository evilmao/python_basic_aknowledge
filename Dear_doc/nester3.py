#!/usr/bin/env python
#encoding:utf-8

import sys

"""
这是“nester2.py”模块，提供了一个名为print_lol的函数，这个函数的作用是打印列表，
其中有可能（也可能不包含）嵌套列表。
"""

def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
	"""这个函数取一个位置参数，名为the_list,这个可以是任何一个python列表
	（也可以包含嵌套列表的列表）。所指定的列表中的每个数据项（递归地）输
	出到屏幕上，各行数据各占一个行。第2个参数indent 用来控制输出格式，是
	否需要缩进，默认缩进；第3个参数（level）用来在遇到嵌套列表时，插入制
	表符,第四个参数fn通过模块sys内置方法sys.stdout类似print进行文件标准
	输出，生成新的文件。
	"""
	for each_item in the_list:                             #for循环,遍历列表中的每一个元素。              
		if isinstance(each_item, list):                    #判断列表中是否存在嵌套列表，方法isinstance为判断参数是否为列表方法。
			print_lol(each_item, indent, level+1,fn)       #如果是列表（为真），递归返回函数,每次递归调用函数时将level值增1
		else:                                              #如果元素不是列表（为假），
			if indent:                                     # if条件，控制是否缩进，默认有缩进      
				for tab_srop in range(level):              #for循环，当遇到壳套列表时，打印制表符
					print ('\t', end='',file=fn)           #输出打印格式，'\t'是制表符，end='',表示末尾
			print (each_item, file=fn)                     #打印输出结果，并保存文件
