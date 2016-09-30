"""
Once a model is learned, use this to play it.
"""
import sys
sys.path.append("game/")
import carmunk
import numpy as np
from time import sleep
from nn import neural_net
import tensorflow as tf

NUM_SENSORS = 3
GAME = 'carmunk'


def play(model, sess):


    car_distance = 0
    game_state = carmunk.GameState()

    # Do nothing to get initial.
    _, state = game_state.frame_step((2))

    # Move.
    while True:
        car_distance += 1

        # Choose action.
        action = (np.argmax(model.predict(state, batch_size=1)))
	#action = (np.argmax(readout_t))
        # Take action.
        _, state = game_state.frame_step(action)
	
	sleep(0.01)

        # Tell us something.
        if car_distance % 1000 == 0:
            print(("Current distance: %d frames." % car_distance))


if __name__ == "__main__":
    saved_model = 'saved-models/164-150-100-50000-125000.h5'
    model = neural_net(NUM_SENSORS, [164, 150], saved_model)
    sess = tf.Session()
    play(model, sess)
