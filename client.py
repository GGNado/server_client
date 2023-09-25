import sys
import socket
def invia_comandi(s):
    print("Ecco un esempio di comandi da poter inviare.\n- ipconfig\n- ls\n- pwd")
    while True:
        messaggio = input("Inserisci messaggio: ")
        if messaggio == "lange":
            print("Chiusura della connessione")
            s.close()
            sys.exit()
        else:
            s.send(messaggio.encode())
            data = s.recv(4096)
            print(str(data, "utf-8"))

def connessione(indirizzo):
    try:
        s = socket.socket()
        s.connect(indirizzo)
        print(f"Connessione al server {indirizzo} stabilita")
    except socket.error as errore:
        print(f"Errore, non riesco a continuare. \nTipo errore: {errore}")
        sys.exit()
    invia_comandi(s)

if __name__ == "__main__":
    connessione(("127.0.0.1", 15000))



