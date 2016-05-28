from socket import *
proxyName = '192.168.11.210'
proxyPort = 15000
proxyAddress = (proxyName, proxyPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(proxyAddress)
request = "GET www.google.com/index.html HTTP/1.1\r\n\r\n"
clientSocket.send(bytes(request,'UTF-8'))
response = clientSocket.recv(2048)
print("response: ", response)
clientSocket.close()

# # connect to google and receive a reply
# from socket import *
# serverName = 'www.google.com'
# serverPort = 80
# address = (serverName, serverPort)
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect(address)
# request = "GET /index.html HTTP/1.1\r\n\r\n"
# clientSocket.send(bytes(request,'UTF-8'))
# response = clientSocket.recv(2048)
# print("response: ", response)
# clientSocket.close()