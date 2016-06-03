import threading
received = 0
sent = 1
count  = 0
while (sent<=10):
	print("sending ", sent)
	ct = threading.Thread()
	ct.start

	# print(threading.current_thread())
	# print("outer ", outer)
	outer += 1
print("I am outside now")