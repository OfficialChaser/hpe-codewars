budget, items = [int(i) for i in input().split(" ")]
originalOrder = []

purchasedItems = []
itemDict = {}

for item in range(items):
    name, price = input().split(" ")
    price = int(price)
    itemDict[price] = name
    originalOrder.append(name)

keys = list(itemDict.keys())
keys.sort()
sItemDict = {i: itemDict[i] for i in keys}

for price in sItemDict:
    if (budget >= price):
        budget -= price
        purchasedItems.append(sItemDict[price])
        
for itemName in originalOrder:
    if (itemName in purchasedItems):
        print(f"I can afford {itemName}")
    else:
        print(f"I can't afford {itemName}")

if (len(purchasedItems) == 0):
    print("I need more Yen!")

print(budget)