flag1=True
flag2 =True

while flag1:
    try:
        a = int(input("valor 1: "))
        flag1=False
    except ValueError:
        print("incorrecto")
print("complete mi primer loop")
print(f"mi valores obtenido son {a} ")  


while flag2:
    try:
       b = int(input("valor 2: "))
       flag2=False 
    except ValueError:
        print("incorrecto")
print("termine mi segundo loop")
print(f"mi valores obtenido son {a} ")
if (a%b)==0:
   r=f"{a} / {b} es exacta"
elif (a%b)==2:
    r=f"{a} / {b} es exacta"

print(r)
   
 