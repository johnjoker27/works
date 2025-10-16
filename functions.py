def greet_user(username): #this is the func definition part
    '''display a simple greeting'''
    print(f'hello,{username.title()}')

greet_user('jesse')


#message
def display_message(name):
    print(f"hello! i am learning to write {name.title()}")

display_message('functions')    

#favourite book
def favourite_book(book):
    print(f"One of my favourite books is {book}")


favourite_book('Alice in the borderlands.')


def describe_pet(animal_type,pet_name):
    '''displays info about pets '''
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry')

#using keyword arguments
describe_pet(animal_type ='dog',pet_name ='berry')

#using default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

def make_shirt(shirt_size,message):
    print(f'i wear size {shirt_size} shirts.')
    print(f" I want the message {message} printed on it.")
    
make_shirt('medium-sized','Allahu Akbr')

def make_shirt(shirt_size = 'large',message):
    print(f'i wear size {shirt_size} shirts.')
    print(f" I want the message {message} printed on it.")
    
make_shirt('Allahu Akbr wa Al-Rahman.')


def describe_city(city,country= 'Ghana'):
    print(f"{city} in {country}")

describe_city('Accra')
describe_city('Kumasi')
describe_city('Tamale')

