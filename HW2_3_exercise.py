from pathlib import Path  # Імпорт класу Path для роботи з файловими шляхами
import logging  # Імпорт модуля logging для роботи з логуванням подій
from colorama import init, Fore, Style  # Для кольорового виведення

# Ініціалізуємо Colorama для використання кольорового тексту в консолі
init(autoreset=True)

# Налаштовуємо логування для відстеження потенційних помилок і подій в коді
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

# Функція створює структуру директорій на основі заданого шляху


def create_directory_structure(base_path):
    """
    Створює структуру директорій включаючи папку 'picture' та вкладену 'Logo'.
    """
    try:
        # Створення головної директорії 'picture'
        picture_path = base_path / 'picture'
        # exist_ok=True запобігає помилці, якщо папка вже існує
        picture_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Створено директорію: {picture_path}")

        # Створення піддиректорії 'Logo' всередині 'picture'
        logo_path = picture_path / 'Logo'
        logo_path.mkdir(exist_ok=True)
        logger.info(f"Створено піддиректорію: {logo_path}")

        # Створення файлів у директорії 'picture'
        # .touch() створює файл, якщо він не існує
        (picture_path / "bot-icon.png").touch()
        (picture_path / "mongodb.jpg").touch()
        logger.info("Створено файли у директорії 'picture'.")

        # Створення файлів у піддиректорії 'Logo'
        (logo_path / "IBM+Logo.png").touch()
        (logo_path / "ibm.svg").touch()
        (logo_path / "logo-tm.png").touch()
        logger.info("Створено файли у піддиректорії 'Logo'.")

    except Exception as e:
        logger.exception("Помилка при створенні структури директорій: %s", e)

# Функція візуалізує структуру директорії в консолі з кольорами


def visualize_directory_structure(directory_path):
    """
    Візуалізує структуру директорії 'picture' у консолі з використанням кольорового тексту.
    """
    try:
        path = Path(directory_path)
        # Виводимо назву головної папки синім кольором
        print(Fore.BLUE + f"📦{path.name}/")
        for item in sorted(path.iterdir()):  # Перебираємо всі елементи в директорії
            if item.is_dir():  # Якщо елемент є папкою
                # Виводимо назву папки синім кольором
                print(Fore.BLUE + f" ┣ 📂{item.name}/")
                for subitem in sorted(item.iterdir()):  # Перебираємо вміст папки
                    # Виводимо назви файлів зеленим кольором
                    print(Fore.GREEN + f" ┃ ┣ 📜{subitem.name}")
                print(Fore.BLUE + f" ┃ ┗")  # Закриваємо блок папки
            else:
                # Виводимо назви файлів зеленим кольором
                print(Fore.GREEN + f" ┗ 📜{item.name}")

    except Exception as e:
        logger.exception(
            "Помилка під час візуалізації структури директорій: %s", e)


# Шлях до файла скрипта, що містить цей код
script_path = Path(__file__).resolve()
base_path = script_path.parent

# Створюємо структуру директорії та візуалізуємо її
create_directory_structure(base_path)
visualize_directory_structure(base_path / 'picture')
