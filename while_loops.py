current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1


prompt= "\n Tell me something to repeat back to you"
prompt += "\n You can enter quit to close the application"

message = ""
while message != 'quit':
    message=input(prompt)
    
    if message != "quit":
     print(message)

active = True
while active:
   message = input(prompt)


   if message.lower()== 'quit':
      active = False
   else:
      print(message)


#using break in loops
new_prompt = "\n Enter the name of a city you have visited before."
new_prompt = new_prompt + "\n Enter the word quit if you would like to exit the program."

while True:
   city = input(new_prompt)

   if city.lower() == 'quit':
      break
   else:
      print(f"\n I would love to visit {city} sometime in the future.")

#using continue in loops
current_number = 0
while current_number <= 10:
   current_number += 1
   if current_number % 2 == 0:
      continue
   
   
   print (current_number)


#pizza toppings inputs
toppings = "enter what toppings you would like."


while True:
   pizza = input(toppings)
   
   if pizza.lower() == 'quit':
     break
   else:
      print(f" \ni'll add {pizza} toppings to your pizza")
      


#using while loops to move items from one list to another
unconfirmed_users =['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
   current_user = unconfirmed_users.pop()

   print(f'Verifying User:{current_user.title()}')
   confirmed_users.append(current_user)

   print('\n the following users have been confirmed:')
   for confirmed_user in confirmed_users:
      print(confirmed_user.title())

   
   
   # Collecting data on what mountains people would like to climb
responses = {}

polling_active = True  # this is the flag

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb? ')

    responses[name] = response

    repeat = input('Would you like to enter another one? (yes/no) ')
    if repeat.lower() == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f'{name} would like to climb {response}')


#sandwiches
sandwich_orders=['pastrami','beef','pastrami','chicken','fish','cheese','pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
  print(sandwich_orders) 


while sandwich_orders:
   finished_sandwich = sandwich_orders.pop()

   print(f'here is {finished_sandwich} sandwich')
   finished_sandwiches.append(finished_sandwich)

   print('the following sandwiches have been ordered:')
   for finished_sandwich in finished_sandwiches:
      print(finished_sandwich.upper())


#dream travel spot
dream ={}
poll_active = True

while poll_active:
   name = input('Name?')
   destination = input('What is your dream vacation spot?')


   dream[name]=destination
   another = input('is there another placr you would like to visit?(yes/no)')
   if another.lower() == 'no':
      poll_active = False

print('Here is where you all would like to travel...')
for name,destination in dream.items():
   print(f"{name.title()} would like to travel to {destination}")    