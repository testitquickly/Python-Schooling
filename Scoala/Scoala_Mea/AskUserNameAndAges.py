# ! /usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Created on 10 дек. 2018 г.
@author: astenix
page 51
'''
# It's as if the interpreter inserts this at the top
# of your module when run as the main program. 
if __name__ == '__main__':

# Интерактивно приветствует юзера и получаем ввод от юзера в переменную userName
	print('Здравствуйте. Как вас зовут?')
	userName = input()

# на ходу высчитываем количество символов в переменной с именем юзера и выводим его
	print('Ваше имя в длину не превышает '  + str(len(userName)) + ' букв. А сколько вам лет?')

# получаем от юзера цифру и кладем ее в пременную userAges
	userAges = input()

# вычисляем, сколько лет будет юзеру через год
	userAgesInOneYear = str(int(userAges) + 1)
	print('Это сегодня вам ' + userAges + ', ' + userName + '. А через год будет ' + userAgesInOneYear +'. А потом что, начнем джаз слушать?')
	print('До свидания')
	userInput = input()
	if userInput == 'До свидания':
		print('О, вежливый, сука!')
		print('До свидания, до свидания...')
	else:
		print('Впадлу попрощаться?')
		print('Ты мутный тип.') 
	print('Конец программы')