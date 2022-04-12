# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 22:55:43 2022

@author: shabdar
"""


# tas simulator
min=1
max=6

import random
rolling = "y"

while rolling =="y":
   rolling=input("آیا تاس بندازم؟")
   print("عدد 6 جایزه دارد.")
   x=(random.randint(min,max))
   print(x)
   if x==max:
       print(random.randint(min,max))
       