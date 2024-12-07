"""
1. Calcular precio y tipo en función de la edad y guardarlo para luego...

2. Pedir la edad
    Validar que sea entero positivo
    Pedir las edad hasta que se introduzca "" 

3. Calcular el precio total del grupo

4. Mostrar el precio total y el desglose por edades (tipo de entrada)

"""

precioTotal = 0
grupo_personas= []

GRATUITA = 0
NINYOS = 1
ADULTOS = 2
JUBILADOS = 3

# Calcular precio y tipo en función de la edad y guardarlo para luego

def calculo_precio_y_tipo_Billete(edad: int):
    precio = 0
    tipo = GRATUITA
    if edad >= 3 and edad <= 12:
        precio = 14
        tipo = NINYOS
    if edad >= 13 and edad < 65:
        precio = 23
        tipo = ADULTOS
    elif edad >= 65:
        precio = 18
        tipo = JUBILADOS

    return precio, tipo

# Validar que sea entero positivo

def valida_entero_positivo(dato: str):
    """
    Devuelve True si dato es entero positivo
             False en otro caso
    """
    res = False
    try:
        int(dato)
        res = True
    except ValueError:
        res = False
    return res
    
"""
Bucle de peticion de edades, para cada edad debe imrpimir precio y tipo
y acabar cuando se introduzca ""
"""

# Pedir las edad hasta que se introduzca "" 

while True:
    edad = input("Cuantos años tienes: ")
    if edad == "":
        break
    elif valida_entero_positivo(edad):
        grupo_personas.append(calculo_precio_y_tipo_Billete(int(edad)))

# Calcular el precio total del grupo
# Mostrar el precio total y el desglose por edades (tipo de entrada)

num_entradas = len(grupo_personas) 


num_entradas_gratuitas = 0
num_entradas_ninyos = 0 
num_entradas_adultos = 0
num_entradas_jubilados = 0

precioTotal_gratuitas = 0
precioTotal_ninyos = 0
precioTotal_adultos = 0
precioTotal_jubilados = 0

for precio, tipo in grupo_personas:
    precioTotal = precioTotal + precio

    if tipo == GRATUITA:
        num_entradas_gratuitas += 1
        precioTotal_gratuitas += precio

    if tipo == NINYOS:
        num_entradas_ninyos += 1
        precioTotal_ninyos += precio

    if tipo == ADULTOS:
        num_entradas_adultos += 1
        precioTotal_adultos += precio

    if tipo == JUBILADOS:
        num_entradas_jubilados += 1
        precioTotal_jubilados += precio

print(f"{num_entradas_gratuitas:2d} entradas gratuitas: {precioTotal_gratuitas:6.2f} €")
print(f"{num_entradas_ninyos:2d} entradas ninyos: {precioTotal_ninyos:6.2f} €")
print(f"{num_entradas_adultos:2d} entradas adultos: {precioTotal_adultos:6.2f} €")
print(f"{num_entradas_jubilados:2d} entradas jubilados: {precioTotal_jubilados:6.2f} €")
print("-"*25)


print(f"Numero de entradas: {num_entradas:3d}")
print(f"Total a pagar.....: {precioTotal:.2f} €")


