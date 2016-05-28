from socket import *
from random import randint
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
	
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
serverPort = 15000
tcpSerSock.bind(('',serverPort))
tcpSerSock.listen(1)

while 1:
	# Start receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	message = tcpCliSock.recv(2048)
	print(message)
	# Extract the filename from the given message
	print(message.decode('UTF-8').split()[1])
	filename = message.decode('UTF-8').split()[1].partition("/")[2]
	print("filename: ",filename)
	fileExist = "false"
	filetouse = "/" + filename
	print("file_to_use ",filetouse)
	try:
		# Check whether the file exist in the cache
		f = open(filetouse[1:], "r")                      
		outputdata = f.readlines()                        
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send(bytes("HTTP/1.0 200 OK\r\n", 'UTF-8'))            
		tcpCliSock.send(bytes("Content-Type:text/html\r\n\r\n",'UTF-8'))
		response = f.read()
		tcpCliSock.send(bytes(response,'UTF-8'))
		print('Sent from cache')     
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false": 
			# Create a socket on the proxyserver
			c = socket(AF_INET, SOCK_STREAM)
			hostn = message.decode('UTF-8').split()[1].partition("/")[0].replace("www.","",1)                  
			print("hostname: ", hostn)                                   
			try:
				# Connect to the socket to port 80
				c.connect((hostn, 80))
				print("connected to: ", hostn)
				c.send(message)
				response = c.recv(2048)

				# Create a new file in the cache for the requested file. 
				# Also send the response to the client socket and the corresponding file in the cache
				tcpCliSock.send(response)
				tmpFile = open("./" + filename,"wb")
				tmpFile.write(response)
				tmpFile.close()  			
			except:
				print("Illegal request")                                               
		else:
			# HTTP response message for file not found
			header = bytes("HTTP/1.1 404 Not Found\r\n\r\n", 'UTF-8')
			tcpCliSock.send(header)
	# Close the client and the server sockets    
	tcpCliSock.close() 
tcpSerSock.close()