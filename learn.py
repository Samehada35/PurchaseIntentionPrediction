import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
import mathfunc as mf

def insertModel(bestModels,model):
	if(len(bestModels)<3):
		bestModels.append(model)
		bestModels.sort(key=lambda x : (x[1].history.get('acc')[-1],x[2][1]), reverse=True)
	else:
		if((model[1].history.get('acc')[-1] > bestModels[2][1].history.get('acc')[-1]) and model[2][1] > bestModels[2][2][1]):
			bestModels[2] = model
			bestModels.sort(key=lambda x : (x[1].history.get('acc')[-1],x[2][1]), reverse=True)

def getNextLayersConf(conf,max):
	if(len(conf)==1 and conf[0]==max):
		conf[0] = 10;
		conf.append(10);
	elif(len(conf)==1):
		conf[0] = conf[0]+10
	elif(len(conf)==2 and conf[1]==max):
		if(conf[0] == max):
			conf[0] = 10
			conf[1] = 10
			conf.append(10)
		else:
			conf[0] = conf[0] + 10
			conf[1] = 10
	elif(len(conf)==2):
		conf[1] = conf[1] + 10
	elif(len(conf)==3 and conf[2]==max):
		if(conf[1] == max):
			if(conf[0] == max):
				conf = None
			else:
				conf[0] = conf[0] + 10
				conf[1] = 10
				conf[2] = 10
		else:
			conf[1] = conf[1] + 10
			conf[2] = 10
	else:
		conf[2] = conf[2] + 10
		

def plotGraphs(hist,score,trainTargets,trainOutputs,validationTargets,validationOutputs,testTargets,testOutputs):

	miny = min(hist.history['val_loss'])
	minx = hist.history['val_loss'].index(miny)


	plt.subplots(num=None, figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')

	plt.subplot(2,2,1)
	plt.plot(hist.history['loss'],label='Performance',color='red',linewidth=2)
	plt.plot(hist.history['val_loss'],label='Performance',color='green',linewidth=2)
	plt.legend(['Train','Validation'])
	plt.yscale('linear')
	plt.xlabel('Epochs')
	plt.ylabel('Performance')
	plt.title('Best validation performance is '+str(round(miny,4))+' at epoch '+str(minx))


	plt.subplot(2,2,2)
	plt.plot(hist.history['acc'],color='red',label='Regression',linewidth=2)
	plt.plot(hist.history['val_acc'],color='green',label='Regression',linewidth=2)
	plt.legend(['Train','Validation'])
	plt.yscale('linear')
	plt.xlabel('Epochs')
	plt.ylabel('Accuracy')
	plt.title('Accuracy according to epochs')


	trainTargetsSoftmax = [mf.softmax(t) for t in trainTargets]
	validationTargetsSoftmax = [mf.softmax(t) for t in validationTargets]
	testTargetsSoftmax = [mf.softmax(t) for t in testTargets]

	plt.subplot(2,2,4)

	targets = np.argmax(trainTargetsSoftmax,axis=1)
	outputs = np.amax(trainOutputs,axis=1)


	a,b = np.polyfit(targets,outputs,deg=1)
	f = lambda x : a*x+b
	plt.plot(targets,f(outputs),color='red',linewidth=2)


	targets = np.argmax(validationTargetsSoftmax,axis=1)
	outputs = np.amax(validationOutputs,axis=1)
	a,b = np.polyfit(targets,outputs,deg=1)
	f = lambda x : a*x+b
	plt.plot(targets,f(outputs),color='green',linewidth=2)


	targets = np.argmax(testTargetsSoftmax,axis=1)
	outputs = np.amax(testOutputs,axis=1)
	a,b = np.polyfit(targets,outputs,deg=1)
	f = lambda x : a*x+b
	plt.plot(targets,f(outputs),color='blue',linewidth=2)


	plt.yscale('linear')
	plt.xlabel('Targets')
	plt.ylabel('Outputs')


	plt.subplot(2,2,3)
	plt.hist([hist.history['loss'],hist.history['val_loss']],np.linspace(-1, 1, 20),color=['red','green'],label=['Train','Validation'])
	plt.legend(['Train','Validation'])
	plt.xlabel('Errors = Targets - Outputs')
	plt.ylabel('Instances')
	plt.title('Error histogram with 20 bins')


	plt.show()
