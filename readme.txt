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
	
	
*******	compute ate and rte of SLAM system!!!!*********
	
rgbd_benchmark_tools的使用方法：


1、“associate.txt”用来读取 “rgb.txt”和“depth.txt”的timestamp,寻找最佳的时间匹配。

	usage: associate.py [-h] [--first_only] [--offset OFFSET]
		            [--max_difference MAX_DIFFERENCE]
		            first_file second_file

	This script takes two data files with timestamps and associates them

	positional arguments:
	  first_file            first text file (format: timestamp data)
	  second_file           second text file (format: timestamp data)

	optional arguments:
	  -h, --help            show this help message and exit
	  --first_only          only output associated lines from first file
	  --offset OFFSET       time offset added to the timestamps of the second file
		                (default: 0.0)
	  --max_difference MAX_DIFFERENCE
		                maximally allowed time difference for matching entries
		                (default: 0.02)

2、Evaluation-----Absolute Trajectory Error (ATE) 绝对误差：更适合Visual SLAM

	使用方法：
	./evaluate_ate.py --plot PLOT --verbose ../../data/groundtruth/rgbd_dataset_freiburg1_360-groundtruth.txt ../../data/rgbdslam/freiburg1_360-rgbdslam.txt 
	
	解释：
	evaluate_ate.py [-h] [--offset OFFSET] [--scale SCALE]
                       [--max_difference MAX_DIFFERENCE] [--save SAVE]
                       [--save_associations SAVE_ASSOCIATIONS] [--plot PLOT]
                       [--verbose]
                       first_file second_file

	This script computes the absolute trajectory error from the ground truth
	trajectory and the estimated trajectory.

	positional arguments:
	  first_file            first text file (format: timestamp tx ty tz qx qy qz
	                        qw)
	  second_file           second text file (format: timestamp tx ty tz qx qy qz
	                        qw)

	optional arguments:
	  -h, --help            show this help message and exit
	  --offset OFFSET       time offset added to the timestamps of the second file
	                        (default: 0.0)
	  --scale SCALE         scaling factor for the second trajectory (default:
	                        1.0)
	  --max_difference MAX_DIFFERENCE
	                        maximally allowed time difference for matching entries
	                        (default: 0.02)
	  --save SAVE           save aligned second trajectory to disk (format: stamp2
	                        x2 y2 z2)
	  --save_associations SAVE_ASSOCIATIONS
	                        save associated first and aligned second trajectory to
	                        disk (format: stamp1 x1 y1 z1 stamp2 x2 y2 z2)
	  --plot PLOT           plot the first and the aligned second trajectory to an
	                        image (format: png)
	  --verbose             print all evaluation data (otherwise, only the RMSE
	                        absolute translational error in meters after alignment
	                        will be printed)


3、Evaluation-----Relative Pose Error (RPE)       相对误差：更适合Visual Odometry

	使用方法：
	./evaluate_rpe.py --fixed_delta --plot PLOT --verbose ../../data/groundtruth/rgbd_dataset_freiburg1_360-groundtruth.txt ../../data/rgbdslam/freiburg1_360-rgbdslam.txt 

	解释：
	usage: evaluate_rpe.py [-h] [--max_pairs MAX_PAIRS] [--fixed_delta]
		               [--delta DELTA] [--delta_unit DELTA_UNIT]
		               [--offset OFFSET] [--scale SCALE] [--save SAVE]
		               [--plot PLOT] [--verbose]
		               groundtruth_file estimated_file

	This script computes the relative pose error from the ground truth trajectory
	and the estimated trajectory.

	positional arguments:
	  groundtruth_file      ground-truth trajectory file (format: "timestamp tx ty
		                tz qx qy qz qw")
	  estimated_file        estimated trajectory file (format: "timestamp tx ty tz
		                qx qy qz qw")

	optional arguments:
	  -h, --help            show this help message and exit
	  --max_pairs MAX_PAIRS
		                maximum number of pose comparisons (default: 10000,
		                set to zero to disable downsampling)
	  --fixed_delta         only consider pose pairs that have a distance of delta
		                delta_unit (e.g., for evaluating the drift per
		                second/meter/radian)
	  --delta DELTA         delta for evaluation (default: 1.0)
	  --delta_unit DELTA_UNIT
		                unit of delta (options: 's' for seconds, 'm' for
		                meters, 'rad' for radians, 'f' for frames; default:
		                's')
	  --offset OFFSET       time offset between ground-truth and estimated
		                trajectory (default: 0.0)
	  --scale SCALE         scaling factor for the estimated trajectory (default:
		                1.0)
	  --save SAVE           text file to which the evaluation will be saved
		                (format: stamp_est0 stamp_est1 stamp_gt0 stamp_gt1
		                trans_error rot_error)
	  --plot PLOT           plot the result to a file (requires --fixed_delta,
		                output format: png)
	  --verbose             print all evaluation data (otherwise, only the mean
		                translational error measured in meters will be
		                printed)





