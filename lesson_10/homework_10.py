'''Завдання 1
Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), '
'Developer(ім')я, зарплата, мова програмування),
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"{super().__str__()}, Programming Language: {self.programming_language}"


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

    def __str__(self):
        return (f"Name: {self.name}, Salary: {self.salary}, "
                f"Department: {self.department}, Programming Language: {self.programming_language}, "
                f"Team Size: {self.team_size}")


m = Manager("Євген", 1000, "Маркетинг")
d = Developer("Ігор", 2000, "Python")
t = TeamLead("Найда", 3000, "Production", "SQL", 11)

print(m)
print(d)
print(t)

'''Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. 
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. 
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.'''

from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
#1.коло Площа = π · r² Периметр (довжина кола)= 2 · π · r
class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return f"Коло (радіус = {self.__radius})"
#2.прямокутник Площа= a · b Периметр = 2 · (a + b)
class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"Прямокутник (ширина = {self.__width}, висота = {self.__height})"
#3.трикутник Напівпериметр= (a + b + c) / 2 Площа= √[p · (p – a) · (p – b) · (p – c)]
#Периметр= a + b + c
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def __str__(self):
        return f"Трикутник (сторони = {self.__a}, {self.__b}, {self.__c})"

figures = [
    Circle(7),
    Rectangle(6, 8),
    Triangle(9, 5, 11)
]
for f in figures:
    print(f"{f}:")
    print(f"  Площа = {f.area():.2f}")
    print(f"  Периметр = {f.perimeter():.2f}\n")