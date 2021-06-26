class Publisher:
    pass
class Book(Publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title of book :",self.title)
        print("Author of the book :",self.author)
class Python(Book):
    def __init__(self,title,author,price,no_of_pages):
        super().__init__(title,author)
        self.price=price 
        self.no_of_pages=no_of_pages
    def display(self):
        print("Book Details")
        print("Title of book :",self.title)
        print("Book Author :",self.author)
        print("Price of book :",self.price)
        print("Number of pages :",self.no_of_pages)

book1=Python("Ships That Pass","Shashi Deshpande",150,200)
book1.display()
        
