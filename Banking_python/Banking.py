saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

def depositar(valor):
    global saldo
    saldo += valor
    depositos.append(valor)
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")

def sacar(valor):
    global saldo, saques_diarios
    if saldo >= valor and saques_diarios < 3 and valor <= 500:
        saldo -= valor
        saques.append(valor)
        saques_diarios += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    elif saldo < valor:
        print("Saldo insuficiente para realizar o saque.")
    elif saques_diarios >= 3:
        print("Limite diário de saques atingido.")
    else:
        print("Valor de saque excede o limite permitido (R$500.00).")

def extrato():
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato bancário:")
        for i in range(len(depositos)):
            print(f"Depósito {i+1}: R${depositos[i]:.2f}")
        for i in range(len(saques)):
            print(f"Saque {i+1}: R${saques[i]:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")

while True:
    print("Bem-vindo(a) ao sistema bancário!")
    print("Digite 1 para realizar um depósito.")
    print("Digite 2 para realizar um saque.")
    print("Digite 3 para visualizar o extrato bancário.")
    print("Digite 4 para sair do sistema.")
    escolha = input("Opção escolhida: ")

    if escolha == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        depositar(valor)
    elif escolha == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        sacar(valor)
    elif escolha == "3":
        extrato()
    elif escolha == "4":
        print("Obrigado(a) por utilizar o sistema bancário!")
        break
    else:
        print("Opção inválida, tente novamente.")