# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:15:40 2022

@author: shabdar
"""


# word exite
keep_going = 'y'
# محاسبه تعدادی از اعداد ورودی تا کلمه exite وارد شود
#a=float(input("لطفا یک عدد وارد کنید"))
total = 0

while keep_going =='y':
    a = float(input("لطفا یک عدد وارد کنید"))
    #1print(a)
    total = total + a
    print(total)
    keep_going = input("اگر می خواهید از برنامه خارج شوید exit را وارد کنید")
    if keep_going =='exit':
        keep_going !='y'
    else:
        keep_going ='y'
        
print(total)