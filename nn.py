#!/usr/bin/env python


from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import RMSprop
from keras.layers.recurrent import LSTM
from keras.callbacks import Callback

import tensorflow as tf

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


def neural_net(num_sensors, params, load=''):
    model = Sequential()

    # First layer.
    with tf.device("/cpu:0"):
	    model.add(Dense(
		params[0], init='lecun_uniform', input_shape=(num_sensors,)
	    ))
	    model.add(Activation('relu'))
	    model.add(Dropout(0.2))

    # Second layer.
    with tf.device("/cpu:0"):
	    model.add(Dense(params[1], init='lecun_uniform'))
	    model.add(Activation('relu'))
	    model.add(Dropout(0.2))

    # Output layer.
    with tf.device("/cpu:0"):
	    model.add(Dense(3, init='lecun_uniform'))
	    model.add(Activation('linear'))

    rms = RMSprop()
    model.compile(loss='mse', optimizer=rms)

    '''
    
    '''

    if load:
        model.load_weights(load)

    return model
