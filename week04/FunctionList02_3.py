###################################
# 파이썬 print함수 사용법
# print함수 : 기본 사용법
# print함수 : f옵션을 이용한 방법
# country라는 변수에 문자열 Korea를 저장
# welcome to 라는 문자열과 country 라는 변수를 나란히 출력
# size에 정수형 데이터 10을 저장하고 print로 My Size와 size 값을 출력
# name에 문자열 Alice를 저장하고 age에는 숫자 25를 저장
# {}은 변수 값을 넣는 포맷팅 기호, (포멧팅: 문자열 안에 값을 넣어서, 문장을 완성하는 과정)/ 문자열은 따옴표로 감싼 글자
# f는 중괄호 안에 있는 변수를 실제 내장되어 있는 값으로 바꿔주는 역할을 한다.
###################################

country = "Korea"
print("welcome to ", country)
print("=====================================")

size = 10
print("My Size ", size)
print("=====================================")

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
print("=====================================")