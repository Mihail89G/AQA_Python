import allure
import pytest

from sqlalchemy import create_engine, Column, Integer, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.dialects.mssql import NVARCHAR


connection_string = (
    "mssql+pyodbc:///?"
    "odbc_connect="
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"  
    "Database=TEST;"
    "Trusted_Connection=yes;"
)

Base = declarative_base()
engine = create_engine(connection_string, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR(50))
    courses = relationship('Course', secondary=student_course_table, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR(50))
    students = relationship('Student', secondary=student_course_table, back_populates='courses')

Base.metadata.create_all(engine)


def add_student(name):
    student = Student(name=name)
    session.add(student)
    session.commit()
    return student

def add_course(name):
    course = Course(name=name)
    session.add(course)
    session.commit()
    return course

def enroll_student(student_id, course_id):
    student = session.get(Student, student_id)
    course = session.get(Course, course_id)
    student.courses.append(course)
    session.commit()

def update_student(student_id, new_name):
    student = session.get(Student, student_id)
    student.name = new_name
    session.commit()

def delete_student(student_id):
    student = session.get(Student, student_id)
    session.delete(student)
    session.commit()


@pytest.fixture(autouse=True)
def clean_db():
    yield
    session.execute(student_course_table.delete())
    session.query(Student).delete()
    session.query(Course).delete()
    session.commit()


@allure.feature("Students")
class TestStudents:

    @allure.title("Додавання студента")
    def test_add_student(self):
        with allure.step("Додати студента"):
            student = add_student("Іван")

        with allure.step("Перевірити наявність студента в БД"):
            assert session.get(Student, student.id) is not None

    @allure.title("Оновлення студента")
    def test_update_student(self):
        with allure.step("Створити студента"):
            student = add_student("Марія")

        with allure.step("Оновити імʼя"):
            update_student(student.id, "Марина")

        with allure.step("Перевірити оновлення"):
            assert session.get(Student, student.id).name == "Марина"

    @allure.title("Видалення студента")
    def test_delete_student(self):
        with allure.step("Створити студента"):
            student = add_student("Олег")

        with allure.step("Видалити студента"):
            delete_student(student.id)

        with allure.step("Перевірити, що студент видалений"):
            assert session.get(Student, student.id) is None


@allure.feature("Courses")
class TestCourses:

    @allure.title("Запис студента на курс")
    def test_enroll_student(self):
        with allure.step("Створити студента і курс"):
            student = add_student("Денис")
            course = add_course("Біологія")

        with allure.step("Записати студента на курс"):
            enroll_student(student.id, course.id)

        with allure.step("Перевірити запис"):
            assert course in student.courses

#PowerShell
#cd C:\Users\38068\PycharmProjects\PythonProject_DOCKER
#allure serve allure-results
#або налаштувати а пайчарм



