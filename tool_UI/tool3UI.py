from tool_uni import tool3_filter
from tool_UI.toolui import *



def tool3(root):
    root.iconify()
    new_window = tk.Toplevel(root)
    new_window.title("批量构建蛋白文件")
    new_window.geometry("800x600")

    button1 = tk.Button(new_window, text="返回主窗口",
                        command=lambda x=new_window: go_back(x, root))
    button1.grid(row=0, column=0)
    label1 = tk.Label(new_window, text="批量构建蛋白文件")
    label1.grid(row=0, column=1)

    # 选择数据库
    label2 = tk.Label(new_window, text="请选择数据库：")
    label2.grid(row=1, column=0, padx=10, pady=5)
    entry2 = tk.Entry(new_window, width=40)
    entry2.grid(row=1, column=1, padx=10, pady=5)
    button2 = tk.Button(new_window, text="选择文件",
                        command=lambda x=entry2: open_file_dialog(x, var))
    button2.grid(row=1, column=2)

    # 选择目标文件
    label3 = tk.Label(new_window, text="请选择目标筛选文件：")
    label3.grid(row=2, column=0, padx=10, pady=5)
    entry3 = tk.Entry(new_window, width=40)
    entry3.grid(row=2, column=1, padx=10, pady=5)
    button3 = tk.Button(new_window, text="选择文件",
                        command=lambda x=entry3: open_file_dialog(x, var))
    button3.grid(row=2, column=2)

    # 选择保存文件夹
    label4 = tk.Label(new_window, text="请选择保存位置：")
    label4.grid(row=3, column=0, padx=10, pady=5)
    entry4 = tk.Entry(new_window, width=40)
    entry4.grid(row=3, column=1, padx=10, pady=5)
    button4 = tk.Button(new_window, text="选择文件夹",
                        command=lambda x=entry4: open_directory_dialog(x, var))
    button4.grid(row=3, column=2)

    # 设置保存文件名
    label5 = tk.Label(new_window, text="请输入保存文件名：")
    label5.grid(row=4, column=0, padx=10, pady=10)
    entry5 = tk.Entry(new_window, width=20)
    entry5.insert(0, "结果.xlsx")
    entry5.grid(row=4, column=1, padx=10, pady=10)

    # 设置进度变量
    var = tk.StringVar()
    var.set('000')

    label4 = tk.Label(new_window, textvariable=var)
    label4.grid(row=5, column=1, padx=10, pady=10)

    # 状态说明栏子窗口
    frame1 = tk.Frame(new_window)
    frame1.grid(row=6, column=1, padx=10, pady=10)
    # 滚动条
    scbar = tk.Scrollbar(frame1)
    scbar.pack(side=tk.RIGHT, fill=tk.Y)
    # 状态说明栏
    text9 = tk.Text(frame1, yscrollcommand=scbar.set, width=40, height=20)
    text9.pack()
    scbar.config(command=text9.yview)

    # 开始按钮
    button4 = tk.Button(new_window, text="开始",
                        command=lambda dataset_url=entry2, input_url=entry3, save_url=entry4, save_filename=entry5, text=text9:
                        tool3_filter.too4_main(dataset_url, input_url, save_url, save_filename, text, var))
    button4.grid(row=5, column=0, padx=10, pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("测试")
    root.geometry("700x300")


    tool3(root)

    root.mainloop()