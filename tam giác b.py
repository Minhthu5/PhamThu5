# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:19:06 2024

@author: 84982
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Các cạnh của tam giác phải lớn hơn 0.")
elif a + b > c and a + c > b and b + c > a:
    # Xác định loại tam giác
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or b == c or a == c:
        # Kiểm tra tam giác cân
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("Tam giác cân và vuông.")
        else:
            print("Tam giác cân.")
    else:
        # Kiểm tra tam giác vuông
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("Tam giác vuông.")
        else:
            print("Tam giác thường.")
else:
    print("a, b, c không thể là ba cạnh của một tam giác.")