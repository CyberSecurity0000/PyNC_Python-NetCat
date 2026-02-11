# Biblioteca
import sys, os
from Server import server
from Client import client


# SERVIDOR: TCP | UDP
def servidor():
    
    if len(sys.argv) != 5:
        print(f"# Usage: python3 {sys.argv[0]} --server --port <porta> --tcp")
        print(f"# Usage: python3 {sys.argv[0]} --server --port <porta> --udp")

    else:
        # IP
        ip = "0.0.0.0"              # Arg: 2 - IP (não precisa ser passado)

        # Porta
        param_porta = sys.argv[2]       # Arg: 3 (--port)
        porta       = int(sys.argv[3])  # Arg: 4 - Porta (precisa ser passado)

        # Conexão
        param_tcp = sys.argv[4]     # Arg: 5 (--tcp)
        param_udp = sys.argv[4]     # Arg: 5 (--udp)

        try: 
            if param_tcp == "--tcp":
                server.Server.tcp(ip, porta)

            elif param_udp == "--udp":
                server.Server.udp(ip, porta)

            else:
                print("Conexão invalida !")

        except KeyboardInterrupt as e:
            print("Programa interrompido !")
    
        except OverflowError as e:
            print("Porta inválida !")


# CLIENTE: TCP | UDP
def cliente():

    if len(sys.argv) != 7:
        print(f"# Usage: python3 {sys.argv[0]} --client --ip <ip> --port <porta> --tcp")
        print(f"# Usage: python3 {sys.argv[0]} --client --ip <ip> --port <porta> --udp")

    else:

        # IP
        param_ip = sys.argv[2]  # Arg: 2 (--ip)
        ip       = sys.argv[3]  # Arg: 3 (127.0.0.1)

        # Porta
        param_porta = sys.argv[4]       # Arg: 2 (--port)
        porta       = int(sys.argv[5])  # Arg: 3 - Porta

        # Conexão
        param_tcp = sys.argv[6]     # Arg: 4 (--tcp)
        param_udp = sys.argv[6]     # Arg: 5 (--udp)

        try: 
            if param_tcp == "--tcp":
                client.Client.tcp(ip, porta)

            elif param_udp == "--udp":
                client.Client.udp(ip, porta)

            else:
                print("Conexão invalida !")

        except KeyboardInterrupt as e:
            print("Programa interrompido !")
    
        except OverflowError as e:
            print("Porta inválida !")


def main():

    try:
        opc = sys.argv[1]

        if opc == "--client":
            cliente()

        elif opc == "--server":
            servidor()

    except:
        
        os.system("clear")
        print("=-= Manual =-=\n")
        
        print("- SERVER")
        print(f"# Usage: python3 {sys.argv[0]} --server --port <porta> --tcp")
        print(f"# Usage: python3 {sys.argv[0]} --server --port <porta> --udp")

        print("\n- CLIENT")
        print(f"# Usage: python3 {sys.argv[0]} --client --ip <ip> --port <porta> --tcp")
        print(f"# Usage: python3 {sys.argv[0]} --client --ip <ip> --port <porta> --udp")


# Execução
main()
