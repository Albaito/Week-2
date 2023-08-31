class Author:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def publish(self, book_title):
        self.book_list.append(book_title)
        return
    
    def __str__(self):
            books_string = ''
            for book in self.book_list:
                books_string += book + '\n'

            return f'Books by {self.name}:\n{books_string}'
    


def main():
    james = Author('James')
    james.publish('How to not be an idiot')
    print(james)

    bobby = Author('Bobby')
    bobby.publish('Wonderful wisps and where to find them')
    bobby.publish('How to avoid spaghetti code')
    print(bobby)

main()