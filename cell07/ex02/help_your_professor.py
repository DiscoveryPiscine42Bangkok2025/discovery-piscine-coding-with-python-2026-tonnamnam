#!/usr/bin/env python3

def average(classCheck):
    student = 0
    point = 0
    for score in classCheck.items():
        point = point + score[1]
        student = student + 1
    result = point / student
    return result

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")