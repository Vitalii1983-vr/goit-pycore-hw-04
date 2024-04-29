from pathlib import Path  # Імпорт класу Path для роботи з файловими шляхами
import os  # Імпорт модуля os для перевірки існування файлів

# Встановлення шляху до текстового файлу
file_path = Path(
    r'C:\Users\roger\Desktop\Магістратура 2024\My_HW_VR\2_HW\path_HW_2_ex_2\info_cats_file.txt')

# Перевірка на існування файлу та його створення у разі відсутності
if not file_path.exists():
    with file_path.open(mode='w', encoding='utf-8') as file:  # Відкриття файлу для запису
        # Запис інформації про котів
        file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
        file.write("60b90c2413067a15887e1ae2,Vika,1\n")
        file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
        file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
        file.write("60b90c4613067a15887e1ae5,Tessi,5\n")

# Функція для зчитування інформації про котів


def get_cats_info(path):
    if not os.path.exists(path):  # Перевірка наявності файлу
        # Повідомлення про помилку
        raise FileNotFoundError(f"Файл {path} не знайдено.")

    cats = []  # Створення пустого списку для зберігання даних про котів

    with open(path, 'r', encoding='utf-8') as file:  # Відкриття файлу для читання
        for line in file:
            line = line.strip()  # Видалення зайвих пробілів та символів переходу на новий рядок
            parts = line.split(',')  # Розділення рядка на частини

            if len(parts) != 3:  # Перевірка на коректність формату даних
                raise ValueError(f"Некоректний формат даних: {line}")

            cat_id, name, age_str = parts  # Виділення частин інформації

            try:
                age = int(age_str)  # Спроба конвертувати вік у ціле число
            except ValueError:
                raise ValueError(f"Некоректний вік кота для {name}: {age_str}")

            # Створення словника з інформацією про кота
            cat = {"id": cat_id, "name": name, "age": age}
            cats.append(cat)  # Додавання словника до списку

    return cats  # Повернення списку з даними про котів


# Виклик функції та виведення результатів
cats_info = get_cats_info(file_path)  # Отримання інформації про котів
print(cats_info)  # Друк результатів
