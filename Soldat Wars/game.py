import random
from tqdm import tqdm
import time
from datetime import datetime

def data():
    global version, titres, random_word
    random_word = ['Чтобы написать предложение или жалобу просто напишите в конце игры слово "report"',"Одна секунда в реальной жизни как 1 суток в игре!","Заддержка ходов колеблиться от 3 до 8 секунд","Подсказки определяются рандомно нет что-то типо редкая подсказка или частый!","В данный момент версии 2.1 имеютсся 12 подсказок!","В массовой атаке вы можете потерять от 14% до 17% армии, но это не рандом а округление число является 6.5 по факту округление происходит рандомно","Отсупая вы потеряете 5% своей армии!","Массовая атака наносит на 50% больше ущерба противнику но потери с вашей стороны при этом будут высоки чем обычно","Скрываясь вы можете потерять 0.66% своей армии","Даже при защите можно нанести ущерб противнику но ущерб будет очень маленьким!","Атакуя вы делаете ущерб в 30-35% больше чем противик!","Ход выбирается по-очередно а было рандомно!"]
    version = "2.4"
    titres = (
        """Руководитель: Умарбек Кайимов \n Разработчик: Умарбек Кайимов \n Помощники: Нет""")

data()

class loading():
    global version,titres,random_word
    print(f"Версия: {version}")
    print(f"Титры:\n {titres}")
    time.sleep(1)
    print(f"\nПодсказка: {random.choice(random_word)}")
    for i in tqdm(range(3),desc="loading.."):
        time.sleep(1)

### ПРОЧИЕ ПЕРЕМЕННЫЕ
xod = random.randint(1,2)
intime = 0
### - ПРОЧИЕ ПЕРЕМЕННЫЕ - 

print("Имя первого игрока?")
name1 = str(input())
print("Имя второго игрока?")
name2 = str(input())
print(f"Сколько солдат будет у {name1}?")
soldat1 = int(input())
print(f"Сколько солдат будет у {name2}?")
soldat2 = int(input())

total_units = soldat1 + soldat2

total_streng_player1 = soldat1*10
total_streng_player2 = soldat2*10

start = datetime.now()
while True:
    intime +=1
    rtime = random.randint(3,8)
    intime +=rtime
    xod +=1
    elapsed1 = soldat1
    elapsed2 = soldat2
    if xod == 3:
        xod = 1
    if xod == 1:
        print(f"Ход {name1}")
        print("Выберите действия: Защита(2) - Атака(1) - Отсупать(3) - Скрываться(4) - Массовая атака(5)")
        operation = int(input())
        if operation == 2:
            total_streng_player1 -= total_streng_player2/30
            total_streng_player2 -= total_streng_player1/100
        if operation == 1:
            total_streng_player1 -= total_streng_player2/15
            total_streng_player2 -= total_streng_player1/100
        if operation == 3:
            total_streng_player1 -= total_streng_player2/20
        if operation == 4:
            total_streng_player1 -= total_streng_player2/150
        if operation == 5:
            total_streng_player2 -= total_streng_player1/5
            total_streng_player1 -= total_streng_player2/round(6.5)
    if xod == 2:
        print(f"Ход {name2}")
        print("Выберите действия: Защита(2) - Атака(1) - Отсупать(3) - Скрываться(4) - Массовая атака(5)")
        operation = int(input())
        if operation == 2:
            total_streng_player2 -= total_streng_player1/30
            total_streng_player1 -= total_streng_player2/100
        if operation == 1:
            total_streng_player2 -= total_streng_player1/15
            total_streng_player1 -= total_streng_player2/10
        if operation == 3:
            total_streng_player2 -= total_streng_player1/20
        if operation == 4:
            total_streng_player2 -= total_streng_player1/150
        if operation == 5:
            total_streng_player1 -= total_streng_player2/5
            total_streng_player2 -= total_streng_player1/round(6.5)
    soldat1 = round(total_streng_player1/10)
    soldat2 = round(total_streng_player2/10)
    if total_streng_player1 < 0:
        print(f"Игрок {name1}: Проиграл!")
        break
    if total_streng_player2 < 0:
        print(f"Игрок {name2}: Проиграл!")
        break
    print(f"Численность армии {name1}: {soldat1} (Потерь: {elapsed1-soldat1}): {(elapsed2-soldat2)-(elapsed1-soldat1)}")
    print(f"Численность армии {name2}: {soldat2} (Потерь: {elapsed2-soldat2}): {(elapsed2-soldat1)-(elapsed1-soldat2)}")
    if soldat1 > soldat2:
        print(f"Выйгрывает {name1} ")
    if soldat2 > soldat1:
        print(f"Выйгрывает {name2} ")
    print(f"Прошло {intime} суток")
    time.sleep(rtime)

stop = datetime.now() - start


print("Война закончена за " + str(stop) + " суток!")

end = str(input())

if end == "report":
    print("Пишите свое предложение или жалобу (Максимум 150 символов)")
    report = str(input())
    if len(report) > 150:
        print("Предложение слишком длинное!")
    report_file = open("report.txt",mode="a+",encoding="utf8",errors="ignore")
    time.sleep(1)
    report_file.write(f"\n\n\n{datetime.now}\n")
    report_file.write(report)
    print("Успешно записано! Спасибо!")
    time.sleep(3)
    report_file.close()
    SystemExit(1)
else:
    SystemExit(1)
