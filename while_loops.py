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


   if message == 'quit':
      active = False
   else:
      print(message)
        