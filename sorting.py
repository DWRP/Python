import random,os

menu = True
record = 0

while menu:
    os.system('cls')
    print("Recorde:", record)
    numero_comparacao = random.randint(0,50)

    contador = 0

    numero_usuario = input('Digite um número:\n')

    while contador<15:
        print(f'Número: {numero_comparacao}')
        if (numero_usuario == str(numero_comparacao)):
            print('Acertou')
            print(f'Você tentou {contador} vezes!')
            
            if (contador < record):
                record = contador
            if(record == 0):
                record = contador

            contador = 15

        else:
            print('Errouuu!!')

            if(numero_usuario<str(numero_comparacao)):
                print('O número está acima')
            else:
                print('O número está abaixo')

        if(contador<10):
            numero_usuario = input('Digite um número:\n')
        
        contador += 1

    print(f'Fim de jogo! Número: {numero_comparacao}')
    
    option = input('Deseja continuar a jogar?')

    if (option.lower() != 's' and option.lower() != 'sim'):
        menu = False