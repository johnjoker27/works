import time


'''my_time = int(input('Enter the time in seconds.:'))


for x in (range(0,my_time)):
    seconds = x % 60
    minutes = int(x//60) % 60
    hours = int(x//3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    print(x)
    time.sleep(1)

print('Time is up!')


#OR TO REVERSE

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x//60) % 60
    hours = int(x//3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    print(x)
    time.sleep(1)

print('Time is up!')


#or
for x in reversed(range(0,my_time)):
    seconds = x % 60
    minutes = int(x//60) % 60
    hours = int(x//3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    print(x)
    time.sleep(1)

print('Time is up!')'''



#CREATING A SELF TIMER
study = int(input('How long do you want to study for in seconds?'))

d = int(input("Enter the delay for the counting"))


'''for s in range(0 +1,study):
    seconds = int(s % 60)
    minutes = int(s/60) % 60
    hours =int(s//3600) % 3600
    print(f"{hours}:{minutes}:{seconds} is how long you have to study for.")
    time.sleep(d)

print(f'Congrats on studying for {hours}:{minutes}:{seconds}.')   ''' 



for q in range(0 ,study + 1):
    seconds = int(study% 60)
    minutes = int(study/60) % 60
    hours =int(study//3600) % 3600


    elapsed = q
    sec_elapsed = q % 60
    min_elapsed  = (q//60) %60
    hour_elapsed = (q//3600) %3600

    remaining_time = study - q 
    sec_rem = int(remaining_time%60)
    min_rem = int(remaining_time//60) % 60
    hr_rem = int(remaining_time //3600) % 60

    progress= int((elapsed/study)*20) if q > 0 else 0 

    progress_bar = progress * '-' + '!' * (20-progress)


    print(f"{seconds}:{minutes}:{hours} are to be studied.")
    print(f"{sec_elapsed}:{min_elapsed}:{hour_elapsed} have elapsed.")
    print(progress_bar)
    print(f"{sec_rem}:{min_rem}:{hr_rem}")

    
  
   
   
   
    time.sleep(d)