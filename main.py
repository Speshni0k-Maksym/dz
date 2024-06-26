import string
import random
c = ""
n = int(input("Enter width of password: "))
a = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
for i in range(n):
    c += random.choice(a)
print(c)