import requests
import urllib.parse

BASE_URL = "http://127.0.0.1:8080"
FILE_PATH = "test.jpg"

# Завантаження зображення (POST)
with open(FILE_PATH, "rb") as f:
    files = {"image": f}
    response = requests.post(f"{BASE_URL}/upload", files=files)


print("POST /upload:")
print("Код стану:", response.status_code)
print("Відповідь JSON:", response.json())

if response.status_code != 201:
    exit()

uploaded_url = response.json()["image_url"]
filename = uploaded_url.split("/")[-1]
encoded_filename = urllib.parse.quote(filename)

# Отримання URL файлу (GET)
response = requests.get(f"{BASE_URL}/image/{encoded_filename}", headers={"Content-Type": "text"})
print("\nGET /image:")
print("Код стану:", response.status_code)
print("Відповідь JSON:", response.json())

# Видалення файлу (DELETE)
response = requests.delete(f"{BASE_URL}/delete/{encoded_filename}")
print("\nDELETE /delete:")
print("Код стану:", response.status_code)
print("Відповідь JSON:", response.json())

#Як це виконати:
#1.Наприклад в одну директорію покласти файли app.py (від вчителя), test.jpg (просто створив пустий), homework_19_2.py
#2. Під цією директорією запустити в терміналі python app.py
#3. Під цією директорією запустити в новому терміналі python homework_19_2.py
