# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:07:25 2024

@author: 84982
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    # Tính nghiệm của phương trình
    x = -b / a
    print(f"Nghiệm của phương trình {a}x + {b} = 0 là: x = {x}")