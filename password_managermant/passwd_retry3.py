#coding=utf-8
#!/usr/bin/env python

'''
密码验证登录系统：1.可以实现注册，登录，退出作用，当输入不同的指令进入相应的操作提示。
				  2.注册功能:a提示输入用户名，当输入用户名，需判断注册的用户名是否已
				             经存在；b.如果存在，提示退出系统;c.用户不存在，进行密码
				             设置：通过再次确认密码，提示‘注册成功’，退出系统;d.将用
				             户名及密码保存至序列化格式文档的字典中。
				  3.登录功能:a.提示输入用户名和密码:b.判断用户名是否存在，如果不存在
				  			 给予提示，返回下一步操作指令;c.如果存在，提示密码正确，进
				  			 入下一步操作指令。
				  4.退出功能：输入某指令，系统退出。
'''
import pickle                                                          # 导入pickle模块，实现二进制文件读取写入
import getpass                                                         # 导入getpass模块，实现密码输入加密功能（不可视化）
 
def open_database():                                                   # 定义函数：读取当前目录下存储有用户名密码文档的二进制文件。 
	try:                                                               # try 异常判断。
		with open('passwd.pkl','rb') as f:                             # with open (...) as f:使用文档上下文管理器，读取文档f赋值给变量f。 
			return pickle.load(f)                                      # 使用pickle.load(f) 读取二进制文件
	except IOError as e:                                               # 发生IOError 异常时，返回为假。
		return False
	except Exception as e:
		raise e

def update_database(user_data):                                        # 用户名密码更新函数：实现新注册的数据有效存储。使用user_data参数，进行更新。
	try:                                                               # try判断异常，保护以下代码
		with open('passwd.pkl','wb') as f:                             # 上下文本管理器，新建文本文件'passwd.pkl'以二进制格式写入新的内容，同时赋值给新的变量f;
			pickle.dump(user_data,f)                                   # 使用pickle.dump(user_data,f)将use_data数据写入变量f 中。
			return True                                                # 返回为真
	except IOError as e:                                               # 指定异常
		return False                                                   # 返回为假
	except Exception as e:                                             # 指定异常
		raise e                                                        # 抛出异常，打印log

def register():                                                        # 新用户注册函数：
	username = input('\033[31m请输入用户名：\033[0m')                  # 指定变量username，注册用户名。       
	user_data = open_database() if open_database() else {}             # 读取存储数据（调用open_database()）:判断如果数据存在将其赋值给user_data,否则，user_data为空字典。
	if username in user_data.keys():                                   # 如果username(字典键)存在于基础数据中：
		print ('\033[32m用户已经存在。\033[0m')                        # 说明新注册的用户名已存在基础数据中，提示'用户已存在'
		return False                                                   # 返回为假，注册功能终止。
	user_passwd = getpass.getpass('\033[33m请设置密码：\033[0m')       # 如果新注册用户名不在基础数据中；提示‘为用户名设置密码’
	user_data[username] = user_passwd                                  # 将user_passwd 与user_data字典的键值对应
	db_status = update_database(user_data)                             # 调用密码更新函数，赋值给变量db_status
	if not db_status:                                                  # 如果db_status 为假（为空）
		print ('\033[34m注册失败！\033[0m')						       # 提示注册失败
	print ('\033[35m注册成功！\033[0m')                                # 否则，提示注册成功。


def login():                                                           # 登录函数
	username=input ('\033[35m请输入用户名：\033[0m')                   # 提示输入用户名
	count = 0                                                          # 设置变量count =0 ,实现最大循环次数。
	while count < 3:                                                   # while 循环，当count < 3 (为真)：执行以下循环 
		user_passwd = getpass.getpass('\033[36m请输入密码：\033[0m')   #  提示输入用户名密码。getpass实现密码加密
		user_data = open_database()                                    # 调用open_database 函数即读取数据库，赋值给user_data
		passwd = user_data.get(username)                               # 使用get 方法（user_data为字典）讲 键为username的只赋值给变量passwd
		if passwd is None:                                             # 如果username键对应的值不存在;
			print ('用户不存在')                                       # 说明数据库中不存在此用户名
			break                                                      # 登录系统终止
		if user_passwd != passwd:                                      # 如果输入的密码不等于username（键）对应的值
			count += 1                                                 # count 计数加Ⅰ
			print (('\033[35m密码错误,已重试 %s 次 \033[0m') % count)  # 提示输入密码错误，请重试。
			continue                                                   # continue，执行while循环。
		print 	('\033[34m密码正确\033[0m')                            # 当输入的密码等于键值，提示密码正确。
		break                                                          # 登录系统终止
	else:                                                              # 当count >3 后，说明密码已经重试了三次。
		print ('\033[34m重试了三次，退出!\033[0m')                     # 提示，登录系统终止。

if __name__ == '__main__':                                             
	while True:                                                              # while True:死循环
		user_choice = input ('\033[36m1.注册 ，2.登录 ，0.退出 \n\033[0m')   # 用户选择，程序执行的起始部分
		if user_choice == "1":                                               # 如果user_choice 等于1
			register()                                                       # 执行用户注册功能
		elif user_choice == "2":                                             # 如果user_choice等于 2
			login()                                                          # 执行登录操作
		else:                                                                # user_choice为其他值时
			break                                                            # 程序终止。
		
