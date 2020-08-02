import flask
import re
import this



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



