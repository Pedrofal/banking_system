def deposito(saldo, depositos):
    valor_deposito = float(input("Qual o valor do depósito? "))
    saldo += valor_deposito
    depositos.append(f"Você depositou R$ {valor_deposito:.2f}")
    return saldo, depositos

def saque(saldo, saques, numero_saques, limite_saques):
    valor_saque = float(input("Qual o valor do saque? "))
    if valor_saque > saldo:
        print("Saldo Insuficiente")
    elif valor_saque > limite:
        print("Limite máximo de saque: R$500.00")
    elif numero_saques == limite_saques:
        print("Limite de saques atingido")
    else:
        saldo -= valor_saque
        numero_saques += 1
        saques.append(f"Você sacou R$ {valor_saque:.2f}")
    return saldo, saques, numero_saques

def extrato(saldo, depositos, saques):
    print(f"Você recebeu os seguintes depósitos: {depositos}")
    print(f"Você fez os seguintes saques: {saques}")
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def exibir_menu():
    menu = """
    Escolha uma opção:

    [1] Deposito
    [2] Sacar
    [3] Extrato
    [4] Sair
    """

    return int(input(menu))

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
depositos = []
saques = []

while True:
    opcao = exibir_menu()

    if opcao == 1:
        saldo, depositos = deposito(saldo, depositos)
    elif opcao == 2:
        saldo, saques, numero_saques = saque(saldo, saques, numero_saques, limite_saques)
    elif opcao == 3:
        extrato(saldo, depositos, saques)
    elif opcao == 4:
        print("Você saiu do sistema")
        break
