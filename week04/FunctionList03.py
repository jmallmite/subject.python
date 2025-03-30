##############################
# capacity에 5를 저장
# array에 [None이 5개 저장]
# size 에 0을 저장
# def로 isFull을 함수로 정의 size ==capacity 이면 True, 아니면 False를 반환
# def로 insert를 함수로 정의 하고 pose 위치에 e를 삽입한다.
# global을 통해 size를 전역 변수로 만든다
# 만약 size == capacity가 틀렸을 경우 그리고 pos가 0 이상, size가 pos 보다 크거나 같을 경우 array라는 리스트에 pos 번째 위치에 e값을 넣는다.
# 그리고 size 에는 1을 증가시키도록 한다.
# if 이외의 경우는 else로 print에서 리스트 overflow 또는 유효하지 않은 삽입 위치가 출력되고 exit()로 프로그램 종료가 된다
# if __name__ == "__main__": 로 프로그램이 시작된다.
# 1번째는는 size 변수의 값은 0, 초기 capacity의 값은 5
# 현재 size 값: 1, size와 capapcity 값은 같은가에 대해서는 False, 현재 array는 array 배열의 0부터 capacity 끝까지를 출력한다, 시작하는 위치인 0번째 위치에는 insert 0에 10을 넣는다
# 2번째도 0번째에 20을 넣는다
# 3번째는 1에 30을 넣는다
# 4번째는 2에 40을 넣는다
# 5번째는 3에 50을 넣고 size 값이 capacity 값과 같아지는 순간으로 true가 나온다.

##############################
capacity = 5 # 전역 변수
array = [None] * capacity # 전역 변수
size = 0 # 전역 변수 

def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환 

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull() and 0 <= pos <= size:
        array[pos] = e
        size += 1  # 요소의 수가 하나 증가
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

if __name__ == "__main__":
    print("초기 size 변수의 값은", size)
    print("초기 capacity 변수의 값은", capacity) 

    # insert함수 호출 1
    insert(0, 10)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity])


    # insert함수 호출 2
    insert(0, 20)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity])

    # insert함수 호출 3
    insert(1, 30)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity]) 

    # insert함수 호출 4
    insert(2, 40)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity]) 

    # insert함수 호출 5
    insert(3, 50)
    print("현재 size변수의 값은?", size)
    print("현재 size와 capacity의 값은 같은가?", isFull())
    print("현재 array", array[0:capacity])