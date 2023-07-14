def crearproductos(lista_productos):
    producto ={}
    
    flag=True
    while flag:
        try:
            nombreproducto = input("nombre del producto")
            marcaproducto = (input("marca del producto"))
            costoproducto = int(input("costo del producto"))
            cantidadproducto = int(input("cantidad del producto"))

        

        except ValueError:
         print("algo salio mal intentalo otra vez")
    else:
        producto["nombre"]= nombreproducto
        producto["marca"]= marcaproducto
        producto["costo"]= costoproducto
        producto["cantidad"]= cantidadproducto
        lista_productos.append(producto)
        productos = {}
        pregunta = input("desea agrear mas productos")
        if str(pregunta) != "si":
         flag = False
         return lista_productos

def listaproductos(lista_productos):
     print('producto | cantidad | precio')
     for producto in lista_productos:
        print(f"{producto.get('nombre')} | {producto.get('cantidad')} | {producto.get('costo')}")

   