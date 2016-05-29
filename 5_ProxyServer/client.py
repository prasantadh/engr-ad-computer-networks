from socket import *
proxyName = '10.225.45.166'
proxyPort = 15000
proxyAddress = (proxyName, proxyPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(proxyAddress)
request = "GET www.google.com/index.html HTTP/1.1\r\n\r\n"
clientSocket.send(bytes(request,'UTF-8'))
response = clientSocket.recv(2048)
print("response: ", response)
clientSocket.close()
