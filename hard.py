#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

#Точность вычислений
EPS = 1e-10

if __name__ == "__main__":
    x = float(input("x = "))

    # Первый член ряда: а0 = х
    a = x
    S = a
    n = 0

    #Найти сумму членов ряда
    #Рекуррентная формула: a_n+1 = a_n * x^2 / (2n+2)(2n+3)
    while math.fabs(a) > EPS:
        a *= x * x / ((2 * n + 2) * (2 * n + 3))
        S += a
        n += 1

    print(f"Shi({x}) = {S}")