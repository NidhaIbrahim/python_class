class Book:

    def __init__(self, book_name, author, book_id, genre, number_of_pages):
        self.book_name_ = book_name
        self.author_ = author
        self.book_id_ = book_id
        self.genre_ = genre
        self.number_of_pages_ = number_of_pages

    def issue(self):
        print("the book has been issued")

    def returnn(self):
        print("the book has been returned")

book = Book("Da Vinci Code", "Dan Brown", "D1029", "Mystery", "451")
print(book.book_name_)
print(book.author_)
print(book.genre_)