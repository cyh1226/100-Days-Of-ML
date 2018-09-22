import json
import xlwt
import os
from collections import OrderedDict#使用该模块使得转换的json字符串仍保有原来的顺序

def read_file(path):
	file = open(path, encoding = 'utf-8')
	cont = ''
	for line in file.readlines():
		cont += line.strip()#将文件中文本读取为一整个字符串
	#print(cont)
	j = json.loads(cont, object_pairs_hook = OrderedDict)#将原文本转换为json数据并保持原有次序！！！json数据是字典格式
	for key,value in j.items():
		print(str(key))
		for v in value:
			print(v)
	return j

def new_excel(data):
	w = xlwt.Workbook()#新建表单对象
	ws = w.add_sheet('student')#添加名为student的表
	i = 0
	for key,value in data.items():
		j = 0
		ws.write(i,j,key)
		for v in value:
			j += 1
			ws.write(i,j,v)
		i += 1
	w.save('0014_student.xls')#写入数据并保存存储
	print("new excel has just been finished~")


if __name__ == '__main__':
	path = r'0014_student.txt'
	j = read_file(path)
	new_excel(j)