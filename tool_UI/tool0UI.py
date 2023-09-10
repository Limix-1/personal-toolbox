from tool_uni import tool0_splitSDF
from tool_UI import tool_ui
import tkinter as tk


def tool0(root):
    root.iconify()
    new_window = tk.Toplevel(root)
    new_window.title("SDF切分工具")
    new_window.geometry("800x600")

    button1 = tk.Button(new_window, text="返回主窗口",
                        command=lambda x=new_window: tool_ui.go_back(x, root))
    button1.grid(row=0, column=0)

    label1 = tk.Label(new_window, text="SDF切分工具")
    label1.grid(row=0, column=1)
    # 设置进度变量
    var = tk.StringVar()
    var.set('000')

    # 选择目标文件
    label2 = tk.Label(new_window, text="请选择一个文件：")
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry_file_name2 = tk.Entry(new_window, width=40)
    entry_file_name2.grid(row=1, column=1, padx=10, pady=10)

    button2 = tk.Button(new_window, text="选择文件",
                        command=lambda x=entry_file_name2: tool_ui.open_file_dialog(x, var))
    button2.grid(row=1, column=2)

    # 选择保存文件夹
    label3 = tk.Label(new_window, text="请选择输出位置：")
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry_file_name3 = tk.Entry(new_window, width=40)
    entry_file_name3.grid(row=2, column=1, padx=10, pady=10)

    button3 = tk.Button(new_window, text="选择文件夹",
                        command=lambda x=entry_file_name3: tool_ui.open_directory_dialog(x, var))
    button3.grid(row=2, column=2)

    button4 = tk.Button(new_window, text="开始",
                        command=lambda x=entry_file_name2, y=entry_file_name3, v=var:
                        tool0_splitSDF.splitSDF(x, y, v))
    button4.grid(row=3, columnspan=2)

    label4 = tk.Label(new_window, textvariable=var)
    label4.grid(row=3, column=2, padx=10, pady=10)
