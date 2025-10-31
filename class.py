#instantination is basically making a class from objects
class Dog:
    '''A simple attempt to model a dog.'''

    def __init__(self,name,age):
        '''Initialize name and age attributes.'''
        self.name = name 
        self.age = age


    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''Simulate rolling over in response to command.'''
        print(f'{self.name} rolled over!')


 #The  _init_() Method 
        
my_dog = Dog('Willie',5)


print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy',4)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


#ex9
#restaurant
class Restaurant:
    '''This is an exercise so pay no heed.'''
    def __init__(self,restaurant_name,cuisine_type):
        '''Initailizing the restaurant_name and cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """This function prints some info about the restaurant."""
        print(f"{ self.restaurant_name } is a great restaurant and the serve great {self.cuisine_type} food.")



    def  open_restaurant(self):
        """This function is to tell the user that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!!")


restaurant = Restaurant('THe_vodka_shak','Russian')

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")
#tion is to tell the Three Restaurants 
class Restaurant:
    '''This is an exercise so pay no heed.'''
    def __init__(self,restaurant_name,cuisine_type):
        '''Initailizing the restaurant_name and cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """This function prints some info about the restaurant."""
        print(f"{ self.restaurant_name } is a great restaurant and the serve great {self.cuisine_type} food.")



    def  open_restaurant(self):
        """This funcuser that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!!")


restaurant = Restaurant('THe_vodka_shak','Russian')

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant1 = Restaurant("mama kitchen","fish")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("nina's room","Nigerian")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Halal rest","Muslim food")
restaurant3.describe_restaurant()

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    

    def describe_user(self):
        print(f"My name is {self.last_name} {self.first_name}.")
       



    def greet_user(self):
        print(f"Hello! {self.first_name} {self.last_name} glad to have you back.")
       

hello = User("Aminu","Abdul-Hameed")
hello.describe_user()
hello.greet_user()




#the car class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
      

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def fill_gas_tank(self):
        """this is just something i added later when the book explained a concept."""
        print("remember to check the gas tank before you set off.")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self,mileage):
       # """Set the odometer reading to the given value."""
        """set the odometer reading to the given value and reject the change if it attempts to roll the odometer back."""
        #self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")    
    
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
# Create an instance of the Car class
my_new_car = Car('audi', 'a4', 2024)

# Display car info
print(my_new_car.get_descriptive_name())

# Display odometer reading
my_new_car.read_odometer()

#modifying an attribute odometer reading
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#updating the odometer reading
my_new_car.update_odometer(23)
my_new_car.read_odometer


#miles added after buying
my_used_car = Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

#Creating a subclass 

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self,make,model,year):
        """Inirialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank():
        """This is when you notice that electric cars do not have gas tanks."""
        print("This car doesn't have a gas tank to be filled.")    

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


class Battery:
    """A simple attempt tp model a battery for an electric car."""


    def __init__(self,battery_size=40):
        """Initialie the vattery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")




class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""


    def __init__(self,make,model,year):
        """
        Initialize attributes specific to an electric car.
        Then initialie attributes specific to an electric car.
        """

        super().__init__(make,model,year)
        self.battery = Battery() 
        


my_leaf = ElectricCar('nissan','leaf',2024)   
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() 


#ice cream stands
# Base class
class Restaurant:
    """A simple model of a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print info about the restaurant."""
        print(f"{self.restaurant_name} is a great restaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Announce that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!!")


# Subclass
class IceCreamStand(Restaurant):
    """Represent a specific kind of restaurant — an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavours):
        """Initialize attributes of the parent class, then the ice cream stand's attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours 

    def display_flavours(self):
        """Display the available ice cream flavours."""
        print("Available ice cream flavours:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")



junkie = IceCreamStand('My Stand', 'Dessert', ['vanilla', 'chocolate', 'strawberry'])
junkie.describe_restaurant()
junkie.display_flavours()
