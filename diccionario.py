auto = {
    "marca" : "toyota", 
    "modelo" : "hilux", 
    "numeroaccidentes": 1,
    "estado": True
    "colores": ["negro", "gris"],
}


#keys
#values
#get
for llave, valor in auto.items():
    print(llave, valor)
    print(auto.get("modelo")) 