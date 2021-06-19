# Таска 2 - калькулятор
import time
num1 = int(input("Введите первое число:\n"))
print(f'Вы ввели {num1}')
num2 = int(input("Введите второе число:\n"))
print(f'Вы ввели {num2}')
symb = input("Введите знак операции:\n")
print(f'Вы ввели {symb}')
time.sleep(1)
print("Ваша операция: " + str(num1)+ " "+ symb+ " "+ str(num2))
time.sleep(1)
if symb == "+":
    res1 = num1 + num2
    print("Ваш результат: "+ str(res1))
elif symb == "-":
    res2 = num1 - num2
    print("Ваш результат: "+ str(res2))
elif symb == "*":
    res3 = num1 * num2
    print("Ваш результат: "+ str(res3))
elif symb == "/":
    res4 = num1/num2
    print("Ваш результат: "+ str(res4))
else:
    print("Вы ввели неправильное значение")
