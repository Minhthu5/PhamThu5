# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:09:44 2024

@author: 84982
"""
import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        # Phương trình trở thành phương trình bậc nhất bx + c = 0
        x = -c / b
        print(f"Nghiệm của phương trình {b}x + {c} = 0 là: x = {x}")
else:
    # Tính toán discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Hai nghiệm phân biệt
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}")
    elif discriminant == 0:
        # Một nghiệm kép
        x = -b / (2 * a)
        print(f"Phương trình có một nghiệm kép: x = {x}")
    else:
        # Không có nghiệm thực
        print("Phương trình vô nghiệm trong tập số thực.")