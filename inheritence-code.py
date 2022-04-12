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
    
class Vehicle:
    def __init__(self,make,model):
        self.__make = make
        self.__model = model
    
    #getters/setters for make and model here
    
    def drive(self,speed,time):
        #drive a given speed for a given time, straight forward
        pass

class Car(Vehicle):
    def __init__(self,make,model,mpg,horsepower):
        super().__init__(make,model)
        self.__mpg = mpg
        self.__horsepower = horsepower
        
    #getters and setters for mpg and horsepower here
    
class Bicycle(Vehicle):
    def __init__(self,make,model,style):
        super().__init__(make,model)
        self.__style = style
        
    #getter and setter for style here

class Boat(Vehicle):
    def __init__(self,make,model,boat_type):
        super().__init__(make,model)
        self.__boat_type = boat_type
        
    #getter and setter for boat_type here
    
class HotAirBalloon(Vehicle):
    def __init__(self,make,model,balloon_pattern):
        super().__init__(make,model)
        self.__balloon_pattern = balloon_pattern
        
    #getter and setter for balloon_pattern here