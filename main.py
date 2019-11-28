#!/usr/bin/env python
# -*- coding: utf-8 -*-

meMap = [['r', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['r', 'x', 'n', 'x', 'x', 'x', 'x', 'x', 'n', 'x'],
        ['r', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'n', 'x', 'x', 'x', 'x', 'x', 'r', 'r'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'r', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'r', 'x', 'x', 'x', 'x'],
        ['x', 'n', 'x', 'x', 'x', 'r', 'x', 'x', 'n', 'x'],] 

class personne():
    #stat de base ne peut pas etre modifier
        #endu= int #scale avec les stats variable, (endu + stat v max) 
        #vitesse= int #nbr de depla par tour peux pas etre a 0 
    #stat variable, -1 par tour de jeu (toute), rechager au max suivant l'event, start pas forcement au max 
        #repo= int #def someil max=2
        #soif= int #def boire max=2
        #faim= int #def faim max=5
    #coord
        # ne peux pas aller dans les rivieres, ni sur les autre joueur
        # peux aller sur la nouriture pour manger
            #x= int
            #y= int

    def __init__(self, endu, vitesse, x, y):
        self.x = x
        self.y = y
        self.endu = endu
        self.vitesse = vitesse
        self.repo = 2
        self.faim = 5
        self.soif = 2

    def move(self, meMap, x, y):
        if (-1 < self.x + x < 10 and -1 < self.y + y < 10 and meMap[self.x + x][self.y + y] != 'r' and meMap[self.x + x][self.y + y] != 'p'):
            if (meMap[self.x + x][self.y + y] == 'n'):
                self.faim = 5 + self.endu
            meMap[self.x][self.y] = 'x'
            meMap[self.x + x][self.y + y] = 'p'
            self.x += x
            self.y += y
    
    def drink(self, meMap):
        check_x = (1,1,-1,-1)
        check_y = (1,-1,1,-1)
        for (x, y) in zip(check_x, check_y):
            if (meMap[self.x + x][self.y + y] and meMap[self.x + x][self.y + y] == 'r'):
                self.soif = 2 + self.endu

    

        

test = personne(5, 2, 2, 4)
test.move(meMap, 1, 0)
for i in range(10):
    test.move(meMap, 0, -1)
print(test.__dict__)
for i in range(len(meMap)):
    for j in range(len(meMap[i])):
        print(meMap[i][j], end = ' ')
    print('')