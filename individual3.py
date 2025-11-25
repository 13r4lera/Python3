#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    cost = int(input("Enter the cost: "))

    if cost < 0:
        print("The cost cannot be negative.", file=sys.stderr)
        exit(1)

    total_bills = 0
    if cost >= 500:
        total_bills += cost // 500
        print(f"You need {cost // 500} bills per 500 rubles")
        cost = cost % 500
    if cost >= 100:
        total_bills += cost // 100
        print(f"You need {cost // 100} bills per 100 rubles")
        cost = cost % 100
    if cost >= 10:
        total_bills += cost // 10
        print(f"You need {cost // 10} bills per 10 rubles")
        cost = cost % 10
    if cost >= 5:
        total_bills += cost // 5
        print(f"You need {cost // 5} bills per 5 rubles")
        cost = cost % 5
    if cost >= 2:
        total_bills += cost // 2
        print(f"You need {cost // 2} bills per 2 rubles")
        cost = cost % 2
    if cost >= 1:
        total_bills += cost // 1
        print(f"You need {cost // 1} lists per 1 ruble")

    print(f"Totally you will need {total_bills} bills.")