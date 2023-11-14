from numeros.soma import somar
from numeros.subtracao import subtrair
from numeros.multiplicacao import multiplicar
from numeros.divisao import dividir
def menu():
    while True:
        print('Digite 1 para somar')
        print('Digite 2 para subtração')
        print('Digite 3 para divisão')
        print('Digite 4 para multiplicação')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            a = float(input('Digite o primeiro valor: '))
            b = float(input('Digite o segundo número: '))
            print(f'Resultado: {somar(a,b)}')
        elif opcao =='2':
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            print(f'Resultado: {subtrair(num1,num2)}')
        elif opcao =='3':
            num1 = float(input('Digite um número: '))
            num2 = float(input('Digite um número: '))
            print(f'Resultado: {dividir(num1, num2)}')
        elif opcao == '4':
            num1 = float(input('Digite um número: '))
            num2 = float(input('Digite um número: '))
            print(f'Resultado: {multiplicar(num1, num2)}')

menu()