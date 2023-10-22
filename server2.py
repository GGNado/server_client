import socket
HOST = "127.0.0.1"
PORT = 24110
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server start on port: {PORT}")
goAgain = True
while goAgain:
	connessione, indirizzo_del_client = server_socket.accept()
	print(f"Connessione stabilita con {indirizzo_del_client}")
	messaggio = connessione.recv(1024).decode()
	print(messaggio)
	connessione.close()
