"""
1. Contact 클래스 생성하고 출력 확인
2. 사용자 입력 받아 확인
3. 메인메뉴 구성
4. 연락처 입력 받기
5. 연락처 출력하기
6. 연락처 삭제하기
"""
class Contact:
    def __init__(self, name, phone_number, email, addr):
        # (1) 멤버변수들 초기화
        pass

    def print_info(self):
        # (2) 멤버변수들 출력
        pass


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (3)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    # Contact 객체를 생성하고
    # 생성된 객체 리턴
    return

def print_contact(contact_list):
    # (4)
    # 각 contact_list 의 요소인 Contact 객체의 print_info() 호출
    pass

def delete_contact(contact_list, name):
    # (5)
    # 해당이름과 같은 요소를 찾아서 삭제
    pass

def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(contact_list,name)


if __name__ == "__main__":
    run()
