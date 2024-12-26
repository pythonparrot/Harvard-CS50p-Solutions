class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self.capacity = capacity
            self.size = 0
        else:
            raise ValueError

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
