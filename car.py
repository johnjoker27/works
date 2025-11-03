"""A class that can be used to represent a car."""


class Car:
    """A simple attempt to rep a car."""


    def __init__(self,make,model,year):
        """Initialie attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


        def get_descriptive_name(self):
            """re\\Retun a neatly formatted descriptive name."""
            long_name = f"{self.year} {self.make} {self.model} "
            return long_name.title()
        
        def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print(f"This car has {self.odometer_reading} miles on it.")


        def update_odometer(self):
            """
            Set the odometer reading to the given value .
            Rehect the change if it attempts to roll the odometer back.
            """
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage    