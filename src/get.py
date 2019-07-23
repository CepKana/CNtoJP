# -*- coding: utf-8 -*-
import os
import tkinter.messagebox
import sys


title = '日文文件乱码转换工具v0.2.1 by羊君'
if not tkinter.messagebox.askyesno(title, '本工具只适用于简体中文系统，\
请确保目录下均为日文文件名，是否继续？'):
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
            file.encode('Shift-JIS')
            return file
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
        #排除根目录
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
        #不想考虑重名情况了，正常情况下不可能重名
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
#以上为更改目录和文件名，下面开始修改txt文件内容


txtlist = []
txtcount = 0
# 创建记录txt文件的list，同时记录txt文件数量
for files in os.walk(cwd):
    for file in files[-1]:
        path_name = os.path.join(files[0], file)
        if path_name[-4:] == '.txt':
            txtlist.append(path_name)
            txtcount += 1
            # 记录txt文件的路径


if tkinter.messagebox.askyesno(title, '已经检测到' + str(txtcount) + \
                                      '个txt文件，是否进行txt内容的转换？'):
    ask = tkinter.messagebox.askyesnocancel(title, '是否将转换后的txt直接替代原文件？\
    \n选择是：替代；选择否：在同一目录建立新的txt文件；选择取消：取消\
    转换txt文件的操作')
    #询问对txt的操作
    if ask is None:
        pass
    else:
        for i in txtlist:
            try:
                txtfile = open(i, 'r', encoding='gb2312')
                txtfile.read()
                txtfile.close()
                #只有当使用read时，python才会尝试decode
            except UnicodeDecodeError:
                try:
                    txtfile = open(i, 'r', encoding='Shift-JIS')
                    txtfile0 = txtfile.read()
                    txtfile.close()
                    if ask:
                        new_file = open(i, 'w+', encoding='utf-8')
                        new_file.write(txtfile0)
                        new_file.close()
                    else:
                        inew = i[0:-4] + '0' + i[-4:]
                        # 建立的新文件在原文件名后加0
                        new_file = open(inew, 'w+', encoding='utf-8')
                        new_file.write(txtfile0)
                        new_file.close()
                except UnicodeDecodeError:
                    pass


tkinter.messagebox.showinfo(title, '转换成功！')
#运行完成弹出提示窗口

