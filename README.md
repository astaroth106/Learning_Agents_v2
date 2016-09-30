# Learning-Agents-v.2

Overview
==========
This project trains a virtual machine to drive a car and avoid obstacles on the screen. This is part of my senior project 2. I, Carlos Pena, and my partner Angel Hernandez intent to develop this code a little further, before starting implementation in an RC car. 

Dependencies
============

* Numpy (http://www.numpy.org/)
* Pygame. '''pip install pygame'''
* Pymunk. Use Pymunk 4. Using version 5 will not work as it was a major refactor. V4 is [here](https://github.com/viblo/pymunk/releases/tag/pymunk-4.0.0)
* Keras ```pip3 install keras```
* Tensorflow. Follow the installation instructions at https://www.tensorflow.org/versions/r0.10/how_tos/variables/index.html#initialization
* h5py ```pip3 install h5py```


Usage
======

1. Make sure ~/.keras/keras.json looks like this:
{
    "image_dim_ordering": "th", 
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "backend": "tensorflow"
}

2. Run self_driving_car.py to resume training from my last model, otherwise change the line in the main "saved_model = 'saved-models/164-150-100-50000-125000.h5'" to only "saved_model=''"

3. Specify in the code the model you want to observe, and run playing.py to observe the trained model, increase the sleep(sec) in the code to slow down the car.

4. Using plotting.py get the csv files created from the learning progress to output graphs for learn data and loss data.
