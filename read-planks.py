from collections import Counter

plankpath =  'preallocated_planks.txt'

plankfile = open(plankpath,'r')

planklist = []

for line in plankfile:
        line = line.strip('\n')
        line = line.strip('\r')
        planklist.append(line)

print(len(planklist),"planks found")
print(Counter(planklist))
c = Counter(planklist)

unsort = c.items()
sorted = sorted(unsort, key = lambda  x: x[1], reverse = True)

for plank in sorted:
    print(plank)    