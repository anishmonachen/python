import socket

def Main():
		host = '127.0.0.1'
		port = 5001
		
		mySocket = socket.socket()
		mySocket.connect((host,port))
		
		message = input(" Enter your message: ")
              		
		while message != 0 :
				mySocket.send(message.encode())
				data = mySocket.recv(1024).decode()
				
				print ('Client 2: ' + data)
				
				message = input(" You:")
				
		mySocket.close()

if __name__ == '__main__':
	Main()
