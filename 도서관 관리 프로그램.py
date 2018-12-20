class Account:#ID, Password, 이름, 계정타입, 생년월일, 전화번호, 대여중인 책 목록
    r = open('건드리지 마시오.txt','r')
    r.seek(0)
    id = r.readline().split()
    password=r.readline().split()
    name=r.readline().split()
    type=r.readline().split()
    birth=r.readline().split()
    phone_num=r.readline().split()
    books=[]
    for i in range(len(id)):
        A = r.readline()
        if A == '빈\n':
            books.append(list())
        else:
            books.append(A.split())
    r.close()

class Book:#시리얼 넘버는 자동생성, 이외에는 중복가능
    r = open('건드리지 마시오2.txt','r')
    r.seek(0)
    num_temp = r.readline().split()
    num = []
    for i in num_temp:
        num.append(int(i))        
    name =r.readline().split()
    category = r.readline().split()
    writer = r.readline().split()
    publisher = r.readline().split()# 대여가능,대여불가능
    status = r.readline().split()
    number = int(r.readline())
    r.close()

class Main:
    login_type = ''
    login_id = ''
    def login():
        id = input('ID를 입력하세요. : ')
        if id in Account.id:
            password = input('비밀번호를 입력하세요. : ')
            if password == Account.password[Account.id.index(id)]:
                input('로그인 되었습니다.\n메인화면으로 넘어갑니다.')
                Main.login_type = Account.type[Account.id.index(id)]
                Main.login_id = id              
                Main.show_menu()
            else:
                input('\n비밀번호가 맞지않습니다.')
                Main.login()
        else:
            input('\n해당 ID는 존재하지 않습니다.\n')
            Main.login()
    def show_menu():
        try:
            if Main.login_type == 'Manager':
                choice = int(input('1.계정관리 2.도서 조회 및 검색 3.로그아웃 4.프로그램 종료 : '))
                if choice == 1:
                    Main.manage_account()
                elif choice == 2:
                    Main.check_book(1)
                elif choice == 3:
                    Main.logout()
                elif choice == 4:
                    Main.turn_off()
                else:
                    input('\n1~4 안에서 고르세요.\n')
                    Main.show_menu()
            elif Main.login_type == 'Operator':
                choice = int(input('1.계정관리 2.도서 관리 3.도서 조회 및 검색 4.로그아웃 5.프로그램 종료 : '))
                if choice == 1:
                    Main.manage_account()
                elif choice == 2:
                    Main.manage_book()
                elif choice == 3:
                    Main.check_book(1)
                elif choice == 4:
                    Main.logout()
                elif choice == 5:
                    Main.turn_off()
                else:
                    input('\n1~5 안에서 고르세요.\n')
                    Main.show_menu()            
            else:
                choice = int(input('1 계정관리 2.도서 조회 및 검색 3.대여 4.반납 5.로그아웃 6.프로그램 종료 : '))
                if choice == 1:
                    Main.manage_account()
                elif choice == 2:
                    Main.check_book(1)
                elif choice ==3:
                    Main.borrow_book(0)
                elif choice == 4:
                    Main.return_book()
                elif choice == 5:
                    Main.logout()
                elif choice == 6:
                    Main.turn_off()
                else:
                    input('\n1~6 안에서 고르세요.\n')
                    Main.show_menu()
        except:
            Main.show_menu()
    def manage_account():# 계정 조회,계정등록,<---운영자이상에게만노출,비밀번호변경
        try:
            if Main.login_type == 'Manager' or Main.login_type == 'Operator':
                choice3 = int(input('1.계정 조회 2.계정 등록 3.비밀번호 변경 4.계정 삭제 5.뒤로가기 : '))
                if choice3 == 1:
                    Main.check_id_list()
                elif choice3 == 2:
                    Main.generate_account()
                elif choice3 == 3:
                    Main.change_password()
                elif choice3 == 4:
                    Main.delete_account()
                elif choice3 == 5:
                    Main.show_menu()
                else:
                    input('\n1~3 안에서 고르세요.\n')
                    Main.manage_account()            
            else:
                choice3 = int(input('1.비밀번호 변경 2.뒤로가기 : '))
                if choice3 == 1:
                    Main.change_password()
                elif choice3 == 2:
                    Main.show_menu()
                else:
                    input('\n1,2 중에 고르세요.\n')
                    Main.manage_account()
        except:
            Main.manage_account()
    def manage_book():#(운영자에게만 노출) 도서등록,삭제,
        try:
            choice4 = int(input('1.도서 등록 2.도서 삭제 3.뒤로가기 : '))
            if choice4 == 1:
                Main.generate_book()
            elif choice4 == 2:
                Main.delete_book()
            elif choice4 == 3:
                Main.show_menu()
            else:
                input('\n1~3 중에 고르세요.\n')
                Main.manage_account()
        except:
            Main.manage_book()
    def borrow_book(count):#(대여,반납)<-일반사용자만 노출 ,로그아웃,프로그램종료
        login_index = Account.id.index(Main.login_id)
        try:
            if count == 3:
                input('이미 세권을 대여했습니다.')
                Main.show_menu()
            else:
                search = input('대여하려는 도서의 시리얼 번호를 입력하세요 : ')
                if search == '.':
                    Main.show_menu()
                else:pass
                search = int(search)
                if search in Book.num:
                    num = Book.num.index(search)  
                else:
                    input('해당 도서는 존재하지 않습니다.')
                    Main.borrow_book(count)
                if Book.status[num] == '대여가능':
                    count += 1
                    Book.status[num] = '대여불가'
                    Account.books[Account.id.index(Main.login_id)].append(Book.name[num])
                    choice = int(input('대여 완료\n1.이어서 대여 2.뒤로가기 : '))
                    if choice == 1:
                        Main.borrow_book(count)
                    else:
                        Main.show_menu()
                else: 
                    input('이미 대여된 도서입니다.')
                    Main.borrow_book(count)
        except:
            Main.borrow_book(count)
    def return_book():
        try:
            search = int(input('반납하려는 책의 시리얼 번호를 입력하세요 : '))
            if search in Book.num:
                num = Book.num.index(search)
                if Book.status[num] == '대여가능':
                    input('해당 도서는 이미 반납되었습니다.')
                    Main.return_book()
                else:
                    Book.status[num] = '대여가능'
                    Account.books[Account.id.index(Main.login_id)].remove(Book.name[num])
                    choice10 = int(input('반납 되었습니다.\n1.이어서 반납 2.뒤로가기 : '))
                    if choice10 == 1:
                        Main.return_book()
                    else:
                        Main.show_menu()
            elif search == '.':
                Main.show_menu()
            else:
                input('해당 도서는 존재하지 않습니다.')
                Main.return_book()
        except:
            Main.retrun_book()
    def logout():
        Main.login_type = ''
        Main.login_id = ''
        Main.login()
    def turn_off():
        f = open('건드리지 마시오.txt','w')
        f.write(' '.join(Account.id)+'\n')
        f.write(' '.join(Account.password)+'\n')
        f.write(' '.join(Account.name)+'\n')
        f.write(' '.join(Account.type)+'\n')
        f.write(' '.join(Account.birth)+'\n')
        f.write(' '.join(Account.phone_num)+'\n')
        for i in Account.books:
            if len(i) == 0:
                f.write('빈'+'\n')
            else:
                f.write(' '.join(i)+'\n')
        f.close()
        f = open('건드리지 마시오2.txt','w')
        temp = []
        for i in Book.num:
            temp.append(str(i))
        f.write(' '.join(temp)+'\n')
        f.write(' '.join(Book.name)+'\n')
        f.write(' '.join(Book.category)+'\n')
        f.write(' '.join(Book.writer)+'\n')
        f.write(' '.join(Book.publisher)+'\n')
        f.write(' '.join(Book.status)+'\n')
        f.write(str(Book.number))
        f.close()
        return
    def generate_account():
        try:
            a_id = input('등록할 ID를 입력하시오 : ')
            if a_id in Account.id:
                input('해당 아이디는 이미 존재합니다.')
                Main.generate_account()
            elif a_id == '.':
                Main.manage_account()
            else:
                Main.press_password(a_id)
        except:
            Main.generate_account()
    def press_password(a_id):
        try:
            password = input('비밀번호는? : ')
            if password == '.':
                Main.manage_account()
            elif len(password) < 4 or len(password) > 12:
                input('비밀번호는 4~12자리를 써야합니다.')
                Main.press_password(a_id)
            else:
                password_check = input('비밀번호 확인을 위해 한번도 입력하세요. : ')
                if password_check != password:
                    input('비밀번호가 서로 다릅니다. 다시입력하세요.')
                    Main.press_password()
                else:
                    name = input('이름을 입력하세요. : ')
                    birth = input('생일을 입력하세요. : ')
                    phone = input('전화번호를 입력하세요. : ')
                    if Main.login_type == 'Manager':
                        choice5 = int(input('계정의 타입은?\n1.운영자 2.일반유저 : '))
                        if choice5 == 1:
                            id_type = 'Operator'
                        elif choice5 == 2:
                            id_type = 'User'
                        else:
                            input('1, 2중에 고르세요.')
                    else:
                        id_type = 'User'
                    Account.name.append(name)
                    Account.id.append(a_id)
                    Account.password.append(password)
                    Account.type.append(id_type)
                    Account.birth.append(birth)
                    Account.phone_num.append(phone)
                    Account.books.append(list())
                    Main.manage_account()
        except:
            Main.press_password(a_id)
                
#계정 등록시 ID, 비밀번호, 비밀번호 확인, 이름, 계정타입, 생년월일, 전화번 호를 입력해야 한다. 
#기존 회원 중 중복되는 ID가 없고 비밀번호가 비밀번호 확인과 일치하면 등 록할 수 있다.
#ID와 비밀번호는 최소 4자리, 최대 12자리의 영문과 숫자로 구성된다. (반드 시 숫자, 영문이 같이 들어갈 필요는 없다.
#대소문자는 구분한다.)
#실패할 경우 왜 실패했는데 이유를 알려준다. 
    
    def change_password():
        try:
            if Main.login_type == 'Manager':
                change_id = input('변경하려는 id 입력 : ')
                if change_id == '.':
                    Main.manage_account()
                if change_id in Account.id:
                    Main.continue_change(change_id)
                else:
                    input('해당 id가 없습니다.')
                    Main.change_password()
            elif Main.login_type == 'Operator':
                change_id = input('변경하려는 id 입력 : ')
                if change_id in Account.id and Account.type[Account.id.index(change_id)] != 'Manager' and Account.type[Account.id.index(change_id)] != 'Operator':
                    Main.continue_change(change_id)
                elif change_id == Main.login_id:
                    Main.continue_change(change_id)
                else:
                    input('id가 존재하지 않거나 권한이 없습니다.')
                    Main.change_password()
            else:
                Main.continue_change(Main.login_id)
        except:
            Main.change_password()             
    def continue_change(login_id):
        try:
            b_password = input('기존 비밀번호 입력 : ')
            if b_password == Account.password[Account.id.index(login_id)]:
                n_password = input('새로운 비밀번호 입력 : ')
                if len(n_password) < 4 or len(n_password) > 12:
                    input('비밀번호는 4~12자리로 해주십시오.')
                    Main.continue_change(login_id)
                else:pass
                a_password = input('비밀번호 확인 : ')
                if n_password == a_password:
                    input('성공적으로 비밀번호가 변경됨')
                    Account.password[Account.id.index(login_id)] = n_password
                    Main.manage_account()
                else:
                    input('비밀번호가 다릅니다.')
                    Main.continue_change(login_id)
            else:
                input('비밀번호가 다릅니다.')
                Main.continue_change(login_id)
        except:
            Main.continue_change(login_id)
        #기존 비밀번호, 새 비밀번호, 새 비밀번호 확인을 입력하여
        #기존비밀번호가 변경 전 비밀번호화 일치하고 새 비밀번호가 새 비밀번호 확인과 일치하면
        #새 비밀번호로 변경한다. 실패할 경우 왜 실패했는데 이유를 알려준다.
        #비밀번호는 최소 4자리, 최대 12자리의 영문과 숫자로 구성된다.
        #(반드시 숫 자, 영문이 같이 들어갈 필요는 없다. 대소문자는 구분한다.) 
    def delete_account():
        try:
            d_id = input('지우려는 아이디를 쓰시오 : ')
            if d_id in Account.id:
                if Main.login_type == 'Operator' and Account.type[Account.id.index(d_id)] == 'Operator' or Account.type[Account.id.index(d_id)] == 'Manager':
                    input('해당 id를 삭제할 권한이 없습니다.')
                    Main.delete_account()
                else:
                    choice6 = int(input("정말 삭제 하시겠습니까?\n1.예 2.아니오"))
                    if choice6 == 1:
                        del Account.name[Account.id.index(d_id)]
                        del Account.type[Account.id.index(d_id)]
                        del Account.phone_num[Account.id.index(d_id)]
                        del Account.birth[Account.id.index(d_id)]
                        del Account.id[Account.id.index(d_id)]
                        del Account.password[Account.id.index(d_id)]
                        del Account.books[Account.id.index(d_id)]
                        Main.manage_account()
                    elif choice6 == 2:
                        Main.manage_account()
                    else:
                        input('1, 2중에 고르세요.')
                        Main.delete_account()
            elif d_id == '.':
                Main.manage_account()
            else:
                input('해당 id는 존재하지 않습니다.')
                Main.delete_account()
        except:
            Main.delete_account()
    def check_id_list():
        counter = 0
        for i in Account.type:
            if Main.login_type == 'Operator' and i == "Manager":
                pass
            elif Main.login_type == 'Operator' and i == "Operator":
                pass
            else:
                print('id:',Account.id[counter],'/ 이름:',Account.name[counter],'/ 계정타입:',i,'/ 생년월일:',Account.birth[counter],'/ 전화번호:',Account.phone_num[counter],'/ 대여목록:',Account.books[counter])
            counter+=1
        Main.manage_account()
        #계정 조회시 조회할 수 있는 모든 계정목록을 보여준다.
        # 총 계정 수와 함께 계정별 ID, 이름, 계정타입, 생년월일, 전화번호, 대여중인 도서 목록을 노출한다.
        # 단, 관리자 계정은 운영자계정과 일반사용자 계정을 조회할 수 있고
        # 운영자 계정은 일반 사용자 계정만 조회할 수 있고
        #일반사용자 계정은 계정조회를 할 수 없다. 

    def check_book(page):
        # 시리얼 오름차순,총 도서권수,시리얼,이름,카테고리,저자,출판사,대여상태 출력
        if len(Book.num) % 10 == 0:
            whole_page = len(Book.num) / 10
        else:
            whole_page = int((len(Book.num) / 10) + 1)
        output_list = list(range(len(Book.num)))
        Main.book_list(output_list,whole_page,page)

    def book_list(list,whole_page,page):
        min =(page-1)*10
        max =page*10
        input_list = list[min:max]
        try:
            for m in input_list:
                print(Book.num[m],Book.name[m],Book.category[m],Book.writer[m],Book.publisher[m],Book.status[m])
                # 10개씩 노출, 그보다많으면 리스트를 123 순으로 나눠서 조회 / 메뉴는 <이전목록 >다음목록 f검색,0~10000까지
        except:
            pass
        print('총 도서 권수 : %s / 총 페이지 : %s / 현재 페이지 : %s' %(len(Book.num),whole_page,page))
        choice9 = input('<.이전목록 >.다음목록 f.페이지 검색 : ')
        if choice9 == '<' and page == 1:
            input('첫페이지입니다.')
            Main.book_list(list,whole_page,page)
        elif choice9 == '<':
            page -= 1
            min -=10
            max -=10
            Main.book_list(list,whole_page,page)
        elif choice9 == '>' and page == whole_page:
            input('마지막 페이지 입니다.')
            Main.book_list(list,whole_page,page)
        elif choice9 == '>':
            page += 1
            min +=10
            max +=10
            Main.book_list(list,whole_page,page)
        elif choice9 == 'f':
            search = input('찾으려는 문자열을 입력해주세요 : ')
            search_list = []
            counter = 0
            for i in Book.name:
                if search in i:
                    search_list.append(counter)
                counter +=1
            counter = 0
            for i in Book.category:
                if search in i and counter not in search_list:
                    search_list.append(counter)
                counter+=1
            counter = 0
            for i in Book.writer:
                if search in i and counter not in search_list:
                    search_list.append(counter)
                counter+=1
            counter = 0
            for i in Book.publisher:
                if search in i and counter not in search_list:
                    search_list.append(counter)
                counter += 1
            input('검색 종료')
            Main.book_list(search_list,whole_page,page)
                   
        elif choice9 == '.':
            Main.show_menu()
        else:
            Main.book_list(list,whole_page,page)
                
                
                

    # 도서검색, 조건은 문자열을 포함한 이름,카테고리,저자,출판사 노출
    # 10개씩 노출,
    def generate_book(): #운영자만 등록,삭제가능 / 등록시 이름 카테고리,저자,출판사를 입력,대여가능이 기본값
        try:
            choice11 = int(input('1.등록하기 2.뒤로가기 : '))
            if choice11 == 1:
                name,cate,writ,publ = input('등록할 도서의 이름, 카테고리, 저자, 출판사를 순서대로 쓰시오\n"/"로 구분함 : ').split('/')
                Book.num.append(Book.number)
                Book.number +=1
                Book.name.append(name)
                Book.category.append(cate)
                Book.writer.append(writ)
                Book.publisher.append(publ)
                Book.status.append('대여가능')
                Main.manage_book()
            elif choice11 == 2:
                Main.manage_book()
            else:
                Main.generate_book()
        except:
            input('양식에 맞게 기재해 주세요.')
            Main.generate_book()
    def delete_book():#시리얼번호를 입력하여 삭제한다,대여상태상관없이삭제가,번호가없으면'책이 존재하지 않습니다.'출력
        try:
            choice12 = int(input('1.삭제하기 2.뒤로가기 : '))
            if choice12 == 1:
                num = input('삭제하려는 도서의 시리얼 번호를 입력 : ')
                if num == '.':
                    Main.manage_book()
                else:
                    pass
                num = int(num)
                if num in Book.num:
                    choice8 = int(input('정말 삭제하시겠습니까?\n1.네 2.아니오 : '))
                    if choice8 == 1:
                        d_num = Book.num.index(num)
                        del Book.num[d_num]
                        del Book.name[d_num]
                        del Book.category[d_num]
                        del Book.writer[d_num]
                        del Book.publisher[d_num]
                        del Book.status[d_num]
                        input('성공적으로 삭제 되었습니다.')
                        Main.delete_book()
                    elif choice8 == 2:
                        Main.delete_book()
                    else:
                        input('1,2중에 고르시기 바랍니다.')
                        Main.delete_book()
                else:
                    input('책이 존재하지 않습니다.')
                    Main.delete_book()
            else:
                Main.manage_book()
        except:
            Main.delete_book()

Main.login()
#동작 시나리오
# 아이디,패스워드순으로 입력,로그인
#로그인에 성공하면  메인메뉴 노출, 실패하면 아이디, 패스워드 재입력  계정에 맞는 메뉴를 노출한다.
#사용자가 메뉴의 번호를 입력하면 하위메뉴를 노출하거나 하위메뉴가 없으 면 해당 메뉴의 기능을 실행한다.
#모든 메뉴의 단계에서 .을 입력하면 상위 메뉴로 돌아갈 수 있어야 한다.
#메뉴의 입력은 한글자의 숫자, 영문, 특수문자로 입력받고 대소문자는 구분 하지 않는다. 
