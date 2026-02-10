#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    keyword = sys.argv[1]
    check = input("What was parameters? ")
    if check == keyword:
        print("Good job!")
    else:
        print("Nope, sorry...")