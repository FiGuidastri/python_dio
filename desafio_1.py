menu ='''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 600
extrato = ''
numero_saques = 0
LIMITES_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: {valor:.2f}\n'

        else:
            print('Operação falhou! O valor informado é inválido.')
    
    elif opcao == 's':
        valor = float(input('Informe o valor que deseja sacar: '))

        excedeu_Saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_Saldo:
            print('Saldo insuficiente para realizar a operação!')
        
        elif excedeu_limite:
            print('O valor desejado excede o limite permitido da conta!')
        
        elif excedeu_saques:
            print('Limite de saques atingido!')

        else:
            print(f'Retire o valor de R$ {valor:.2f} abaixo!')
            extrato += f'Saque: {valor:.2f}\n'
            saldo -= valor
            numero_saques += 1
                
    elif opcao == 'e':
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: {saldo:.2f}\n')
        print('==========================================')
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')