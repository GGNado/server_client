import socket
HOST = "127.0.0.1"
PORT = 24110
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
while True:
	messaggio = input("Scirvi qualoca -> ")
	socket.send(messaggio.encode())
	#socket.close() Se lo vuoi mettere leva il while true oppure crea un modo per uscire dal loop