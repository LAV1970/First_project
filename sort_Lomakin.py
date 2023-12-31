import os
import shutil
import sys

# Глобальная константа для соответствия расширения файлов к категориям
EXTENSIONS = {
    'Images': ('.jpeg', '.png', '.jpg', '.svg'),
    'Video': ('.avi', '.mp4', '.mov', '.mkv'),
    'Documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    'Audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'Archives': ('.zip', '.gz', '.tar')
}

# Глобальная таблица транслитерации
TRANSLIT_TABLE = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
    'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
    'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
}

# Функция для нормализации и транслитерации имени файла или папки
def normalize(name):
    # Заменяем кириллические символы на латиницу
    for cyrillic, latin in TRANSLIT_TABLE.items():
        name = name.replace(cyrillic, latin)

    # Заменяем все символы, кроме латинских букв и цифр, на '_'
    name = ''.join(c if c.isalnum() or c == '.' or c == '_' else '_' for c in name)

    return name

def organize_files(folder_path):
    # Создаем папки для каждой категории
    for category in EXTENSIONS.keys():
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)
    # Функция для перемещения файлов в соответствующие папки
    def move_file(file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        base_name = os.path.basename(file_path)
        base_name_without_ext, ext = os.path.splitext(base_name)

        # Нормализуем имя файла без расширения
        normalized_base_name = normalize(base_name_without_ext)

        for category, ext_list in EXTENSIONS.items():
            if file_extension in ext_list:
                target_folder = os.path.join(folder_path, category)

                # Создаем нормализованное имя файла с сохранением расширения
                target_file = os.path.join(target_folder, f"{normalized_base_name}{ext}")

                # Добавляем инкремент к имени файла, если он уже существует
                index = 1
                while os.path.exists(target_file):
                    target_file = os.path.join(target_folder, f"{normalized_base_name}_{index}{ext}")
                    index += 1

                shutil.move(file_path, target_file)
                return
        # Если расширение не соответствует ни одной категории, перемещаем в "неизвестные"
        unknown_folder = os.path.join(folder_path, 'unknown')
        os.makedirs(unknown_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(unknown_folder, normalize(base_name)))

    # Рекурсивная функция для обхода всех файлов в папке и ее подпапках
    def organize_recursively(current_folder):
        for root, _, files in os.walk(current_folder):
            for file in files:
                file_path = os.path.join(root, file)
                move_file(file_path)

    organize_recursively(folder_path)

    # Удаление пустых папок (кроме archives, video, audio, documents, images)
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            if dir_to_check != folder_path:
                try:
                    os.rmdir(dir_to_check)
                except OSError:
                    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python sort_Lomakin.py <путь>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Недопустимый путь к папке:", folder_path)
        sys.exit(1)

    organize_files(folder_path)
    print("Файлы успешно организованы и переименованы, пустые папки удалены!")