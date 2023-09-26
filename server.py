import socket
import subprocess

#Funzione che risponde in base al messaggio inviato, prende in input la connessione con il client
def ricevi_comando(connessione):
	while True:
		#Riceviamo una richiesta
		richiesta = connessione.recv(4096)
		print(f"L'utente ha inviato: {richiesta.decode()}")

		#Messaggi predefiniti di risposta
		if richiesta.decode().lower() == "ciao":
			messaggio = "Ciao user, come stai?".encode()
			connessione.send(messaggio)
		elif richiesta.decode().lower() == "gruppo":
			messaggio = "Progetto fatto da Vasil, Lange, Luigi, Christian".encode()
			connessione.send(messaggio)
		elif richiesta.decode().lower() == "link":
			messaggio = "Link powerpoint: https://www.canva.com/design/DAFvdgu15F4/ury6Jyhj3oGIKI6_mKcytA/view?utm_content=DAFvdgu15F4&utm_campaign=designshare&utm_medium=link&utm_source=editor\nLink codice: https://github.com/GGNado/server_client".encode()
			connessione.send(messaggio)
		else:
			#Entriamo qui se il messaggio predefinito non esiste, probabilmente perchè l'utente ha inviato un comando come ls
			risposta = subprocess.run(richiesta.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			data = risposta.stdout + risposta.stderr
			#Se il comando non esiste risponderà con [comando]: command not found
			connessione.send(data)

def server(indirizzo, backlog=1):
	try:
		s = socket.socket()
		#con bind diciamo al socket di fare da server passandogli l'indirizzo dove i client manderanno richieste
		s.bind(indirizzo)
		#Con backlog diciamo quante connessioni in attesa posso esserci
		s.listen(backlog)
		print("Server pronto e in ascolto")
	except socket.error as errore:
		print(f"Errore. \nTipo errore {errore}.\nProvo a ristartare")
		#Richiamiamo la funzione in caso ci sia stato qualche errore di avvio
		server(indirizzo)

	#Il client si sta connettendo
	connessione, indirizzo_del_client = s.accept()
	print(f"Connessione stabilita con {indirizzo_del_client} ")
	#Pronto a ricevere
	ricevi_comando(connessione)

if __name__ == "__main__":
	#Porta a nostro piacimento
	server(("127.0.0.1", 15000))
