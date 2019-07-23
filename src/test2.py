# -*- coding: utf-8 -*-
import tkinter.messagebox

#s = ['e:/dksd.txt/dksjk/12345.txt', 'e:/fdsa/sfsf/dsjk', 'f:/dsd.txt/dd/sss.asd']
#for i in s:
    #if i[-4:] == '.txt':
        #print(i)

t = tkinter.messagebox.askyesnocancel('a','a')
if t:
    print('True')
elif t is None:
    print('None')
else:
    print('False')