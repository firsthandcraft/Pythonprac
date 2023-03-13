#프로그래밍 시작하기 in Python
#
#코멘트
print('hello')
print("hello Wolrd!")
#run 하면 결과창에 hello hello Wolrd! 가 나온다.

#자료형 개요 dataType
#1. 숫자 정수 integer // 소수 FloatingPoint 가 있다.
#정수와 소수'2.0' 문자열 '2' 는 다르다.
#2. 자료형
#문자열
#3.불린 참 거짓값을 알려

#추상화 개요
#복잡한 내용을 숨기고 주요기능만 신경쓰자
#추상화 종류 변수 , 함수 ,객체가 있다.
#변수 Variable (값저장)
x=235
y=200
print("----- 추상화 개요 Part -----")
print(x+y)
#변수 만들기
print("----- 변수 지정연산자-----")
burgerPrice=4990 #지정연산자 오른쪽에서 왼쪽으로 =등호로 지정한다.
friesPrice=1490
drinkPrice=1250
print(burgerPrice)
print(burgerPrice*2)
print(burgerPrice+friesPrice)
#함수 - 명령을 저장

print("----- 내장함수 : 이미 저장되어있는 함수 print같은거 -----")
print("함수 정의 하기 ")
def hello():
    print("Hello")
    print("Welcome to handcraft")

hello()
hello()
hello()

#파라미터
