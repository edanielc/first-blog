def queNum(variable):
    if variable  == 0:
        print ("igual a 0")
    elif 0 < variable < 10:
        print ("primera decena")
    elif 10 < variable < 100:
        print ("bajo la centena")
    else:
        print ("mayor a 100")

def hi():
    print("hola")

hi()
queNum(444)

girls = ["nina", "ana", "maria", "raquel", "lourdes"]
def saludos(arreglo):
    for item in arreglo:
        print ("hola " + item)

saludos(girls)
