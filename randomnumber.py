# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:37:28 2022

@author: shabdar
"""

#پر کردن یک لیست با اعداد تصادفی و غیر تکراری
import random
my_list=[]

n = int(input("طول لیست را اعلام کنید:"))

for i in range(n):
    
    q=random.randint(0,1000)
    my_list.append(q)
    my_list=list(set(my_list))
    my_list.sort()
print(my_list)
    
