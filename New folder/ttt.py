# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:06:59 2021

@author: LUJ9WX
"""

import tkinter as tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
import pandas as pd
from pandas.testing import assert_frame_equal as pcheck

def open_file():
    """Open a file for editing."""
    filepath = askopenfilenames(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    for i in filepath:
        #text = pd.read_csv(i,encoding='utf-8',skiprows=3,sep=';')
        text = pd.read_csv(i,encoding='ANSI',skiprows=3,sep=';').head(20)
        text.fillna(0,inplace=True)
        txt_edit.insert(tk.END, text).encoding('GBK')
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
