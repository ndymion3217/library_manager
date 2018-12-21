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

    def change_type(self, type):
        pass

    def __del__(self):
        pass


class Book:
    cur_serial_num = 1
    def __init__(self, title, category, writer, publisher):
        self.serial_num = Book.cur_serial_num
        Book.cur_serial_num += 1
        self.title = title
        self.category = category
        self.writer = writer
        self.publisher = publisher
        self.available = True

    def __del__(self):
        pass


class Main:
    def __init__(self):
        self.account_list = []
        self.book_list = []
        self.cur_login_type = None

    def login(self):
        login_id = input('ID를 입력하세요 : ')
        for i in Main.account_list:
            if i.id == login_id:
                while True:
                    login_password = input('비밀번호를 입력하세요 : ')
                    if i.password == login_password:
                        input('{} 님 반갑습니다. 로그인 되었습니다.'.format(i.name))
                        Main.cur_login_type = i.type
                        Main.show_menu()
                    else:
                        input('비밀번호가 다릅니다.')

    def generate_account(self):
        pass

    def generate_book(self):
        pass

    def show_menu(self):
        pass

    def manage_account(self):
        pass

    def manage_book(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def logout(self):
        pass

    def turn_off(self):
        pass

    def show_id_list(self):
        pass

    def show_book_list(self):
        pass

    def delete_book(self):
        pass

    def delete_id(self):
        pass


