# -*- coding: utf-8 -*-
age = int(input("Введите ваш возраст "))
name = input("Как вас зовут ")
if 0 < age < 75:
    if age >= 16 and name != "Иван":
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Извините, вы не поступили")
        if age < 16:
            goda = 16 - age
            if goda < 5:
                print("Вначале окончите школу, вам осталось ", goda, "год(а)", sep=" ")
            else:
                print("Вначале окончите школу, вам осталось ", goda, "лет", sep=' ')
else:
    print("Ошибка")