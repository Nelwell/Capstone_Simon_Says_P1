# classes

class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name  # name is an instance variable in the student object
        self.school_id = school_id  # doesn't need to have same name as the argument above but is common to do so
        self.gpa = gpa

    def __str__(self):  # returns string representation of an object
        return f'Student name: {self.name}, ID: {self.school_id}, Current GPA: {self.gpa}'


alex = Student('Alex', 'avfgefd', 2.4)
print(alex.name)
print(alex.school_id)
print(alex)

sam = Student('Sam', 'qwerty', 3.2)
print(sam)

nick = Student('Nick', '12345', 4.0)
print(nick)
print(nick.gpa)