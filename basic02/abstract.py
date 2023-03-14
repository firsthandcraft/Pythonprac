#01. 변수 제대로 이해하기
#지정연산자 오른쪽 값을 왼ㅉ고에 대입
name="김현승"
x=7
x= x + 1
print(x) #8

#02함수의 실행 순서
def square(x):
    return x * x
print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

#03.return문 제대로 이해하기
#함수가 무언가 값을 돌려주는 것 , 함수를 즉시 종료 시켜준다.
def suqare(x):
    return x * x
    print("함수 끝")# return으로 끝나서 죽은 코드 이다.

print(square(4))#16

#04. return과 print의 차이
print("----- return과 print의 차이 -----")
def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print_square(3) #print_square x에 3이 지정-> 후 계산되어 9
print(get_square(3)) #get_square에 3이 지정 계산됨 = 9-> print를 통해 9가 출력
print("-----")
print(print_square(3)) #9  none
# #print_square에 3이 넘어가고 print되어 9가 되고-> return 값이 없어 none 이 출력된다.

#05. 옵셔널 파라미터
print("----- 옵셔널 파라미터 -----")

#파라미터에게 '기본값(default value)'을 설정할 수 있는데요.
# 기본값을 설정해 두면, 함수를 호출할 때 꼭 파라미터에 값을 안 넘겨 줘도 됩니다.
# 이런 파라미터를 '옵셔널 파라미터(optional parameter)'라고 합니다.
# 필수로 넘겨 줄 필요가 없으니까 '옵셔널'이라고 하는 거죠.

def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
#내 이름은 코드잇 // 나이는 1살 // 국적은 미국
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우
#내 이름은 코드잇 // 나이는 1살 // 국적은 한국

#참고로 옵셔널 파라미터는 모두 마지막에 있어야 합니다.
# 아래처럼 옵셔널 파라미터를 중간에 넣으면 오류가 나옵니다!
# def myself(name, nationality="한국", age):
#     print("내 이름은 {}".format(name))
#     print("나이는 {}살".format(age))
#     print("국적은 {}".format(nationality))
#
#
# myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
# print()
# myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때

#06. Syntactic Sugar
#자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법을 'syntactic sugar'라고 합니다.
# 다음 두 줄은 같습니다
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7

#08. scope
print("----- scope -----")
def my_function():
    r = 3
    print(r)

my_function()#3
#print(r)    #r 라는 이름이 정의 된적이 없다. 로컬 변수 r이 유효하지 않은 범위에 정의 해서
r1= 6 #글로벌 변수
def my_function():
    r1 = 3 #로컬변수
    print(r1)#3

my_function()
print(r1)#6

#scope정리
    #scope : 변수가 사용가능한 범위
    #로컬변수 : 변수를 정의한 함수내에서만 사용 가능
    #글로벌 변수 : 모든 곳에서 사용 가능
    #함수에서 변수를 사용하, 로컬 변수를 먼저 찾고 나서 글로벌 변수를 찾음

#10. 상수 constant
#상수는 모든 글자가 대문자로 만들기
#대문자로 만들어도 값은 수정이 가능하다. 상수값은 대문자가 매너 이다.
print("----- 상수 -----")
PI = 3.14  #원주율 '파이'
def calculate_area(r):
    return PI * r * r

radius = 4 #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
#반지름이 4면, 넓이는 50.24

radius = 6 #반지름
print("반지름이 {}면, 넓이는 {:.2f}".format(radius, calculate_area(radius)))
#반지름이 4면, 넓이는 50.24

radius = 7 #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
#반지름이 4면, 넓이는 50.24

#11.스타일
print("----- 스타일 -----")
#버거를 주문할 시에 혜택차원에서 음료수 및 감자튀김을 받을 수 있다.
#버거를 주문하면 음료수와 감자튀김은 서비스 이다.
# 간결하게 쓰는 코드가 좋다.
print(6.28 * 4)
print(3.14 * 4)
print(6.28 * 8)
print(3.14 * 8)

#간결하게 정리 하면
PI1= 3.14
radius=4
print(6.28 * radius)
print(PI1 * radius)
print(6.28 * (radius * 2))
print(3.14 * (radius * 2))

#공식으로 정리 하면
#   반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI1 * r
#반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI1 * r * r
radius=4
print(calculate_circumference(radius))
print(calculate_area(radius))

# 실습
print("---- 실습 -----")
#짝수 홀수
#어떤 수가 짝수인지 홀수인지 판단해 주는 함수 is_evenly_divisible를 쓰세요.
# is_evenly_divisible는 number(수)를 파라미터로 받습니다. 짝수인 경우, 즉 number가 2로 나누어 떨어질 경우에는 True를 리턴해 줍니다. 홀수인 경우, 즉 number가 2로 나누어 떨어지지 않을 경우에는 False를 리턴해 줍니다.
# 함수 안에는 print문이 아닌, return문을 사용해야 합니다. 그리고 참고로 불린 개념을 잘 사용하면, 함수 단 한 줄로 작성할 수 있습니다!

def is_evenly_divisible(number):
    # 여기에 코드를 작성하세요
    return (number % 2 == 0)
# 테스트 코드
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))
# False
# False
# True
# True
# False

#실습
#거스름돈 계산기
# 현명하게 거스름돈을 계산해 주는 프로그램을 만들려고 합니다. 예를 들어 33,000원짜리 물건을 사기 위해 100,000원을 냈다면,
#
# 50,000원 1장
# 10,000원 1장
# 5,000원 1장
# 1,000원 2장
# 이런 식으로 '가장 적은 수'의 지폐를 거슬러 주는 것입니다. 방금 같은 경우에는 총 5장을 거슬러 준 거죠.
# 우리는 calculate_change라는 함수를 작성하려고 하는데요. 이 함수는 지불한 금액을 나타내는 payment와 물건의 가격을 나타내는 cost를 파라미터로 받습니다.
# 아래의 코드에 이어서 깔끔하게 프로그램을 작성해 보세요.
def calculate_change(payment, cost):
    # 여기에 코드를 작성하세요
    change = payment - cost

    fifty_count = change // 50000  # 50,000원 지폐//버림 나눗셈 사용
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐
    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))

# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
# 50000원 지폐: 1장
# 10000원 지폐: 1장
# 5000원 지폐: 1장
# 1000원 지폐: 2장
#
# 50000원 지폐: 2장
# 10000원 지폐: 2장
# 5000원 지폐: 0장
# 1000원 지폐: 2장







