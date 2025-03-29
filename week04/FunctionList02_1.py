######
# capacity에 5저장
# array 배열 변수(리스트)에 None을 5개 만든다.
# size에 5를 저장
# def: 함수 정의, isFull: 함수 이름, (): 매개변수 없음
# size == capacity -> 비교 연산 결과를 바로 반환
# def insert 함수를 생성하고 pos에 e 값을 삽입
# global로 size 전역변수를 선언
# 만약 isFull():이 성립되지 않을 경우 array의 pos 번째 위치에 e 값을 넣는다
# 또다른 경우로 isFull(): 이 성립될 경우 print 의 값이 출력된다.
# 프로그램 종료
# if __name__ == "__main__": 프로그램 시작이 되고 size 변수의 값은? 0, 현재 capacity 변수의 값은? 에 5가 출력된다.
# 현재 array 에는 array[0:capacity] -> 배열에서 0부터 capacity 끝까지를 출력하고 0번째 위치에 10을 넣는다. 나머지는 부분은 None
# 현재 array 에는 1번째 위치에 20을 넣는다
# 현재 array 에는 2번째 위치에 30을 넣는다
# 현재 array 에는 3번째 위치에 40을 넣는다
# 현재 array 에는 0번째 위치에 10을 덮어쓰기로 50이 들어간다.
######


capacity = 5                        # 전역 변수
array = [None]*capacity              # 전역 변수
size = 0                             # 전역 변수

# 리스트의 연산: 일반 함수
def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull():
        array[pos] = e   # array[0] = 10
        size += 1  # size변수의 값에 +1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

# 프로그램의 시작
if __name__ == "__main__":
    print("(초기값) 현재 size 변수의 값은 ? ", size)   
    print("(초기값) 현재 capacity 변수의 값은 ? ", capacity)   
    print("----------------------------------------------------")   

    # insert함수 호출 1
    insert(0, 10)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 2
    insert(1, 20)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 3
    insert(2, 30)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 4
    insert(3, 40)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 5
    insert(0, 50)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    
    # insert함수 호출 6
    insert(0, 60)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   