from tool_UI import *
import tkinter as tk
from tkinter import filedialog
import pywintypes
import win32api


root = tk.Tk()
root.title("脚本工具箱")
root.geometry("650x300")

# 工具0 UI
label1 = tk.Label(root, text="SDF文件切分工具")
label1.grid(row=0, column=0, padx=10, pady=10)
button1 = tk.Button(root, text="打开工具", command=lambda x=root: tool0UI.tool0(x))
button1.grid(row=0, column=1, padx=10, pady=10)
label1 = tk.Label(root, text="将大的SDF文件切分为一个个单独的SDF小文件。", wraplength=300)
label1.grid(row=0, column=3, padx=10, pady=10)

# 工具1 UI
label2 = tk.Label(root, text="多肽全组合工具")
label2.grid(row=1, column=0, padx=10, pady=10)
button2 = tk.Button(root, text="打开工具", command=lambda x=root: tool1UI.tool1(x))
button2.grid(row=1, column=1, padx=10, pady=10)
label2 = tk.Label(root, text="将Excel表格中的多肽序列切分为氨基酸组合。", wraplength=300)
label2.grid(row=1, column=3, padx=10, pady=10)

# 工具2 UI
label2 = tk.Label(root, text="批量构建蛋白文件")
label2.grid(row=2, column=0, padx=10, pady=10)
button2 = tk.Button(root, text="打开工具", command=lambda x=root: tool2UI.tool2(x))
button2.grid(row=2, column=1, padx=10, pady=10)
label2 = tk.Label(root, text="使用'https://www.ddl.unimi.it'网站批量构建蛋白文件。", wraplength=300)
label2.grid(row=2, column=3, padx=10, pady=10)

# 工具3 UI
label2 = tk.Label(root, text="氨基酸检索工具")
label2.grid(row=3, column=0, padx=10, pady=10)
button2 = tk.Button(root, text="打开工具", command=lambda x=root: tool3UI.tool4(x))
button2.grid(row=3, column=1, padx=10, pady=10)
label2 = tk.Label(root, text="将目标文件中的每个数据在数据库中检索，筛选出在目标文件在数据库中重复占比超过50%的数据。", wraplength=300)
label2.grid(row=3, column=3, padx=10, pady=10)

# 工具4 UI
label2 = tk.Label(root, text="氨基酸检索工具—上色")
label2.grid(row=4, column=0, padx=10, pady=10)
button2 = tk.Button(root, text="打开工具", command=lambda x=root: tool4UI.tool4(x))
button2.grid(row=4, column=1, padx=10, pady=10)
label2 = tk.Label(root, text="将目标文件中的每个数据在数据库中检索，筛选出在目标文件在数据库中重复占比超过50%的数据,并按规则上色。", wraplength=300)
label2.grid(row=4, column=3, padx=10, pady=10)


root.mainloop()
