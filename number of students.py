# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:09:44 2022

@author: shabdar
"""


#تعداد دانشجویان کلاس و نمرات آنها
student_number = int(input("تعداد دانشجویان کلاس چند نفر هستند : "))
total=0
a=0
b=100
for num in range(student_number):
    grade=float(input("لطفا نمره درس برنامه نویسی را وارد کنید"))
    total=total+grade

    
    if grade>a:
        a=grade
    else:
        a!=grade
        
    if grade<b:
        b=grade
    else:
        b!=grade        
    
    
average=total/student_number
print("میانگین نمرات درس برنامه نویسی",average) 
print("بزرگترین نمره : ",a)  
print("کمترین نمره : ",b) 