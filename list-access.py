#!/usr/bin/env python

import random
import copy
def generate_list(numOfElts):
	array = []
	for i in range(numOfElts):
		array.append(i + 1)
	print("The initial state of the list:", array)
	return array

def generate_sequence(length, numOfElts):
	seq = []
	for i in range(length):
		num = random.randint(1, numOfElts)
		seq.append(num)
	print("The access request sequence:", seq)
	return seq

# The partial cost model is followed
def do_nothing(array, seq):
	cost = 0
	for i in seq:
		cost += array.index(i)
	return cost

def move_to_front(array, seq):
	cost = 0
	for i in seq:
		cost += array.index(i)
		array.remove(i)
		array.insert(0, i)
	return cost

def move_to_front_even(array, seq):
	cost = 0
	move = [False] * len(array)
	for i in seq:
		if (verbose):
			print(array)
		cost += array.index(i)
		if (move[i-1]):
			array.remove(i)
			array.insert(0, i)
		move[i-1] = not move[i-1]
	return cost


# The function parameters and runs
numOfElts = 3
length = 10
verbose = False
array = generate_list(numOfElts)
seq = generate_sequence(length, numOfElts)

print("The cost of the algorithm do-nothing:", do_nothing(array, seq))
array_copy = copy.deepcopy(array)
print("The cost of the algorithm move-to-front:", move_to_front(array_copy, seq))
array_copy = copy.deepcopy(array)
print("The cost of the algorithm move-to-front-even:", move_to_front_even(array_copy, seq))


