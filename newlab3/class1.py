class MyClass:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Please enter a string: ")

    def printString(self):
        print(self.my_string.upper())
