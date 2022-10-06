#3. Using the two strings x="supercalifragilisticexpialidocious" and y="pneumonoultramicroscopicsilicovolcanoconiosis"
#print all the characters in x that are not in y
x = "supercalifragilisticexpialidocious"
y = "pneumonoultramicroscopicsilicovolcanoconiosis"
chars = []
for c in x:
    if c not in y:
        chars.append(c)
    print(chars) #['x', 'g', 'f', 'd']