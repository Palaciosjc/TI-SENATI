def crearproductos(lista_productos):
    producto = {}

    flag=True
    while flag:
        try:
                nombreproducto = input("nombre del producto")
                marcaproducto = input("marca del producto")
                costoproducto = numerosdenentrada("costo del producto")
                cantidadproducto = numerosdenentrada("cantidad del producto")

        

        except ValueError:
         print("algo salio mal intentalo otra vez")
        else:
            producto["nombre"]= nombreproducto
            producto ["marca"]= marcaproducto
            producto ["costo"]= costoproducto
            producto ["cantidad"]= cantidadproducto
            flag_repeticion = coincidenciaproducto(nombreproducto, cantidadproducto, lista_productos)
            if not flag_repeticion:
                lista_productos.append(producto)
        producto = {}
        pregunta = input("desea agrear mas productos? SI/NO")
        if str(pregunta) != "si":
            flag = False
            print(lista_productos)

    return lista_productos
def listaproductos(lista_productos):
    print('producto | cantidad | precio')
    contador = 0
    for producto in lista_productos:
        contador +=1
        print(f"{producto.get('nombre')} | {producto.get('cantidad')} | {producto.get('costo')}")

    
    
def numerosdenentrada(mensaje):

    while True:
        try:
            numero_ingreso = input(input(mensaje))
        except ValueError:
            print("te equivocaste esto debe ser un numero")
        else:
          break
    return numero_ingreso

def coincidenciaproducto(nombreproducto, marcaproducto,cantidadproducto,lista_producto):
    flag = False
    for producto in lista_producto:
       if producto.get("nombre","marca")== nombreproducto and marcaproducto:
          print("este producto ya esta registrado")
          producto["cantidad"]=producto.get("cantidad") + cantidadproducto
          flag = True
       return flag     

