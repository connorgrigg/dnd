#!/bin/python3

import random
import sys

def roll(quantity, dice):
	sum = 0
	out = 0
	try:
		for i in range(quantity):
			out = random.randint(1,dice)
			if is_plus:
				out = out+plusout
			print(out)
			sum = sum+out
		if quantity > 1:
			print("Sum: ", sum)
		if multiplier != "a":
			print("Multiplied Sum: ",  sum*multiplierout)
	except Exception as e:
		print("Invalid input - example input, 2d10+5")

parsed = "a"
multiplier = "a"
plus = "1"
is_plus = False
input = sys.argv[1]
try:
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
except Exception as e:
	print("invalid input")

quantity = int(parsed[0])
if multiplier != "a":
	if "+" in multiplier:
		plus = multiplier[1].split("+")
		plusout = int(plus[1])
		is_plus = True
		dice = plus[0]
	else:
		dice = multiplier[0]
else:
	if "+" in parsed[1]:
		plus = parsed[1].split("+")
		plusout = int(plus[1])
		is_plus = True
		dice = plus[0]
	else:
		dice = parsed[1]
roll(quantity,int(dice))

# usage example: python3 dieroll.py 2D4X10+1
