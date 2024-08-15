# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:24:57 2024

@author: 84982
"""

a=float(input("Nhập quảng đường(km): "))
if a <= 1:
    tong_tien = 20000
elif a <= 3:
    tong_tien = 20000 + (a - 1) * 13000
elif a <= 8:
    tong_tien = 20000 + 2 * 13000 + (a - 3) * 12000
elif a > 8:
    tong_tien = 20000 + 2 * 13000 + 5 * 12000 + (a - 8) * 10000                                                                                                                
elif tong_tien > 100000:
    tong_tien = tong_tien - tong_tien * (8/100)
elif tong_tien <= 100000:
    tong_tien =  tong_tien
print("số tiền taxi là", tong_tien)