# Таска 1 - чат
import time
print("Привет, введи своё имя")
username = input()
time.sleep(1)
print("Добро пожаловать, "+ username)
time.sleep(1)
print(username + ", читал ли ты Булгакова. 1 - это да; 2 - это нет")
bulgakov = input()
if bulgakov == str(1):
    time.sleep(1)
    print ("Ура, "+ username + ", ты умный человек!!!")
    time.sleep(1)
    print(username + " Любишь Мастера и Маргариту?")
    Master_and_Margaret = input().lower()
    Master_and_Margaret_list = ["да", "lf"]  
    if Master_and_Margaret in Master_and_Margaret_list:
        time.sleep(1)
        print("Красава!")
        time.sleep(1)
        print("Чат закрыт!")
    else:
        time.sleep(1)
        print("Значит ты всё таки дурачек!")
        time.sleep(1)
        print("Чат закрыт!")
elif bulgakov == str(2):
    time.sleep(1)
    print ("Ничего страшного, "+username+ ", будет время прочти и возращайся")
    time.sleep(1)
    print("Чат закрыт!")
else:
    time.sleep(1)
    print (username + ", это был тест на идиота и ты победил")
    time.sleep(1)
    print("Чат закрыт!")
