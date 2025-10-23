import module
module.make_pizza(16,'pepperoni')
module.make_pizza(12,'mushrooms','green peppers','extra cheese')


#to import a specific function
from module import make_pizza


from module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

from module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from module import weekly_goals as wg 
wg('Tuesday','Pray','Code','listen')
