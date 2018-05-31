#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pygame
from formlayout import fedit

pygame.display.init()
pygame.display.set_caption('cardreg')
screen = pygame.display.set_mode(pygame.display.list_modes()[0], pygame.FULLSCREEN)

form1 = [(u'Имя', u''),
            (u'Фамилия', u''),
            (u'Номер группы', u'')
            ]
res =  fedit(form1, title=u'регистрация карт', comment = u'Кто ты есть?')

with open("list.txt", "a") as f:
	f.write((res[0] + ' ' + res[1] + ' ' + res[2] + '\n').encode("utf-8"))
	f.close()
