from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from nptdms import TdmsFile
import numpy as np
import pandas as pandas
import ftplib
import datetime
 
# server = 'ENTER_YOUR_SERVER_ADDRESS'
# username = 'ENTER_YOUR_USERNAME'
# password = 'ENTER_YOUR_PASSWORD'
# ftp_connection = ftplib.FTP(server, username, password)
# remote_path = "/content/"
# ftp_connection.cwd(remote_path)
# fh = open("C:/tempupload/a.txt", 'rb')
# ftp_connection.storbinary('STOR a.txt', fh)
# fh.close()

# Data Set
random_tdms = TdmsFile("Spectral/SpectralOut_001.tdms")
power_tdms = TdmsFile("Power/PowerOut_001.tdms")
b = random_tdms.object("Untitled", "Untitled")
c = power_tdms.object("Untitled","Untitled")
x_set=np.array([b.data])
power_set = np.array([c.data])
# print(power_set[0])
for x in range(1, 60):
    b = random_tdms.object("Untitled","Untitled "+str(x))
    np1=np.array([b.data])
    x_set = np.concatenate((x_set,np1),axis=0)

# for y in range(1, 60):
#     c = random_tdms.object("Untitled","Untitled "+str(y))
#     np1=np.array([c.data])
#     # power_set = np.concatenate((power_set,np1),axis=0)

# print(power_set)
model = joblib.load('model.pkl') 
predicted=model.predict(x_set)
probability = model.predict_proba(x_set)
print("predicted")
# print(predicted)
# print(power_set[0])
# print(type(predicted))
# print(type(power_set))
combined = zip(predicted,power_set[0])
f = open("OutputFile1.txt","w")
for i in combined:
	f.write(str(i[0])+', '+str(i[1])+'\n')
f.close()

print probability
print combined
