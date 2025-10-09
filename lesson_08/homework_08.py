#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
#Створіть об('єкт цього класу, представляючи студента. '
#Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. '
#'Виведіть інформацію про студента та змініть його середній бал.)

#клас
class student:
    # об'єкт
    def __init__(self,name,surname, age,aver_value):
        self.name = name
        self.surname = surname
        self.age = age
        self.aver_value = aver_value
        # Метод
     def change_aver_value(self,change_aver_value):
         self.aver_value = change_aver_value

    # метод виведення
    def __str__(self):
        return f"Студент: {self.name} {self.surname}, Вік: {self.age}, Середній бал: {self.aver_value}"

student_1 = student("Михало", "Гапоненко", 36, 70)
print(student_1)

student_1.change_aver_value(100)
print(student_1)
