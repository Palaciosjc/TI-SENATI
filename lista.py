def cant_vc(n):
    cantidad_vocales=0
    cantidad_consonantes=0
    n = n.lower()
    
    for letra in n:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            cantidad_vocales += 1
        else:
            cantidad_consonantes += 1
    r = f"""NOMBRE:{n.capitalize()}
            NUMERO de vocales: {cantidad_vocales}
            NUMERO de consonantes: {cantidad_consonantes}
            NUMERO de letras: {len(n)}"""
    return r 

lista_nombres = []
flag=True
while flag:
    nombre = input("ingresar nombres o para terminar escriva x:") 
    if nombre == "x":  
        flag=False
    else: 
        cnombre = nombre.capitalize()
        if  cnombre in lista_nombres:
            pass 
        else:   
            lista_nombres.append(cnombre)

lista_nombres.sort()
print(lista_nombres)
print(f"la cantidad de nombres son{len(lista_nombres)}")  
for i in lista_nombres:
    print(cant_vc(i))
