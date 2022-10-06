#Write code that prints five random integers between 1 and 100 (inclusive) to a file called rand.txt,
# where each line in the file has one number on it. 
import random
filename = "rand.txt"
with open("rand.txt", "w") as file:
    for i in range(5):
        line = str(random.randint(1,100))
        file.write(line)
        file.write("\n")
        print(line)
    file.close()