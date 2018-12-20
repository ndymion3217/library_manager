import pickle


class Account:
    def __init__(self, id, password, name, type, birth, phone):
        self.id = id
        self.password = password
        self.name = name
        self.id_type = type
        self.birthday = birth
        self.phone_num = phone
        self.borrowed_book = []

    def change_password(self, type):
        if type == 'operator':
            pass
        elif type == 'manager':
            pass
        elif type == 'user':
            pass

    def show_menu(self, type):
        pass

    def


class Book:
    pass

class Main:
    cur_login_id = ''
    cur_login_type = ''
    def login(self):