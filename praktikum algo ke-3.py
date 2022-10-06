# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:40:53 2022

@author: putri
"""

import math
a = int(input("masukan nilai A = "))
b = int(input("masukan nilai B = "))
c = int(input("masukan nilai C = "))

if (a == 0):
    print("bukan merupakan persamaan kuadrat, karena nilai A =" + str(a))
else:
    D = pow(b, 2)-(4*a*c)   
    if (D > 0):
        x1 = ((-b)+math.sqrt(D))/(2*a)
        x2 = ((-b)-math.sqrt(D))/(2*a)
        print("persamaan kuadrat " + str(a) + " x² + "+ str(b) + "x + " + str(c))
        print("Determinannya = " + str(D))
        print("memiliki akar berbeda")
        print("Akar x1 = " + str(x1))
        print("Akar x2 = " + str(x2))
    elif (D == 0):
        x1 = (-b)/(2*a)
        x2 = x1
        print("persamaan kuadrat " + str(a) + "x² + (" + str(b) + ")x + " + str(c))
        print("Determinannya = " + str(D))
        print("merupakan Akar kembar")
        print("Akar = " + str(x2))
    elif (D < 0) :
        print("persamaan kuadrat " + str(a) + " x² + "+ str(b) + "x + " + str(c))
        print("Determinannya = " + str(D))
        print("merupakan Akar imaginer")
        print("Akar x1 = -" + str(b) + " + √" + str(D) + "/2*" + str(a))
        print("Akar x2 = -" + str(b) + " - √" + str(D) + "/2*" + str(a))
    else:
        print("Error, masukkan Angka yang valid")