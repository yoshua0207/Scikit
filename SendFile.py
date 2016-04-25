import ftplib
import os

# Terminal
# ftp utili.ddns.net
# enter usename 
# enter password
class SendFile:
	def __init__(self, filename, address, user, passw):
		self.filename = filename
		self.address = address
		self.user = user
		self.passw = passw
		self.counter  = 1

	def send(self):
		ftp = ftplib.FTP(self.address)
		ftp.login(self.user, self.passw)
# filename = "OutputFile1.txt"
# ftp = ftplib.FTP("utili.ddns.net")
# ftp.login("chryssia", "jh2-4012")
# ftp.set_pasv(False)
# ftp.cwd("/Unix/Folder/where/I/want/to/put/file")
# os.chdir(r"\\windows\folder\which\has\file")
		
		# successFile = open('Success.txt','r')
		# fileSize = ftp.GetSizeByName(self.filename + '.txt')
		# while (fileSize < 0): #File does not exist
		# 	wait(1)
		# 	fileSize = ftp.GetSizeByName(self.filename + '.txt')

		myfile = open(self.filename, 'r')
		print 'open file'
    	
    	# ftp.storlines('STOR '+'Success.txt',successFile)
		# else:
    		# myfile = open(self.filename+str(self.counter)+'.txt', 'r')
    		# ftp.storlines('STOR ' + self.filename+'.txt', myfile)
    		# ftp.storlines('STOR '+'Success.txt',successFile)
		# ftp.storlines('STOR ' + self.filename, myfile)
		# ftp.storlines('STOR ' + 'Success.txt',successFile)
		ftp.storlines('STOR ' + self.filename, myfile)
		print 'send file'
		# successFile.close()
		myfile.close()