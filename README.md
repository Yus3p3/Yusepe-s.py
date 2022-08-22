n1=str(input("Ingrese su primer nombre"))
n2=str(input(" Ingrese su segundo nombre"))
a1=str(input("ingrese su primer apellido"))
a2= str(input("Ingrese su segundo apellido"))
#En estas primeras lineas le decimos al usuario que ingrese sus nombres y apellidos
in1 = 0
#esta variable la usamos para decir que caracter vamos a extraer 
nj1 = n1[in1]
#extraemos la primera letra del primer numbre
nj2 =n2[in1]
#extraemos la primera letra del segundo nombre
nc= nj1, nj2, ("."), a1, a2, ("@baco.com")
#juntamos todo en forma de lista
Strnc = "".join(nc)
#convertimos la lista en un string para poder imprimirla 
print("Su correo es el siguiente",Strnc)
#printeamos el resultado 
