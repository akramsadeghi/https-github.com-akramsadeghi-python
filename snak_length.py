# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:02:47 2022

@author: shabdar
"""

#رسم مار

n=int(input("طول مار  را برای رسم مشخص کنید:"))
for i in range(n): 
    if i%2==0:
        print('*',end='')
    else:
        print('#',end='')
    