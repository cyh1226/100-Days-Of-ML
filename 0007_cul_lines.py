import os
import time

def filelist(orginpath):
	for parent,dirnames,filenames in os.walk(orginpath):
		fl = list()
		for filename in filenames:
			if filename.split('.')[-1] == 'py':
				fl.append(os.path.join(parent,filename))
	return fl

def count(files):
	blank_num = 0
	anno_num = 0
	code_num = 0
	t_blank_num = 0
	t_anno_num = 0
	t_code_num = 0
	for f in files:
		for line in open(f, encoding = 'utf-8').readlines():
			line = line.strip()
			if line == '':
				blank_num += 1
			elif line.startswith('#'):
				anno_num += 1
			else:
				code_num += 1
		print(f + '\t' + str(blank_num) + '\t' + str(anno_num) + '\t' + str(code_num))
		t_blank_num += blank_num
		t_anno_num += anno_num
		t_code_num += code_num
	print('Total num are listed' + '\t' + str(t_blank_num) + '\t' + str(t_anno_num) + '\t' + str(t_code_num))


if __name__ == '__main__':
	filepath = r'E:\python-程序'
	count(filelist(filepath))