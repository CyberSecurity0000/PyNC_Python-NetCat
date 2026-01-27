# Importa rede e argumentos do terminal
import socket, sys

# IP do servidor (1° argumento)
ip = sys.argv[1]

# Porta do servidor (2° argumento)
porta = int(sys.argv[2])

# Cria um socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop infinito de envio e recebimento
while True:

    # Envia a mensagem digitada para o servidor
    s.sendto(input("# ").encode(), (ip, porta))

    # Recebe a resposta do servidor (até 1024 bytes)
    msg_server, ip_server = s.recvfrom(1024)

    # Mostra a resposta na tela
    print(f"\n* Server ({ip_server[0]}): {msg_server.decode()}")
