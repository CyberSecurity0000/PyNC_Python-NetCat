# Biblioteca
import socket


# SERVIDOR: TCP | UDP
class Server:

    def tcp(ip, porta):

        # Tomada
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, porta))
        s.listen(1)

        print(f"Aguardando conexão TCP {ip} {porta}")
        con, cliente = s.accept()

        con.send("Digite a senha: ".encode())
        senha = con.recv(1024)


        if senha.decode() == "senhafoda123":

            while True:
                
                msg = input("> ")

                if msg == "sair":
                    s.close()
                    break

                msg += "\n"

                # Envio e recebimento
                con.send(msg.encode())
                dados = con.recv(1024).decode()

                print(dados)

            else:
                s.close()


    def udp(ip, porta):

        # Tomada
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((ip, porta))

        print(f"Aguardando conexão UDP {ip} {porta}")

        while True:

            dados, cliente = s.recvfrom(1024)
            print(f"{cliente[0]} - {dados.decode()}")

            msg = input(">")
            s.sendto(msg.encode(), cliente)
