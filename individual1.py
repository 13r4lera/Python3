#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


wallpaper_cost = int(input("How much did one wallpaper cost? "))
paint_cost = int(input("How much did one paint cost? "))

if wallpaper_cost <= 0 or paint_cost <= 0:
    print("Cost must be positive", file=sys.stderr)
    exit(1)

total_cost = 8 * wallpaper_cost + 2 * paint_cost
print(f"Your total cost without discount is {total_cost:.2f}")

if 199 < total_cost < 501:
    discount_cost = total_cost * 0.97
    print(f"Your total cost is {discount_cost:.2f}")
elif 500 < total_cost < 801:
    discount_cost = total_cost * 0.95
    print(f"Your total cost is {discount_cost:.2f}")
elif 800 < total_cost < 1001:
    discount_cost = total_cost * 0.93
    print(f"Your total cost is {discount_cost:.2f}")
elif total_cost > 1000:
    discount_cost = total_cost * 0.91
    print(f"Your total cost is {discount_cost:.2f}")
else:
    print("You don't have discount!")
