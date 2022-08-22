from math import sqrt

while True:
    a = int(input('Introdu lungimea laturii a: '))
    b = int(input('Introdu lungimea laturii b: '))
    c = int(input('Introdu lungimea laturii c: '))

    if a > b and c and a == sqrt(b ** 2 + c ** 2):
        print('Triunghiul este dreptunghic')
    elif b > a and c and b == sqrt(a ** 2 + c ** 2):
        print('Triunghiul este dreptunghic')
    elif c > a and b and c == sqrt(a ** 2 + b ** 2):
        print('Triunghiul este dreptunghic')
    elif a != b and a != c and b != c:
        print('Triunghiul este oarecare')
    elif a == b and b == c:
        print('Triunghiul este echilateral')
    else:
        print('Triunghiul este isoscel')
    question = input('Vrei sa continui?: ')
    if question == 'd' or 'da':
        continue
    else:
        break
