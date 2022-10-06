#6. The 4 characters below specify the following update rules
#N -> x + (0,1)
#S -> x + (0,-1)
#E -> x + (1,0)
#W -> x + (-1,0)
#Apply the rules in the string "NNNEEESSWNNSW" starting from the position (0,0) and print the final position 

x =[0,0]
for c in "NNNEEESSWNNSW":
    if   c == 'N' : x[1] += 1;
    elif c == 'S' : x[1] -= 1;
    elif c == 'E' : x[0] += 1;
    elif c == 'W' : x[0] -= 1;
    else:
        print("Error");
        break;
print(x)