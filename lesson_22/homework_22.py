from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker #створює базовий клас, звязки, сесію
from sqlalchemy.dialects.mssql import NVARCHAR # додав бо тоді в базі буде ????, так як використовую укр. імена

# З'єднання з базою даних SQL Server Management Studio
server = r"localhost"
database = "TEST"

connection_string = (
    "mssql+pyodbc:///?"
    "odbc_connect="
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={server};"
    f"Database={database};"
    "Trusted_Connection=yes;"
)

# Створення базового класу для визначення моделей даних
Base = declarative_base()

# Для відображення в консолі
engine = create_engine(connection_string, echo=True)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Проміжна таблиця
student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Таблиця з студентами
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR(50))
    courses = relationship('Course', secondary=student_course_table, back_populates='students')

# Таблиця з курсами
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR(50))
    students = relationship('Student', secondary=student_course_table, back_populates='courses')

# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Функція додавання студенту
def add_student(name):
    student = Student(name=name)
    session.add(student)
    session.commit()
    print(f"Додано студента {name}")

# Функція додавання курсу
def add_course(name):
    course = Course(name=name)
    session.add(course)
    session.commit()
    print(f"Додано курс {name}")

# Функція додавання в проміжну таблицю, після того як додали в попередні
def enroll_student(student_id, course_id):
    student = session.query(Student).get(student_id)
    course = session.query(Course).get(course_id)
    student.courses.append(course)
    session.commit()
    print(f"Студент {student.name} записаний на курс {course.name}")

# Виводимо студентів та курси
def show_students_on_course(course_id):
    course = session.query(Course).get(course_id)
    print(f"Студенти на курсі {course.name}:")
    for s in course.students:
        print(s.name)

def show_courses_of_student(student_id):
    student = session.query(Student).get(student_id)
    print(f"Курси студента {student.name}:")
    for c in student.courses:
        print(c.name)

# Оновлення даних
def update_student(student_id, new_name):
    student = session.query(Student).get(student_id)
    if student:
        student.name = new_name
        session.commit()
        print(f"Студента {student_id} оновлено: нове ім'я {new_name}")
    else:
        print("Студента не знайдено")

def update_course(course_id, new_name):
    course = session.query(Course).get(course_id)
    if course:
        course.name = new_name
        session.commit()
        print(f"Курс {course_id} оновлено: нова назва {new_name}")
    else:
        print("Курс не знайдено")

# Видалення студента
def delete_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студент {student.name} видалений з бази")
    else:
        print("Студента не знайдено")

'''
# Для перевірки
# Додавання курсів
add_course("Геометрія")
add_course("Алгебра")
add_course("Статистика")
add_course("Фізика")

# Додавання студентів
add_student("Петро")
add_student("Зіна")
add_student("Даша")

# Запис студентів на курси
enroll_student(1, 1)
enroll_student(2, 2)
enroll_student(1, 3)
enroll_student(3, 4)

# Перегляд
show_courses_of_student(1)
show_students_on_course(1)

# Оновлення
update_student(1, "Олег")
update_course(1, "Моделювання")

# Видалення
delete_student(3)
'''