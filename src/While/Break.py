# ! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
Created on 15 янв. 2021 г.
@author: astenix
'''

if __name__=='__main__':
    while True:
        print('Type your name.')
        name=input()
        # Приводим условие
        if name=='your name':
            # Просто прервать выполнение wile и перейти к следующей строке
            break
    print('Ok')
