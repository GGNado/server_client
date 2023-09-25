import socket
import subprocess


def ricevi_comando(connessione):
	while True:
		richiesta = connessione.recv(4096)
		print(f"L'utente ha inviato: {richiesta.decode()}")

		if richiesta.decode().lower() == "ciao":
			messaggio = "Ciao user, come stai?".encode()
			connessione.send(messaggio)
		elif richiesta.decode().lower() == "gruppo":
			messaggio = "Progetto fatto da Vasil, Lange, Luigi, Christian".encode()
			connessione.send(messaggio)
		elif richiesta.decode().lower() == "link":
			messaggio = "Link powerpoint: https\nLink codice: https".encode()
			connessione.send(messaggio)
		else:
			risposta = subprocess.run(richiesta.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			data = risposta.stdout + risposta.stderr
			connessione.send(data)

def server(indirizzo, backlog=1):
	try:
		s = socket.socket()
		s.bind(indirizzo)
		s.listen(backlog)
		print("Server pronto e in ascolto")
	except socket.error as errore:
		print(f"Errore. \nTipo errore {errore}.\nProvo a ristartare")
		server(indirizzo)
	connessione, indirizzo_del_client = s.accept()
	print(f"Connessione stabilita con {indirizzo_del_client} ")
	ricevi_comando(connessione)

if __name__ == "__main__":
	server(("127.0.0.1", 15000))
