# sebastian
print('miles <-> kilometers')
factor = 1.60934

while True:
    print('(1) miles -> kilometers')
    print('(2) kilometers -> miles')
    print('(3) end')
    choise = int(input('your choise:'))

    if choise == 1:
        a = float(input('distance in miles:'))
        a = a * factor
        print(f'these are: {a} kilometers')
    elif choise == 2:
        a = float(input('distance in miles:'))
        a = a / factor
        print(f'these are: {a} miles')
    elif choise == 3:
        break
    else:
        print('incorrect input')
    input()

print('end')