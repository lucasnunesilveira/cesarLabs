import Operadores
import os
import time

while True:
    time.sleep(21)
    os.system('cls')
    try:
        print("Bem vindo a calculadora:")
        print("1-Somar:")
        print("2-Subtrair")
        print("3-Dividir")
        print("4-multiplicar:")
        print("5-modulo:")
        print("6-Sair")
        escolha = int(input("Escolha: "))
        if escolha == 1:
            n1 = float(input("digite o primeiro numero da soma:"))
            n2 = float(input("digite o segundo  numero da soma:"))
            Operadores.somar(n1, n2)
        elif escolha == 2:
            n1 = float(input("digite o primeiro numero da subtrair:"))
            n2 = float(input("digite o segundo  numero da subtrair:"))
            Operadores.subtrair(n1, n2)
        elif escolha == 3:
            n1 = float(input("digite o primeiro numero da dividir:"))
            n2 = float(input("digite o segundo  numero da dividir:"))
            Operadores.dividir(n1, n2)
        elif escolha == 4:
            n1 = float(input("digite o primeiro numero da multiplicar:"))
            n2 = float(input("digite o segundo  numero da multiplicar:"))
            Operadores.multiplicar(n1, n2)
        elif escolha == 4:
            n1 = float(input("digite o primeiro numero da do modulo:"))
            n2 = float(input("digite o segundo  numero do modulo :"))
            Operadores.multiplicar(n1, n2)
        elif escolha == 5:
            exit()
        elif escolha < 0 or escolha > 6:
            print("Fora das opcao de escolha")

    except ValueError:
        print("\ndigie o valor correto !\n")
