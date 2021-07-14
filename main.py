# Таска 1 - чат
import time
author_name = "Булгакова"# писать в родительном падеже
proizvidenie_name = "Мастера и Маргариту" # писать в родительном падеже
# Функции
def greetings():
    print("Привет, введи своё имя")
def litterature_quiz_start():
    print (username + ", читал ли ты "+ author_name +"? 1 - это да; 2 - это нет")
def first_answer_handler():
    time.sleep(1)
    print ("Ура, "+ username + ", ты умный человек!!!")
def first_first_answer_handler(proizvidenie_name_answer):
    proizvidenie_name_answer_list = ["да", "lf","yes","da"] 
    if proizvidenie_name_answer in proizvidenie_name_answer_list:
        time.sleep(1)
        print("Красава!")
        time.sleep(1)
        print("Чат закрыт!")
    else:
        time.sleep(1)
        print("Значит ты всё таки дурачек!")
        time.sleep(1)
        print("Чат закрыт!")
def second_answer_handler():
    time.sleep(1)
    print ("Ничего страшного, "+username+ ", будет время прочти и возращайся")
    time.sleep(1)
    print("Чат закрыт!")
def third_answer_handler():
    time.sleep(1)
    print (username + ", это был тест на идиота и ты победил")
    time.sleep(1)
    print("Чат закрыт!")

#Сценарий выполнения
greetings()
username = input()
time.sleep(1)
print("Добро пожаловать, "+ username)
time.sleep(1)
litterature_quiz_start() 
first_answer = input()
if first_answer == str(1):
    first_answer_handler()
    time.sleep(1)
    print(username + " Любишь " + proizvidenie_name + "?")
    proizvidenie_name_answer = input().lower()
    first_first_answer_handler(proizvidenie_name_answer)
elif first_answer == str(2):
    second_answer_handler()
else:
    third_answer_handler()
