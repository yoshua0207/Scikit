from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from nptdms import TdmsFile
import numpy as np
import pandas as pandas
import ftplib
import datetime
import os
import time
import SendFile
# Data Set


number = 1
model = joblib.load('MachineLearningModel/model.pkl') 
address = "utili.ddns.net"
user = "chryssia"
passw = "jh2-4012"
outputFile = "PowerOutput.txt"
while(1):
	if(number<10):
		randomFile = "SpectralOut_00"+str(number)+".tdms"
		powerFile = "PowerOut_00"+str(number)+".tdms"
	elif(number<100):
		randomFile = "SpectralOut_0"+str(number)+".tdms"
		powerFile = "PowerOut_0"+str(number)+".tdms"
	elif(number<1000):
		randomFile = "SpectralOut_"+str(number)+".tdms"
		powerFile = "PowerOut_"+str(number)+".tdms"
	print randomFile
	if(os.path.exists(randomFile)):
		print "inside " + randomFile
		random_tdms = TdmsFile('Spectral/' + randomFile)
		power_tdms = TdmsFile('Power/' + powerFile)
		b = random_tdms.object(random_tdms.groups()[0], "Untitled")
		c = power_tdms.object(power_tdms.groups()[0],"Untitled")
		x_set=np.array([b.data])
		power_set = np.array([c.data])
		# print(power_set[0])
		for x in range(1, 60):
		    b = random_tdms.object(random_tdms.groups()[0],"Untitled "+str(x))
		    np1=np.array([b.data])
		    x_set = np.concatenate((x_set,np1),axis=0)

		
		predicted=model.predict(x_set)
		# probability = (model.predict_proba(x_set).max(1))
		# for i in range(1,len(probability)):
		# 	if (probability[i] < 0.8):
		# 		predicted[i] = 1

		combined = zip(predicted,power_set[0])
		f = open(outputFile,"a")
		for i in combined:
			f.write(str(i[0])+', '+str(i[1])+'\n')
		f.close()
		# print(probability)# 

		if(number%5==0):
			f = SendFile.SendFile(outputFile, address, user, passw)
			f.send()
			os.remove(outputFile)

		
		number = number + 1


		
# ftp.cwd("/Unix/Folder/where/I/want/to/put/file")
# os.chdir(r"\\windows\folder\which\has\file")

	else:
		time.sleep(5)
