import sys

if len(sys.argv) != 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        result = "Table de " + str(i) + " :"
        while j <= 10:
            result += " " + str(i * j)
            j += 1
        print(result)
        i += 1