#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    alp = "ism"
    for i in range(1, len(sys.argv)):
        word = sys.argv[i]
        if alp in word:
            continue
        print(word + alp)