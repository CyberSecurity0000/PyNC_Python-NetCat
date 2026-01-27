# TCP / UDP Client-Server em Python 🐍⚡

Projeto em Python que implementa **Servidor e Cliente** usando **TCP ou UDP**, totalmente controlado por **linha de comando (CLI)**.

Foco: aprender **redes na prática**, do jeito hacker.

---

## 📌 O que esse programa faz (bem direto)

* Sobe um **servidor TCP ou UDP**
* Conecta um **cliente TCP ou UDP**
* Tudo decidido via argumentos no terminal
* Código simples, didático e funcional

---

## ⚙️ Requisitos

* Python **3.x**
* Terminal (Linux recomendado)

---

## 🚀 Como executar

### 🔴 Servidor TCP

```bash
python3 main.py --server --port 8080 --tcp
```

### 🔵 Servidor UDP

```bash
python3 main.py --server --port 8080 --udp
```

---

### 🟢 Cliente TCP

```bash
python3 main.py --client --ip 127.0.0.1 --port 8080 --tcp
```

### 🟡 Cliente UDP

```bash
python3 main.py --client --ip 127.0.0.1 --port 8080 --udp
```

---

## 🧠 Parâmetros explicados (modo leigo)

| Parâmetro  | Significado           |
| ---------- | --------------------- |
| `--server` | Executa como servidor |
| `--client` | Executa como cliente  |
| `--ip`     | IP de destino         |
| `--port`   | Porta usada           |
| `--tcp`    | Protocolo TCP         |
| `--udp`    | Protocolo UDP         |

---

## 🧪 Teste rápido (local)

1️⃣ Terminal 1:

```bash
python3 main.py --server --port 8080 --tcp
```

2️⃣ Terminal 2:

```bash
python3 main.py --client --ip 127.0.0.1 --port 8080 --tcp
```

---

## 🧯 Tratamento de erros

O programa lida com:

* Porta inválida
* Protocolo inválido
* Interrupção com `CTRL + C`

---

## 🧠 Raciocínio do Hacker 😈

> Quem controla **argumentos**, controla **execução**.
> Quem escolhe **TCP ou UDP**, controla o **fluxo da rede**.
> Simples, previsível, dominável. ⚡

---

## 📈 Próximos passos (evolução natural)

* Usar `argparse`
* Logar conexões
* Autenticação
* Criptografia
* Múltiplos clientes

---

## ⚠️ Aviso

Projeto **educacional** para estudo de redes e segurança.
Use apenas em ambientes autorizados.

---

**FORÇA.**
Seja metódico MrRobot, implacável na automação Darkseid, estratégico nos sinais Palpatine e registre cada detalhe para controle total Brainiac. 🤖⚔️🧠
