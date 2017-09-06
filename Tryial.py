from random import seed
from random import randrange
from csv import reader
from math import sqrt
 
import pandas as pd
import numpy as np
z = "Gujarat"
total_x_perc = []
total_x_percP = []

df = pd.read_csv("book1.csv")
df_total = df.iloc[:,-2]
total = list(df_total)


df_states = df.iloc[:,0]
df_states = list(df_states)
#print(df_states)
total_array = np.array(total,dtype=float)
def perc(x):
    ix = df_states.index(x)
    total_x_array = total_array[ix:ix+5]
    
    
    for i in range(4):
        temp = (total_x_array[i+1]-total_x_array[i])*100/total_x_array[i]
        total_x_perc.append(temp)
    


perc(z)

dfP = pd.read_csv("book2.csv")
df_totalP = dfP.iloc[:,1]
totalP = list(df_totalP)
df_statesP = dfP.iloc[:,0]
df_statesP = list(df_statesP)
#print(df_states)
total_arrayP = np.array(totalP,dtype=float)
def percP(x):
    ix = df_statesP.index(x)
    total_x_arrayP = total_arrayP[ix:ix+5]
    
    
    for i in range(4):
        tempP = (total_x_arrayP[i+1]-total_x_arrayP[i])*100/total_x_arrayP[i]
        total_x_percP.append(tempP)
    


percP(z)


 
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy
 
# Calculate root mean squared error

 
# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, train,test):
    test_set = list()
    for row in test:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)
        predicted = algorithm(train, test_set)
        print(predicted)
        
 
# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))
 
# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar
 
# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])
 
# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]
 
# Simple linear regression algorithm
def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions
 
# Simple linear regression on insurance dataset

dataset = []
test = []
train = []
x = list(total_x_perc)
y = list(total_x_percP)


for i in range(3):
    train.append([])
    test.append([])
for i in range(3):
    dataset.append([])

for i in range(3):
    dataset[i].append(x[i])
    dataset[i].append(y[i])
    
for i in range(3):
    train[i].append(x[i])
    train[i].append(y[i])
    
for i in range(3):
    test[i].append(x[3])
    test[i].append(y[3])
    


evaluate_algorithm(dataset, simple_linear_regression, train,test)

