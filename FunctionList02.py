#####################################
# capacity에 5를 저장한다
# array의 리스트에 None이 5개임을 저장한다.
# size에 0을 저장한다.
# def로 isFull이 함수 임을 정의한다
# size==capacity의 결과를 return을 통해 반환한다.
# size 앞에 global을 붙혀서 size가 전역변수(함수 안팎을 막론하고 프로그램 어디든지 접근할 수 있는 변수) 임을 정의한다.
# size += 1 은 size의 값에 1을 증가시키는 연산으로 만약 리스트가 가득 차지 않았다면 size에 1을 더한다.(not은 예약어)
# 만약 리스트가 가득 차지 않은것의 또다른 경우로 print의 내용이 출력된다.
# exit() 는 프로그램을 종료하는 함수
# if __name__ == "__main__": 을 통해 프로그램이 시작되고 print 안에 값이 출력 그리고 size, capacity의 값인 0하고 5도 각각 호출되어 출력된다.
# insert 함수에서 size는 size와 capacity가 서로 값이 맞지 않기 때문에 size에 1이 증가되어 되어 나타나고 isFull()은 false가 출력된다.
# 그렇게 서로 값이 맞지 않은 관계로 size는 1이 증가되고 idFull()은 False가 나오게 된다
# 5번째는 size와 capacity가 값이 같아지는 구간으로 size 변수의 값은 5가 나오고 size와 capacity의 값이 같은가에 대해서는 True가 나온다.
# 6번째는 이미 size와 capacity의 값이 같기 때문에 else 에서 print 안의 리스트 overflow 또는 유효하지 않은 삽입 위치라는 값이 출력된다.

#####################################


capacity = 5                        # 전역 변수
array = [None]*capacity              # 전역 변수
size = 0                             # 전역 변수

# 리스트의 연산: 일반 함수
def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

def insert():
    global size  # size는 전역변수
    if not isFull():
        size += 1  # size변수의 값에 +1   // size = size+1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

# 프로그램의 시작
if __name__ == "__main__":
    print("(초기값) 현재 size 변수의 값은 ? ", size)   
    print("(초기값) 현재 capacity 변수의 값은 ? ", capacity)   
    print("----------------------------------------------------")   

    # insert함수 호출 1
    insert()
    print("현재의 size 변수의 값은? ", size)         
    print("현재의 size와 capacity의 값은 같은가?", isFull())         
    print("----------------------------------------------------")   

    # insert함수 호출 2
    insert()
    print("현재의 size 변수의 값은? ", size)         
    print("현재의 size와 capacity의 값은 같은가?", isFull())         
    print("----------------------------------------------------")   

    # insert함수 호출 3
    insert()
    print("현재의 size 변수의 값은? ", size)         
    print("현재의 size와 capacity의 값은 같은가?", isFull())         
    print("----------------------------------------------------")   

    # insert함수 호출 4
    insert()
    print("현재의 size 변수의 값은? ", size)         
    print("현재의 size와 capacity의 값은 같은가?", isFull())         
    print("----------------------------------------------------")   

    # insert함수 호출 5
    insert()
    print("현재의 size 변수의 값은? ", size)         
    print("현재의 size와 capacity의 값은 같은가?", isFull())         
    print("----------------------------------------------------")   

    # insert함수 호출 6
    insert()
    print("현재의 size 변수의 값은? ", size)         
    print("현재의 size와 capacity의 값은 같은가?", isFull())         
    print("----------------------------------------------------")   


