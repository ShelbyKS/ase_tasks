f = open('farm.txt', 'r')

animals = []

for i in f:
    animals.append(int(i))

sum_legs = animals[0] * 4 + animals[1] * 4 + animals[2] * 2
print(sum_legs)

f.close()