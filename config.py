import json
from copy import deepcopy
from datetime import datetime

class Notes:
    path = 'Notes.json'

    def __init__(self, path):
        self.path = path
        self.notes = {}
        self.old_notes = {}

    def open_file(self):
        with open(self.path, 'r') as file:
            data_json = file.read()
            self.notes = json.loads(data_json)
            print('Файл открыт')
        self.old_notes = deepcopy(self.notes)

    def save_file(self):
        data_json = json.dumps(self.notes)
        with open(self.path, 'w') as file:
            file.write(data_json)
        self.old_notes = deepcopy(self.notes)

    def show_notes(self):
        if(len(self.notes)) == 0:
            print('Файл не открыт либо пуст')
        else:
            for item in self.notes.items():
                print(item)

    def show_one_note(self):
        if (len(self.notes)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите название заметки, которую Вы хотите посмотреть: ')
            a = 0
            for value in self.notes.values():
                if value['name'] == user_info:
                    print(value)
                else:
                    a = a + 1
            if a == len(self.notes):
                print('Такой заметки нет')

    def add_note(self):
            note_name = input('Введите название заметки: ')
            note_info = input('Введите заметку: ')
            note_date = str(datetime.now())

            keys_of_notes = tuple(self.notes.keys())
            max = keys_of_notes[0]
            for i in keys_of_notes:
                if int(i) > int(max):
                    max = int(i)
            if len(self.notes) == 0:
                new_id = 0
            else:
                new_id = str(max + 1)

            self.notes[new_id] = {"name": note_name, "info": note_info, "date": note_date}
            new_data_json = json.dumps(self.notes)
            with open(self.path, "w") as file:
                file.write(new_data_json)

    def change_note(self):
        if(len(self.notes)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите название заметки, которую Вы хотите изменить: ')
            a = 0
            for key, value in self.notes.items():
                if value['name'] == user_info:
                    print (value)
                    question = input ('Эту заметку хотите изменить? (y/n): ')
                    if question == 'y':
                        new_note_info = input('Введите новый текст заметки: ')
                        new_note_date = str(datetime.now())
                        del self.notes[key]
                        self.notes[key] = {"name": user_info, "info": new_note_info, "date": new_note_date}
                        new_json_string = json.dumps(self.notes)
                        with open(self.path, "w") as file:
                            file.write(new_json_string)
                        break
                else:
                    a = a + 1
            if a == len(self.notes):
                print('Такой заметки нет')

    def delete_note(self):
        if(len(self.notes)) == 0:
            print('Файл не открыт либо пуст')
        else:
            user_info = input('Введите название заметки, которую Вы хотите удалить: ')
            a = 0
            for key, value in self.notes.items():
                if value['name'] == user_info:
                    print (value)
                    question = input ('Эту заметку хотите удалить? (y/n): ')
                    if question == 'y':
                        del self.notes[key]
                        print('Заметка удалена')
                        new_json_string = json.dumps(self.notes)
                        with open(self.path, "w") as file:
                            file.write(new_json_string)
                        break
                else:
                    a = a + 1
            if a == len(self.notes):
                print('Такой заметки нет')

    def quit(self):
        if self.notes != self.old_notes:
            answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n): ')
            return True if answer == 'y' else False

