# -*- coding: utf-8 -*-
import chardet

s = '我的师姐'.encode('gbk')
print(chardet.detect(s))
