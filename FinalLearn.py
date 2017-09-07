import pandas as pd
import numpy as np
finalpredicted = []

statesList = []
total_percE = []
total_percP = []

states = pd.read_csv("StatesN.csv")
states = states.iloc[:,0]
statesList = list(states)

dfE = pd.read_csv("book1.csv")
df_total = dfE.iloc[:,-2]

totalE = list(df_total)
df_statesE = dfE.iloc[:,0]
df_statesE = list(df_statesE)

dfP = pd.read_csv("book3.csv")
df_totalP = dfP.iloc[:,1]
totalP = list(df_totalP)
df_statesP = dfP.iloc[:,0]
df_statesP = list(df_statesP)

def perc(x,listD,listS):
    total_array = np.array(listD,dtype=float)
    ix = listS.index(x)
    total_x_array = total_array[ix:ix+5]
    listFinal = []
    for i in range(4):
        temp = (total_x_array[i+1]-total_x_array[i])*100/total_x_array[i]
        listFinal.append(temp)
    return listFinal


def evaluate_algorithm(dataset, algorithm, train,test):
    test_set = list()
    for row in test:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)
        predicted = algorithm(train, test_set)
        return predicted
        
def mean(values):
	return sum(values) / float(len(values))
 
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar
 
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])
 
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]
 
def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions
 




def initializeList():
    for i in range(3):
        train.append([])
        test.append([])
        dataset.append([])

def makeTrainData():
    for i in range(3):
        dataset[i].append(x[i])
        dataset[i].append(y[i])
        train[i].append(x[i])
        train[i].append(y[i])
    
def makeTestData():
    for i in range(3):
        test[i].append(x[3])
        test[i].append(y[3])

    
for i in statesList:
    total_percE = perc(i,totalE,df_statesE)
    total_percP = perc(i,totalP,df_statesP)
    dataset = []
    test = []
    train = []
    tempList = []
    x = list(total_percP)
    y= list(total_percE)
    initializeList()
    makeTrainData()
    makeTestData()
    tempList = evaluate_algorithm(dataset, simple_linear_regression, train,test)
    finalpredicted.append(tempList[0])
finalarray = np.array(finalpredicted)
finalarray = finalarray+100
    
df_2016E = dfE.iloc[:,-2]
df_2016Elist = list(df_2016E)
df_16List = []
def E2016(i,df_2016EList,df_statesE):
    ix = df_statesE.index(i)
    temp = df_2016EList[ix+3]
    return temp;
    
    
for i in statesList:
    temp = E2016(i,df_2016Elist,df_statesE)
    df_16List.append(temp)
df_16A = np.array(df_16List)
temp_array = finalarray * df_16A

temp_array = temp_array / 100

Predicted_2017E = list(temp_array)

df_predict = pd.DataFrame({'State':statesList,'2017':Predicted_2017E })

#def PredictEnergy():
    
    