import socket
import pickle   # Importação dos módulos que serão utilizados no código.
import menus

clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Criação do socket TCP.

host = "127.0.0.1"
port = 2121  # Variáveis.
valconv = []

try:
    clisocket.connect((host, port))  # Conexão com o servidor.
except:
    print("Conexão não realizada, tente novamente.")

# Envia o valor do vetor para o servidor

def sendDataCli():
    sendSv = pickle.dumps(valconv)
    clisocket.send(sendSv)

    sendSv = pickle.loads(sendSv)
    sendSv.clear()

# Recebe os valores do servidor e imprime na tela

def receiveDataCli():
    receiveAnswer = clisocket.recv(1024)
    receiveAnswer = pickle.loads(receiveAnswer)
    print("Valor convertido de acordo com sua escolha: {:.2f}".format(receiveAnswer))
    valconv.clear()
    return receiveAnswer

# Função relacionada a escolha do menu, conversão de medidas de comprimento e input dos valores.

def cliMenuComprimento(menuCli):
        try:
            if menuCli == 1:
                valconv.append(menuCli)
                cliente = menus.menuComprimento()
                if cliente == 1:
                    valconv.append(cliente)
                    valueCm = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueCm)
                elif cliente == 2:
                    valconv.append(cliente)
                    valuePalmo = float(input("Digite o valor para a conversão: "))
                    valconv.append(valuePalmo)
                elif cliente == 3:
                    valconv.append(cliente)
                    valueMetros = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueMetros)
                elif cliente == 4:
                    valconv.append(cliente)
                    valueKm = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueKm)
            if menuCli == 0:
                print("Nada para converter. Saindo...")
                valconv.append(menuCli)
                menuCli.clear()
            sendDataCli()
            receiveDataCli()
        except:
            print("Digite um valor válido!")

# Função relacionada a escolha do menu, conversão de medida de massa e input dos valores.

def cliMenuMassa(menuCli):
        try:
            if menuCli == 2:
                valconv.append(menuCli)
                cliente = menus.menuMassa()
                if cliente == 1:
                    valconv.append(cliente)
                    valueKg = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueKg)
                elif cliente == 2:
                    valconv.append(cliente)
                    valueQuilate = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueQuilate)
                elif cliente == 3:
                    valconv.append(cliente)
                    valueG = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueG)
                elif cliente == 4:
                    valconv.append(cliente)
                    valueLB = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueLB)
            if menuCli == 0:
                print("Nada para converter. Saindo...")
                valconv.append(menuCli)
                menuCli.clear()
            sendDataCli()
            receiveDataCli()
        except:
            print("Digite um valor válido!")

# Função relacionada a escolha do menu, conversão de escalas termométricas e input dos valores.

def cliMenuTemperatura(menuCli):
        try:
            if menuCli == 3:
                valconv.append(menuCli)
                cliente = menus.menuTemperatura()
                if cliente == 1:
                    valconv.append(cliente)
                    valueC = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueC)
                elif cliente == 2:
                    valconv.append(cliente)
                    valueKelvin = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueKelvin)
                elif cliente == 3:
                    valconv.append(cliente)
                    valueF = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueF)
                elif cliente == 4:
                    valconv.append(cliente)
                    valueC2 = float(input("Digite o valor para a conversão: "))
                    valconv.append(valueC2)
            if menuCli == 0:
                print("Nada para converter. Saindo...")
                valconv.append(menuCli)
                menuCli.clear()
            sendDataCli()
            receiveDataCli()
        except:
            print("Digite um valor válido!")

# Função que chama o tipo de conversão dependendo da escolha do usuário.

def chamaMenu():
    menuCli = 4
    while menuCli != 0:
        menuCli = menus.menu1()
        if menuCli == 1:
            cliMenuComprimento(menuCli)
        elif menuCli == 2:
            cliMenuMassa(menuCli)
        elif menuCli == 3:
            cliMenuTemperatura(menuCli)
        elif menuCli == 0:
            print('Nada para converter. Saindo...')


chamaMenu()  # Função sendo chamada.
