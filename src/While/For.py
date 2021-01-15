# ! /usr/bin/env python
#  -*- coding: utf-8 -*-
import sys

'''
Created on 15 янв. 2021 г.
@author: astenix

For и While могут выполнять одну и ту же задачу, но For короче в записи и, вероятно, понятнее.
	Результат выполнения:
			I shoot the sherif
			 (0) times
			 (1) times
			 (2) times
			 (3) times
			 (4) times
'''

if __name__=='__main__':
	print('I shoot the sherif with WHILE')
	# Инструкция for увеличивает значение переменной i через цикл
	i=0
	while i<5:
		print(' ('+str(i)+') times')
		i=i+1

	print('I shoot the sherif again with FOR')
			# Инструкция for увеличивает значение переменной i на range
	for i in range (5):
		print(' ('+str(i)+') times')
	sys.exit()

(5>4) and (5<6)
