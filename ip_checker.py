
from ipaddress import ip_address

def controlla_ip():
    testo = input("Inserisci un indirizzo IP: ")

    try:
        indirizzo = ip_address(testo)

        print("IP valido!")
        print(f"Versione: IPv{indirizzo.version}")
        print("Indirizzo globale:", indirizzo.is_global)

    except ValueError:
        print("Indirizzo IP non valido!")

controlla_ip()
