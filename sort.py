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

def organize_files(folder_path):
    # Создаем папки для каждой категории
    for category in EXTENSIONS.keys():
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    # Функция для перемещения файлов в соответствующие папки
    def move_file(file_path):
        file_extension = os.path.splitext(file_path)[1].lower()

        for category, ext_list in EXTENSIONS.items():
            if file_extension in ext_list:
                target_folder = os.path.join(folder_path, category)
                target_file = os.path.join(target_folder, os.path.basename(file_path))

                # Добавляем инкремент к имени файла, если он уже существует
                index = 1
                while os.path.exists(target_file):
                    filename, file_extension = os.path.splitext(os.path.basename(file_path))
                    target_file = os.path.join(target_folder, f"{filename}_{index}{file_extension}")
                    index += 1

                shutil.move(file_path, target_file)
                return

        # Если расширение не соответствует ни одной категории, перемещаем в "неизвестные"
        unknown_folder = os.path.join(folder_path, 'unknown')
        os.makedirs(unknown_folder, exist_ok=True)
        shutil.move(file_path, unknown_folder)

    # Рекурсивная функция для обхода всех файлов в папке и ее подпапках
    def organize_recursively(current_folder):
        for root, _, files in os.walk(current_folder):
            for file in files:
                file_path = os.path.join(root, file)
                move_file(file_path)

    organize_recursively(folder_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python sort.py <путь>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Недопустимый путь к папке:", folder_path)
        sys.exit(1)

    organize_files(folder_path)
    print("Файлы успешно организованы!")

