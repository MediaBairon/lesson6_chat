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
# функции вычисления
def summ (num1, num2):
    res1 = num1 + num2
    print(res1)
def difference (num1, num2):
    res2 = num1 - num2
    print(res2)
def multiply (num1, num2):
    res3 = num1 * num2
    print(res3)
def divide (num1, num2):
    res4 = num1/num2
    print(res4)
def wrong_expression():
    print("Вы ввели неправильное значение")
#Логика калькулятора
if symb == "+":
    summ (num1, num2)
elif symb == "-":
    difference (num1, num2)
elif symb == "*":
    multiply (num1, num2)
elif symb == "/":
    divide (num1, num2)
else:
     wrong_expression()
