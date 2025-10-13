prompt = "if you share your name, we can personalize a message for you."
prompt +="\n What is your first name?"

name=input(prompt)
print(f"\nHello,{name}")

#making inputs integers
age= input('How many moons have you lived?')
age=int(age)
print(age>=18)

height=input("how tall are ya in metres?")
height=int(age)

if height >= 47:
    print('you are tall enough to ride')
else:
    print('naah lil bro this ride for big kids ')

# %-modulo-shows remainders
number = input("Enter a number and i'll let you know if its even or odd.")
number = int(number)
if number % 2 == 0:
    print('\n the number you entered is even')
else:
    print('\nthe number entered is odd.')



 #RENTAL CARS
car = input("Enter the name of the car you would like.")
print(f"{car.title()}? Lemme see if i can you find one you would like?")

#RESTAURANT SEATING
peeps = input ('How many people are in the friend group?')
peeps= int(peeps)

if peeps <= 8:
    print("Your table is ready.")
else:
    print("you are going to have to wait.")

#MULTIPLES OF 10
multiple = input("Enter a number that you think is a multiple of 10(ten) between 1 and 500: ")
multiple = int(multiple)
proof= int(multiple%10) 
#whole_number= range(1,500,10)

if proof == 0 :
    print('this is a multiple of ten')
else:
    print('sorry little man.')

















































