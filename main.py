# This is a sample Python script.

import random
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint

class Jeu:
    def __init__(self, m, n):
        self.m=random.randint(1,m)
        self.n=n
    def test(self):
        k=(input('rentrez k :'))
        if type(k) != int:
            k=int(input('Veuillez rentrer un entier svp:'))


        while k is not int(self.m):
            print ('essayez encore')
            k=int(input('rentrez k: '))

        print ("Trouvé")


print('hell')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
p = Jeu(3,2)
p.test()