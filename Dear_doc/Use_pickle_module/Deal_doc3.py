# coding=utf-8
# /usr/bin/env python

'''
脚本作用（第三次更新）1.来打开的文档是否存在，如果存在输出特定格式；如果不存在给予提示。
                      2.将存在的文本文件进行特定格式的处理；
                      3.将处理的文本分成两部分，保存在两个列表中；
                      4.将两列表中的内容通过pickle模块进行序列化处理，输出到新建的两个文本文件中（二进制格式）。
                      5.关闭两文档。
                      
'''
import os                                                    # 导入os模块                                                        
import pickle                                                # 导入pickle模块，使用内置方法dump/load对列表进行序列化保存/恢复。

man=[]                                                       # 新增变量man为一个空列表                      
other=[]                                                     # 新增变量other位一个空列表

if os .path.exists('sketch.txt'):                            # 使用os内置方法exists判断当前路径下是否存在需要打开的文档。
    data=open('sketch.txt')                                  # 利用变量data打开指定文件文件
    for each_line in data:                                   # 对每行文档进行迭代处理。
        try:                                                 # try 异常处理。。
            (role,line_spoken)=each_line.split(':',1)        # 格式处理：对读出的每行文本文件使用split方法（分隔符为‘:’参数1为分割1次）分割两部分分别复制给两个变量。
            line_spoken = line_spoken.strip()                # 对第二个变量末尾进行去除空白符处理。
            if role == 'Man':                                # 判断如果第1个变量值等于字符串'Man' ;
                man.append(line_spoken)                      # 利用append()方法将第二个变量文本追加到新增变量man的空列表中
            elif role == 'Other Man':                        # 否则，如果第一个变量的值等于字符串'Other Man'
                other.append(line_spoken)                    # 利用append()方法将第二个变量文本追加到新增变量other的空列表中.
        except ValueError:                                   # 发生异常，忽略
            pass                     
    data.close()                                             # 关闭文档，打开———关闭。
                
else:                                                        # 如果打开的文档不存在。
    print('The datafile is nod found!')                      # 输出结果给予提示。

try:                                                         # try判断异常，保护以下代码
    with open ('man_data.txt','wb') as man_file:             # 使用上下文本管理器，新建文本文件'other_data.txt'以二进制格式写入新的内容，同时赋值给新的变量man_file
        pickle.dump(man, man_file)                           # 使用pickle内置方法dump将man列表序列化，保存到man_file文件中。
    with open ('other_data.txt','wb') as other_file:         # 同上
        pickle.dump(other, other_file)
       
except pickle.PickleError as err:                            # except...as err 将指定异常抛出.                                   
    print ('File error'+ str(err))                           # 给予错误提示，并打印log

finally:                                                     # finally 最终执行以下代码
    if 'man_file' in locals():                               # if判断，并使用locals判断man_file文本文件是否存在于局部命名空间变量中。
        man_file.close()                                     # 如果man_file 存在，执行文本关闭。
    if 'other_file' in locals():                             # 同上。
        other_file.close()


