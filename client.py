import socket
import threading

PASSW = "MR.3X3"

passw = input("Enter The Password: ")
if passw == PASSW:
	print("Welcome :)")
else:
	print("Login Failed")
if passw == PASSW:


	PORT = 5050
	FORMAT = "utf-8"
	D = "DES"
	HEADER = 64
	SERVER = "169.254.78.254"
	ADDR = (SERVER,PORT)
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(ADDR)


	def send(msg):
		MSG = msg.encode(FORMAT)
		msg_len = len(MSG)
		send_len = str(msg_len).encode(FORMAT)
		send_len +=b' '*(HEADER - len(send_len))
		client.send(send_len)
		client.send(MSG)

	def read():
		msg_len = client.recv(HEADER).decode(FORMAT)
		if msg_len:
			msg_len = int(msg_len)
			msg = conn.recv(msg_len).decode(FORMAT)
			print(f"{msg}")

	x = ''
	while 1:
		x = input()
		if x!='DES':
			print("Say AnyThing: ")
			send(x)
		thread = threading.Thread(target=read)
		thread.start()
	send(D)