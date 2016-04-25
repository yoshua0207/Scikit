from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from nptdms import TdmsFile
import numpy as np
import pandas as pandas
# lampTrain1 = np.genfromtxt('/Users/Chryssia/Desktop/SchoolStuff/Gatech/ECE4011/SeniorDesign/Scikit/MachineLearningData/Lamp/LampAverage_1.csv',delimiter=' ',dtype=None)

# Item ID
# 1. No load
# 2. Lamp
# 3. Hair Drier
# 4. Small Blender
# 5. Big Blender
# 6. Hand Mixer
# 7. TV Box
# 8. Hair Drier and Lamp

# Lamp Training
lamp_tdms = TdmsFile("Lamp_001.tdms")
a = lamp_tdms.object("Untitled","Untitled 5")

x_train=np.array([a.data])
y_train = np.array(['2'])
for x in range(1, 10):
    a = lamp_tdms.object("Untitled","Untitled "+str(x*5))
   
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[2]),axis=0)

# Hair Drier Training
hairDrier_tdms = TdmsFile("HairDyer_001.tdms")
for x in range(1, 11):
    a = hairDrier_tdms.object("Untitled","Untitled "+str(x*5))
  
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[3]),axis=0)

# No Load Training
noLoad_tdms = TdmsFile("NoLoad_001.tdms")
for x in range(1, 11):
    a = noLoad_tdms.object("Untitled","Untitled "+str(x*5))
 
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[1]),axis=0)

# Small Blender Training
smallBlender_tdms = TdmsFile("SmallBlender_001.tdms")
for x in range(1, 11):
    a = smallBlender_tdms.object("Untitled","Untitled "+str(x*5))
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[4]),axis=0)

# Big Blender Training
bigBlender_tdms = TdmsFile("BigBlender_001.tdms")
for x in range(1, 11):
    a = bigBlender_tdms.object("Untitled","Untitled "+str(x*5))
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[5]),axis=0)

# Hand Mixer Training
handMixer_tdms = TdmsFile("HandMixer_001.tdms")
for x in range(1, 21):
    a = handMixer_tdms.object("Untitled","Untitled "+str(x*2))
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[6]),axis=0)

# # Hair drier and lamp Training
hairDrier_and_Lamptdms = TdmsFile("HairDrierAndLamp_001.tdms")
for x in range(1, 21):
    a = hairDrier_and_Lamptdms.object("Untitled","Untitled "+str(x*2))
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[8]),axis=0)

# TVBOX
TVBOXtdms = TdmsFile("TVBox.tdms")
for x in range(1, 21):
    a = TVBOXtdms.object("Untitled","Untitled "+str(x*2))
    np1=np.array([a.data])
    x_train = np.concatenate((x_train,np1),axis=0)
    y_train = np.concatenate((y_train,[7]),axis=0)


 


# # Data Set
# random_tdms = TdmsFile("Random3_001.tdms")
# b = random_tdms.object("Untitled", "Untitled")
# x_set=np.array([b.data])


# for x in range(1, 60):
#     b = random_tdms.object("Untitled","Untitled "+str(x))
#     np1=np.array([b.data])
#     x_set = np.concatenate((x_set,np1),axis=0)



# Model Fit
model=KNeighborsClassifier(n_neighbors = 5)
model.fit(x_train,y_train)
joblib.dump(model, 'model.pkl') 
# Prediction
# predicted=model.predict(x_set)
# probability = model.predict_proba(x_set)
# print("predicted")
# print(predicted)
# print(probability)
# print("expected")
# print(expected)
