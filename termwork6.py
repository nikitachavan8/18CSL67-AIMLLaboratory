# Author : Dr.Thyagaraju G S , Context Innovations Lab , DEpt of CSE , SDMIT - Ujire 
# Date : July 11 2018 
#version 1
import random
import csv


attributes = [['Sunny','Rainy'],
              ['Warm','Cold'],
              ['Normal','High'],
              ['Strong','Weak'],
              ['Warm','Cool'],
              ['Same','Change']]


num_attributes = len(attributes)


print (" \n The most general hypothesis : ['?','?','?','?','?','?']\n")
print ("\n The most specific hypothesis : ['0','0','0','0','0','0']\n")

a = []
print("\n The Given Training Data Set \n")

with open('FIND-S.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,delimiter=',')
    for row in reader:
        a.append (row)
        print(row)


print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)

# Comparing with First Training Example 
for j in range(0,num_attributes):
        hypothesis[j] = a[0][j];

# Comparing with Remaining Training Examples of Given Data Set

print("\n Find S: Finding a Maximally Specific Hypothesis\n")

for i in range(0,len(a)):
    if a[i][num_attributes]=='Yes':
            for j in range(0,num_attributes):
                if a[i][j]!=hypothesis[j]:
                    hypothesis[j]='?'
                else :
                    hypothesis[j]= a[i][j] 
    print(" For Training Example No :{0} the hypothesis is ".format(i),hypothesis)
                
print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)


#VERSION 2:


import pandas as pd
import numpy as np
 
#to read the data in the csv file
data = pd.read_csv("C:\\Users\\umk\\Desktop\\EVEN 2021\\LAB AI ML\\FIND-S.csv")
print(data,"n")
 
#making an array of all the attributes
d = np.array(data)[:,:-1]
print("n The attributes are: ",d)
 
#segragating the target that has positive and negative examples
target = np.array(data)[:,-1]
print("n The target is: ",target)
 
#training function to implement find-s algorithm
def train(c,t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
                 
    return specific_hypothesis
 
#obtaining the final hypothesis
print("n The final hypothesis is:",train(d,target))
