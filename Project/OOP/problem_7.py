class library:
    def __init__(self):
        self.book=[]


    def add(self,title):
        self.book.append(title)
        print(f"{title} added")

    def remove(self,title):
        if title in self.book:
            self.book.remove(title)
            print(f"{title} removed")
    
    def show_book(self):
        for index,title in enumerate(self.book):
            print(f"{index+1}.{title}")

my_library=library()

my_library.add("Harry Potter")
my_library.add("1984")
my_library.show_book()
my_library.remove("Harry Potter")