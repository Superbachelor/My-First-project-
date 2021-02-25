# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:52:00 2020

@author: LUJ9WX
"""

#open files
from tkinter import *

from tkinter import filedialog
import pandas as pd
from pandas.testing import assert_frame_equal as pcheck

table2=pd.DataFrame(index=['Pressure','ET'])

def openfile():
    file=filedialog.askopenfilenames(title='打开文件',filetypes=[('text files', '.txt'),('all files', '.*')])
    injnamelist=[]
    x=0
    for i in file:
        try:
            data = pd.read_csv(i,encoding='ANSI',skiprows=3,sep=';')
            data.fillna(0,inplace=True)
            
            #找到测试轨压和加点时间
            
            s=data[' Lastpunkt'].str.contains(' Measure')
            s.fillna(False,inplace=True)
            press=data[s][' P_Rail(S)_Soll']
            press.name='Pressure'
            et=data[s][' t_MI(S)_Soll']
            et.name='ET'
            stu=pd.concat([press,et],axis=1).reset_index(drop=True)
            print(stu)
            
            if x==0:
                stup=stu
                x+=1
            if x>0:
                try:pcheck(stup,stu,check_dtype=False)
                except: 
                    print('测试点不相同')
                    break
            table=pd.concat([stu,stu,stu],axis=0).reset_index(drop=True)
            
           
        except:
            raise ValueError
            
    for i in file:
        seriesname=pd.read_csv(i,encoding='ISO-8859-1',nrows =1,sep=';')
        injname=seriesname.loc[0,' Partnumber']
        
        #喷油器测试结果    
        data = pd.read_csv(i,encoding='ISO-8859-1',skiprows=3,sep=';')
        data.fillna(0,inplace=True)
        intq= data[s][' Q_emi2_MI(MV)']
        #intq.name=injname
        bfq= data[s][' Q_Inj_BF(MV)']
       # bfq.name=injname
        ts=data[s][' Q_emi2_MI_3s(MV)']
        #ts.name=injname
        injector=pd.concat([intq,bfq,ts],axis=0).reset_index(drop=True)
        table[injname]=injector
    
    #table=table(index_col=None)
    table.to_excel('People22.xlsx')           
            
wnd=Tk()

wnd.geometry('100x50+10+10')
Button(text='打开',command=openfile).pack(anchor='s',side='left',padx=10)

mainloop()

#from tkinter import *
#from tkinter.scrolledtext import ScrolledText
#
#def load():
#    with open(filename.get()) as file:
#        contents.delete('1.0', END)
#        contents.insert(INSERT, file.read())
#
#def save():
#    with open(filename.get(), 'w') as file:
#        file.write(contents.get('1.0', END))
#
#top = Tk()
#top.title("Simple Editor")
#
#contents = ScrolledText()
#contents.pack(side=BOTTOM, expand=True, fill=BOTH)
#
#filename = Entry()
#filename.pack(side=LEFT, expand=True, fill=X)
#
#Button(text='Open', command=load).pack(side=LEFT)
#Button(text='Save', command=save).pack(side=LEFT)
#
#mainloop()