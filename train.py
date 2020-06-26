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


# read csv file
data = pr.prepare_data('online_shoppers_intention.csv', 12330, 18)

# shuffle data to avoid similar inputs in same set
random.shuffle(data)

# get inputs and targets from data
inputs = pr.extractInputs(data)
targets = pr.extractTargets(data)

# standatdize inputs to be in [0,1] range
mf.standardize(inputs)

# extract train,validation and test sets
(trainInput,validationInput,testInput,trainTarget,validationTarget,testTarget) = pr.divideData(inputs,targets,0.7,0.2,0.3)


e = 100
lr = 0.001
m = 0.9

# initialize network and layers
network = keras.Sequential()
network.add(Dense(40,activation='sigmoid',input_shape=(17,),use_bias=True))
network.add(Dense(40,activation='sigmoid',use_bias=True))
network.add(Dense(2, activation='sigmoid'))

sgd = optimizers.SGD(lr=lr,momentum=m)
network.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy','mean_squared_error'])

# train the model
hist = network.fit(trainInput,trainTarget,verbose=1,batch_size=128,epochs=e,validation_data=(validationInput, validationTarget))

# evaluate model on test set
scores = network.evaluate(testInput, testTarget, batch_size=128)
print('\nConfiguration : Layers=',[10],' Epochs=',e,' Learning rate=',lr,' Momentum=',m)
print('Accuray on train data : ',hist.history.get('acc')[-1])
print('Accuray on test data : ',scores[1])

trainOutputs = np.asarray([network.predict(np.array([x])) for x in np.asarray(trainInput)])[:,0]
validationOutputs = np.asarray([network.predict(np.array([x])) for x in np.asarray(validationInput)])[:,0]
testOutputs = np.asarray([network.predict(np.array([x])) for x in np.asarray(testInput)])[:,0]

predictedOutput = network.predict(np.array([inputs[8109]]))

learn.plotGraphs(hist,scores,trainTarget,trainOutputs,validationTarget,validationOutputs,testTarget,testOutputs)