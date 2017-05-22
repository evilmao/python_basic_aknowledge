#！/user/bin/env  python
# coding = utf -8

"""
程序名称：密码管理程序
程序要求  A. 主密码验证（超过三次后，给提示，密码加密）
		  B. 进入后 ：    
		            a). 可以看到所有存储的密码   
		            b). 用来存储用户密码（密码title, 真实密码--加密）
		            c). 可以自动生成密码（密码长度）
		            d). 密码分类存储。
		            e). 获取查看密码。
"""

"""
逻辑分析：1.主密码验证程序：需将整个验证放在管理密码函数之外，主密码已设置完毕，以二进制方式存储起到简单加密效果，导入getpass模块使用户输入密码隐藏。
          2.正确输入主密码后，键入不同的指令对密码管理器可以进入密码的存储，查看功能，此时需要调用argparse模块（命令解析工具）。
          3.分类存储利用字典内部嵌套方式存储。首先定义一个类，使用类的属性方法将需要保存的相关信息写入空字典中。键值对分别存储对应的信息，将信息存入文档中
          4.使用类和字典相结合的读取文档存储的分类密码信息。
          5.可以输入指定的命令查看指定类下title的信息
          6.使用string和random 模块随机生成指定位长的密码。
"""       


import argparse                                                                # 导入argparse模块（用于解析命令行参数和选项）。命令解析工具
import getpass
import pickle                                                                  # 导入pickle模块，使用内置方法dump/load对列表进行序列化保存/恢复（二进制）
import pprint                                                                  # 导入pprint模块，使得打印输出的格式更加优美。
import random                                                                  # 导入random模块（ 提供了一些不同的随机数字生成器），用于实现自动生成密码功能。
import sys                                                                     # 导入string模块。
import string                                                                  # 导入string模块，调用string.ascii_letters 和string.digits方法取a-Z,0-9所有字符串。  

parser = argparse.ArgumentParser()                                             # 设置一个命令化对象接受命令解析
parser.add_argument('-m', action='store', dest='method',                       # 对象利用add_argument()设置程序可接受的命令行参数。
                    help='操作方式 w：写密码， r：查找密码， g：生成密码')
parser.add_argument('-c', action='store', dest=' category',
                    help='类别')
parser.add_argument('-i', action='store', dest='title',
                    help='查找的名称')
parser.add_argument('-l', type=int, action='store', dest='length',
                    help='密码长度')
args = parser.parse_args()                                                    #  parse_args()实际上是从命令行中返回一些数据，及add_arguments 增加的指令


'''
密码管理器

* 保存密码
* 获取密码

格式：
 * 密码 title
 * {"title": "passwd"}

分类：
 * web
 * 服务器

格式：
 {
 "web":{"jingfeng":"123456", "zhihu":"123456"}
 }
 title | passwd | url

自动生成安全密码 （用户可以输入长度）
'''


def select_db():                                                                   # 定义密码管理器读取函数select_db        
    try:                                                                           # try 判断异常
        with open('zpass.pass', 'rb') as f:                                        # 上下文本管理器打开密码管理器文档，赋值给变量f
            return pickle.load(f)                                                  # pickle.load方法打印出f
    except Exception as e:                                                         # except出现异常
        return False                                                               # 终止



def insert_db(obj):                                                                 # 定义密码管理器写入函数inawer_db，设置一个参数obj.
    with open('zpass.pass', 'wb') as f:                                             # 使用文本管理器打开（关闭）密码管理器文档zpass.pass将打开的文档赋值给变量f
        pickle.dump(obj, f)                                                         # 调用pickle.dump方法，将参数obj 写入f中。


class PassWord(dict):                                                               # 定义PassWord类，父类为dict(z字典)
    
    def __init__(self, category, title, user, passwd):                              # 类方法初始化，设定4个参数（category用来实现密码管理器的分类）
        '''
        {'title':                                                                   # title 参数为了实现标题
                    {
                        user:test,                                                  # user 参数为设置的用户名
                        passwd:123456, 
                        url:jingfeng.com                                            # passwd 参数为密码
                    }
        }
        '''
        super().__init__()                                                          # supper().__init() 继承父类（字典）的方法                                               
        self.title = title                                                          # 定义初始化方法self.title = title
        self.category = category                                                    # catrgory为密码存储的类，为字典的key
        self[title] = {'user': user, 'passwd': passwd}                              # 利用字典的方法d[key]确定user,及passwd


    def passwd_data(self):                                                          # 获取密码的方法
        '''
        {'title': 'test', 'user': 'test', 'passwd': '123456', 'url': 'url.com'}
        |
        V
        {
            'web':{'title':
                    {
                        user:test, 
                        passwd:123456, 
                        url:jingfeng.com
                    }
                }
        }
        '''
        pwd_data = select_db() if select_db() else {}                              # 判断密码管理器文本是否存在，如果存在赋值给变量pwd_data，如果不存在pwd_data为一个空字典。
        if not pwd_data or self.category not in pwd_data:                          # 如果pwd_data为空，或self.catetory(key)不在pwd_data（密码文本中）
            pwd_data[self.category] = {}                                           # 则密码文本文件zpass.pass（字典形式存储）中'分类存储'定义为一个空字典
            pwd_data[self.category][self.title] = self[self.title]                 # 利用字典特性：密码文件--类--title
        pwd_data[self.category][self.title] = self[self.title]                     # 否则直接利用字典方法，确定title 
        return pwd_data                                                            # 返回一个类的的密码存储信息

    def save_passwd(self):                                                         # 密码保存方法
        passwd_data = self.passwd_data()                                           # 将密码存储信息(调用类方法passwd_data)赋值个passwd_data
        pprint.pprint(passwd_data)                                                 # 使用pprint.pprint方法打印输出密码 
        insert_db(passwd_data)                                                     # 同时将密码管理信息写入密码文本文件zpass.pass  (调用管理器写入函数：inawer_db)
        return True                                                                # 返回为真。

    @classmethod                                                                   # 使用类方法（固定写法参数cls：类本身作为对象进行操作的方法）
    def get_item(cls):
        cls.item = ['title', 'user', 'passwd']                                     # 定义cls.item =[['title', 'user', 'passwd']     ]
        return cls.item                                                            # 返回保存值

    @staticmethod                                                                  # 类静态方法：是一种普通函数，就位于类定义的命名空间中，它不会对任何实例类型进行操作。
    def get_passwd():                                                              # 函数用来得到密码管理器密码
        passwd =  select_db()                                                      # 将读取的zpass.pass文件赋值给变量passwd
        return passwd[args.category].get(args.title)                               # 返回密码字段:利用get访问字典项的方法，当参数过多时使用args（self）替代 
 

class WebPassWord(PassWord):                                                       # 定义一个子类用来存储 web类的密码管理器
    def __init__(self, category, title, user, passwd, url):                        # 初始化类方法，包含五个参数  
        super().__init__(category, title, user, passwd)                            # 继承父类方法，传入父类类的4个参数。
        self[title]['url'] = url                                                   # 利用字典d[key]方法，得到url字段

    @classmethod                                                                   # 调用类的方法
    def get_item(cls):                                                             # 类方法固定格式，参数为cls（类本身）
        super().get_item()                                                         # 继承父类方法 get_item()
        cls.item.append('url')                                                     # 通过append()方法，将url追加至 ['title', 'user', 'passwd'] 列表中 
        return cls.item                                                            # 返回列表


class ServerPassWord(PassWord):                                                    # 定义一个子类用来存储 sever类的密码管理器
    
    def __init__(self, category, title, user, passwd, hostname, ip):               # 初始化类方法，包含6个参数
        super().__init__(category, title, user, passwd)                            # 继承父类方法，切记继承父类方法时需要同时传入父类参数。
        self[title]['hostname'] = hostname                                         # 利用字典d[key]方法，得到hostname字段
        self[title]['ip'] = ip                                                     # 同上方法得到ip字段方法

    @classmethod                                                                   # 调用类的方法
    def get_item(cls):                                                             # 类方法固定格式，参数为cls（类本身）
        super().get_item()                                                         # 继承父类方法 get_item()                     
        cls.item.append('hostname')                                                # 通过append()方法，将url追加至 ['title', 'user', 'passwd'] 列表中 
        cls.item.append('ip')                                                      # 同理将ip值 追加值列表末尾
        return cls.item                                                            # 返回列表。


def handle_passwd():                                                               # 定义一个函数用力手动处理密码管理器如何操作。
    passwd_args = {}                                                               # 变量pwsswd_args赋值一个空字典
    user_choice = input("\033[34m1 web, 2 server, 0 退出 \n \033[0m")              # 根据相应的选择可对密码管理器进行相应的操作（选择1时为web类密码，2为服务器类，0退出系统）
    if user_choice != '1' and user_choice != '2':                                  # 当用户输入指令不是1或者2时，系统自动退出。                                      
    	print ('\033[35m退出系统，谢谢使用！\033[0m')                              # 退出系统提示。
    	sys.exit()                                                                 # sys模块退出系统指令
    else:	                                                                       # 当输入对应的1或2指令时进入相应操作。
	    pwd_class = {                                                              # 定义一个字典pwd_class.字典包含两个键值对。
	    '1': ('web', WebPassWord),                                                 # 键1对应的value为一个包含"web"字符和webpassword类的一个元组
	    '2': ('server', ServerPassWord)}                                           # 键2对应的value为包含"server"字符和ServerPassWord类的一个元组
	    category = pwd_class[user_choice][0]                                       # 使用d[key]和元组元素访问方法将"web"或"server"赋值给变量category,从而确定执行哪种类密码的管理。                                   
	    handle_class = pwd_class[user_choice][1]                                   # 同理确定执行哪一类的操作（user_choice值的确定起关键作用）
	    for i in handle_class.get_item():                                          # 确定handle_class后（及类的对象）调用对应的类方法 get_item()得到某一个类下的相关信息（列表的形式存在），利用for遍历所有元素赋值个i
	        passwd_args[i] = input(i + ":")                                        # 因passwd_args为一个空字典，当以i为键时，会将input输入的信息当做item存入空字典中。最终将get_item()的到的列表都会转为字典形式存储。
	    pwd = handle_class(category=category, **passwd_args)                       # pwd是类handle_class（及为web或server类）的一个对象，并传入的参数（category 和**（表示多个参数）passwd_args）
	    stat = pwd.save_passwd()                                                   # 对象pwd调用save_passwd()方法保存对应类的密码信息，赋值给变量stat
	    if stat is False:                                                          # if 判断如果stat 为空，则保存失败。                                                    
	        print('保存失败！')
	    print('保存成功！')



def gen_passwd(length):                                                            # 定义自动生成密码的函数。函数名为gen_passwd，包含一个参数length，控制密码长度
    chars = string.ascii_letters + string.digits + "!@#$%^&*():;"'`'               # 利用string库中string.ascii_letters和string.digits取a-Z,0-9的字符串赋值给变量chars
    return ''.join([random.choice(chars) for i in range(length)])                  # 利用random模块中的random.choice方法及字符串join方法+列表推导式生成随机要求（length）长度的密码 


def main():                                                                        # 定义主函数。
    if args.method == 'r':                                                         # 判断 如果args.method 输入的指令为 r
        print(PassWord.get_passwd())                                               # 则执行密码读取操作
    elif args.method == 'w':                                                       # 如果输入指令为w,则执行密码管理器 写入操作
        handle_passwd()
    elif args.method == 'g':                                                       # 如果输入的指令为g,则执行自动生成随机密码操作。
        print(gen_passwd(args.length))



if __name__ == '__main__':                                                          # 执行主函数
    with open ('main_passwd.pass','rb') as f:                                       # 打开主密码文档文件。
    	main_passwd = pickle.load(f)
    count = 0                                                                       # count变量为0，设置密码验证输入次数      
    while count <3:
    	user_passwd = getpass.getpass("\033[32m欢迎进入密码管理系统，请输入主密码:\033[0m")
    	if user_passwd != main_passwd:
    		count +=1
    		print ("\033[36m密码错误，已重试{}次！\033[0m".format(count))
    		continue
    	print ("\033[31m密码正确，欢迎使用密码管理系统！\033[0m")
    	main()
    else:                                                                             
	    print ('\033[34m重试了三次，退出!\033[0m')                                 # 当count >3 后，说明密码已经重试了三次。
