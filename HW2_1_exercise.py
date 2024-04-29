from pathlib import Path  # Імпорт класу Path для роботи з файловими шляхами
import os  # Імпорт модуля os для роботи з операційною системою  

# Шлях до файлу з даними про зарплати
file_path = Path(
    r'C:\Users\roger\Desktop\Магістратура 2024\My_HW_VR\2_HW\path_HW_2_ex_1\salaries.txt')

# Створення файлу, якщо він не існує
if not file_path.exists():
    # Відкриття файлу на запис
    with file_path.open(mode='w', encoding='utf-8') as file:
        # Запис даних до файлу
        file.write("Alex Korp,3000\n")
        file.write("Nikita Borisenko,2000\n")
        file.write("Sitarama Raju,1000\n")
        file.write("Vitalii Rudenko,50000\n")

# Функція для обрахування загальної та середньої зарплат


def total_salary(path):
    # Перевірка наявності файлу
    if not os.path.exists(path):
        # Якщо файл не знайдено, виводиться повідомлення про помилку
        raise FileNotFoundError(f"Файл {path} не знайдено.")

    total = 0  # Сума зарплат
    count = 0  # Кількість записів

    # Відкриття файлу для читання
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Видалення пробілів та переносів рядка
            parts = line.split(',')  # Розділення рядка на частини

            # Перевірка коректності даних
            if len(parts) != 2:
                raise ValueError(f"Некоректний формат даних: {line}")

            name, salary_str = parts  # Витягнення імені та зарплати
            try:
                salary = float(salary_str)  # Перетворення строки в число
            except ValueError:
                raise ValueError(f"Некоректна зарплата у {name}: {salary_str}")

            total += salary  # Додавання зарплати до загального підсумку
            count += 1  # Збільшення лічильника записів

    # Розрахунок середньої зарплати
    average = total / count if count > 0 else 0

    return total, average  # Повернення загальної та середньої зарплат


# Виведення результатів роботи функції
total, average = total_salary(file_path)
print(f"Загальна сума зарплат: {total}, Середня зарплата: {average}")
