#while 반복문
# while 조건 부분true:
#     수행 부분분
i = 1
while i <= 3:
    print("나눈 잘생김")
    i += 1

#실습
# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력해 보세요.
# 출력 결과는 아래와 같이 나와야 합니다.
# 2
# 4
# 6
# 8
# .
# .
# .
# 94
# 96
# 98
# 100

i = 1
while i <= 100 :
    print(i * 2)
    i += 1

#실습
#while문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
#115
i = 100
while i % 23 != 0:
    i += 1
print(i)

#05. if문 개념
# if 조건 부분 (불린 값으로 계산되는 식):
#     수행부분
temperature = 16
if temperature <= 10:
    print("자켓을 입니다.")
else:
    print("자켓을 입지 않는다.")

#06.elif문
# if 조건 부분:
#     수행 부분
# else:
#   if 수행부분

# if 점수가 90점 이상이다:
#     A를 준다
# elif 점수가 80점 이상이다:
#     B를 준다
# else:
#     C를 준다

#실습
# 학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.
#
# 이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.
#
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 여기에 코드를 작성하세요
    if total >= 90 :
        print("A: 90점 이상")
    elif total >= 80:
        print("B: 80점 이상")
    elif total >= 70:
        print("C: 70점 이상")
    elif total >= 60:
        print("D: 60점 이상")
    else:
        print("F: 60점 미만")
# 테스트 코드
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)
# B
# F
# D
# A

#실습
# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
# 예를 들어서 16은 8의 배수이지만 12의 배수가 아니니까 조건에 부합합니다. 하지만 48은 8의 배수이면서 12의 배수이기도 해서 조건에 부합하지 않습니다.
# 실행하면 콘솔에 아래와 같이 출력되어야 합니다.
# 8
# 16
# 32
# 40
# 56
# 64
# 80
# 88

i = 0
while i <= 100:
    if i % 8 == 0 and i % 12 != 0 :
        print(i)

    i += 1

#실습
# 10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.
# 333167
i = 1
total = 0
while i < 1000 :
    if i % 2 == 0 or i % 3 == 0 :
        total += i
    i += 1

print(total)

#실습
#11.약수 찾기
# 정수 n의 약수는 n을 나누었을 때 나누어 떨어지는 수입니다. 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야 하는 거죠.
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요. 아래처럼 콘솔에 출력되어야 합니다.
# 1
# 2
# 3
# 4
# 5
# 6
# 8
# 10
# 12
# 15
# 20
# 24
# 30
# 40
# 60
# 120
# 120의 약수는 총 16개입니다.
print("-------- 약수 --------")
def divisor(num) :
    i = 1
    count =0
    while i <= num :
        if num % i == 0 :
            print(i)
            count += 1
        i += 1
    print("{}의 약수는 총 {}개입니다.".format(num,count))

divisor(120)

#실습 설명
# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만원을 받았습니다. 하지만 바둑 외에는 아는 게 없으니, 이웃 어른들에게 이 돈으로 무엇을 해야 할지 물어보기로 하였습니다.
# 은행에서 근무하는 동일 아저씨는 은행에 돈을 맡겨서 매년 이자로 12%씩 받는 것을 추천하셨습니다. 1년 후인 1989년에는 5,000만원의 12% 이자인 600만원이 더해져 5,600만원이 된다고 하면서요.
# 이 이야기를 들은 미란 아주머니는 고작 12% 때문에 생돈을 은행에 넣느냐며, 얼마 전 지어진 은마아파트를 사라고 추천하셨습니다. 당시 은마아파트의 매매가는 5,000만원이었죠.
# 2016년 기준 은마아파트의 매매가는 11억원인데요. 1988년 은행에 5,000만원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여, 동일 아저씨와 미란 아주머니 중 누구의 말을 듣는 것이 좋았을지 판단해 보세요. 2016년 은행에 얼마가 있을지는 꼭 while문을 사용해서 계산해 주세요!
# 2016년에 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.가 출력되도록 하세요. 반대로 은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다.가 출력되도록 하세요. 여기서는 꼭 if문을 사용해 주세요!
#정답
#94193324원 차이로 동일 아저씨 말씀이 맞습니다.
year = 1988 #년도
print(1988-2016)
INTEREST = 1.12
reward = 5000
difference = 0
while year < 2016 :
    reward = INTEREST * reward
    year += 1

if reward > 110000:
    difference = reward - 110000
    difference = difference * 10000
    print("{:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.".format(difference))

else :
    difference = 110000 - reward
    difference = difference * 10000
    print("{:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.".format(difference))

#실습 13. 피보나치 수열
# 실습 설명
# 피보나치 수열(Fibonacci Sequence)라고 들어 보셨나요?
# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다. 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다. 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며, 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.
# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요.
print("----- 피보나치 수열 -----")
i = 1
current = 1
previous = 1
result = 1
print(previous)
print(current)
while i <= 48:

    previous = current
    current = result
    # print("previous" + str(previous))
    # print("current" + str(current))
    result = current + previous
    # print("result" + str(result))
    print(result)
    i += 1

#정답 1
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1

# 정답 2
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1


#실습 구구단
# while문을 사용해서 구구단 프로그램을 만들어 봅시다. 실행하면 아래와 같은 결과물이 출력되어야 합니다.
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .
# .
# .
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81
i = 1
j = 1
while i <= 9 :
    # print("i = "+str(i))
    j = 1
    while j <= 9 :
        print("{} * {} = {}".format(i,j,i*j))
        # print("j = "+str(j))
        j += 1
    i += 1

#15. 제어문 꿀팁
# break문
# 만약 while문의 조건 부분과 상관 없이 반복문에서 나오고 싶으면, break문을 사용하면 됩니다.
print("----- break문 -----")
i = 100
while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i = i + 1

print(i)#115

# continue문
# 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문을 쓰면 됩니다.
print("----- continue문 -----")

i = 0

while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)
# 2
# 4
# 6
# 8
# 10
# 12
# 14