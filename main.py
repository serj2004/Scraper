# from selenium import webdriver
# driver = webdriver.Chrome("C:/Users/Сергей/IdeaProjects/testselenium/drivers/chromedriver.exe")
# driver.get("https://yandex.ru/")
# from typing import TextIO
# import csv
import flask

# app = flask.Flask(__name__)
# @app.route('/')
# def index():
#     return "Hello world!"
# app.run(port='8000')

import re
import this
# my_list = list()
# with open('C:\\Users\Сергей\Desktop\файлы 10мб\File_113.csv', "r",) as f:
#     r = csv.reader(f, delimiter=",")
#     for row in r:
#         print(",".join(row))
#w = csv.writer(f, delimiter=",")
#w.writerow(["один","два", "три"])
#w.writerow(["четыре", "пять", "шесть"])

# f.write("Пще однаА строка.")
# my_list.append(f.read())
# print(my_list)




class Person():
    def __init__(self,w,h,a,n):
        self.weight = w
        self.height = h
        self.age = a
        self.name = n
    def parameters(self):
        print((self.age, self.height, self.weight, self.name)*3)


person1 = Person(100, 180, 40, "Serg")
person1.parameters()


class Man(Person):
    pass


ivan = Man(80, 175, 35, "Ivan")
ivan.parameters()



