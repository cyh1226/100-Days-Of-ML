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
	#w_l = ["北京","牛逼","牛比"]
	word = input("请输入：")
	for w in w_l:
		if w in word:
			word = word.replace(w,'*' * len(w))
	print(word)
	
