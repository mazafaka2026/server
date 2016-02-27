print "helo"
import socket
data=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2222))
s.listen(5)
while True:
	conn, addr = s.accept()
	 while True:
	 	data=conn.recv(1024)
	 	if not data:
			break
		conn.send(data)
	if data == "close":
		conn.close()
