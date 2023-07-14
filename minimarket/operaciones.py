from productos import crearproductos, listaproductos


def menu():
    lista_de_productos=[]

    omenu = """
    MINIMARKET
    ___________________
    1.listar producto
    2.Agregar producto
    3.Salir
    """
    flag = True
    while flag:
        try:
             print(omenu)
             opcion = int(input("elige una opcion:"))
        except ValueError:
            print('has elegido una opcion que no esta en el menu')
        else:
            if opcion == 1:
                print("listado productos")
                listaproductos(lista_de_productos)

            elif opcion ==2:
                print("agragando productos")
                crearproductos(lista_de_productos)
            elif opcion ==3:
                print("saliendo")  
                flag = False


menu()             



