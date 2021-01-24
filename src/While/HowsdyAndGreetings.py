# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
Created on 24 янв. 2021 г.
@author: astenix

Напишите программу, в которой выводятся разные сообщения в зависимости от
значения, которое хранится в переменной spam: 
* Hello — при значении 1, 
* Howdy — при значении 2,
* Greetings! — при любом другом значении.
'''
if __name__=='__main__':
	spam=input()
	if spam=="1":
		print('Hello')
	elif spam=="2":
		print('Howdy')
	else:
		print('Greetings!')

	print('The End')
