# This program asks the user for classes they are taking this semester, adds them to a list and displays them line by line

classes = []

class_name = input('Name a class you are taking this semester. If none, press Enter to exit. ')

while class_name:
    classes.append(class_name)
    class_name = input('Any other classes? Press Enter if finished. ')

for index, c in enumerate(classes):
    print(f'{index +1}. {c}')