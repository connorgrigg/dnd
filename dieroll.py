import random
import sys

def roll(quantity, dice):
	sum = 0
	out = 0
	for i in range(quantity):
		out = random.randint(1,dice)
		print(out)
		sum = sum+out
	if quantity > 1:
		print("Sum: ", sum)
	if multiplier != "a":
		print("Multiplied Sum: ",  sum*multiplierout)

parsed = "a"
multiplier = "a"
input = sys.argv[1]
if "D" in input:
	parsed = input.split("D")
elif "d" in input:
	parsed = input.split("d")
if "X" in input:
	multiplier = parsed[1].split("X")
	multiplierout = int(multiplier[1])
elif "x" in input: 
	multiplier = parsed[1].split("x")
	multiplierout = int(multiplier[1])
quantity = int(parsed[0])
if multiplier != "a":
	dice = multiplier[0]
else:
	dice = parsed[1] 
roll(quantity,int(dice))

# usage example: python3 dieroll.py 2D4X10
