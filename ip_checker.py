
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


while True:
    print("\n--- PYTHON IP CHECKER ---")
    print("1. Controlla un indirizzo IP")
    print("2. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        controlla_ip()

    elif scelta == "2":
        print("Programma terminato.")
        break

    else:
        print("Scelta non valida!")

