from productos import crearproductos, listarproductos

def menu():
    lista_de_productos = []
    omenu = """
    MINIMARKET
    ___________________
    1.Listar productos
    2.Agregar productos
    3.Venta
    4.Salir
    """
    flag = True
    while flag:
        try:
            print(omenu)
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print('Has elegido una opcion que no esta en el menu')
        else:
            if opcion == 1:
                print("Listando productos")
                print(lista_de_productos)
                listarproductos(lista_de_productos)
            elif opcion == 2:
                print("Agregando productos")
                crearproductos(lista_de_productos)
            elif opcion == 3:
                print("Iniciar Venta")
                lista_venta = []
                producto_venta = {}
                listarproductos(lista_de_productos)
                seleccionproducto = int(input('elija el numero del producto: '))
                producto = (lista_de_productos[seleccionproducto-1])
                cantidadproducto = int(input(f'escriba cantidad de {producto.get("nombre")}: '))
                producto["cantidad"] = producto.get("cantidad") - cantidadproducto
                producto_venta["producto"] = producto.ge("nombre")
                producto_venta["cantidad"] = cantidadproducto
                producto_venta["subtotal"] = cantidadproducto * producto.get("costo")
                lista_venta.append(producto_venta)
                listarproductos(lista_de_productos)
                print(lista_venta)



            elif opcion == 4:
                print("Saliendo")
                flag = False
menu()

def coincidenventa(nombreproducto,cantidadproducto,costoproducto,producto_venta, marcaproducto):
   flag = False
   for producto in producto_venta:
        if producto.get("nombre")== nombreproducto and producto.get("marca")== marcaproducto and producto.get("cantidad")== cantidadproducto and producto.get("costo")==costoproducto:
            print("este producto ya esta registrado")
            flag_repeti=coincidenventa(nombreproducto,cantidadproducto,costoproducto,producto_venta)
        else:
            if not flag_repeti:
               producto_venta.append(producto)
            producto = {}
            pregunta = input("Desea agregar mas Productos? SI/NO")
            if str(pregunta) != "SI":
                flag = False
            producto["cantidad"]=producto.get("cantidad") + cantidadproducto and producto.get("costo")+costoproducto
            flag = True
        return flag