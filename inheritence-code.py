class Animal:
    def __init__(self, name, weight, habitat):
        self.__name = name
        self.__weight = weight
        self.__habitat = habitat
        
    @property
    def name(self):
        return self.__name
        
    @name.getter
    def name(self, newname):
        self.__name = newname
    
    #repeat getters and setters for other attributes
    
    def move(self, direction, speed, time):
        #move a given direction at a given speed for a given time
        pass
        
class Fish(Animal):
    #Fish class, inheriting from Animal
    def __init__(self,name,weight,habitat,vertebrate):
        super().__init__(name,weight,habitat)
        self.__vertebrate = vertebrate
    
    @property
    def vertebrate(self):
        return self.__vertebrate
        
    @vertebrate.setter
    def vertebrate(self, newval):
        self.__vertebrate = newval
        
class Snake(Animal):
    #Snake class inheriting from Animal
    def __init__(self,name,weight,habitat,venomous):
        super().__init__(name,weight,habitat)
        self.__venomous = venomous
    
    #getter and setter for self.__venomous here
    
class Person(Animal):
    #Person class inheriting from animal
    def __init__(self,name,weight,habitat,race):
        super().__init__(weight,habitat)
        self.__name = "Human"
        self.__race = race
        
    #getter and setter for race here

class Book:
    def __init__(self,title,author,genre,pages):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pages = pages
        
    #getters and setters for attributes go here
    
    def book_open(self,page):
        #open the book to a given page
        pass
        
class Textbook(Book):
    def __init__(self,title,author,genre,pages,subject):
        super().__init__(title,author,genre,pages)
        self.__subject = subject
        
    #getter and setter for subject here
    
class AddressBook(Book):
    def __init__(self,title,author,genre,pages,region):
        super().__init__(title,author,pages)
        self.__genre = "reference"
        self.__region = region
        
    #getter and setter for region here
    
