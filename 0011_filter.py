import os
import sys

def  in_filter_list():
	path = r'filtered_words.txt'
	word_file = open(path, encoding = 'utf-8')
	word_list = list()
	for l in word_file.readlines():
		print(l.strip())
		word_list.append(l.strip())
	return word_list


if __name__ == '__main__':
	w_l = in_filter_list()
	word = input("输入词语：")
	if word in w_l:
		print("Freedom")
	else:
		print("Human Rights")