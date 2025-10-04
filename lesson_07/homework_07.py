# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 9:               #тут логічно поставити 9 для таблиці множення (або гнучко  while True:)
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:                 #має бути int
            # Enter the action to take if the result is greater than 25
            break                        #хай зупиняється break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(a, b):
    return a + b
print(sum_numbers(1, 2))

#sum_numbers(2,2)

#без return
def sum_numbers(a, b):
    print(a + b)
sum_numbers(1, 2)  # виведе 3

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_numbers(start,stop):
    list_numbers = list(range(start,stop))
    average = sum(list_numbers) / len(list_numbers)
    return average
print(avg_numbers(1, 100))

#avg_numbers(1,10)

#без return
def avg_numbers(start, stop):
    list_numbers = list(range(start, stop))
    average = sum(list_numbers) / len(list_numbers)
    print(average)
avg_numbers(1, 100)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_text(t):
    return t[::-1]
text = "Написати функцію, яка приймає рядок та повертає його у зворотному порядку"
reversed_text_1 = reverse_text(text)
print(reversed_text_1)

 #reverse_text('HELLO')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not words:
        return None
    return max(words, key=len)
words_list = ["Ben", "Alisa", "Igor", "Sergey"]
print(longest_word(words_list))

#longest_word(["Написати", "функцію", "яка", "приймає"])

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

  return str1.find(str2) #дописав тут

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 10_homework_01
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
def total_book_price():
    first = 8
    second = first + 2
    third = (first + second) / 2

    total = first + second + third
    return total

print(total_book_price())

# task 9_homework_01
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
def kids_today(boys=24, girls=None, sick_boys=1, absent_girls=2):
    if girls is None:
        girls = boys // 2
    present_boys = boys - sick_boys
    present_girls = girls - absent_girls
    total_present = present_boys + present_girls
    return total_present

print(kids_today())

# task 08_homework_01
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
def evening_temperature():
    morning = 5
    after_lunch = morning - 10
    evening = after_lunch + 4
    return evening
print(evening_temperature())

# task 10_homework_03
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
import math

def car_trip(distance_km=1600, fuel_per_100km=9, tank_capacity=48):
    total_fuel = (distance_km / 100) * fuel_per_100km
    refills = math.ceil(total_fuel / tank_capacity)
    return total_fuel, refills
fuel_needed, min_refills = car_trip()
print(f"Бензину потрібно: {fuel_needed} л")
print(f"Мінімальна кількість заправок: {min_refills}")