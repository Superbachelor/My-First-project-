# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:47:55 2021

@author: LUJ9WX
"""

from tkinter import *

from tkinter import filedialog
import pandas as pd
from pandas.testing import assert_frame_equal as pcheck

def openfile():
    file=filedialog.askopenfilenames(title='打开文件',filetypes=[('text files', '.txt'),('all files', '.*')])
    print(file)
    return file


def findmark(label, base):
    x=0
    for i in label:
        if i in base:
            x=i
        else:
            pass
    if x ==0:
        print('not found')
        
    return x   
        

def findresult(l, p, e, Q, bq, s3,file):
    tex = pd.read_csv(file[0],encoding='ANSI',skiprows=3,sep=';')            
#    tex.fillna(0,inplace=True)
    
    x = findmark(l, tex.columns[0])
    
#    pr = findmark(p, tex.columns[0])
#    et = findmark(e, tex.columns[0])
#    inq = findmark(Q, tex.columns[0])
#    baq = findmark(bq, tex.columns[0])
#    ts = findmark(s3, tex.columns[0])
    
               
    k=tex.loc[tex[str(x)]=='Measure'].index[0]
    print(k)
#    press=key[pr]
#    print(press)
#    press.name='Pressure'
#    etime=key[et]
#    etime.name='ET'
            
#   table_head = pd.concat([press,etime],axis=1).reset_index(drop=True)
    
    #return key, pr, et, inq, baq, ts
    return k

if __name__ == '__main__':
    file = openfile()
    
    l = (' Lastpunkt','1')
    p = [' P_Rail(S)_Soll']
    e = [' t_MI(S)_Soll']
    Q = [' Q_emi2_MI(MV)']
    bq = [' Q_Inj_BF(MV)']
    s3 = [' Q_emi2_MI_3s(MV)']

#    key,pr,et,inq, baq, ts = findresult(l, p, e, Q, bq, s3, file)
    key = findresult(l, p, e, Q, bq, s3, file)



#    file = openfile()
#    for i in file:
#        try:
#            data = pd.read_csv(i,encoding='ANSI',skiprows=3,sep=';')
#            data.fillna(0,inplace=True)
#            s=data[' Lastpunkt'].str.contains(' Measure')
#            s.fillna(False,inplace=True)
#            press=data[s][' P_Rail(S)_Soll']
#            press.name='Pressure'
#            et=data[s][' t_MI(S)_Soll']
#            et.name='ET'
#            stu=pd.concat([press,et],axis=1).reset_index(drop=True)
#            print(stu)
#            
#            if x==0:
#                stup=stu
#                x+=1
#            if x>0:
#                try:pcheck(stup,stu,check_dtype=False)
#                except: 
#                    print('测试点不相同')
#                    break
#            table=pd.concat([stu,stu,stu],axis=0).reset_index(drop=True)
#            
#           
#        except:
#            raise ValueError
   # mainloop()