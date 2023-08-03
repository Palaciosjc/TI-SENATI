flag=True
while flag:
    try:
       numero = int(input('ingrese solo numeros'))
       print(numero)
       flag=False
    except ValueError as e:
        print("ustede escribio una letra")
