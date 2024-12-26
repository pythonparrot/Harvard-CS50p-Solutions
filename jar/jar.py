class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self.capacity = capacity
            self.size = 0
        else:
            raise ValueError

    def __str__(self):
        to_return = ""
        for i in range(self.size):
            to_return += "🍪"
        return to_return

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.size - n >= 0:
            self.size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size

# def main():
#     jar = Jar(3)
#     print(jar)

# if __name__ == "__main__":
#     main()
