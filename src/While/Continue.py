# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
Created on 15 янв. 2021 г.
@author: astenix

При достижении инструкции continue управление немедленно
передается в начало цикла, где условие вычисляется заново.
'''

if __name__=='__main__':
	while True:
		print('Who are you?')
		name=input()
# Приводим условие
		if name!='Joe':
			continue
		print('Hello, Joe, provide the password like SWORDFISH without capitals')
# Просто прервать выполнение wile и перейти к следующей строке
		password=input()
		if password=='swordfish':
			break
	print('Ok')
