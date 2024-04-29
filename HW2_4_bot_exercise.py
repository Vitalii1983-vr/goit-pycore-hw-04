import sys  # Для роботи з аргументами командного рядка
from pathlib import Path  # Для роботи з файловими шляхами

# Функція для розбору введеної користувачем команди


def parse_input(user_input):
    cmd, *args = user_input.split()  # Розбивка команди на окремі частини
    cmd = cmd.strip().lower()  # Переведення команди у нижній регістр
    return cmd, args  # Повернення команди та аргументів

# Функція для додавання нового контакту


def add_contact(args, contacts):
    if len(args) != 2:  # Перевіряємо правильність кількості аргументів name та phone
        return "Некоректна кількість аргументів. Використовуйте: add [ім'я] [телефон]"

    name, phone = args  # Розпаковка значень ім'я та телефон зі списку args
    contacts[name] = phone  # Додаємо контакт до словника
    return "Контакт додано."  # Підтвердження додавання контакту

# Функція для зміни інформації про контакт


def change_contact(args, contacts):
    if len(args) != 2:  # Перевіряємо правильність кількості аргументів
        return "Некоректна кількість аргументів. Використовуйте: change [ім'я] [новий телефон]"

    name, phone = args
    if name not in contacts:  # Якщо контакт відсутній
        return f"Контакт '{name}' не знайдено."

    contacts[name] = phone  # Оновлюємо контакт
    return "Контакт оновлено."  # Підтвердження оновлення контакту

# Функція для відображення номера телефону


def show_phone(args, contacts):
    if len(args) != 1:  # Перевіряємо правильність кількості аргументів
        return "Некоректна кількість аргументів. Використовуйте: phone [ім'я]"

    name = args[0]
    if name not in contacts:  # Якщо контакт відсутній
        return f"Контакт '{name}' не знайдено."

    return contacts[name]  # Повертаємо номер телефону

# Функція для відображення всіх контактів


def show_all(contacts):
    if not contacts:  # Якщо словник контактів порожній
        return "Контакти не знайдено."

    # Повертаємо всі контакти у вигляді рядка
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Головна функція, яка керує роботою бота


def main():
    contacts = {}  # Словник для збереження контактів
    # Вітання після запуску кода (бота)
    print("Вітаємо у Вас у асистент боті управління контактами!")

# Безкінечний цикл, який очікує введення користувачем команди,
# та розбирає введену команду на окремі частини
    while True:
        user_input = input("Введіть команду: ")  # Очікуємо введення команди
        command, args = parse_input(user_input)  # Розбираємо введену команду

        if command in ["close", "exit"]:  # Закінчуємо роботу
            print("До побачення!")  # Повідомлення про завершення
            break

        elif command == "hello":  # Обробка команди "hello"
            print("Як я можу вам допомогти?")  # Вивід привітання

        elif command == "add":  # Обробка команди "add"
            print(add_contact(args, contacts))  # Додавання контакту

        elif command == "change":  # Обробка команди "change"
            print(change_contact(args, contacts))  # Зміна контакту

        elif command == "phone":  # Обробка команди "phone"
            print(show_phone(args, contacts))  # Показ номера телефону

        elif command == "all":  # Обробка команди "all"
            print(show_all(contacts))  # Показ всіх контактів

        else:  # Обробка невірної команди
            print("Некоректна команда.")  # Повідомлення про невірну команду


if __name__ == "__main__":
    main()  # Запуск головної функції


# Робота з ботом, список команд (можна ввести такі команди):
# 1. "hello" - Привітання.
# 2. "add [ім'я] [телефон]" - Додати новий контакт.
# 3. "change [ім'я] [новий телефон]" - Змінити номер телефону існуючого контакту.
# 4. "phone [ім'я]" - Відобразити номер телефону для вказаного контакту.
# 5. "all" - Показати всі контакти.
# 6. "exit" - Вийти з програми.
# 7. "close" або "exit" - Завершити роботу програми.
