from config import Notes

nt = Notes('Notes.json')

def print_menu():
    print('''\nЭто заметки. Возможные действия:
          1. Открыть файл
          2. Сохранить файл
          3. Показать все заметки
          4. Добавить заметку
          5. Редактировать заметку
          6. Удалить заметку
          7. Выход''')
    while True:
        choice = input('Введите номер необходимого действия: ')
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        else:
            print('Номер действия должен быть от 1 до 7 включительно. "Давай по новой, Миша.. (с)"')

while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            print('Открыть файл')
            nt.open_file()
        case 2:
            nt.save_file()
            print('Файл сохранен')
        case 3:
            print('Показать все заметки')
            nt.show_notes()
        case 4:
            print('Добавить заметку')
            nt.add_note()
        case 5:
            print('Редактировать заметку')
            nt.change_note()
        case 6:
            print('Удалить заметку')
            nt.delete_note()
        case 7:
            if nt.quit():
                if True:
                    nt.save_file()
            print('До свидания!')
            break

