from socket import *
serverName = 'localhost'
serverPort = 12000
address = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(address)
request = "GET /index.html HTTP/1.1\r\n"
clientSocket.send(bytes(request,'UTF-8'))
response = clientSocket.recv(2048)
print("response: ", response)
clientSocket.close()