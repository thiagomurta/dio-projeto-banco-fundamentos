limite = 500
saldo = 0
extrato = ''
LIMITE_SAQUES = 3
numero_saques = 0

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":

        print('DEPÓSITO')
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f'DEPÓSITO, R$ {valor:.2f}\n'

        else:
            print('\nOperação não efetuada. Valor inválido.')

    elif opcao == "s":

        print('SAQUE')
        valor = float(input("Digite o valor que deseja sacar: "))

        if LIMITE_SAQUES > numero_saques:
            if saldo > 0:

                if valor < limite:
                    saldo -= valor
                    extrato += f'SAQUE, R$ {valor:.2f}\n'
                    numero_saques+=1

                else:
                    print('\nValor excede o limite.')

            else:
                print(f'\nImpossível realizar saque, saldo insuficiente.')
        else:
            print('\nLimite de saques atingido.')

    elif opcao == "e":
        print('EXTRATO\n')
        print('Não possui movimentações.\n' if not extrato else extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == "q":
        break

    else:
        print('Digite uma opção válida.')