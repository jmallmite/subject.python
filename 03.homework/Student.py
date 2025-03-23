class Student:

     # __init__ 호출하는 순간 인스턴스(self)가 생성되고, 인스턴스에는 인수로 받은 값들이 변수에 저장된다.
    def __init__(self, name, department, number): # 객체 생성자
        self.name = name 
        self.department = department
        self.number = number

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_number(self):
        return self.number

best = Student('김재민', '스마트콘텐츠학과', 2024145049)
print(best.get_name()) 
print(best.get_department())
print(best.get_number())