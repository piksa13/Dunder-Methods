# Dunder methods are automatically called by many of Python's build-in operations
# They allow devs customise the behaviour of the objects rather than returning object address

class Book():

    def __init__(self, title, author, no_pages):
        self.title = title
        self.author = author
        self.no_pages = no_pages

    # Without that method the instance of the class would return the memory ref
    def __str__(self):
        return f"{self.title} by {self.author}"

    #  overriding the == func
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    # less than
    def __lt__(self, other):
        return self.no_pages < other.no_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        if key == "author":
            return  self.author

book1 = Book("The Tolkien", "J.R.R Talkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion", "C.S. Lewis", 172)
book4 = Book("The Lion", "C.S. Lewis", 172)

print(book1.__eq__(book2))
print(book3 == book4)
print(book3.__eq__(book4))
print(book2 < book3)
print("Is there a word lion in the title of the book no4: " )
print("Lion" in book4)

print(book1['title'])