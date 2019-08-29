# -*- coding: utf-8 -*
import tkinter as tk
from tkinter import ttk
from lib import dial ,writeEdit
import os

class Account(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.gui_Treeview()
        self.print_call_back()
        self.write_call_back()
        self.open_call_back()
        self.master.title('宽带账号密码获取器')

    def print_call_back(self):
        self.print = tk.Button(self, text='获取账号密码', command=self.printResults)
        self.print.grid()

    def gui_Treeview(self):
        self.tree = ttk.Treeview(self, height=10, show="headings")  # 表格
        self.tree['columns'] = ("账号", "密码", "结果")
        self.tree.column("账号", width=100)  # 表示列,不显示
        self.tree.column("密码", width=100)
        self.tree.column("结果", width=100)
        self.tree.heading("账号", text="账号")  # 显示表头
        self.tree.heading("密码", text="密码")
        self.tree.heading("结果", text="结果")
        self.tree.grid()

    def write_call_back(self):
        self.write = tk.Button(self, text='可用账号生成', command=self.writeResults)
        self.write.grid()

    def open_call_back(self):
        self.open = tk.Button(self, text='打开生成的文件', command=self.OpenFileWindow)
        self.open.grid()

    def gui_label(self, input='        ',colour="#ffffff" ):
        self.label = tk.Label(self, text = input,bg=colour)
        self.label.grid()

    def printResults(self):
        global data
        data = self.getResults()
        for text in data[0]:
            i = 0
            self.tree.insert("", i,  values=text)  # 插入数据，
            i += 1
        self.gui_label('账号密码获取完成', 'yellow')

    def getResults(self):
        return dial()

    def writeResults(self):
        writeEdit(data[1])
        self.gui_label('文件写入成功', 'blue')

    def openwindow(self, dir_path):
        os.system("explorer %s" % dir_path)

    def OpenFileWindow(self):
        file_path = os.getcwd() + r'\Retract.txt'
        print(file_path)
        self.openwindow(file_path)
        self.gui_label('文件以打开', '#00ff00')

if __name__ == '__main__':
    app = Account()
    app.mainloop()
