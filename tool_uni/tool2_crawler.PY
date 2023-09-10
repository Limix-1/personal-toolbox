#导入requests库
import requests
from bs4 import BeautifulSoup
import openpyxl
import os
import json
import tkinter as tk
'''
使用本脚本前，需要将处理数据集单独保存为<dataset.xlsx>文件，并与本脚本放至同一目录下
<dataset.xlsx>文件只有能有一个sheet并且将数据去除表头放入第A列
'''


# 加载处理数据集
def loadset(url):
    data_set = []
    wb = openpyxl.load_workbook(url)
    # 加载第几个表
    ws = wb.worksheets[0]
    # 数据库在第几列
    col = ws['A']
    for each in col:
        data_set.append(each.value)

    # 输出为列表
    return data_set


# 用item，提出post ，返回下载地址
def postreq(base_url, tool_url, headers, data, item):
    data['molecule'] = item
    r1 = requests.post(tool_url, data=data, headers=headers)
    soup = BeautifulSoup(r1.text, 'lxml')
    a = soup.select('a')
    re = a[2].attrs['href']
    PDB_url = base_url + re
    return PDB_url


# 保存PDB文件
def savePDB(PDB_url, save_url, item, headers):
    if not os.path.exists(save_url):
        os.mkdir(save_url)
    r2 = requests.get(PDB_url, headers=headers)
    with open(save_url + '/' + item + '.pdb', 'wb') as f:
        pdb = r2.content
        f.write(pdb)


def crawler(dataset_url, save_url, headers, base_url, tool_url, setting_data, text, var):
    dataset_url = dataset_url.get()
    save_url = save_url.get()+'/PDB'
    headers = json.loads(headers.get())
    base_url = base_url.get()
    tool_url = tool_url.get()
    setting_data = json.loads(setting_data.get())

    # dataset = ['NNN', 'PTL', 'EEEDEDE']
    var.set('正在读取数据')
    dataset = loadset(dataset_url)
    count = 1
    total = len(dataset)
    var.set('正在生成PDB文件')
    for item in dataset:
        text.insert(tk.END, f'正在处理第{count}/{total}个，{item} \n')
        pdb_url = postreq(base_url, tool_url, headers, setting_data, item)
        savePDB(pdb_url, save_url, item, headers)
        count += 1
    var.set("操作已完成")

if __name__ == '__main__':
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    base_url = 'https://www.ddl.unimi.it'
    tool_url = 'https://www.ddl.unimi.it/vegaol/probuilder_run.php'
    save_url = './output'
    dataset_url = './dataset.xlsx'
    data = {'format': 'PDB2',
            'secstruct': 'AlphaHelix',
            'phi': '-135',
            'psi': '135',
            'omega': '180',
            'molfile': '(binary)',
            'molecule': ''}
    crawler(headers, save_url, dataset_url)

