import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# Логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('test_search.log', encoding='utf-8') #додав utf-8 бо були проблеми
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Базовий URL
BASE_URL = "http://127.0.0.1:8080"

# Фікстура для авторизації
@pytest.fixture(scope="class")   # зробив для класу
def auth_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"

    username = "test_user"
    password = "test_pass"

    logger.info("Авторизація користувача...")
    response = session.post(auth_url, auth=HTTPBasicAuth(username, password))
    assert response.status_code == 200, f"Auth failed: {response.text}"

    access_token = response.json().get("access_token")
    assert access_token, "Access token не отримано!"

    session.headers.update({'Authorization': f'Bearer {access_token}'})
    logger.info("Отримано токен доступу.")
    yield session
    session.close()

# Параметризація тестів
@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 10),
        ("brand", 3),
        ("engine_volume", 7),
        ("price", 1),
        ("year", 20),
        ("brand", 8),
    ]
)
class TestCarSearch:

    def test_get_cars(self, auth_session, sort_by, limit):
        url = f"{BASE_URL}/cars"
        params = {"sort_by": sort_by, "limit": limit}

        logger.info(f"Виконую GET запит: {url} з параметрами {params}")
        response = auth_session.get(url, params=params)
        logger.info(f"Статус код відповіді: {response.status_code}")
        assert response.status_code == 200, f"GET /cars failed: {response.text}"

        cars = response.json()
        logger.info(f"Отримано {len(cars)} автомобілів")

        # Перевірка кількості авто (не більше limit)
        assert len(cars) <= limit, f"Очікувано максимум {limit} автомобілів, отримано {len(cars)}"

        # Перевірка структури та типів полів
        for car in cars:
            assert "brand" in car and isinstance(car["brand"], str)
            assert "year" in car and isinstance(car["year"], int)
            assert "engine_volume" in car and isinstance(car["engine_volume"], (int, float))
            assert "price" in car and isinstance(car["price"], int)

        # Перевірка сортування
        if cars:
            values = [car[sort_by] for car in cars]
            # Текстове поле сортується алфавітно
            if sort_by == "brand":
                assert values == sorted(values), f"Масив не відсортований за {sort_by}: {values}"
            else:  # числові поля по зростанню
                assert values == sorted(values), f"Масив не відсортований за {sort_by}: {values}"

        logger.info(f"Тест для параметрів sort_by={sort_by}, limit={limit} пройшов успішно.")
        print(cars)  # додав щоб було видно результат по авто

#Тест 1: sort_by=price, limit=5
'''
[{'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018},
{'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020}, 
{'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016}, 
{'brand': 'Kia', 'engine_volume': 2.0, 'price': 31000, 'year': 2019},
{'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015}]'''
#Тест 2: sort_by=year, limit=10
'''
[{'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015},
{'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016}, 
{'brand': 'Toyota', 'engine_volume': 2.4, 'price': 35000, 'year': 2017}, 
{'brand': 'Subaru', 'engine_volume': 2.5, 'price': 40000, 'year': 2017}, 
{'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}, 
{'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018},
{'brand': 'Mazda', 'engine_volume': 2.0, 'price': 32000, 'year': 2018}, 
{'brand': 'Jeep', 'engine_volume': 3.6, 'price': 45000, 'year': 2018}, 
{'brand': 'Mercedes', 'engine_volume': 2.5, 'price': 55000, 'year': 2019}, 
{'brand': 'Volkswagen', 'engine_volume': 2.0, 'price': 33000, 'year': 2019}]'''
#Тест 3: sort_by=brand, limit=3
'''
[{'brand': 'Acura', 'engine_volume': 2.4, 'price': 48000, 'year': 2020}, 
{'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020}, 
{'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}]'''
#Тест 4: sort_by=engine_volume, limit=7
'''
[{'brand': 'Tesla', 'engine_volume': 0.0, 'price': 80000, 'year': 2020}, 
{'brand': 'Nissan', 'engine_volume': 1.5, 'price': 40000, 'year': 2021}, 
{'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016}, 
{'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020},
{'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020}, 
{'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018}, 
{'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}]'''
#Тест 5: sort_by=price, limit=1
'''[{'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018}]'''
#Тест 6: sort_by=year, limit=20
'''
[{'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015},
{'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016},
{'brand': 'Toyota', 'engine_volume': 2.4, 'price': 35000, 'year': 2017},
{'brand': 'Subaru', 'engine_volume': 2.5, 'price': 40000, 'year': 2017},
{'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}, 
{'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018},
{'brand': 'Mazda', 'engine_volume': 2.0, 'price': 32000, 'year': 2018},
{'brand': 'Jeep', 'engine_volume': 3.6, 'price': 45000, 'year': 2018},
{'brand': 'Mercedes', 'engine_volume': 2.5, 'price': 55000, 'year': 2019},
{'brand': 'Volkswagen', 'engine_volume': 2.0, 'price': 33000, 'year': 2019},
{'brand': 'Kia', 'engine_volume': 2.0, 'price': 31000, 'year': 2019},
{'brand': 'Infiniti', 'engine_volume': 3.5, 'price': 52000, 'year': 2019},
{'brand': 'Volvo', 'engine_volume': 2.0, 'price': 46000, 'year': 2019},
{'brand': 'Bugatti', 'engine_volume': 8.0, 'price': 350000, 'year': 2019},
{'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020},
{'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020},
{'brand': 'Acura', 'engine_volume': 2.4, 'price': 48000, 'year': 2020},
{'brand': 'Land Rover', 'engine_volume': 2.0, 'price': 55000, 'year': 2020},
{'brand': 'Tesla', 'engine_volume': 0.0, 'price': 80000, 'year': 2020},
{'brand': 'Lamborghini', 'engine_volume': 6.5, 'price': 300000, 'year': 2020}]'''
#Тест 7: sort_by=brand, limit=8
'''
[{'brand': 'Acura', 'engine_volume': 2.4, 'price': 48000, 'year': 2020}, 
 {'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020}, 
 {'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}, 
 {'brand': 'Bugatti', 'engine_volume': 8.0, 'price': 350000, 'year': 2019}, 
 {'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018}, 
 {'brand': 'Ferrari', 'engine_volume': 6.3, 'price': 250000, 'year': 2021}, 
 {'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015}, 
 {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016}]'''