print "helo"
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2222))
s.listen(5)
while True:
	conn, addr = s.accept()
	if data == "close":
	 conn.close()
	else:
	 while True:
	 	data=conn.recv(1024)
	 	if not data:
		 break
		conn.send(data)
	 conn.close()
