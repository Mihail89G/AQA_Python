'''ДЗ 19.1. Бекап офіційних Nasa фото
url = https://images-api.nasa.gov/search?q=mars&media_type=image
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON.
Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли.
Завдання:
1) Послати запит до вказуного url щоб отримати загальну інформацію
2) У відповіді знайти посилання на фото(collections->items->links
3) Послати запит на викпадкові 2-3 urlk і зберегти ці фото локально'''


import requests

url = "https://images-api.nasa.gov/search"
params = {"q": "mars", "media_type": "image"}

# 1. Отримуємо загальну інформацію
response = requests.get(url, params=params)
data = response.json()

# 2. Знаходимо всі посилання на фото (по факту бачу що фото однакові але різні розміри, тому рахуються як різні
# додав і закоментував для повної унікальності, якщо потрібно)
items = data["collection"]["items"]

photo_links = []

for item in items:
    links = item.get("links", [])
    for link in links:
        href = link.get("href", "")
        if href.lower().endswith(".jpg"):
            photo_links.append(href)
            #if href not in photo_links:  # для повної унікальністі якщо така потрібна
                #photo_links.append(href)
            #break

print(f"Знайдено посилань на фото: {len(photo_links)}")

# Беремо перші 3 фото
selected_photos = photo_links[:3]

# 3. Скачування вибраних фото
for idx, img_url in enumerate(selected_photos, start=1):
    print(f"Скачую {idx}: {img_url}")

    img_data = requests.get(img_url).content

    filename = f"mars_photo{idx}.jpg"
    with open(filename, "wb") as f:
        f.write(img_data)

    print(f"Збережено як {filename}")

print("Готово!")


