# -*- coding: utf-8 -*-



#k1 = s.encode('gbk')
#print(k1)
#k2 = k1.decode('Shift-JIS')
#print(k2)

fd = open('readme.txt', 'r', encoding='gb2312')
print(fd.read())