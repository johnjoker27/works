#instantination is basically making a class from objects
class Dog:
    '''A simple attempt to model a dog.'''

    def _init_(self,name,age):
        '''Initialize name and age attributes.'''
        self.name = name 
        self.age = age


    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''Simulate rolling over in response to command.'''
        print(f'{self.name} rolled over!')
