#accesssing values in dict
alien_0={'color':'green'}
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
new_points=alien_0['points']
print(f'you have {new_points} points')

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#starting dictionaries with an empty dict
info={}
info['size']=int(input('how big are ya in numbers?'))
info['height']=int(input('how tall are you?'))
info['color']=input('what colour do you like?')
print(info)


alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"original position:{alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3


alien_0['x_position']=alien_0['x_position'] + x_increment


favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
language=favourite_languages['sarah'].title()
said=f'sarahs favourite language is {language}'
print(said)


#using get() - so this one uses first argument to fetch corresponding value and second argument is what is printed if the key doesn't exist
alien_1=alien_0.get('children','The alien does not have children.')
print(alien_1)



#ex-6-1
lil_bro={
    'Name':'Ibrahim',
    'Age':'56',
    'Strong_foot':'Right',
}
print(lil_bro['Name'].upper())

#looping through lists
for k,v in lil_bro.items():
    print(f"\n{k}:")
    print(f"{v}")

#keys() is used when you want to fetch only the value
print(lil_bro.keys()) 

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
     aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


#nesting dictionaries
users={
    'aeinstein':{
        'First':'albert',
        'Last':'einstein',
        'Location':'princeton' 
        },
    'ahameed':{
        'First':'abdul',
        'Last':'hameed',
        'Location':'kumasi'
        },
    'aibrahim':{
        'First':'ibrahim',
        'Last':'aminu',
        'Location':'kumasi',
        },       
}
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name=f"{user_info['First']} {user_info['Last']}"
    location=user_info['Location']
    print(f'\tFull name:{full_name.title()}')
    print(f'\tLocation:{location.title()}')


people ={
    'aba4':{
        "Name":'Aba',
        'Residence':'44 becker street',
        'Cell':'024567899',
    },
    'kojo5':{
        'Name':'Kojo',
        'Residence':'56 docker street',
        'Cell':'0546789945',
    },
    'ibro10':{
        'Name':'ibrahim',
        'Residence':'76 muslim street',
        'Cell':'0567890098'
    }
}
for a,b in people.items():
    Cinfo = f"\n{b['Name']} {b['Residence']}"
    tphone = f"\n{b['Cell']}"
    Sentence = f"your name and residence are: {Cinfo}"
    print(Sentence)


