# Biblioteca
import socket


class Client:

        def tcp(ip, porta):

            # Tomada
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, porta))

            resp_server = s.recv(1024).decode()

            senha = input(resp_server)
            s.send(senha.encode())

            while True:
            
                print(f"> Servidor: {s.recv(1024).decode()}")
                #s.send(input("# " + "\n").encode())
                s.send(input("# ").encode())


        def udp(ip, porta):

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
