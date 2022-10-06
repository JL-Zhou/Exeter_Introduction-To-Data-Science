#7. Write code that generates 100 random integers between 1 and 10 (inclusive)
#counts how many of each number occurs and prints that number of asterisks
#Output should be formatted like
#1. ****
#2. **
#3. ...

from collections import Counter
from random import randint
c = Counter()
for i in range(100): c[randint(1,10)] +=1
for i in range(1, 11):
    print("{}. ".format(i) + "*"*c[i])