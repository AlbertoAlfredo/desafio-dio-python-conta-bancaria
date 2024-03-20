menu = """

[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=>"""

saldo =0
limite = 500
saques_efetuados =0
LIMITE_SAQUE = 3


def saque(valor):
    global saldo
    global saques_efetuados
    if saques_efetuados < 3:
        if valor < saldo:
            saldo -= valor
            saques_efetuados += 1
        else:
            print("Valor do saque excede valor na conta")
    else:
        print('Limite de saque excedido, poderá voltar a sacar amanhã')

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
    else:
        print("Valor do depósito deve ser positivo")

    


def extrato():
    print("""

    ############################
            EXTRATO
    ############################
          
    Saldo: {:.2f}
          
    ############################

    """.format(saldo))




while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Digite o valor do depósito: ')
        valor = float(input().replace(',', '.'))
        deposito(valor)


    elif opcao == 's':
        print('Digite o valor do saque: ')
        valor = float(input().replace(',', '.'))
        saque(valor)

    elif opcao == 'e':
        extrato()
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

