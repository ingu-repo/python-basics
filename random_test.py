import random

# random.seed(1)
print(random.sample([0, 1, 2, 3, 4, 5], 2))
print(random.choice(["red", "blue", "white"]))
print(random.random())
print(random.randrange(10))

for i in range(1000):
    j = random.randrange(10)
    if (j == 9):
        print (f"picked {j} after {i} times loop")
        break

