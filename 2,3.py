import random

otric = []
polozh = []

for i in range(250):
    x = random.randint(-1000,1000)
    if x<0:
        otric.append(x)
    else:
        polozh.append(x)

print(otric)
print(polozh)
