# de fyra tal sätten
print('plus   [1]')
print('minus  [2]')
print('gånger [3]')
print('delat  [4]')
t = input('hur vill du räkna ')
# int för att inte talen blir ihopp satttyp 4+2= 42 men med inte så blir det 4+2= 6
# och jag har float så att man kan räkna med decimaltal
t = int(t)
if t == 1:
    num1 = input('enter a number: ')
    num2 = input('enter a number: ')
    result = float(num1) + float(num2)
    print(result)
if t == 2:
    num1 = input('enter a number: ')
    num2 = input('enter a number: ')
    result = float(num1) - float(num2)
    print(result)
if t == 3:
    num1 = input('enter a number: ')
    num2 = input('enter a number: ')
    result = float(num1) * float(num2)
    print(result)
if t == 4:
    num1 = input('enter a number: ')
    num2 = input('enter a number: ')
    result = float(num1) / float(num2)
    print(result)
else:
    print('hejdå')
