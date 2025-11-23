#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    circle1_x = float(input("Enter the first circle x coordinate: "))
    circle1_y = float(input("Enter the first circle y coordinate: "))
    radius1 = float(input("Enter the radius of the first circle: "))

    circle2_x = float(input("Enter the second circle x coordinate: "))
    circle2_y = float(input("Enter the second circle y coordinate: "))
    radius2 = float(input("Enter the radius of the second circle: "))

    if radius1 < 0 or radius2 < 0:
        print("Invalid input", file=sys.stderr)
        sys.exit(1)

    distance = math.sqrt((circle1_x - circle2_x) ** 2 +
                         (circle1_y - circle2_y) ** 2)

    if distance == 0 and radius1 == radius2:
        print("The circles coincide")
    elif distance > (radius1 + radius2) or distance < abs(radius1 - radius2):
        print("Two circles have 0 common points")
    elif distance == (radius1 + radius2) or distance == abs(radius1 - radius2):
        print("Two circles have 1 common point")
    else:
        print("Two circles have 2 common points")