from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rnchar():
	return chr(random.randint(65,90))#随机生成字符ASCII代码

def rncolor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))#随机生成颜色代码


for i in range(200):
	image = Image.new('RGB',(60*4,60),(255,255,255))#新建一张60*240大小的空白图片，设置此图片存储颜色模式为RRGB

	font = ImageFont.truetype('0001_Arial.ttf',36)#载入字体

	draw = ImageDraw.Draw(image)#新建draw对象，准备已有图像进行作图处理

	for w in range(60*4):#填充随机色块
		for h in range(60):
			draw.point((w,h),fill = rncolor())

	for w in range(4):#写入随机字符
		draw.text((60*w+10,10),rnchar(),font = font , fill = rncolor())

	image.save(r'C:\Users\82449\Desktop\codes\code'+ str(i) +'.jpg', 'jpeg')