import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(self.houses)}")


hat = Hat()
hat.sort("Harry")
