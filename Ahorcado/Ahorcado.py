import os
os.system('cls')

palabra="alguna"
oculta=palabra
comparar=palabra
tamano=len(palabra)
error=0
for i,caracter in enumerate(palabra):
    oculta=oculta.replace(caracter,"-")
print("Bienvenido al juego del ahorcado, tendra 3 oportunidades para equivocarse o finalizara el juego")
print(f"\nSu palabra posee {tamano} letras \n\nQue comience el juego\n")
os.system("pause")
while (error<3):
    for i,caracter in enumerate(palabra):
        if comparar[i]=="-":
            print(palabra[i],end=" ")
        else:
            print(oculta[i],end=" ")
    os.system("cls")
    letra=input("\n\nIngrese una letra\n\n->")    
    if letra in palabra:
        print(f"Hay {palabra.count(letra)} letras {letra} en la palabra\n")
        for i,caracter in enumerate(palabra):
            if caracter==letra:
                comparar=comparar.replace(caracter,"-")
        os.system("pause")
    else:
        print("Su letra no esta en la palabra, sigue intentando")
        error=error+1
        os.system("pause") 
    if oculta==comparar:
        break
if error==3:
    os.system("cls")
    print("Ya no tiene mas oportunidades, ud ha PERDIDO")
else:
    os.system("cls")
    print(f"Acerto, la palabra es: {palabra}")