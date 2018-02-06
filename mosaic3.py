import cv2
import numpy as np 
from os import walk
from os.path import join

pic='f:\\test1\\a.jpg'
#input("请输入原始图文件名，按回车则访问默认图片：\n")					#原始图
pic_pool_folder='f:\\test2_cond'
#input("请输入图片池所在文件夹路径，按回车则访问默认路径：\n")				#待匹配图文件夹
#if pic_pool_folder[-1]!='\\':
#	pic_pool_folder.append('\\')
#elif pic_pool_folder=='':
#	pic_pool_folder='f:\\test2\\'


parts_x=10
parts_y=10




def get_pics(pic_pool_folder):
	files=[]
	for (dirpath,dirnames,filenames) in walk(pic_pool_folder):
		files.extend(filenames)
	return files

def pic_pool_process(pic_pool_folder):
	pic_pool_files=get_pics(pic_pool_folder)
	img_pool_names=[]
	img_pool=[]
	for pic_pool_file in pic_pool_files:
		image=cv2.imread(join(pic_pool_folder,pic_pool_file))			#分开写，处理匹配时用灰度图，转换时用原图
#		image_ZO=cv2.resize(image,(160,120))									#调整小图尺寸，路径不能有中文字符
		img_pool.append(image)		
	return img_pool	


def combine(img1,img2):
	dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
	return dst

image=cv2.imread(pic)
#image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)		#分开写，处理匹配时用灰度图，转换时用原图
img_ZO=cv2.resize(image,(3200,2400))

parts_size_x=img_ZO.shape[0]//parts_x
parts_size_y=img_ZO.shape[1]//parts_y

img_pool=pic_pool_process(pic_pool_folder)
i=0
kv={}
for x in range(0,img_ZO.shape[0],parts_size_x):
	for y in range(0,img_ZO.shape[1],parts_size_y):
		img_part=img_ZO[x:x+parts_size_x,y:y+parts_size_y]
		dst=combine(img_part,img_pool.pop())		
		img_ZO[x:x+parts_size_x,y:y+parts_size_y]=dst

		i=i+1
cv2.imwrite('f:\\test1\\finish.jpg',img_ZO)
print("完成"+str(i))	