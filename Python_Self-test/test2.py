#2. What is the sum of the multiples of 3 and 5 between 1 and 1000?
# e.g. S = 3+5+6+9+10+...+1000
s = 0
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        s += i
    print(s)