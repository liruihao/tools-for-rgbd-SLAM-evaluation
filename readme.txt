RGBD evaluation tools forked from TUM


作者：李睿豪


目的：对齐rgb和depth图像的时间序列，重新按照1,2,3……的顺序进行编号，以便进行slam。


使用方法：

1、chmod +x prepare.sh  给.sh文件以执行属性（或者右键文件，在allow excuting file as programme上打勾） 

2、./prepare.sh

解释：
	prepare.sh为linux脚本程序，这里是把多个python程序放在一起运行。
	
	1、python generateTxt.py  以时间序列排列产生rgb.txt和depth.txt(名称也为时间序列)
		注：freiburg文件中大部分含有这两个txt文件,但不全，仅是keyframe的
		
	2、python associate.py rgb.txt depth.txt --max_difference 0.02 > associate.txt
		关联深度图像和rgb图像
		
	3、python associate_rgb_time.py rgb.txt depth.txt --max_difference 0.02 > associate.txt
		关联深度图像和rgb图像,保存rgb和depth的timestamp，便于读取图像以及和groundtruth比较
	
	#4、python change2index.py（按照1,2,3……编号，但是和groundtruth的时间序列对不上），应该自己从associate.txt里面读取图像，进行VO。
	

