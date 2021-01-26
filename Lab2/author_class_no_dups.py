# Author class program

class Author:
    def __init__(self, title):
        self.title = title
        self.books = []

    def publish(self, title):
        if title not in self.books:
            self.books.append(title)
        else:
            print(f'{title} has already been published by that author.')

    def __str__(self):
        # if self.books:  # resolves as true if the list is not empty
        #     book_list = ', '.join(self.books)
        # else:
        #     book_list = 'No books'
        book_list = ', '.join(self.books) or 'No published books'  # from slide example, sets to what's after "or" if
        # first statement is false
        return f'Author: {self.title}, Published books: {book_list}'


def main():
    rowling = Author('JK Rowling')
    rowling.publish('Harry Potter')
    rowling.publish('Fantastic Beasts')
    rowling.publish('Fantastic Beasts')

    elwell = Author('Nick Elwell')
    print(rowling)
    print(elwell)


main()
