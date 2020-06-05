# O código começa sorteando um número aleatório.
#O usuário começa digitando um número.
#Se o número que ele digitou foi o número que o código sorteou, ele ganha.
#O objetivo é acertar o número na menor quantidade de tentativas. Então tem que registrar também quantas vezes a pessoa tentou.
#E esse código pode ou não dizer dicas, fica a seu critério...

numero_comparacao = 0
numero_usuario = input('Digite um número:\n')

while (numero_usuario != str(numero_comparacao)):
    
    if (numero_usuario == str(numero_comparacao)):
        print('Acertou')
    else:
        print('Errouuu!!')
    
    numero_usuario = input('Digite um número:\n')