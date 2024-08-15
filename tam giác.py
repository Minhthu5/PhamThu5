# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:17:38 2024

@author: 84982
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print("a, b, c có thể là ba cạnh của một tam giác.")
    else:
        print("a, b, c không thể là ba cạnh của một tam giác.")
else:
    print("Các cạnh của tam giác phải lớn hơn 0.")
    