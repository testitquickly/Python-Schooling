# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
Created on 15 янв. 2021 г.
@author: astenix
'''

if __name__=='__main__':
    name=''
    # Продолжаем спрашивать до тех  пор, пока юзер не скажет своё имя.
    while not name:
        print('What is your name?')
        name=input()
    print ('How many guests we will have?')
    # Ждём цифру.
    numOfGuests=int(input())
    if numOfGuests:
        print ('Be sure to have enough chairs.')
    print('Done')
