import random,os

def dar_dica(num,comp):
    if num<comp:
        return 'Maior'
    return 'Menor'

def premiar(acerto):
    if(not acerto):
        return ['Parabens você acertou',True]
    return ["Você errou. Tente novamente",False]

def comparar(num_user,num_principal):
    if(num_user == num_principal):
        return False
    return True

def it_number(numero):
    if (numero.isdigit()):
        return [int(numero),True]    
    return [numero,False]

def repita(lista):
    if (lista[1]):
        return lista
    else:
        return repita(
            it_number(
                input('Não é um número.\nDigite novamente um número: \n')
                )
            )

def main():
    
    sorteado = random.randint(0,50)
    menu = True

    while menu:
        usuario = repita(it_number(input('Digite um número: \n')))
        
        if(usuario[1]):
            menu = comparar(usuario[0],sorteado)
            acerto = premiar(menu)
            if(acerto[1]):
                print(acerto[0])
            else:
                print(f"{acerto[0]}. O número é {dar_dica(usuario[0],sorteado)}")
main()