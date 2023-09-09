from tool import tool2_crawler
from toolUI.toolui import *



def tool2(root):
    root.iconify()
    new_window = tk.Toplevel(root)
    new_window.title("批量构建蛋白文件")
    new_window.geometry("800x600")

    button1 = tk.Button(new_window, text="返回主窗口",
                        command=lambda x=new_window: go_back(x, root))
    button1.grid(row=0, column=0)
    label1 = tk.Label(new_window, text="批量构建蛋白文件")
    label1.grid(row=0, column=1)

    # 选择目标文件
    label2 = tk.Label(new_window, text="请选择一个文件：")
    label2.grid(row=1, column=0, padx=10, pady=5)
    entry2 = tk.Entry(new_window, width=40)
    entry2.grid(row=1, column=1, padx=10, pady=5)
    button2 = tk.Button(new_window, text="选择文件",
                        command=lambda x=entry2: open_file_dialog(x, var))
    button2.grid(row=1, column=2)

    # 选择保存文件夹
    label3 = tk.Label(new_window, text="请选择输出位置：")
    label3.grid(row=2, column=0, padx=10, pady=5)
    entry3 = tk.Entry(new_window, width=40)
    entry3.grid(row=2, column=1, padx=10, pady=5)
    button3 = tk.Button(new_window, text="选择文件夹",
                        command=lambda x=entry3: open_directory_dialog(x, var))
    button3.grid(row=2, column=2)

    # headers, base_url, tool_url, set_data显示
    label5 = tk.Label(new_window, text="headers")
    label5.grid(row=4, column=0, padx=10, pady=5)
    v5 = tk.StringVar()
    v5.set('{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}')
    entry5 = tk.Entry(new_window, width=40, textvariable=v5, state="readonly")
    entry5.grid(row=4, column=1, padx=10, pady=5)

    label6 = tk.Label(new_window, text="base_url")
    label6.grid(row=5, column=0, padx=10, pady=5)
    v6 = tk.StringVar()
    v6.set('https://www.ddl.unimi.it')
    entry6 = tk.Entry(new_window, width=40, textvariable=v6, state="readonly")
    entry6.grid(row=5, column=1, padx=10, pady=5)

    label7 = tk.Label(new_window, text="tool_url")
    label7.grid(row=6, column=0, padx=10, pady=5)
    v7 = tk.StringVar()
    v7.set('https://www.ddl.unimi.it/vegaol/probuilder_run.php')
    entry7 = tk.Entry(new_window, width=40, textvariable=v7, state="readonly")
    entry7.grid(row=6, column=1, padx=10, pady=5)

    label8 = tk.Label(new_window, text="setting_data")
    label8.grid(row=7, column=0, padx=10, pady=5)
    v8 = tk.StringVar()
    v8.set('{"format": "PDB2","secstruct": "AlphaHelix","phi": "-135","psi": "135","omega": "180","molfile": "(binary)","molecule": " "}')
    entry8 = tk.Entry(new_window, width=40, textvariable=v8, state="readonly")
    entry8.grid(row=7, column=1, padx=10, pady=5)


    # 设置进度变量
    var = tk.StringVar()
    var.set('000')
    label4 = tk.Label(new_window, textvariable=var)
    label4.grid(row=8, column=1, padx=10, pady=10)

    # 状态说明栏
    text9 = tk.Text(new_window, width=40, height=20)
    text9.grid(row=9, column=1, padx=10, pady=10)


    # 开始按钮
    button4 = tk.Button(new_window, text="开始",
                        command=lambda dataset_url=entry2, save_url=entry3, headers=v5, base_url=v6, tool_url=v7, setting_data=v8, text=text9:
                        tool2_crawler.crawler(dataset_url, save_url, headers, base_url, tool_url, setting_data, text, var))
    button4.grid(row=8, column=0, padx=10, pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("测试")
    root.geometry("700x300")


    tool2(root)

    root.mainloop()