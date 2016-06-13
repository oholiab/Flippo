# -*- coding: utf-8 -*-

# RUNS ONLY IN PYTHON 3.
# python3 flippo.py

import time
import sys

animation = ["          ┳━┳     ", 
			 " ヽ       ┳━┳     ", 
			 " )ヽ      ┳━┳     ",
			 " °)ヽ     ┳━┳     ",
			 " -°)ヽ    ┳━┳     ",
			 " °-°)ヽ   ┳━┳     ",
			 " ヽ°-°)ヽ ┳━┳     ", 
			 " (ヽ°-°)ヽ┳━┳     ",
			 " (ヽ°-°)ヽ┳━┳     ",
			 " (ヽ°-°)ヽ┳━┳     ", 
			 " (╯ °□°）╯︵ ┻━┻  ", 
			 "██████████████████",
			 " (ヽ°-°)ヽ   ┻━┻   ",
			 " (ヽ°-°)ヽ   ┻━┻  ",  
			 " ﾉ(°-°ﾉ)     ┻━┻  ", 
			 " (°-°ﾉ)      ┻━┻  ", 
			 " °-°ﾉ)       ┻━┻  ", 
			 " -°ﾉ)        ┻━┻  ", 
			 " °ﾉ)         ┻━┻  ", 
			 " ﾉ)          ┻━┻  ",
			 " )           ┻━┻  ",  
			 "             ┻━┻  "]

for i in range(len(animation)):
	if i != 10 and i != 11:
		sys.stdout.write(animation[i] + "\r",)
		time.sleep(0.2)
	else:
		for i in range(1, 8):
			sys.stdout.write(animation[10] + "\r",)
			time.sleep(0.1)
			sys.stdout.write(animation[11] + "\r",)
			time.sleep(0.1)
			
	sys.stdout.flush()