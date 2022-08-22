cuentacuentos= 0
p= str(input("Ingrese el texto "))
le= str(input("Ingrese la letra que quiera saber cuantas veces se repitio "))

for l in p :
  if l == le :
    cuentacuentos += 1
    
print ("Se repitiero",cuentacuentos,"veces la letra:", le) 
#El usuario dice la letra que desea buscar para despues pedirle una frase para ver cuantas veces se repetio la letra que te el usuario
