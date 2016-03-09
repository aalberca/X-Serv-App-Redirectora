#este ejercicio hace redirecciones a nosotros mismos
import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind(('localhost', 8080))

mySocket.listen(5)

print mySocket
try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'Requiest received:'
		print recvSocket.recv(1301)
		print 'Answering back...'
		numero = random.randint(0, 10000000000000)
		print recvSocket.send("HTTP/1.1 302 Found\r\n\r\n" +
							  "<html><head>" +
							  #'<Location="http://google.es">' +
							  '<meta http-equiv="refresh" content="0;url=http://localhost:8080" />' +
							  "</head><html>" + "\r\n")

		recvSocket.close()

except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
