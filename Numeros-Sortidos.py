__AUTHOR__ = "Néfi"

import random 

numeroSortido = random.randint(0, 10)

sn = 's'
sn1 = 'n'
contadora = 0

while sn == "s":
    numero = int(input("Digite um numero : "))
    while numero >= 11:
            print(" Digite um numero correto entre 0 e 10")
            numero = 0
            numero = int(input("Digite um numero : "))
            if (numero <= 10):
                continue
            else:
                print(" Opção Invalida ")
                exit(numero)

    if(numero == numeroSortido):
        print(" Voce acertou")
        print(" Deseja continuar  s para sim, n para não? ")
        opcao = str(input("Digite s / n :"))
        if (opcao == sn):
            contadora = contadora + 1
            continue
        elif(opcao == sn1):
            print(f" Voce tentou {contadora}") 
            exit(opcao)
        else:
            print(" Opção Invalida ")
        
            
    elif (numero != numeroSortido):
        print(f" Voce errou, o numero esta proximo de : {numeroSortido - 1}")
        print(" Deseja continuar  s para sim, n para não? ")
        opcao1 = str(input("Digite s / n :"))
        if (opcao1 == sn):
            contadora = contadora + 1
            continue
        elif(opcao1 == sn1):
            print(f" Voce tentou {contadora}")
            exit(opcao1)
        else:
            print(" Opção Invalida ")
                    
        
