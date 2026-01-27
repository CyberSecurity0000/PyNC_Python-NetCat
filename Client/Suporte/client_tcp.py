# Biblioteca
import socket, sys

ip = sys.argv[1]
porta = int(sys.argv[2])

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
