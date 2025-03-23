class Computer:
    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def get_cpu(self):
        return self.cpu

    def get_memory(self):
        return self.memory

    def get_disk(self):
        return self.disk

# 사용 예시
my_computer = Computer("Intel Core i7", "16GB", "128GB")
print(my_computer.get_cpu())
print(my_computer.get_memory())
print(my_computer.get_disk())
