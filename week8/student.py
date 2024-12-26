class Student:
    ...

def main():
    student = Student("Harry", "Gryffindor")
    print(f"{student.name} from {student.house}")

def Student(name, house):
    self.name = name
    self.house = house

if __name__ == "__main__":
    main()
