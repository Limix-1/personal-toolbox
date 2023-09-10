import os


def splitSDF(file_name, save_directory, var):
    file_name = file_name.get()
    save_directory = save_directory.get()
    var.set('工具正在运行中')
    # 读取的文件内容保存在列表里
    file_str_list = []
    # 设置文件索引
    index = 0
    # import pdb
    # pdb.set_trace()
    path = f'{save_directory}/saveSDF'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(file_name, 'r+') as f:
        for ln in f:
            if ln != "$$$$\n":
                file_str_list.append(ln)
            else:
                # 将对应的内容按照索引写入文件
                index = index + 1
                with open(f'{path}/{index}.sdf', 'w+') as wt:
                    for ds in file_str_list:
                        wt.write(ds)
                file_str_list = []
    var.set('已完成')

if __name__ == '__main__':
    splitSDF()
