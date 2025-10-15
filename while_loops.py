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
      
   
   
