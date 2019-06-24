class BookStore:
    def __init__(self):
        print("__init__() constructor gets called...")

B1 = BookStore()


class BookStore2:
    instances = 0
    def __init__(self, attrib1, attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        BookStore2.instances += 1

b1 = BookStore2("", "")
b2 = BookStore2("", "")

print("BookStore.instances:", BookStore2.instances)


class BookStore3:
    noOfBooks = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        BookStore3.noOfBooks += 1

    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author, "\n")

#Create a virtual book store
b1 = BookStore3("Great Expectations", "Charles Dickens")
b2 = BookStore3("War and Peace", "Leo Tolstoy")
b3 = BookStore3("Middlemarch", "George Eliot")

# Call member funcitons for each object
b1.bookInfo()
b2.bookInfo()
b3.bookInfo()

print("BookStore3.noOfBooks", BookStore3.noOfBooks)