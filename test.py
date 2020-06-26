import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import preprocess as pr
import mathfunc as mf
import random
import keras
import numpy as np
from keras import  optimizers
from keras.models import Sequential
from keras.layers import Activation, Dense
import matplotlib.pyplot as plt
import learn
from keras.models import model_from_json
from keras.models import load_model

json_file = open('model_0.json', 'r')
model = model_from_json(json_file.read())
model.load_weights('model_0.h5')

data = pr.prepare_data('online_shoppers_intention.csv', 12330, 18)
inputs = np.asarray(pr.extractInputs(data))
targets = np.asarray(pr.extractTargets(data))

predictedOutput = model.predict(np.array([inputs[0]]))

print('Real output : ',targets[0])
print('Predicted output : ',predictedOutput[0])