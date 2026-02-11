#!/usr/bin/env python3

def array_of_names(person):
    array = []
    for i, j in person.items():
        fullName = i.capitalize() + " " + j.capitalize()
        array.append(fullName)
    return array

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))