# Função do menu principal.

def menu1():
    print("----------------------------------------------------")
    print("|{:^50s}|".format("Conversor de medidas"))
    print("----------------------------------------------------")
    print("Digite 0 para finalizar o programa.")
    print("Digite 1 para converter valores de comprimento.")
    print("Digite 2 para converter valores de massa.")
    print("Digite 3 para converter valores de temperatura.")
    print("----------------------------------------------------")
    cliente = int(input("Digite o número com base no que você deseja converter: "))
    return cliente

# Função do menu de conversão de medidas de comprimento.

def menuComprimento():
    print("----------------------------------------------------")
    print("|{:^50s}|".format("Conversão de medidas de comprimento"))
    print("----------------------------------------------------")
    print("Digite 1 para converter de Centímetro para Polegada.")
    print("Digite 2 para converter de Palmo para Centímetro.")
    print("Digite 3 para converter de Metros para Pés.")
    print("Digite 4 para converter de Quilômetro para Jarda.")
    print("----------------------------------------------------")
    cliente = int(input("Digite o valor para converter medidas de comprimento: "))
    return cliente

# Função do menu de conversão de medidas de massa.

def menuMassa():
    print("----------------------------------------------------")
    print("|{:^50s}|".format("Conversão de medidas de massa"))
    print("----------------------------------------------------")
    print("Digite 1 para converter de Quilograma para Tonelada.")
    print("Digite 2 para converter de Quilate para Grama.")
    print("Digite 3 para converter de Grama para Miligrama.")
    print("Digite 4 para converter de Libra para Quilograma.")
    print("----------------------------------------------------")
    cliente = int(input("Digite o valor para converter medidas de massa: "))
    return cliente

# Função do menu de conversão de escalas termométricas.

def menuTemperatura():
    print("----------------------------------------------------")
    print("|{:^50s}|".format("Conversão de escalas termométricas"))
    print("----------------------------------------------------")
    print("Digite 1 para converter de Célsius para Kelvin.")
    print("Digite 2 para converter de Kelvin para Fahrenheit.")
    print("Digite 3 para converter de Fahrenheit para Célsius.")
    print("Digite 4 para converter de Célsius para Fahrenheit.")
    print("----------------------------------------------------")
    cliente = int(input("Digite o valor para converter escalas termométricas: "))
    return cliente
