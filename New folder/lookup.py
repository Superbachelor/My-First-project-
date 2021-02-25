# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:04:18 2020

@author: LUJ9WX
"""
#数据lookup
import pandas as pd

 students = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Students')
#scores = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Scores')
 table = students.merge(scores, how='left', left_on='ID',right_on='ID').fillna(0)
table.Score = table.Score.astype(int)
 print(table)

# students = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Students', index_col='ID')
# scores = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Scores', index_col='ID')
# table = students.merge(scores, how='left', left_on=students.index, right_on=scores.index).fillna(0)
# table.Score = table.Score.astype(int)
# print(table)

# 左连接
students = pd.read_excel('Student_score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('Student_score.xlsx', sheet_name='Scores', index_col='ID')
table = students.join(scores, how='left').fillna(0)
table.Score = table.Score.astype(int)
print(table)

