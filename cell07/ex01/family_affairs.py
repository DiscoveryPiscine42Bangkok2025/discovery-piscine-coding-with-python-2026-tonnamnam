#!/usr/bin/env python3

def find_the_redheads(redHair):
    array = []
    key = "red"
    for i,j in redHair.items():
        if j == key:
            array.append(i)
    return array

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))