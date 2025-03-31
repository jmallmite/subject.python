#########################
# capacity에 5를 저장
# array 리스트에 None 5개를 저장
# size에 0을 저장
# isFull 함수 정의, size와 capacity 비교 연산, return을 통해 함수 실행 결과 반환
# insert 함수를 정의, pos(삽입할 위치)와 e(삽입할 값)을 매개변수로 받는다.
# size를 전역변수로 선언한다
# 만약 ifFull이 not 이라면 그리고 pos가 0 보다 크거나 같고 size 보다 작거나 같다면:
# size 부터 pos까지 -1씩 감소하며 i에 값이 들어간다.
# if 문이 실행 된다면 for 문이 실행된다.
# array 리스트 i 번째에는 i-1 번째로  씌워지게 된다 -> 배열이 한 칸씩 뒤로 이동하게 된다.
# array pos 번째에는 e 값이 들어간다.
# size에는 1이 증가한다.
# else문 은 if 문의 조건이 맞지 않을때 실행된다.
# print 안의 값이 출력되고 프로그램은 종료된다,
# if __name__ == "__main__": 으로 프로그램 시작
# 초기 size 변수의 값은 0, 초기 capacity 변수의 값은 5
# insert 함수 호출 1은 if 문을 통해 size 값 1증가, ifFull은 capacity 값은 5이기 때문에 False 가 나온다. f를 통해 변수와 함수의 값을 넣어준다., 현재 array 에는 [10, None, None, None, None] 이 된다.
# insert 호출 2는 현재 size변수 값은 2이고, size와 capcaity 비교 결과는 False 이다. 가 나오고 array[i] = array[i-1] 을 통해 기존에 있던 i-1번째의 10이 i의 위치로 이동되면서 0번째애는 20이라는 데이터가 들어가고 i에는 20이 들어간다.
# 호출 3은 1번째 위치에 30이라는 데이터가 들어가고 그 자리에 있던 10이라는 데이터는 if 문이 실행됨에 따라 오른른쪽으로 밀려나게 된다.
# 호출 4는 2번쨰 위치에 40이 들어가고 10은 밀려난다.
# 호출 5는 3번째 위치에 50이 들어가고 10은 4번째 위치에 3번째 위치의 데이터가 들어간다., if 문 size += 1을 통해 1씩 증가되여 size 변수의 값은 5 이고 capacity의 값도 5이므로 비교결과는 True가 나온다.


#########################


capacity = 5 # 전역 변수
array = [None] * capacity # 전역 변수
size = 0 # 전역 변수 

def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환 

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]  # 한 칸씩 뒤로 옮김
        array[pos] = e
        size += 1  # 요소의 수가 하나 증가
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

if __name__ == "__main__":
    print("초기 size 변수의 값은", size)
    print("초기 capacity 변수의 값은", capacity) 
    print("=======================================") 

    # insert함수 호출 1
    insert(0, 10)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity])
    print("=======================================") 

    # insert함수 호출 2
    insert(0, 20)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity])
    print("=======================================") 

    # insert함수 호출 3
    insert(1, 30)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity]) 
    print("=======================================") 

    # insert함수 호출 4
    insert(2, 40)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity]) 
    print("=======================================") 

    # insert함수 호출 5
    insert(3, 50)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity])
    print("=======================================") 