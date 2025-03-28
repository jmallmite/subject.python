######################################
# 프로그램 설명
# capacity를 통해 10을 저장
# array라는 저장 공간에 리스트 None을 10번 하여 저장
# size 에 0을 저장
# def를 통해 isfull이 함수 임을 정의 하고 매개변수가 없음으로 size와 capacity의 비교연산 결과를 반환한다
# if __name__ == "main__": 을 통해 프로그램이 시작
# print를 통해 현재 size 변수의 값은 ? 이 출력되고 size에서서 0이라는 값이 호출된다.
# print를 통해 현재 capacity 변수의 값은 ? 이 출력되고 capacit에서 10이라는 값이 호출된다.
# print를 통해 현재의 size와 capacity의 값은 같은가? 가 출력되고 isFull에서 size와 capacity의 비교 연산을 통해 0과10은 같지 않으므로 False가 출력된다.
######################################

capacity = 10                    # 전역 변수
array = [None]*capacity          # 전역 변수
size = 0                         # 전역 변수

# 리스트의 연산: 일반 함수
def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

# 프로그램의 시작
if __name__ == "__main__":
    print("현재 size 변수의 값은 ? ", size)
    print("현재 capacity 변수의 값은 ? ", capacity)   
    print("현재의 size와 capacity의 값은 같은가?", isFull())
