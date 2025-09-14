# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"Apples: {apples}, Bananas: {banana}")

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"perimetery:{perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples=4
pears=apples+5
plum=apples-2
print("Яблук було",apples,"Груш було",pears,"Слив було",plum)
print("Всього дерев", apples+pears+plum)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
Before_lunch=5
After_lunch=Before_lunch-10
In_the_evening=After_lunch+4
print("До обіда",Before_lunch,"Після обіду",After_lunch,"Надвечір",In_the_evening)
print("Надвечір", In_the_evening)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_all=24
girls_all=int(boys_all/2)
sick=1
absent=2
print("Всього хлопчиків",boys_all ,"Всього дівчаток",girls_all,"Всього захворіло",sick,"Всього не прийшло",absent)
print("Всього дітей", boys_all+girls_all-sick-absent)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book=8
second_book=first_book+2
third=int((first_book+second_book)/2)
print("Перша книжка",first_book ,"Друга книга",second_book,"Третя книга",third)
print("Всього за всі книги", first_book+second_book+third)
