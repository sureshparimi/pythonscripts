import sys

mealCost = int(input().strip())
tipPercent = int(input().strip())
taxPercent = int(input().strip())

tip_amount = mealCost * tipPercent / 100 

tax_amount = mealCost * taxPercent / 100 

totalmealCost = int(round(mealCost + tip_amount + tax_amount))

print("the total meal cost is {} dollars".format(totalmealCost))