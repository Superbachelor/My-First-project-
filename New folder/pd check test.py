import pandas as pd
student = pd.read_excel('result.xlsx',index_col="Pressure(bar)")
temp = student.iloc[:,1:].apply(pd.to_numeric,errors='ignore')
student["total"] = temp.sum(axis=1)#axis 0为列，1为行
student["avg"] = temp.mean(axis=1)
print(student)