class User:
    # 클래스 변수: 모든 인스턴스가 공유하는 변수
    count = 0

    def __init__(self, name, email, password): # 인스턴스 형성과 동시에 호출
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def __str__(self): # print 사용시 자동으로 호출
        return f'안녕하세요, 저는 {self.name}입니다.'

    def say_hello(self):
        print(f'Hi! I am {self.name}!')

    def check_name(self, name):
        return self.name == name

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print('Login success!')
        else:
            print('Login failed!')

def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')

    return wrapper

# 데코레이터
# print_hello 함수를 add_print_to로 꾸며주라는 뜻
@add_print_to
def print_hello():
    print('안녕하세요!')

user1 = User('김대위', 'captain@codeit.kr', '12345')
user2 = User('강영훈', 'younghoon@codeit.kr', '98765')
user3 = User('최지웅', 'jiwoong@codeit.kr', '78945')

print(user1)

user1.count = 10 # user1 인스턴스에 count 변수 추가

print(User.count)
print(user1.count)

print_hello()