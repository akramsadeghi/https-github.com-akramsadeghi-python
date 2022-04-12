# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:08:04 2022

@author: shabdar
"""


# cnvert second to time
total_second = float(input(":مجموع ثانیه ها را وارد کنید"))
hours = total_second//3600
if hours>24:
    days=hours//24
    hours=hours%24
    print("یک روز اضافه می شود")

minutes = (total_second%3600)//60

seconds = ((total_second%3600)%60)
print(days,":",hours,":",minutes,":",seconds)
            
            
            
    
    