# dataclasses, more concise version of traditional way, introduced with Python 3.7 to eliminate "boiling plate" code
from dataclasses import dataclass


@dataclass()
class Student:
    name: str  # name is an instance variable in the student object
    school_id: str  # doesn't need to have same name as the argument above but is common to do so
    gpa: float

    # useful if you want more control over formatting or don't want to print out all of the data in the class
    # def __str__(self):  # returns string representation of an object
    #     return f'Student name: {self.name}, ID: {self.school_id}, Current GPA: {self.gpa}'


def main():  # function, a function inside of a class is a method and a function not part of a class is a function
    alex = Student('Alex', 'avfgefd', 2.6)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'qwerty', 3.2)
    print(sam)

    nick = Student('Nick', '12345', 4.0)
    print(nick)
    print(nick.gpa)


if __name__ == '__main__':  # useful if there are multiple files and if code is being imported, it tells python to
    # check if it it running imported code or not in case you do not want to run the entire file of imported code
    main()
