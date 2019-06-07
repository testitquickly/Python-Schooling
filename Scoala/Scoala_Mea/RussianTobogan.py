# ! /usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 22 дек. 2018 г.
@author: astenix
'''
# проверим, можно ли Маше кататься на американских горках, если туда допускают только детей с ростом больше 1,4 метра и возрастом больше 8 лет

if __name__ == '__main__':
	print('На карусель проходят дети от восьми лет и от 140 см ростом.')
	minimum_age = int(8)
	minimum_height = float(1.4)
		# получаем значения от юзера
	print('А вашему сколько лет?')
	your_kid_age = int( input() )
	print('А рост (в метрах, папаша, ради привыкания к float)?')
	your_kid_height = float( input() )
		# вычисление "если хотя бы одно значение меньше нужного = True" то предлагаем уйти.
	decision = ((your_kid_age >= minimum_age) and (your_kid_height >= minimum_height))
		# Don't compare boolean values to True or False using == .
		# You generally don't explicitly compare objects to False/True in Python. Just do if somevalue: or if not somevalue:
		# Надо проверять "или оно есть, или нет", а не проверять слово True/False, как я привык в SeleniumIDE.
		# Вместо [if decision  == True] или [if decision  == False] надо писать [IF decision] или [IF NOT decision]:
	if decision:
		# Проверяем результат в переменной и переводим ее тип в строчный (текст)
		print( str(decision) + '. Всё ок, заходите.')
	else:
		print( str(decision) + '! Уходите, вам ещё нельзя на карусель.')