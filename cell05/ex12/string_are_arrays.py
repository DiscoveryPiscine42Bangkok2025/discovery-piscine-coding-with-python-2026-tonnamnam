#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    keyword = sys.argv[1]
    alp = "z"
    count = keyword.count(alp)
    if count == 0:
        print("none")
    else:
        print(alp * count)