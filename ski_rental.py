import os
import pandas as pd
import numpy as np
from random import randint

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense


#problem instance
b = 10000
r = 100
d = 1
max_num_days = 200
sequence_length = 10

def getX(max_num_days = max_num_days):
	return randint(1, max_num_days)


def initial_sequence(max_num_days = max_num_days, length = 10):
    return [randint(0, max_num_days) for _ in range(length)]

def one_hot_encode(sequence, n_unique = max_num_days):
    encoded_sequence = list()
    for value in sequence:
        vector = [0 for _ in range(n_unique)]
        vector[value] = 1
        encoded_sequence.append(vector)
    return np.array(encoded_sequence)


# decode a one hot encoded string
def one_hot_decode(encoded_seq):
    return [np.argmax(vector) for vector in encoded_seq]



sequence = initial_sequence()


for _ in range(sequence_length):
	x = getX(max_num_days)
	sequence.append(x)
	encoded_sequence = one_hot_encode(sequence)
	decoded_sequence = one_hot_decode(encoded_sequence)
	# define model
	model = Sequential()
	model.add(LSTM(50, batch_input_shape=(5, 5, max_num_days), stateful=True))
	model.add(Dense(max_num_days, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
	df = pd.DataFrame(encoded_sequence)
	values = df.values
	X = values.reshape(len(values), 5, max_num_days)
	y = encoded_sequence


print X.shape, y.shape


print sequence
print encoded_sequence
print decoded_sequence



