
c = input()
b = 0

def interpret(*args):
    for a in list(*args):
        global b
        if 'I' in a:
            b += 1

        if 'V' in a:
            b += 5

        if 'X' in a:
            b += 10

        if 'L' in a:
            b += 50

        if 'C' in a:
            b += 100

        if 'D' in a:
            b += 500

        if 'M' in a:
            b += 1000
    return b

print(interpret(c))



# if a == "V":
#     b += 5
# if a == "X":
#     b += 10
# if a == "L":
#     b += 50
# if a == "C":
#     b += 100
# if a == "D":
#     b += 500
# if a == "M":
#     b += 1000


