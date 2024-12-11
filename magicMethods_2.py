# Dunder methods are automatically called by many of Python's build-in operators e.g. ==, <

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
        elif key == "author":
            return  self.author
        elif key == "no_pages":
            return self.no_pages
        else:
            return f"Key: '{key}' was not found"

book1 = Book("The Tolkien", "J.R.R Talkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion", "C.S. Lewis", 172)
book4 = Book("The Lion", "C.S. Lewis", 172)

print("Checking whether the no of pages are equal: 'book3 == book4'")
print(book3 == book4)
print(book3.__eq__(book4))
print("\nComparing no of pages: 'book2 < book3'")
print(book2 < book3)
print("\nIs there a word 'Lion' in the title of the book no4: " )
print("Lion" in book4)
print("\nReturning value using object key e.g. 'book1['title']' ")
print(book1['title'])
print(book1['author'])
print(book1['no_pages'])
print(book1['co-author'])