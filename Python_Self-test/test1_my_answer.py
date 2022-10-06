#1. What is the sum of the squares all whole numbers between 1 and 100?
#e.g. S = 1+4+9+...
def sum(n):
    sum = 0
    for i in range (1, n+1):
        sum += i*i
    return sum
m = sum(100)
print(m)