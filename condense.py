import cv2
import numpy as np 
from os import walk
from os.path import join
import sys





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
		image_ZO=cv2.resize(image,(320,240))									#调整小图尺寸，路径不能有中文字符

		cv2.imwrite(join(pic_pool_folder+'_cond',pic_pool_file),image_ZO)		
	return '压缩完成'	

pic_pool_folder='f:\\test2'
pic_pool_process(pic_pool_folder)