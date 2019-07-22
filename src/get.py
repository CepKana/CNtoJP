# -*- coding: utf-8 -*-
import os
import tkinter.messagebox
import sys


title = '日文文件乱码转换工具v0.1 by羊君'
if not tkinter.messagebox.askyesno(title, '本工具只适用于简体中文系统，请确保目录下均为日文文件名，是否继续？'):
    #询问用户允许
    sys.exit()
cwd = os.getcwd()
#获取当前目录
content = []
#用来存放目录的list


def change_code(file):
    #修改文件名编码
    try:
        file.encode('gb2312')
    except UnicodeEncodeError:
        try:
            file1 = file.encode('gbk')
            file2 = file1.decode('Shift-JIS')
            return file2
        except(UnicodeDecodeError, UnicodeEncodeError):
            return file
    return file


l = 0
for files in os.walk(cwd):
    #读取当前目录下所有文件/目录及子目录
    if not l == 0:
        if files[0][-1] == '\\':
            content.append(files[0][:-1])
        else:
            content.append(files[0])
    for file in files[-1]:
        #对所有文件（包括子目录中的文件）进行修改操作
        old_name = os.path.join(files[0], file)
        new_name = os.path.join(files[0], change_code(file))
        if not old_name == new_name:
            os.rename(old_name, new_name)
    l += 1


consorted = {}
for cnt in content:
    #查找路径中'\'的出现次数，次数越多说明路径越深
    k = 0
    for i in cnt:
        if i == '\\':
            k += 1
    consorted[cnt] = k


consorted0 = sorted(consorted.items(), key=lambda x: x[1], reverse=True)
#对目录按照'\\'的数量进行排序
for cnt in consorted0:
    #对目录进行修改
    lst = cnt[0].rfind('\\')
    new_path = os.path.join(cnt[0][:lst+1], change_code(cnt[0][lst+1:]))
    if not cnt[0] == new_path:
        os.rename(cnt[0], new_path)


tkinter.messagebox.showinfo(title, '转换成功！')
#运行完成弹出提示窗口

