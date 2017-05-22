# coding=utf-8
# /usr/bin/env python

'''
脚本作用（第一次更新）：1.来打开的文档是否存在，如果存在输出特定格式；如果不存在给予提示。
                        2.将存在的文本文件进行特定格式的处理；
                        3.将处理的文本分成两部分，保存在两个列表中；
                        4.将两列表中的内容写入到新建的两个文本文件中。
                        5.关闭文档。
'''

import os                                                # 导入os模块                                                        


man=[]                                                   # 新增变量man为一个空列表
other=[]                                                 # 新增变量other位一个空列表

if os .path.exists('sketch.txt'):                        # 使用os内置方法exists判断当前路径下是否存在需要打开的文档。
    data=open('sketch.txt')                              # 利用变量data打开指定文件文件
    for each_line in data:                               # 对每行文档进行处理
        try:                                             # try 异常处理。
            (role,line_spoken)=each_line.split(':',1)    # 格式处理：对读出的每行文本文件使用split方法（分隔符为‘:’参数1为分割1次）分割两部分分别复制给两个变量。
            line_spoken = line_spoken.strip()            # 对第二个变量末尾进行禁止换行符处理。   
            if role == 'Man':                            # 判断如果第1个变量值等于字符串'Man' ; 
                man.append(line_spoken)                  # 利用append()方法将第二个变量文本追加到新增变量man的空列表中
            elif role == 'Other Man':                    # 否则，如果第一个变量的值等于字符串'Other Man' 
                other.append(line_spoken)                # 利用append()方法将第二个变量文本追加到新增变量other的空列表中.
        except ValueError:                               # 发生异常，忽略
            pass                     
    data.close()                                         # 关闭文档，打开———关闭。
                
else:                                                    # 如果打开的文档('sketch.txt')不存在。
    print('The datafile is nod found!')                  # 给予提示！

try:                                                     # 再次try判断异常
    man_file = open('man_data.txt','w')                  # 当前目录下创建新（'w'写和新建）文本文件'man_data.txt'并打开，同时复制给新的变量man_file.
    other_file = open('other_data.txt','w')              # 当前目录下创建另一个新文本文件'other_data.txt'并打开，同时复制给另一个新的变量other_file.
    man_file.write(str(man))                             # 利用文本写入方法write,将man的列表内容以字符串的方式写入变量名为man_file文本文件中
    other_file.write(str(other))                         # 利用文本写入方法write,将other的列表内容以字符串的方式写入变量名为man_file文本文件中
    
except IOError as err:                                   # except...as err 将指定异常抛出.                    
    print ('File error'+ str(err))                       # 给予错误提示，并打印err (出错的详情，即生成错误日志 log)

finally:                                                 # finally 语句（是无论是否有异常，最后都要做的一些事情）
    if 'man_file' in locals():                           # if判断，并使用locals(局部命名空间) 判断man_file文本文件是否存在。
        man_file.close()                                 # 如果man_file 存在，执行文本关闭。
    if 'other_file' in locals():                         # 同上
        other_file.close()


