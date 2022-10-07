class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id
    def __str__(self):
        return  f'{self.title} by {self.author}. ${self.price}. [{self.book_id}]'
    # define the necessary method here


# book = Book("sdf", "sdf", 100, "sdf")
# print (book.__str__())
