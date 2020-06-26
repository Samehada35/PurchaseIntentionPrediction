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

bestModels = []
MAX_NEURONS = 50
hiddenLayersConf = [10]

while len(hiddenLayersConf) <= 2: 
	for e in range(50,100,20):
		lr = 0.001
		while lr<=0.003:
			m = 0.7
			while m<=0.9:
				# initialize network and layers
				network = keras.Sequential()
				network.add(Dense(hiddenLayersConf[0],activation='sigmoid',input_shape=(17,),use_bias=True))
				if(len(hiddenLayersConf)==2):
					network.add(Dense(hiddenLayersConf[1],activation='sigmoid',use_bias=True))
				if(len(hiddenLayersConf)==3):
					network.add(Dense(hiddenLayersConf[2],activation='sigmoid',use_bias=True))

				network.add(Dense(2, activation='sigmoid'))

				sgd = optimizers.SGD(lr=lr,momentum=m)
				network.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy','mean_squared_error'])

				# train the model
				hist = network.fit(trainInput,trainTarget,verbose=1,batch_size=128,epochs=e,validation_data=(validationInput, validationTarget))

				# evaluate model on test set
				scores = network.evaluate(testInput, testTarget, batch_size=128)
				print('\nConfiguration : Layers=',hiddenLayersConf,' Epochs=',e,' Learning rate=',lr,' Momentum=',m)
				print('Accuray on train data : ',hist.history.get('acc')[-1])
				print('Accuray on test data : ',scores[1])

				learn.insertModel(bestModels,(network,hist,scores))

				for i in range(len(bestModels)):
					model_json = bestModels[i][0].to_json()


					with open("model_"+str(i)+".json", "w") as json_file:
						json_file.write(model_json)
					bestModels[i][0].save_weights("model_"+str(i)+".h5")


				m = m + 0.1
			lr = lr + 0.001

	learn.getNextLayersConf(hiddenLayersConf,MAX_NEURONS)

	if(hiddenLayersConf == None):
		break
