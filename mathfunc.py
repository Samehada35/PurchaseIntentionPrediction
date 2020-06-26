import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
	return 1/(1+np.exp(-x))

def sigmoidDerivative(x):
	return sigmoid(x)*(1-sigmoid(x))

def error(x,y):
	return np.power(x-y,2)

def softmax(x):
	return np.exp(x)/np.sum(np.exp(x))

def mse(x,y):
	sum = 0

	for i in range(len(x)):
		sum = sum + error(x[i],y[i])

	return sum/len(x)

def errorDerivative(x,y):
	return 2*(x-y)

def normalize(inputs):
    # Normalizing inputs (test on first K)
    mean = 0
    sigma = 0

    for K in range(len(inputs)):

        # Calculate the mean (first step)
        for j in inputs[K]:
            mean = mean + j

        mean = mean / len(inputs[K])

        j = 0
        for j in range(17):
            inputs[j] = inputs[j] - mean

        # Calculate variance (second step)
        for j in inputs[K]:
            sigma = sigma + np.power(j, 2)

        sigma = sigma / len(inputs[K])

        for j in range(17):
            inputs[K] = inputs[K] / sigma


def standardize(inputs):

    for K in range(len(inputs)):
        min = inputs[K].min()
        max = inputs[K].max()

        for i in range(len(inputs[K])):
            inputs[K][i] = (inputs[K][i] - min) / (max - min)

def regression(x,y):

	meanX = np.mean(x)
	meanY = np.mean(y)


	crossDeviation = np.sum(y*x-len(x)*meanX*meanY)
	deviation = np.sum(x*x-len(x)*meanX*meanX)

	a = crossDeviation/deviation
	b = meanY-a*meanX

	return (a,b)

def plotRegression(x,y,a,b):
	plt.scatter(x,y,color= "m",marker="o",s=30)

	out = a*x+b

	plt.plot(x,out,color="g")

	plt.xlabel('Size')
	plt.ylabel('Cost')

	plt.show()

def plotErrorHist(errors):
	plt.hist(errors,density =False,bins=20)
	plt.ylabel('Instances')
