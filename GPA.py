# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 01:06:02 2024

@author: 84982
"""

gpa = float(input("Nhập điểm trung bình (GPA) của bạn: "))
if gpa < 3.5:
    print("Học lực Kém")
elif 3.5 <= gpa < 5.0:
    print("Học lực Yếu")
elif 5.0 <= gpa < 7.0:
    print("Học lực Trung bình")
elif 7.0 <= gpa < 8.0:
    print("Học lực Khá")
elif 8.0 <= gpa < 9.0:
    print("Học lực Giỏi")
elif 9.0 <= gpa <= 10:
    print("Học lực Xuất sắc")
else:
    print("Điểm GPA không hợp lệ")