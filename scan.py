#!/usr/bin/python3

import nmap


def main():
    scanner = nmap.PortScanner()
    print("Bienvenue, ceci est un outil d'automatisation simple pour Nmap")
    print("<----------------------------------------------------->")

    ip_addr = input(
        "Veuillez entrer l'adresse IP que vous souhaitez scanner : ")
    print("L'adresse IP que vous avez saisie est :", ip_addr)

    resp = input("""\nVeuillez entrer le type de scan que vous souhaitez exécuter :
                1) Scan SYN ACK
                2) Scan UDP
                3) Scan Complet\n""")
    print("Vous avez sélectionné l'option :", resp)

    resp_dict = {
        '1': ['-v -sS', 'tcp'],
        '2': ['-v -sU', 'udp'],
        '3': ['-v -sS -sV -sC -A -O', 'tcp']
    }

    if resp not in resp_dict.keys():
        print("Entrez une option valide")
    else:
        try:
            print("Version de Nmap :", scanner.nmap_version())
            port_range = input(
                "Veuillez entrer la plage de ports (par exemple, 1-1024) : ")
            scanner.scan(ip_addr, port_range, resp_dict[resp][0])
            scan_info = scanner.scaninfo()

            if scan_info['scanstats']['uphosts'] == '1':
                print("Statut du scanner :", scanner[ip_addr].state())
                print("Ports ouverts :", list(
                    scanner[ip_addr][resp_dict[resp][1]].keys()))
            else:
                print("L'hôte est hors ligne ou inaccessible.")

        except nmap.PortScannerError as e:
            print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    main()
