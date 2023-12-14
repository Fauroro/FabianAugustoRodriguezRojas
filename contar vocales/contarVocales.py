import os
os.system('cls')

mensaje = "Fundamentos de programacion"
vocal=int(0)
consonante=int(0)
lstVocal="a,e,i,o,u"
for caracter in mensaje:
    if caracter in lstVocal :
        vocal = vocal +1
    elif caracter.isalpha():
        consonante=consonante+1
    
print(f"El total de vocales es = {vocal}")
print(f"El total de consonantes es = {consonante}")

