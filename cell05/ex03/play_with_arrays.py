#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for i in original_array:
    if i > 5:
        value = i + 2
        if value not in new_array:
            new_array.append(value)

print(new_array)