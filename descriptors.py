class PriceControl:
    def __init__(self):
        self.value = None

    def __get__(self, instance, value):
        return self.value

    def __set__(self, instance, value):
        if not 0 <= value <= 100:
            raise ValueError("Price must be between 0 and 100.")
        self.value = value


class NameControl:
    def __init__(self):
        self.value = None
        self.attribute = None
        self.initialized = False

    def __get__(self, instance, value):
        return self.value

    def __set_name__(self, owner, value):
        self.attribute = value

    def __set__(self, instance, value):
        if self.initialized:
            raise ValueError(f"{self.attribute.capitalize()} can not be changed.")
        self.value = value
        self.initialized = True


class Book:
    price = PriceControl()
    author = NameControl()
    name = NameControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
        self.initialized = True

#b = Book("William Faulkner", "The Sound and the Fury", 12)
#print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# #Author='William Faulkner', Name='The Sound and the Fury', Price='12'
#
#b.price = 55
#b.price #55
#b.price = -12  # => ValueError: Price must be between 0 and 100.
#b.price = 101  # => ValueError: Price must be between 0 and 100.
#b.author = "new author"  # => ValueError: Author can not be changed.
#b.name = "new name"      # => ValueError: Name can not be changed.