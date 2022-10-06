#5. Write code that puts a string into alphabetical order e.g. "edcba" -> "abcde" 
# and use it to put the characters in "antidisestablishmentarianism" into order.
a = "antidisestablishmentarianism"
b = ''.join(sorted(a))
print(b)
