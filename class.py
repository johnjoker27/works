class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 4)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


class Restaurant:
    """This is an exercise so pay no heed."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing the restaurant_name and cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """This function prints some info about the restaurant."""
        print(f"{self.restaurant_name} is a great restaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Tell the user that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!!")


restaurant = Restaurant('The Vodka Shak', 'Russian')
print(f"\nRestaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant1 = Restaurant("Mama Kitchen", "Fish")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Nina's Room", "Nigerian")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("Halal Rest", "Muslim Food")
restaurant3.describe_restaurant()


class User:
    """A simple user class."""

    def __init__(self, first_name, last_name):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe the user."""
        print(f"My name is {self.last_name} {self.first_name}.")

    def greet_user(self):
        """Greet the user."""
        print(f"Hello {self.first_name} {self.last_name}, glad to have you back!")


hello = User("Aminu", "Abdul-Hameed")
hello.describe_user()
hello.greet_user()


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
        """Remind to check the gas tank."""
        print("Remember to check the gas tank before you set off.")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value; reject rollback."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2024)
print("\n" + my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print("\n" + my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """printing the range that the car has travelled."""
        range = self.battery_size *1.5
        return range

    def upgrade_battery(self):
        """Updates on the battery."""
        if self.battery_size != 65:
            self.battery_size = 65


car_deets = Battery(56)
car_deets.get_range()


class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class, then battery."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print("\n" + my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()


class IceCreamStand(Restaurant):
    """Represent a specific kind of restaurant — an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavours):
        """Initialize attributes of the parent class and flavours."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def display_flavours(self):
        """Display the available ice cream flavours."""
        print("\nAvailable ice cream flavours:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")


junkie = IceCreamStand('My Stand', 'Dessert', ['vanilla', 'chocolate', 'strawberry'])
junkie.describe_restaurant()
junkie.display_flavours()



class User:
    """A simple user class."""

    def __init__(self, first_name, last_name):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe the user."""
        print(f"My name is {self.last_name} {self.first_name}.")

    def greet_user(self):
        """Greet the user."""
        print(f"Hello {self.first_name} {self.last_name}, glad to have you back!")

class Admin(User):
    """"An attemp to practice the inheritance concept."""
    def __init__(self, first_name, last_name ,privileges):
        """initializing the user and admin attributes."""
        super().__init__(first_name,last_name)
        self.privileges = privileges
    
    def show_privileges(self):
        """Function to display the user's privileges."""
        print(f"these are your privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")


new_one = Admin('Aminu','Ibra',['can send messages','can delete post','can ban user'])
new_one.show_privileges()
new_one.describe_user()


#exercise privileges
class Privileges():
    def __init__(self,privileges):
        """This is to make the privilege class a seperate class."""
        self.privileges = privileges

    def show_privileges(self):
        """This is the function that will be used to show the user's privileges."""
        print("the following are your privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")    


class Admin(User):
    """A special kind of user with the privileges of an Admin."""
    def __init__(self,first_name,last_name,privileges):
        super().__init__(first_name,last_name)
        self.privileges = privileges


new_admin = Admin(
    'Aminu', 'Ibra', 
    ['can add post', 'can delete post', 'can ban user']
)

new_admin.describe_user()
new_admin.privileges.show_privileges()
