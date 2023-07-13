producto = {
    "nombre": "",
    "marca": "",
    "costo": "",
    "cantidad": "",

}
lista_producto = []
flag=True
while flag:
    try:
        nombreproducto = input("nombre del producto")
        marcaproducto = int(input("marca del producto"))
        costoproducto = int(input)("costo del producto")
        cantidadproducto = int(input)("cantidad del producto")

        

    except ValueError:
        print("algo salio mal intentalo otra vez")
    else:
        producto["nombre"]= nombreproducto
        producto ["marca"]= marcaproducto
        producto ["costo"]= costoproducto
        producto ["cantidad"]= cantidadproducto
        lista_producto.append(producto)
        producto = {}
        pregunta = input("desea agrear mas productos")
        if str(pregunta) != "si":
            flag = False
            print(lista_producto)