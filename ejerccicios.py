ass_producto ={}
def init(self, nombre,  valor, desc, cant):
    self.nombre = nombre
    self.valor = valor
    self.desc = desc
    self.cant = cant
c = int(input("¿Cuántos productos ingresará?:"))
productos=[]
for i in range(c):
    print("Producto número: ",i+1)
n = input("nombre del producto: ")
vr = int(input("valor del producto: "))
desc = input("descripción del producto: ")
cant = int(input("cantidad del producto:"))
p = productos("n, vr, desc, cant:")
productos.append (p)
print ("======LISTADO DE PRODUCTOS =====")
for j in range(len(productos)):
    print("nombre: ",productos[j].nombre)
print("descripción: ",productos[j].desc)
print("valor: ",productos[j].valor)
print("canti")