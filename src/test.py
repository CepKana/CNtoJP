# -*- coding: utf-8 -*-


s = '峠垷夣妝崏栤拞'
s1 = s.encode('gbk')
print(s1)
s2 = s1.decode('Shift-JIS')
print(s2)
