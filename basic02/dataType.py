#01숫자형
#덧셈
print(4+7)#11
print(4+7.0)#파이썬는 정수형보다 소수형이 쎄다 #11.0
#뺄셈
print(2-4)#-2
#곱셈
print(5*3)#15
#나머지
print(7%3)#1
#거듭제곱
print(2.0 ** 3.0)#8.0
#나눗셈
print(7/2)#3.5
print(7.0/2)#3.5
print(float(int(42 / 5)))#42를 5로 나누면 8.4가 나옵니다. int(8.4)는 8.4의 소수 부분을 빼서 8이 되고, float(8)은 8에 소수 부분을 붙여서 8.0이 나옵니다.
#사칙연산
print(2+3*2)#8

#02숫자형 연산 심화
#floor division(버림 나눗셈
print(8//3) #2.6666이 2로 나온다.
print(8.0//3)#2.0 소수라서 소수로 나온다.
print(round(3.1415926535))#3
print(round(3.1415926535,2))#3.14 소수점 2째 자리까지

#03문자열
#키보드로 쓸수있는 자료형
#' '따옴표로 된다.
#" "또는 큰따옴표로로
print("hello"*3)#hellohellohello
print("I\'m \"excited\" to learn Python!")#I'm "excited" to learn Python!

#실습
#print 함수와 문자열 개념을 이용해서 다음 두 문장을 출력하세요.

# '응답하라 1988'은 많은 시청자들에게 사랑을 받은 드라마예요.
# 데카르트는 "나는 생각한다. 고로 존재한다."라고 말했다.
print("\'응답하라 1988\'은 많은 시청자들에게 사랑을 받은 드라마예요.")
print("데카르트는 \"나는 생각한다. 고로 존재한다.\"라고 말했다.")
#실습
# print 함수와 문자열 개념을 이용해서 다음 문장을 출력하세요.
# 영화 '신세계'에서 "드루와~"라는 대사가 유행했다.
print("영화 \'신세계\'에서 \"드루와~\"라는 대사가 유행했다.")

#형변환 TypeConversion TypeCasting
print(int(3.8))#3
print(float(3))#3.0
print(int("2")+int("5"))#정수형으로 바꿔서 7
print(float("1.1")+float("2.5"))#3.6
print(str(2)+str(5))#문자열25
age=7
#age가 정수라 오류가 나온다.print("제 나이는"+age+"살입니다.")
print("제 나이는"+str(age)+"살입니다.")

# format을 이용한 문자열 포맷팅
#오늘은 2019년 10월 29일입니다.
year=2019
month=10
day=29
print("오늘은"+str(year)+"년"+str(month)+"월"+str(day)+"알압니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day))
dateString="오늘은 {}년 {}월 {}일입니다."
print(dateString.format(year,month,day))
#배열처럼 순서대로 나온다.
print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성","유재석","빌 게이츠"))
num_1=1
num_2=3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1,num_2,num_1/num_2))
#소수점 2째 자리 까지 올리기
print("{0} 나누기 {1}은 {2:.4f}입니다.".format(num_1,num_2,num_1/num_2))
#정수
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1,num_2,num_1/num_2))

#문자열 포맷팅을 하는 다양한 방식 format메소드
name = "최지웅"
age = 32
print("제 이름은 %s이고 %d살입니다." % (name, age))#제 이름은 최지웅이고 32살입니다.
#이제는 잘 쓰지 않는, 옛날 방식입니다. %s, %d와 같은 '포맷 스트링'이라는 것을 사용하는데요.
#C나 자바 등 많은 언어들에서 이와 유사한 방식으로 문자열 포맷팅을 합니다.
print("제 이름은 {}이고 {}살입니다.".format(name, age))
#2020년 2월 기준, 파이썬 커뮤니티에서 가장 많이 사용하는 방식입니다. 그래서 이걸 최우선적으로 가르쳐 드렸습니다.
print(f"제 이름은 {name}이고 {age}살입니다.")
#파이썬 버전 3.6부터 새롭게 나온 방식입니다. 아직 완전히 대중화되지는 않았지만 좋은 평을 받고 있기 때문에, 곧 f-string을 더 많이 사용하는 추세로 갈 수 있습니다.


#실습
# 문자열 포맷팅의 개념을 이용하여 아래의 문장들을 출력하세요.
# 1시간에 5달러 벌었습니다.
# 5시간에 25달러 벌었습니다.
# 1시간에 5710.8원 벌었습니다.
# 5시간에 28554.0원 벌었습니다.

wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5,wage * 5,"달러"))  # 코드를 채워 넣으세요.
print("{}시간에 %d달러 벌었습니다.".format(5) %(wage*5))
print(f"5시간에 {wage*5}달러 벌었습니다.")
print("{2}시간에 {1}{0} 벌었습니다.".format("달러",wage*5,5))
# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1,wage * 1 * exchange_rate,"원"))  # 코드를 채워 넣으세요.
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * exchange_rate * 5, "원"))  # 코드를 채워 넣으세요.
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))

#불대수
#일상적 논리를 수학적으로 표현한것
#명제가 정확해야한다.
# T && T = T
# T&& F = F
# T || F = T

#불린형 Boolean
print(True)#True
print(False)#False
print(True and True)#True
print(True and False)#False
print(True or True)#True
print(False or True)#True
print(not True)#False
print(not False)#True
print("----- 숫자형 불린 -----")
print(2>1)#T
print(2<1)#F
print(3 >= 2)#T
print(3 <= 3)#T
print(2 == 1)#F
print(2 != 1)#T
print("----- 문자형 불린 -----")
print("Hello"=="Hello")#T
print("Hello"!="Hello")#F
print("----- 복합형 불린 -----")
print(2>1 and "Hello"=="Hello")#T
print(7 == 7 or (4 > 3 and 12 > 10)) #T
x=3
print(x >4 or not (x < 2 or x == 3)) #F or F => F
print("----- 이중 불린 -----")
print(not not True)#T
print(not not False)#F

