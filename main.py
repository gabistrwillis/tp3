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

        print(self.n)
        k=int(input('rentrez k :'))
        while k != int(self.m):
            self.n = self.n - 1
            print ('essayez encore ! Essais restants:',self.n)
            if self.n ==0:
                print("Tu as perdu!!")
                break
            k=int(input('rentrez k: '))

        if k==self.m:
            print ("Trouvé")

print('hell')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
p = Jeu(2,5)
p.test()