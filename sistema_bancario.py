menu = """

Escolha uma opção:

[1] Deposito
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []


while True :
  
    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Qual o valor do deposito?"))
        saldo += valor_deposito
        deposito = f"Você depositou R$: {valor_deposito:.2f}"
        depositos.append(deposito)
    
    if opcao == 2:
        valor_saque = float(input("Qual o valor do saque?"))
        if valor_saque > saldo:
           print("Saldo Insuficiente")
        elif valor_saque > limite:
            print("Limite maximo de saque: R$500.00")    
        elif numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingido")
   
        else:
            saldo -= valor_saque
            numero_saques += 1
            saque = f"Você sacou R${valor_saque}"
            saques.append(saque)
    
    if opcao == 3:
        print(f"Você recebeu os seguintes depósitos: {depositos}")
        print(f"Você fez os seguintes saques: {saques}")
        print(f"Seu saldo atual é: R${saldo:.2f}")
    
    if opcao == 4:
        print("Você saiu do sistema")
        break
   
   