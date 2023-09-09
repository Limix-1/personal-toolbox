import tkinter as tk
from tkinter import filedialog


# 返回主菜单
def go_back(x, root):
    root.deiconify()
    x.destroy()


# 记录目标文件位置
def open_file_dialog(x, var):
    var.set('选择文件位置')
    file_path = filedialog.askopenfilename()
    if file_path:
        x.delete(0, tk.END)
        x.insert(0, file_path)


# 记录选择的文件夹位置
def open_directory_dialog(x, var):
    var.set('选择输出文件')
    file_path = filedialog.askdirectory()
    if file_path:
        x.delete(0, tk.END)
        x.insert(0, file_path)


# 判断是否为数字
def is_digit(content):
    return content.isdigit()


def event(x):
    print("测试")