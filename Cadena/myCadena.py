import os
os.system("cls")
mensaje="biEnvenidos A python"

print(f"{mensaje.swapcase()}")
print(f"{mensaje.capitalize()}")
print(f"{mensaje.upper()}")
print(f"{mensaje.lower()}")
print(f"{mensaje.count('n')}")
print(f"{len(mensaje)}")
print(f"{mensaje.isalpha()}")
for item in mensaje:
    print(item)

for i,item in enumerate(mensaje):
    print(f"Pos {i} - {item}")