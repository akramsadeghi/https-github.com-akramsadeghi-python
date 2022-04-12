# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:42:54 2022

@author: shabdar
"""
#import math
fbonacci =[ ] 
#سری فیبوناچی یک سری بینهایت است پس n را هم تعداد سری فیبوناچی و هم عدد آن قرار دادم.
n = int(input("عدد سری فیبوناچی و تعداد تکرار را وارد کنید."))

f0, f1, f2 = 1, 0, None
list = []
for i in range(n):
        f2 = f1 + f0
        list.append(f2)
        
        f0 = f1
        f1 = f2
        
        
for i in range(0,n,1):
   fbonacci.append(list[i])


print(fbonacci)    
