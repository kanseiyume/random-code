import json
with open("rarities.json") as file:
    possible = json.load(file)

sumchance = 0

print(possible.values())
for x in possible.values():
    sumchance = sumchance + x

print(sumchance)