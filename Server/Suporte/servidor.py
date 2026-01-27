# Biblioteca
import socket, sys


def log(msg, v):

    with open("servidor.log", "a") as log:
        log.write(msg + "\n")

    if v == "-v":
        print(msg)


ip = "0.0.0.0"
porta = int(sys.argv[1])

try:
    verbose = sys.argv[2]

except Exception as e:
    verbose = 0

# Tomada
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, porta))
s.listen(1)

log(f"Aguardando conexão {ip} {porta}", verbose)
con, cliente = s.accept()

con.send("Digite a senha: ".encode())
senha = con.recv(1024)


if senha.decode() == "senhafoda123":
    
    log(f"{cliente} acertou a senha", verbose)

    while True:
        
        msg = input(">")

        if msg == "sair":
            s.close()
            break    

        msg += "\n"

        con.send(msg.encode())
        dados = con.recv(1024)

        print(dados.decode())

else:
    log(f"{cliente} errou a senha", verbose)
    s.close()
