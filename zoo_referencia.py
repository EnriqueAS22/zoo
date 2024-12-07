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

catalogo_entradas = {
    "GRATUITA": {"precio": 0, "e_umbral": 3},
    "NINYOS": {"precio": 14, "e_umbral": 13},
    "ADULTOS": {"precio": 23, "e_umbral": 65},
    "JUBILADOS": {"precio": 18, "e_umbral": float('inf')},
}

factura = {
    "GRATUITA": 0,
    "NINYOS": 0,
    "ADULTOS": 0,
    "JUBILADOS": 0
}

# Calcular precio y tipo en función de la edad y guardarlo para luego

def calculo_precio_y_tipo_Billete(edad: int):
    precio = 0
    tipo = 0

    for tipo in catalogo_entradas:
        if edad < catalogo_entradas[tipo]["e_umbral"]:
            


    for i, edad_umbral in enumerate(edades_umbral):
        if edad < edad_umbral:
            precio = precios[i]
            tipo = i
            break

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


for precio, tipo in grupo_personas:
    precioTotal = precioTotal + precio
    contadores_entradas[tipo] += 1
    totales_entradas[tipo] += precio 

for i, tipo in enumerate[tipos_entradas]:
    print(f"{contadores_entradas[i]:2d} entradas {tipo.lower()}: {totales_entradas[i]:6.2f} €")

print("-"*30)


print(f"Numero de entradas: {num_entradas:3d}")
print(f"Total a pagar.....: {precioTotal:.2f} €")



