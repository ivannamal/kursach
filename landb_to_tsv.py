def read_and_filter_printable_chars(file_path):
    with open(file_path, 'rb') as file:
        # Пропускаємо перші 228 байтів
        file.seek(228)

        # Читаємо вміст файлу
        file_content = file.read()

        # Створюємо список для збереження відфільтрованих символів
        printable_chars = []

        # Перевіряємо байти на предмет символів в діапазоні 32-126
        for i in range(len(file_content) - 1):
            byte = file_content[i]
            next_byte = file_content[i + 1]

            if 32 <= byte <= 126:
                printable_chars.append(chr(byte))

                # Перевіряємо, чи наступний байт не є допустимим
                if not (32 <= next_byte <= 126):
                    printable_chars.append('\n')

        # Останній байт
        last_byte = file_content[-1]
        if 32 <= last_byte <= 126:
            printable_chars.append(chr(last_byte))

        return ''.join(printable_chars)


def edit_lines(text):
    # Розбиваємо на рядки
    lines = text.split('\n')

    print("Ось ваші рядки:")
    for idx, line in enumerate(lines):
        print(f"{idx + 1}: {line}")

    # Запит на редагування
    line_to_edit = int(input("Введіть номер рядка, який хочете відредагувати (0 для завершення): "))
    while line_to_edit != 0:
        if 1 <= line_to_edit <= len(lines):
            new_line = input(f"Введіть новий текст для рядка {line_to_edit}: ")
            lines[line_to_edit - 1] = new_line
        else:
            print("Невірний номер рядка. Спробуйте ще раз.")

        line_to_edit = int(input("Введіть номер рядка, який хочете відредагувати (0 для завершення): "))

    # Повертаємо редаговані рядки назад в одну строку
    return '\n'.join(lines)


def save_edited_content(file_path, edited_text):
    with open(file_path, 'wb') as file:
        file.write(edited_text.encode('utf-8'))


# Приклад використання:
file_path = 'chapters_spanish.landb'  # Замініть на шлях до вашого файлу

# Читання та фільтрація символів
filtered_text = read_and_filter_printable_chars(file_path)
print("\nФільтрований текст:")
print(filtered_text)

# Редагування тексту
edited_text = edit_lines(filtered_text)

# Збереження редагованого тексту назад у файл
save_edited_content("newfile.txt", edited_text)

print("\nТекст успішно редаговано та збережено.")
