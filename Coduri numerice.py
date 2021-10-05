numar = input("Dati un numar: ")
print("Codurile numerice: Direct, Gray, Aiken, Exces 3")
cod = input("Dati un cod numeric: ")

if cod=='Direct':
    if numar == '0':
        print('0000')
    elif numar == '1':
        print('0001')
    elif numar == '2':
        print('0010')
    elif numar == '3':
        print('0011')
    elif numar == '4':
        print('0100')
    elif numar == '5':
        print('0101')
    elif numar == '6':
        print('0110')
    elif numar == '7':
        print('0111')
    elif numar == '8':
        print('1000')
    elif numar == '9':
        print('1001')

if cod=='Gray':
    if numar == '0':
        print('0000')
    elif numar == '1':
        print('0001')
    elif numar == '2':
        print('0011')
    elif numar == '3':
        print('0010')
    elif numar == '4':
        print('0110')
    elif numar == '5':
        print('0111')
    elif numar == '6':
        print('0101')
    elif numar == '7':
        print('0100')
    elif numar == '8':
        print('1100')
    elif numar == '9':
        print('1101')

if cod=='Aiken':
    if numar == '0':
        print('0000')
    elif numar == '1':
        print('0001')
    elif numar == '2':
        print('0010')
    elif numar == '3':
        print('0011')
    elif numar == '4':
        print('0100')
    elif numar == '5':
        print('1011')
    elif numar == '6':
        print('1100')
    elif numar == '7':
        print('1101')
    elif numar == '8':
        print('1110')
    elif numar == '9':
        print('1111')

if cod=='Exces 3':
    if numar == '0':
        print('0011')
    elif numar == '1':
        print('0100')
    elif numar == '2':
        print('0101')
    elif numar == '3':
        print('0110')
    elif numar == '4':
        print('0111')
    elif numar == '5':
        print('1000')
    elif numar == '6':
        print('1001')
    elif numar == '7':
        print('1010')
    elif numar == '8':
        print('1011')
    elif numar == '9':
        print('1100')