# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
Created on 4 янв. 2021 г.
@author: astenix
'''

if __name__ == '__main__':
    # Объявлена переменная без содержимого
    name = ''
    # Выводить приглашение о вводе данных в переменную name до тех пор, пока в неё не будет записано „your name”. С этого момента цикл завершается и "ОК",
    while name != 'your name':
        print('Please give me your name.')
        name = input()
    print('Ok')