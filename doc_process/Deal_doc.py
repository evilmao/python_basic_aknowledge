# coding=utf-8
# /usr/bin/env python

'''
此脚本用来打开的文档是否存在，如果存在输出特定格式；如果不存在给予提示。
'''

import os                                                    # 导入os模块                                                        


if os .path.exists('sketch.txt'):                            # 判断当前路径下是否存在需要打开的文档。
    data=open('sketch.txt')                                  # 打开文件
    for each_line in data:                                   # 对每行文档进行处理
        try:                                                 # try 异常处理。
            (role,spoken_line)=each_line.split(':',1)        # 格式处理
            print (role, end='')
            print ('said:', end='')
            print (spoken_line, end='')
        except:                                              # 发生异常，忽略
            pass                     
    data.close()                                             # 关闭文档，打开———关闭。
                
else:                                                        # 如果打开的文档不存在。
    print('The file is nod found!')                          # 提示
