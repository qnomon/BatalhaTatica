from socket import *
import pickle

serverPort = 27123
serverSocket = socket(AF_INET, SOCK_STREAM)
HOST = '127.0.0.1'
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("Aguardando outro jogador\n")
connectionSocket, addr = serverSocket.accept()

tipos = ["Forte", "Rápido", "Técnico"]
option = 4


print("Você pode escolher entre 3 tipos de golpes [1] Forte, [2] Rápido ou [3] Técnico.\n")
print("Funciona como Pedra, Papel e Tesoura. Rápido vence Forte, Forte vence Técnico e o Técnico vence o Rápido.\n")
while option != 99:
    while option<=0 or option>=4:
        option = int(input("\033[97mFaça sua escolha: [1]Forte [2]Rápido [3]Técnico: "))

    received = connectionSocket.recv(1024)
    enemyoption = int.from_bytes(received, byteorder="little")

    if(option == enemyoption):
        response = "Empate"
        print("\033[93mEmpate")
    if((option== 2 and enemyoption == 1) or (option== 1 and enemyoption == 3) or (option== 3 and enemyoption == 2)):
        response = "Derrota"
        print(f"\033[92mVocê Venceu")
    if ((option == 1 and enemyoption == 2) or (option == 3 and enemyoption == 1) or (option == 2 and enemyoption == 3)):
        response = "Vitória"
        print("\033[91mVocê Perdeu")
    connectionSocket.send(pickle.dumps(response))
    option = 4

connectionSocket.close()