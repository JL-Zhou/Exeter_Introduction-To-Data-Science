#3. Using the two strings x="supercalifragilisticexpialidocious" and y="pneumonoultramicroscopicsilicovolcanoconiosis"
#print all the characters in x that are not in y
x = "supercalifragilisticexpialidocious"
y = "pneumonoultramicroscopicsilicovolcanoconiosis"
def Char(self, x, y):
    for ch in x:
        if ch not in y:
            return ch
        else:
            y = y.replace(ch,"",1)
    print(ch)

#has bug