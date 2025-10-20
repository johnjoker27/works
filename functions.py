#  1. Basic Greeting Function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')


# 2. Display Message
def display_message(topic):
    """Display a message about what you're learning."""
    print(f"Hello! I am learning to write {topic.title()}.")

display_message('functions')


#  3. Favourite Book
def favourite_book(book):
    """Print a message about a favourite book."""
    print(f"One of my favourite books is {book}.")

favourite_book('Alice in the Borderlands.')


#  4. Describing Pets
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Using positional arguments
describe_pet('hamster', 'harry')

# Using keyword arguments
describe_pet(animal_type='dog', pet_name='berry')


#  5. Describing Pets with Default Values
def describe_pet_default(pet_name, animal_type='dog'):
    """Display information about a pet with a default animal type."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_default(pet_name='willie')


# 6. Make Shirt Function
def make_shirt(message, shirt_size='large'):
    """Describe a shirt with a message."""
    print(f"I wear size {shirt_size} shirts.")
    print(f"I want the message '{message}' printed on it.")

make_shirt('Allahu Akbar wa Al-Rahman.')


# 7. Describe City
def describe_city(city, country='Ghana'):
    """Display a city and its country."""
    print(f"{city} is in {country}.")

describe_city('Accra')
describe_city('Kumasi')
describe_city('Tamale')


# 8. Return Formatted Name
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 9. Returning Dictionaries
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

music_man = build_person('jimmy', 'threx')
print(music_man)


# 10. Dictionary with Optional Age
def build_man(first_name, last_name, age=None):
    """Return a dictionary of information about a person, with optional age."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

man = build_man('jimmy', 'hendrix', age=27)
print(man)


#  11. Greeter with While Loop
def get_formatted_name_loop(first_name, last_name):
    """Return a full name neatly formatted."""
    return f"{first_name} {last_name}".title()

# Uncomment this if you want to run the loop
# while True:
#     print('What is your name? (Enter "q" to quit)')
#     f_name = input('First name: ')
#     if f_name.lower() == 'q':
#         break
#     l_name = input('Last name: ')
#     if l_name.lower() == 'q':
#         break
#
#     formatted_name = get_formatted_name_loop(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# 12. City-Country Function with Loop
def city_country(city_name, country_name):
    """Return a string showing a city and its country."""
    return f"{city_name.title()} is in {country_name.title()}."

# Uncomment this if you want to run the loop
# while True:
#     print('\nTell me the city and country you would like to visit.')
#     print('(Enter "end" anytime to quit.)')
#
#     city_nom = input('City: ')
#     if city_nom.lower() == 'end':
#         break
#
#     country_nom = input('Country: ')
#     if country_nom.lower() == 'end':
#         break
#
#     final_destination = city_country(city_nom, country_nom)
#     print(f"\n{final_destination}\n")

#this is a function that stores data about a music album
def make_album(music_name,music_boy,song_number=None):
    '''Returning a dictionary'''
    albums = {'music_name':music_name,'music_boy':music_boy,}
    if song_number:
        albums['song_number'] = song_number
    return albums

album1 = make_album('made in lagos','wizkid')
album2 = make_album('love damini','burna boy')
album3 = make_album( 'timeless','davido', song_number=17)

print(album1)
print(album2)
print(album3)

while True:
    music_title = input('What is the name of the song? or enter q to quit.')
    if music_title.lower() == 'q':
        break
    music_maker = input('Enter the name of the creator: ')
    if music_maker.lower() == 'q':
        break
    song_num = input('Enter the number of the song.')
    if song_num.strip() == "":
        album_owner = make_album(music_title,music_maker)
    else:
        album_owner = make_album(music_title,music_maker,int(song_num))

   
    print(album_owner)    


#lists in functions
def greet_users(names):
    '''print a simple greeting for everyone in a group'''
    for name in names:
        msg = f'Hello human {name.title()}!'
        print(msg)


usernames = ['ty','nina','gringo']
greet_users(usernames)


#modifying a list in a function

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"\n Printing model:{current_design}")
    completed_models.append(current_design)

#Display all completed models.
print('\n The following models have been printed.')
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs,completed_models):
    '''this part is to print the designs'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'\n Printing model:{current_design} ')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    '''Show all the models that were printed'''
    print(f'\n the following models were printed:')
    for complete_model in completed_models:
        print(complete_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#using print_models(unprinted_designs[:],completed_models) -the : makes a copy of the list and uses that one instead of the original one


#message function
messages = [
    'this is the end',
    'close your eyes and count to 10',
    'Let the sky fall',
    'A thousand miles apart'
]

def show_messages(message_list):
    for message in message_list:
        print(message)

def send_messages(send_list, sent_list):
    while send_list:
        current_message = send_list.pop() 
        print(f"Sending message: {current_message}")
        sent_list.append(current_message)  

messages = [
    'this is the end',
    'close your eyes and count to 10',
    'Let the sky fall',
    'A thousand miles apart'
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal list:", messages)
print("Sent messages:", sent_messages)


def send_messages(unsent_messages,sent_messages):
    while unsent_messages:
        current_messages = unsent_messages.pop()
        print(f"The following messages have been sent: {current_messages}")
        sent_messages.append(current_messages)

unsent = messages[:]    
sent = []    

show_messages(messages)   
send_messages(unsent,sent)    


print('the following messages were not  printed:',unsent)
print('the following messages were printed:',sent)



#using * in functions
def pizza_additions(*toppings):
    '''Summary of pizza toppings'''
    print('the following toppingd were added:')
    for topping in toppings:
        print('-',topping)

pizza_additions('pepperoni')
pizza_additions('mushrooms','green peppers','extra cheese')
