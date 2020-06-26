import csv
import numpy as np

# process data #

# months in the file : Feb - Mar - May - June - Jul - Aug - Sep - Oct - Nov - Dec
# VisitorType in the file : Returning_Visitor - New_Visitor - Other

# Give numeric value to the : Month + VisitorType + Weekend + Revenue

# For months : Jan(1) - Feb(2) - Mar(3) - Apr(4) - May(5) - June(6) -
# Jul(7) - Aug(8) - Sep(9) - Oct(10) - Nov(11) - Dec(12)
# For VisitorType : Returning_Visitor(1) - New_Visitor(-1) - Other(0)
# for Weekend : TRUE(1) FALSE(0)
# for Revenue : TRUE(1) FALSE(0)


def prepare_data(file, lines, columns):

    DATA_SET = np.empty([lines, columns+1])
    i = 0
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            if line[10] == "Jan": line[10] = 1
            if line[10] == "Feb": line[10] = 2
            if line[10] == "Mar": line[10] = 3
            if line[10] == "Apr": line[10] = 4
            if line[10] == "May": line[10] = 5
            if line[10] == "June": line[10] = 6
            if line[10] == "Jul": line[10] = 7
            if line[10] == "Aug": line[10] = 8
            if line[10] == "Sep": line[10] = 9
            if line[10] == "Oct": line[10] = 10
            if line[10] == "Nov": line[10] = 11
            if line[10] == "Dec": line[10] = 12
            if line[15] == "Returning_Visitor": line[15] = 1
            if line[15] == "New_Visitor": line[15] = 0
            if line[15] == "Other": line[15] = 2
            if line[16] == "TRUE": line[16] = 1
            if line[16] == "FALSE": line[16] = 0
            if line[17] == "TRUE": 
               line[17] = 0
               line.append(1)
            if line[17] == "FALSE": 
               line[17] = 1
               line.append(0)

            DATA_SET[i] = np.asarray(line)
            i = i + 1
    return DATA_SET


def extractInputs(data):
    return data[:,:-2]

def extractTargets(data):
    return data[:,-2:]

def divideData(inputs,targets,trainRatio,valRatio,testRatio):
	trainSetSize = int(trainRatio*len(inputs))
	validationSetSize = int(valRatio*len(inputs))
	testSetSize = int(testRatio*len(inputs))

	trainInput = inputs[0:trainSetSize]
	validationInput = inputs[trainSetSize:trainSetSize+validationSetSize]
	testInput = inputs[trainSetSize+validationSetSize:]

	trainTarget = targets[0:trainSetSize]
	validationTarget = targets[trainSetSize:trainSetSize+validationSetSize]
	testTarget = targets[trainSetSize+validationSetSize:]

	return (trainInput,validationInput,testInput,trainTarget,validationTarget,testTarget)

#data = prepare_data('online_shoppers_intention.csv', 12330, 18)

# Extracting inputs and output

# Extracting inputs
#inputs = data[:, :-1]

# Extracting output
#outputs = np.empty([12330, 1])
#j = 0

#for i in data:
    #outputs[j] = data[j][17]

#normalize(inputs)

#print(data[0, -1])







