from socket import *
import pickle


serverName = "127.0.0.1"
serverPort = 27123
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

tipos = ["Forte", "Rápido", "Técnico"]
option = 4
color = '\033[93m'

print("Você pode escolher entre 3 tipos de golpes [1] Forte, [2] Rápido ou [3] Técnico.\n")
print("Funciona como Pedra, Papel e Tesoura. Rápido vence Forte, Forte vence Técnico e o Técnico vence o Rápido.\n")

while option != 99:
    while option <= 0 or option >= 4:
        option = int(input("\033[97mFaça sua escolha: [1]Forte [2]Rápido [3]Técnico: "))

    x = option.to_bytes((option.bit_length() + 7) // 8, byteorder='little')
    clientSocket.send(bytes(x))
    result = clientSocket.recv(1024)
    option = 4
    text = pickle.loads(result)
    if(text == "Empate"):
        color = '\033[93m'
    if (text == "Vitória"):
        color = '\033[92m'
    if (text == "Derrota"):
        color = '\033[91m'
    print(color+text)
clientSocket.close()
