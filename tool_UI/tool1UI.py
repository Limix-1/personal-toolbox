from tool_uni import tool1_fullcompare
from tool_UI import tool_ui
import tkinter as tk


def tool1(root):
    root.iconify()
    new_window = tk.Toplevel(root)
    new_window.title("多肽全组合工具")
    new_window.geometry("800x600")

    button1 = tk.Button(new_window, text="返回主窗口",
                        command=lambda x=new_window: tool_ui.go_back(x, root))
    button1.grid(row=0, column=0)
    label1 = tk.Label(new_window, text="多肽全组合工具")
    label1.grid(row=0, column=1)

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

    # 设置保存文件名
    label3 = tk.Label(new_window, text="请输入文件名：")
    label3.grid(row=3, column=0, padx=10, pady=10)
    entry_file_name4 = tk.Entry(new_window, width=20)
    entry_file_name4.insert(0, "结果.xlsx")
    entry_file_name4.grid(row=3, column=1, padx=10, pady=10)

    # 设置进度变量
    var = tk.StringVar()
    var.set('000')

    label4 = tk.Label(new_window, textvariable=var)
    label4.grid(row=3, column=2, padx=10, pady=10)

    # 选择筛序长度
    testCMD = new_window.register(tool_ui.is_digit)

    label4 = tk.Label(new_window, text="选择最小长度")
    label4.grid(row=4, column=0, padx=10, pady=10)
    v1 = tk.StringVar()
    e1 = tk.Entry(new_window, width=10, textvariable=v1, validate="key", validatecommand=(testCMD, '%P'))
    e1.grid(row=5, column=0, padx=10, pady=10)

    label4 = tk.Label(new_window, text="选择最大长度")
    label4.grid(row=4, column=1, padx=10, pady=10)
    v2 = tk.StringVar()
    e2 = tk.Entry(new_window, width=10, textvariable=v2, validate="key", validatecommand=(testCMD, '%P'))
    e2.grid(row=5, column=1, padx=10, pady=10)

    # 开始按钮
    button4 = tk.Button(new_window, text="开始",
                        command=lambda x=entry_file_name2, y=entry_file_name3, v=var, mi=v1, ma=v2, filename=entry_file_name4:
                        tool1_fullcompare.full_com(x, y, v, mi, ma, filename))
    button4.grid(row=6, padx=10, pady=10)

