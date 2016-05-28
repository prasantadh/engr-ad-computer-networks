#Python Code for the Web Server
#import socket module
from socket import *                                  

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1);
print('Ready to serve...')
request_count = 0
while True:
    #Establish the connection
    connectionSocket, addr = serverSocket.accept();  
    try:
        request = connectionSocket.recv(2048) 
        if (request):
            print (request)
            filename = request.decode('UTF-8').split()[1]                 
            f = open(filename[1:])                        
            outputdata = f.read()
            # outputdata = bytes(outputdata,'UTF-8')
            #Send one HTTP header line into socket
            header = bytes("HTTP/1.1 200 OK\r\n\r\n",'UTF-8')
            connectionSocket.send(header)   
            
            #Send the content of the requested file to the client
            # for i in range(0, len(outputdata)):
            #     connectionSocket.send(bytes(outputdata[i],'UTF-8'))
            connectionSocket.send(bytes(outputdata,'UTF-8'))
            request_count = request_count + 1
            
            #close the socket
            print("served ", request_count, " requests.")
            connectionSocket.close()
    except IOError:        
        #Send response message for file not found
        header = bytes("HTTP/1.1 404 Not Found\r\n\r\n",'UTF-8')
        connectionSocket.send(header)                
        
        #Close client socket
        connectionSocket.close()           
serverSocket.close()
