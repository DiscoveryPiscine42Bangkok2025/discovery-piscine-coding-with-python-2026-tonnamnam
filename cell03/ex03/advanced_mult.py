import sys

if len(sys.argv) != 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        result = "Table de " + str(i) + " :"
        while j <= 10:
            result = result + " " + str(i * j)
            j = j + 1
        print(result)
        i = i + 1