# This is a sample Python script.

import random
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint

class Jeu:
    def __init__(self, m):
        self.m=random.randint(0,m)

    def test(self):
        k=int(input('rentrez k :'))
        while k is not int(self.m):
            print ('essayez encore')
            k=int(input('rentrez k: '))

        print ("Trouvé")

print('hello')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
p = Jeu(3)
p.test()