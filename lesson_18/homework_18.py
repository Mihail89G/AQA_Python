'''Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.'''
def simple_generator(numbers):
    for num in range(0, numbers + 1):       #включає всі числа від 0 до N
        if num % 2 == 0:                    #залишає тільки парні числа
            yield num                       #повертає їх по одному як генератор

result = simple_generator(17)
print(list(result))

'''Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.'''
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(50):
    print(next(fib))

'''Ітератори:
Реалізуйте ітератор для зворотного виведення елементів списку.'''
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  # починаємо з останнього елемента

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration  # кінець ітерації
        value = self.data[self.index]
        self.index -= 1
        return value

my_list = [1, 2, 3, 4, 5]
rev_iter = ReverseIterator(my_list)

for item in rev_iter:
    print(item)

'''Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.'''
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0  # починаємо з 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2  # наступне парне число
        return result

even_iter = EvenIterator(10)
for num in even_iter:
    print(num)

'''Декоратори:
Напишіть декоратор, який логує аргументи та результати викликаної функції.'''
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Логування аргументів
        print(f"Виклик функції '{func.__name__}' з args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        # Логування результату
        print(f"Результат функції '{func.__name__}': {result}")
        return result
    return wrapper

# Приклад використання декоратора
@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting="Hello World"):
    return f"{greeting}, {name}!"

# Виклики функцій
add(3, 5)
greet("Misha")
greet("Anna", greeting="Hello")


'''Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.'''
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виняток у функції '{func.__name__}': {e}")
            # Можна повернути значення за замовчуванням
            return None
    return wrapper

# Приклад використання
@exception_handler
def divide(a, b):
    return a / b

# Виклики функції
print(divide(10, 2))
print(divide(10, 0))  # ділення на нуль - виняток