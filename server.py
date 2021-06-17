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
	HEADER = 64
	FORMAT = "utf-8"
	D = "DES"
	SERVER = socket.gethostbyname(socket.gethostname())
	#127.0.0.1
	ADDR = (SERVER, PORT)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)

	def send(msg, client):
		MSG = msg.encode(FORMAT)
		msg_len = len(MSG)
		send_len = str(msg_len).encode(FORMAT)
		send_len +=b' '*(HEADER - len(send_len))
		client.send(send_len)
		client.send(MSG)


	def client(conn, addr,clients):

		print(f"{addr} is connected")
		connected = True
		while connected:
			msg_len = conn.recv(HEADER).decode(FORMAT)
			if msg_len:
				msg_len = int(msg_len)
				msg = conn.recv(msg_len).decode(FORMAT)
				if msg == D:
					connected = False
				print(f"{addr} {msg}")
			for client in clients:
				if client != conn:
					send(msg,client)
		conn.close()

	def start():
		server.listen()
		print("The Server Is Listining To {SERVER}")
		clients = []
		while True:
			conn, addr = server.accept()
			clients.append(conn)
			thread = threading.Thread(target=client, args=(conn, addr, clients))
			thread.start()


	print("The Server Is Starting")
	print("This Script Made By MR.3X3")
	start()
