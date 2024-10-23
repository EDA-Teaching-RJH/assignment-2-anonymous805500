### Part Four -- your code goes here. 
import random
x1 = random.randint(1, 100)
x2 = random.randint(1, 100)
x3 = random.randint(1, 100)
x4 = random.randint(1, 100)
x5 = random.randint(1, 100)
x6 = random.randint(1, 100)
x7 = random.randint(1, 100)
x8 = random.randint(1, 100)
x9 = random.randint(1, 100)
x10 = random.randint(1, 100)
list = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
print("Initial list: " , list)
y = 0
while y < len(list):
    if list[y] % 2 == 0: 
        list.pop(y)
    else:
        y += 1
print("Final list: " , list)
