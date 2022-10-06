#Write code that prints five random integers between 1 and 100 (inclusive) to a file called rand.txt,
# where each line in the file has one number on it. 
from random import randint
with open("rand.txt", 'w') as outfile:
	for i in range(5):
		print(str(randint(1,100)) , file=outfile )
