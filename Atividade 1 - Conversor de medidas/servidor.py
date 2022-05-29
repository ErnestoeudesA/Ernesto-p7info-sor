import socket
import pickle   # Importação dos módulos que serão utilizados no código.

svsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do socket TCP.

host = "127.0.0.1"
port = 2121  # Variáveis


svsocket.bind((host, port))
svsocket.listen()  # Aberto para requisições.

try:
    clisocket, addr = svsocket.accept()  # Conexão aceita. Caso não funcione, uma mensagem será enviada.
except:
    print("Conexão não realizada, tente novamente.")

# Recebe os valores do cliente para serem utilizados no código.

def receiveDataServer():
    receiveCli = clisocket.recv(1024)
    receiveCli = pickle.loads(receiveCli)
    print(receiveCli)
    return receiveCli

# Envia os valores já atualizados de acordo com as requisições para o cliente.

def sendDataServer(sendCli):
    sendCli = pickle.dumps(sendCli)
    clisocket.send(sendCli)

# Função para executar as fórmulas de cada conversão de acordo com a escolha do cliente.
# Nesse caso, será feito a conversão utilizando o menu de comprimento.

def conversaoComprimento(vetor):
    if vetor[0] == 1:
        if vetor[1] == 1:
            valueCm = vetor[2] / 2.54   # Centímetro para polegada.
            sendDataServer(valueCm)
        elif vetor[1] == 2:
            valuePalmo = vetor[2] * 22.86  # Palmo para centímetro.
            sendDataServer(valuePalmo)
        elif vetor[1] == 3:
            valueMetros = vetor[2] * 3.281  # Metros para pés.
            sendDataServer(valueMetros)
        elif vetor[1] == 4:
            valueKm = vetor[2] * 1094  # Quilômetros para jardas.
            sendDataServer(valueKm)


# Função para executar as fórmulas de cada conversão de acordo com a escolha do cliente.
# Nesse caso, será feito a conversão utilizando o menu de massa.

def conversaoMassa(vetor):
    if vetor[0] == 2:
        if vetor[1] == 1:
            valueKg = vetor[2] / 1000  # Quilograma para tonelada.
            sendDataServer(valueKg)
        elif vetor[1] == 2:
            valueQuilate = vetor[2] / 5  # Quilate para grama.
            sendDataServer(valueQuilate)
        elif vetor[1] == 3:
            valueG = vetor[2] * 1000  # Grama para miligrama.
            sendDataServer(valueG)
        elif vetor[1] == 4:
            valueLB = vetor[2] / 2.205  # Libra para Quilograma.
            sendDataServer(valueLB)


# Função para executar as fórmulas de cada conversão de acordo com a escolha do cliente.
# Nesse caso, será feito a conversão utilizando o menu de escalas termométricas.

def conversaoTemperatura(vetor):
    if vetor[0] == 3:
        if vetor[1] == 1:
            valueC = vetor[2] + 273.15  # Célsius para Kelvin.
            sendDataServer(valueC)
        elif vetor[1] == 2:
            valueKelvin = (vetor[2] - 273.15) * 1.8 + 32  # Kelvin para fahrenheit.
            sendDataServer(valueKelvin)
        elif vetor[1] == 3:
            valueF = (vetor[2] - 32) / 1.8  # Fahrenheit para célsius.
            sendDataServer(valueF)
        elif vetor[1] == 4:
            valueC2 = (vetor[2] * 1.8) + 32  # Célsius para fahrenheit.
            sendDataServer(valueC2)

# Chama as funções de acordo com a escolha do menu e o tipo de conversão.

def chamaFuncoes():
    while True:
        try:
            menu = receiveDataServer()
            if menu[0] == 1:
                conversaoComprimento(menu)
            elif menu[0] == 2:
                conversaoMassa(menu)
            elif menu[0] == 3:
                conversaoTemperatura(menu)
        except:
            clisocket.close()
            print('Nada para converter. Saindo...')
            print('Aguardando conexão')
            clisocket, addr = svsocket.accept()


chamaFuncoes()  # Função sendo chamada.
