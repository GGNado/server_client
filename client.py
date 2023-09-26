import sys
import socket

#Funzione che invia comandi o messaggi al server. Prende come parametro il socket
def invia_comandi(s):
    print("Ecco un esempio di comandi da poter inviare.\n- ipconfig\n- ls\n- pwd")
    #Aspettiamo sempre l'input del client
    while True:
        messaggio = input("Inserisci messaggio: ")
        #Se il messaggio è == a lange, la connessione al server si chiuderà
        if messaggio == "lange":
            print("Chiusura della connessione")
            #Chiusura socket
            s.close()
            #Chiusura applicazione
            sys.exit()
        else:
            #attraverso il send inviamo il messaggio che pero' deve essere trasmesso in bytes
            s.send(messaggio.encode())
            #Qui riceviamo una risposta dal server in un buffer da 4096 bytes
            data = s.recv(4096)
            #Stampiamo a schermo decodificando il messaggio in bytes ricevuto
            print(str(data, "utf-8"))

#Funzione che crea la connessione al server che prende come parametro un indirizzo
def connessione(indirizzo):
    try:
        #Creazione socket
        s = socket.socket()
        #proviamo a connetterci
        s.connect(indirizzo)
        print(f"Connessione al server {indirizzo} stabilita")
    except socket.error as errore:
        print(f"Errore, non riesco a continuare. \nTipo errore: {errore}")
        sys.exit()
    #Se tutto è andato a buon fine possiamo inviare comandi
    invia_comandi(s)

if __name__ == "__main__":
    #Porta a nostro piacimento
    connessione(("127.0.0.1", 15000))



