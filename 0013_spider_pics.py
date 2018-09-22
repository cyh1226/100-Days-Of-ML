import requests
from pyquery import PyQuery as pq
import os
import re


url = 'http://tieba.baidu.com/p/2166231880'
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url , headers = headers).text
doc = pq(html)
items = doc('.pb_content.clearfix')
pic_urls = items.find('.d_post_content.j_d_post_content.clearfix img').items()#class中的空格需要用.替换 其余按照规则即可
p_l = list()
for pic_url in pic_urls:
	#print(pic_url)
	pic_url = pic_url.attr.src#提取某具体分支中的src属性
	pi_name = re.findall('\\S*\\.\\w*', pic_url.split('/')[-1], re.S)[0]#匹配提取网页链接中图片名称部分
	pic_path = 'picOfgirl/{0}'.format(pi_name)
	#print('/'.join(pic_path.split('/')[:-1]))
	if not os.path.exists('/'.join(pic_path.split('/')[:-1])):
		os.makedirs('/'.join(pic_path.split('/')[:-1]))#判断存储路径是否存在，通过切分原字符串再用/重新连接除最后一部分
	with open(pic_path, 'wb') as f:
		response = requests.get(pic_url)#访问图片链接，得到图片数据
		f.write(response.content)#将图片数据写入文件
		f.close()
	print("图片{0}下载完成~".format(pic_url.split('/')[-1]))#输出显示

