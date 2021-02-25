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
    return file
    
        
def findresult(l, p, e, Q, bq, s3,file):
    tex = pd.pd.read_csv(file[1],encoding='ANSI',skiprows=3,sep=';')            
    tex.fillna(0,inplace=True)
    x = findmark(l, tex.columns)
    pr = findmark(p, tex.columns)
    et = findmark(e, tex.columns)
    return x, pr, et

def findmark(label, base):
    x='not found'
    for i in label:
        if i in base:
            x=i
    if x =='not found':
        print(x)
    else:
        return x


if __name__ == '__main__':
    #创造界面
    #wnd=Tk()
    #wnd.geometry('100x50+10+10')
    #打开文档
    #file = Button(text='打开',command=openfile).pack(anchor='s',side='left',padx=10)

    l = [' Lastpunkt']
    p = [' P_Rail(S)_Soll']
    e = [' t_MI(S)_Soll']
    Q = [' Q_emi2_MI(MV)']
    bq = [' Q_Inj_BF(MV)']
    s3 = [' Q_emi2_MI_3s(MV)']

    file = openfile()
    sad = findresult(l, p, e, Q, bq, s3, file)
    print(sad)


    # for i in file:
    #     try:
    #         data = pd.read_csv(i,encoding='ANSI',skiprows=3,sep=';')
    #         data.fillna(0,inplace=True)
    #         s=data[' Lastpunkt'].str.contains(' Measure')
    #         s.fillna(False,inplace=True)
    #         press=data[s][' P_Rail(S)_Soll']
    #         press.name='Pressure'
    #         et=data[s][' t_MI(S)_Soll']
    #         et.name='ET'
    #         stu=pd.concat([press,et],axis=1).reset_index(drop=True)
    #         print(stu)
    #
    #         if x==0:
    #             stup=stu
    #             x+=1
    #         if x>0:
    #             try:pcheck(stup,stu,check_dtype=False)
    #             except:
    #                 print('测试点不相同')
    #                 break
    #         table=pd.concat([stu,stu,stu],axis=0).reset_index(drop=True)
    #
    #
    #     except:
    #         raise ValueError
   # mainloop()