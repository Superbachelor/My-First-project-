# -*- coding: utf-8 -*-

from tkinter import *

from tkinter import filedialog
import pandas as pd

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("单点测试_v1.2")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=1, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=1, column=5)

        #文本框
        # self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        # self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=120, height=30)  #处理结果展示
        self.result_data_Text.grid(row=2, column=1, rowspan=20, columnspan=30)
        # self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        # self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="裁入文件", bg="lightblue", width=10,command=self.openfile)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=0)

        self.str_trans_to_md5_button = Button(self.init_window_name, text="保存文件", bg="lightblue", width=10,command=self.savefile)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=4, column=0)

    def openfile(self):
        file = filedialog.askopenfilenames(title='打开文件', filetypes=[('text files', '.txt'), ('all files', '.*')])
        l = [' Lastpunkt']
        p = [' P_Rail(S)_Soll']
        e = [' t_MI(S)_Soll']
        Q = [' Q_emi2_MI(MV)', ' v1.mean(HDA_1)']
        bq = [' Q_Inj_BF(MV)', ' Q_Backflow(M)']
        s3 = [' Q_emi2_MI_3s(MV)', ' V_Inj1StdAbw(HDA_1)']
        partnu = [' Partnumber']

        table, _, _ = findresult(l, p, e, Q, bq, partnu, s3, file[0])

        tab = table.copy(deep=False)

        for i in file:
            check, result, injname = findresult(l, p, e, Q, bq, partnu, s3, i)
            if check.equals(tab) == False:
                print('测试点不相同')
                break

            table[injname] = result
        self.asd = table.set_index('Pressure(bar)', 'ET(us)')
        self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0,self.asd)
    def savefile(self):
        try:

            self.result_data_Text.insert(END,"\n 结果已保存")
            self.asd.to_excel('result.xlsx')
        except:
            self.result_data_Text.delete(1.0, END)
            self.result_data_Text.insert(1.0, "结果保存失败")



def gui_start():



    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()


    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


def findmark(label, base):
    x = 0
    for i in label:
        if i in base:
            x = i
        else:
            pass
    if x == 0:
        print(label, ' is not found')

    return x


def findresult(l, p, e, Q, bq, partnu, s3, i):
    seriesname = pd.read_csv(i, encoding='ISO-8859-1', nrows=1, sep=';', low_memory=False)

    pnu = findmark(partnu, seriesname.columns)
    injname = seriesname.loc[0, pnu]

    tex = pd.read_csv(i, encoding='ANSI', skiprows=3, sep=';', low_memory=False)
    tex.fillna(0, inplace=True)

    x = findmark(l, tex.columns)
    pr = findmark(p, tex.columns)
    et = findmark(e, tex.columns)
    inq = findmark(Q, tex.columns)
    baq = findmark(bq, tex.columns)
    ts = findmark(s3, tex.columns)
    print(injname)
    # inq = findmark(Q, tex.columns[0])
    # baq = findmark(bq, tex.columns[0])
    # ts = findmark(s3, tex.columns[0])
    # x = findmark(l, tex.columns[0])

    Pressure = tex.loc[tex[x] == ' Measure'][pr]
    Pressure.name = 'Pressure(bar)'
    ET = tex.loc[tex[x] == ' Measure'][et]
    ET.name = 'ET(us)'
    table_head = pd.concat([Pressure, ET], axis=1).reset_index(drop=True)
    line_data = {'Pressure(bar)': ['---------'], 'ET(us)': ['---------']}
    line = pd.DataFrame(line_data)
    print(line)
    # table_head2 = pd.concat([table_head,table_head,table_head],key=['injQ','BFQ','3S'], axis=1,ignore_index=True)
    table_head2 = pd.concat([table_head, line, table_head, line, table_head], axis=0, ignore_index=True)
    print(table_head2)

    #    result = pd.concat([inq,baq,ts],axis=0,keys=['injQ','BFQ','3S'], ignore_index=True)
    injQ = tex.loc[tex[x] == ' Measure'][inq]
    Backflow = tex.loc[tex[x] == ' Measure'][baq]
    sss = tex.loc[tex[x] == ' Measure'][ts]
    line2 = pd.DataFrame(['----------'])
    result = pd.concat([injQ, line2, Backflow, line2, sss], axis=0, ignore_index=True)

    return table_head2, result, injname

gui_start()