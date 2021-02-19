import math

# Get height from user
numCoins = 0
	
while True:
	change = float(input("Change owed: "))
        if change < 0:
                continue
        else:
                break

while change > 0:
	if change - 1 >= 0:
		change = round(change - 1, 2)
		numCoins += 1
	elif change - 0.25 >= 0:
		change = round(change - 0.25, 2)
		numCoins += 1
	elif change - 0.1 >= 0:
		change = round(change - 0.1, 2)
		numCoins += 1
	elif change - 0.05 >= 0:
		change = round(change - 0.05, 2)
		numCoins += 1
	elif change - 0.01 < 0.01:
		change = round(change - 0.01, 2)
		numCoins += 1
	print(change)
print(numCoins) 	
