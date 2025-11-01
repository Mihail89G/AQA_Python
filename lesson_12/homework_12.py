'''Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homeworks10.py
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.'''

import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from homeworks import validate_new_user

class TestValidateNewUser(unittest.TestCase):

    # 1. Валідний користувач 1
    def test_valid_user_1(self):
        record = {'id': 1, 'email': 'user@example.com', 'age': 30, 'balance': 100.0, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertTrue(result['all_valid'])

    # 2. Негативний id
    def test_invalid_id(self):
        record = {'id': -5, 'email': 'user@example.com', 'age': 30, 'balance': 100, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertFalse(result['id_valid'])

    # 3. id = 0
    def test_id_zero(self):
        record = {'id': 0, 'email': 'zero@example.com', 'age': 25, 'balance': 50, 'password': 'password1'}
        result = validate_new_user(record)
        self.assertFalse(result['id_valid'])

    # 4. Пустий email
    def test_empty_email(self):
        record = {'id': 2, 'email': '', 'age': 30, 'balance': 100, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertFalse(result['email_valid'])

    # 5. Email без '@'
    def test_invalid_email_format(self):
        record = {'id': 3, 'email': 'userexample.com', 'age': 30, 'balance': 100, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertFalse(result['email_valid'])

    # 6. Вік менше 18
    def test_age_too_low(self):
        record = {'id': 4, 'email': 'user@example.com', 'age': 16, 'balance': 50, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertFalse(result['age_valid'])

    # 7. Вік більше 120
    def test_age_too_high(self):
        record = {'id': 5, 'email': 'user@example.com', 'age': 150, 'balance': 50, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertFalse(result['age_valid'])

    # 8. Негативний баланс
    def test_negative_balance(self):
        record = {'id': 6, 'email': 'user@example.com', 'age': 30, 'balance': -10, 'password': 'secret123'}
        result = validate_new_user(record)
        self.assertFalse(result['balance_valid'])

    # 9. Пароль занадто короткий
    def test_short_password(self):
        record = {'id': 7, 'email': 'test@domain.com', 'age': 25, 'balance': 0, 'password': '123'}
        result = validate_new_user(record)
        self.assertFalse(result['password_valid'])

    # 10. Пустий пароль
    def test_empty_password(self):
        record = {'id': 9, 'email': 'empty@domain.com', 'age': 25, 'balance': 100, 'password': ''}
        result = validate_new_user(record)
        self.assertFalse(result['password_valid'])

if __name__ == '__main__':
    import unittest
    unittest.main()