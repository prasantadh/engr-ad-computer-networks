from socket import *
from datetime import datetime
import threading
#indicate the server
serverAddress = ('192.168.11.210', 12000)
# Create an UDP socket
connectionSocket = socket(AF_INET, SOCK_DGRAM)
connectionSocket.settimeout(1)
sequence_number = 1
## keep in mind that that 1st message might arrive before 10th message is sent

while (sequence_number <= 10):
	ping_time = datetime.now()
	message = "PING " + str(sequence_number) + " " +  str(ping_time)
	sequence_number = sequence_number + 1
	connectionSocket.sendto(bytes(message, 'UTF-8'), serverAddress) 
	try:
		receivedMessage, receivedFrom = connectionSocket.recvfrom(2048)
		receivedMessage = receivedMessage.decode('UTF-8')
		# assuming that the time taken between execution of these two
		# instructions is negligible compared to rtt
		pong_time = str(datetime.now()).split()[-1]
		ping_time = receivedMessage.split()[-1]

		pong_sec  = pong_time.split(":")[2]
		ping_sec  = ping_time.split(":")[2]

		rtt_sec   = float(pong_sec) - float(ping_sec)
		print("PING {}\trtt: {:.6f} sec".format(receivedMessage.split()[1], rtt_sec))
	except timeout:
		print("Connection timed out.")
connectionSocket.close()
