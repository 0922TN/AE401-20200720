# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:33:57 2020

@author: User
"""


import random

ans = random.randint(1,10)
 
n = input("猜一個數字:")
n = int(n)

if ans == n:
    print("猜對了")
    
else:
    print("猜錯了! 答案是",ans)
          