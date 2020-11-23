print('plus   [1]')
print('minus  [2]')
print('gånger [3]')
print('delat  [4]')
t = input('hur vill du räkna ')
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