from dataclasses import dataclass

@dataclass  # dataclass declaration less boilerplate code
class Student:
    name: str
    college_id: int
    gpa: float

def main():
    alice = Student('Alice', 12345, 3.4)
    bob = Student('Bob', 98765, 3.2)

    print(alice)
    print(bob)

main()