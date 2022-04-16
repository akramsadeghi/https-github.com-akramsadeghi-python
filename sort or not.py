# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:38:44 2022

@author: shabdar
"""

#دریافت آرایه ها و تشخیص مرتب بودن یا نبودن آنها
my_list1=[]
my_list2=[]

again='y'

while again=='y':
    w=float(input(":یک آرایه عددی به لیست اضافه کنید"))
    my_list1.append(w)
    
    again=input("آیا هنوز آرایه اضافه میکنید:")
    if again!='y':
        break
    
print(my_list1)
my_list2=sorted(my_list1)
 
 
if my_list2==my_list1:
    print("آرایه ها مرتب هستند")
    print(my_list1)
else:
    print("لیست مرتب شده به صورت زیر هست")  
    print(my_list2)  