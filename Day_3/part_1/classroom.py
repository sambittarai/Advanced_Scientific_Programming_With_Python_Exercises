class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        print(f"{self.get_fullname()} is studying {self.subject}")

class Teacher(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        print(f"{self.get_fullname()} teaches {self.subject}")
