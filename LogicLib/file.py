from field_info import FieldInfo
from field import Field

class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        # Читаем данные из файла
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        return lines

    def write_file(self, lines):
        # Записываем данные в файл
        with open(self.file_path, 'w') as file:
            file.writelines(lines)

    def get_field_value(self, field, line):
        # Получаем значение поля из строки файла
        start, end = field.position
        value = line[start-1:end].strip()
        return value

    def set_field_value(self, field, line, value):
        # Устанавливаем значение поля в строке файла
        start, end = field.position
        line = line[:start-1] + str(value).ljust(end - start + 1) + line[end:]
        return line

    def get_transaction_count(self, lines):
        # Возвращает количество транзакций в файле
        transaction_count = 0
        for line in lines:
            if line.startswith("02"):  # Проверяем, является ли строка транзакцией
                transaction_count += 1
        return transaction_count
