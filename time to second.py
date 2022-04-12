# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:12:20 2022

@author: shabdar
"""


#convert clock to second
#از توابع time استفاده نشده است.

h,m,s =input("زمان را با فرمت مثلا 00:00:00 وارد کنید").split(':')


a=int(h)
b=int(m)
c=int(s)
if a>24 or b>60 or c>60:
    print("توجه داشته باشید که ساعت بیشتر از 24 و دقیقه و ثانیه بیشتر از 60 نمی باشد. ")
else:
    second_time = a*3600+b*60+c
    print("ثانیه",second_time)

