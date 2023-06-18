from config import Notes

nt = Notes('Notes.json')

def print_menu():
    print('''\nЭто заметки. Возможные действия:
          1. Открыть файл
          2. Сохранить файл
          3. Показать все заметки
          4. Показать одну заметку
          5. Добавить заметку
          6. Редактировать заметку
          7. Удалить заметку
          8. Выход''')
    while True:
        choice = input('Введите номер необходимого действия: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Номер действия должен быть от 1 до 8 включительно. "Давай по новой, Миша.. (с)"')

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
            print('Показать одну заметку')
            nt.show_one_note()
        case 5:
            print('Добавить заметку')
            nt.add_note()
        case 6:
            print('Редактировать заметку')
            nt.change_note()
        case 7:
            print('Удалить заметку')
            nt.delete_note()
        case 8:
            if nt.quit():
                if True:
                    nt.save_file()
            print('До свидания!')
            break

