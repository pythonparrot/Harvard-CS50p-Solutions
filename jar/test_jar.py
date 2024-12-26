class Jar:
    def __init__(self, capacity):
        if capacity >= 0:
            self.capacity = capacity
        else:
            raise ValueError

    