'''Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv'''

import os
import csv

folder_path = os.path.dirname(os.path.abspath(__file__))

csv_files = [
    os.path.join(folder_path, "random.csv"),
    os.path.join(folder_path, "random-michaels.csv")
]

for f in csv_files:
    if not os.path.exists(f):
        print(f"Файл не знайдено: {f}")
        exit()

unique_rows = []
seen = set()
headers = None

for file_path in csv_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        file_headers = next(reader)
        if headers is None:
            headers = file_headers
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_rows.append(row)

result_file = os.path.join(folder_path, "result_Haponenko.csv")
with open(result_file, 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out, delimiter=',')
    writer.writerow(headers)
    writer.writerows(unique_rows)

print(f"Результат збережено в {result_file}")

'''Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log'''

import os
import json
import logging

base_folder = os.getcwd()

log_file = os.path.join(base_folder, "json__Haponenko.log")
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

valid_count = 0
invalid_count = 0
invalid_files = []

# Рекурсивний пошук усіх JSON файлів
for root, dirs, files in os.walk(base_folder):
    for file_name in files:
        if file_name.endswith(".json"):
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    json.load(f)
                valid_count += 1
            except json.JSONDecodeError as e:
                logging.error(f"Файл '{file_path}' невалідний JSON: {e}")
                invalid_count += 1
                invalid_files.append(file_path)
            except Exception as e:
                logging.error(f"Помилка при читанні файла '{file_path}': {e}")
                invalid_count += 1
                invalid_files.append(file_path)

print(f"Перевірка завершена. Валідні файли: {valid_count}, невалідні файли: {invalid_count}")
if invalid_files:
    print("Невалідні файли:")
    for f in invalid_files:
        print(f)
print(f"Лог помилок знаходиться у {log_file}")

'''Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо'''

import os
import xml.etree.ElementTree as ET
import logging

# Логування
log_file = "groups.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Путь до XML файлу
folder_path = os.getcwd()
xml_file = os.path.join(folder_path, "groups.xml")

# Функція для отримання incoming по всіх групах
def log_all_incoming():
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall("group"):
            number_elem = group.find("number")
            group_number = number_elem.text if number_elem is not None else "Unknown"

            incoming_value = None
            timing_elem = group.find("timingExbytes")
            if timing_elem is not None:
                incoming_elem = timing_elem.find("incoming")
                if incoming_elem is not None:
                    incoming_value = incoming_elem.text

            if incoming_value is not None:
                logging.info(f"Incoming для group {group_number}: {incoming_value}")
                print(f"Incoming для group {group_number}: {incoming_value}")
            else:
                logging.info(f"Group {group_number} не має incoming або не знайдено")
                print(f"Group {group_number} не має incoming або не знайдено")

    except ET.ParseError as e:
        logging.error(f"Помилка парсингу XML: {e}")
    except FileNotFoundError:
        logging.error(f"Файл не знайдено: {xml_file}")

# Викликаємо функцію
log_all_incoming()