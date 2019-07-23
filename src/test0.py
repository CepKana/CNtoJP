# -*- coding: utf-8 -*-
#import chardet
import os

#s = '我的师姐'.encode('gbk')
#print(chardet.detect(s))


fd = open('test.txt', 'r', encoding='utf-8')
fd0 = fd.read().encode('gbk').decode('Shift-JIS')
fd.close()
print(fd0)
fd1 = open('test.txt', 'w+', encoding='utf-8')
fd1.write(fd0)
fd1.close()

