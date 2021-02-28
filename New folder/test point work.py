
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
        print(label,' is not found')
        
    return x   
        

def findresult(l, p, e, Q, bq,partnu,s3,i):
    seriesname = pd.read_csv(i, encoding='ISO-8859-1', nrows=1, sep=';', low_memory=False)

    pnu = findmark(partnu, seriesname.columns)
    injname = seriesname.loc[0, pnu]

    tex = pd.read_csv(i,encoding='ANSI',skiprows=3,sep=';',low_memory=False)
    tex.fillna(0, inplace=True)
    
    x = findmark(l, tex.columns)
    pr = findmark(p, tex.columns)
    et = findmark(e, tex.columns)
    inq = findmark(Q, tex.columns)
    baq = findmark(bq, tex.columns)
    ts = findmark(s3, tex.columns)

    # inq = findmark(Q, tex.columns[0])
    # baq = findmark(bq, tex.columns[0])
    # ts = findmark(s3, tex.columns[0])
    # x = findmark(l, tex.columns[0])
    
               
    Pressure = tex.loc[tex[x]==' Measure'][pr]
    Pressure.name = 'Pressure(bar)'
    ET = tex.loc[tex[x] ==' Measure'][et]
    ET.name = 'ET(us)'
    table_head = pd.concat([Pressure,ET], axis=1).reset_index(drop=True)
    # table_head2 = pd.concat([table_head,table_head,table_head],key=['injQ','BFQ','3S'], axis=1,ignore_index=True)
    table_head2 = pd.concat([table_head, table_head, table_head], axis=0,keys=['injQ','BFQ','3S'], ignore_index=True)
    print (table_head2)
#    press=key[pr]
#    print(press)
#    press.name='Pressure'
#    etime=key[et]
#    etime.name='ET'
#     press = tex.loc[[pr], [key]]

     # table_head = pd.concat([press,etime],axis=1).reset_index(drop=True)
    
    return x, pr, et, inq, baq, ts
    # return key

if __name__ == '__main__':
    file = openfile()
    
    l = [' Lastpunkt']
    p = [' P_Rail(S)_Soll']
    e = [' t_MI(S)_Soll']
    Q = [' Q_emi2_MI(MV)', ' v1.mean(HDA_1)']
    bq = [' Q_Inj_BF(MV)', ' Q_Backflow(M)']
    s3 = [' Q_emi2_MI_3s(MV)',' V_Inj1StdAbw(HDA_1)']
    partnu = [' Partnumber']

    key,pr,et,inq, baq, ts = findresult(l, p, e, Q, bq, partnu, s3, file[0])

    # key = findresult(l, p, e, Q, bq, s3, file)



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