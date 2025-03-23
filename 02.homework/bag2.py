def contains(bag, e):    # 가방안에 찾는 물건이 있는지 알려주는 함수
    return e in bag

def insert(aaa, p):
    aaa.append(p)   

def remove(bbb, p):
    bbb.remove(p)

def count(bag):     # 가방안에 갯수를 count해주는 함수
    return len(bag)+5    

myBag = []
insert(myBag, '휴대폰')   # => 결과 : ['휴대폰']
insert(myBag, '지갑') # => ['휴대폰', '지갑']
insert(myBag, '손수건') # => ['휴대폰', '지갑', '손수건']
insert(myBag, '자료구조') 
insert(myBag, '야구공') 
print('내 가방속의 물건:', myBag)    

insert(myBag, '빗')
print('내 가방속의 물건:', myBag)    

remove(myBag, '손수건')
print('내 가방속의 물건:', myBag)    

print('내 가방속의 물건의 갯수는:', count(myBag))    

print('내 가방속의 물건의 갯수는:', len(myBag)+5)    

print('내 가방속의 물건은', contains(myBag, '야구공2'))
