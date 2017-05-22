#!/usr/bin/env python
#encoding:utf-8

"""
定义一个movies的模块，提供了一个名为print_lol的函数，此模块用于处理列表，
其中有可能（也可能不包含）嵌套列表。根据用户个人喜好，可以输出不同的答应
格式。
"""

def print_lol(the_list,indent=False,level=0):
	"""此函数取一个位置参数，名为the_list,这个可以是任何一个python列表
	（也可以包含嵌套列表的列表）。所指定的列表中的每个数据项（递归地）输
	出到屏幕上，各行数据各占一个行。第2个参数indent 用来控制输出格式，是
	否需要缩进，默认缩进；第3个参数（level）用来在遇到嵌套列表时，插入制
	表符。
	"""
	for each_item in the_list:                      #for循环,遍历列表中的每一个元素。              
		if isinstance(each_item, list):             #利用方法isinstance判断列表中是否存在嵌套列表。
			print_lol(each_item, indent, level+1)   #如果是列表（为真），递归继续返回函数,每次递归调用函数时将level值增1
		else:                                       #如果元素不是列表（为假），
			if indent:                              # if条件，控制是否缩进，默认有缩进      
				for tab_srop in range(level):       #for循环，当遇到壳套列表时，打印制表符
					print ('\t', end='')            #输出打印格式，'\t'是制表符，end='',表示末尾禁止换行。
			print (each_item) 



movies=['肖申克的救赎',1994,'弗兰克.德拉邦特',142,
        ['提姆.罗宾斯',['摩根.弗里曼','鲍勃.冈顿','威廉姆.赛德勒']]]

if __name__ == '__main__':
	print_lol(movies,True,1)
