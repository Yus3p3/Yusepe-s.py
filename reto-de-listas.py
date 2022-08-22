f1= [1,3,2,1,52,45,17]
f2= [3,2,5,4,777,78,7]
f3= [6,7,7,5,16,2,8]
d= f1[0] + f2[0] +f3[0] + f1[-1] +f2[-1] +f3[-1]
s1=sum(f1)
s2=sum(f2)
s3=sum(f3)
ST=s1+s2+s3-f1[0] - f2[0] -f3[0] - f1[-1] -f2[-1] -f3[-1]

if len(f1) == len(f2) and len(f1)==len(f3):
  print("Ejercio 1: Todas las listas tienen la misma cantidad de numeros ten tu suma guapo :D", d)
else:
  print(" Las listas no tienen la misma cantidad de caracteres :c")
  
print(" ")


#Tarea 3: Sumar todos los numeros que esten en la lista que no sean el primero y el último. 
#Ejemplo: 26

print("Suma total de las listas menos sus primeros y ultimos porque nos caen mal:", ST)

#Tarea #4: Restar los resultados obtenidos de las tareas 2 y 3 
print(" ")
if len(f1) == len(f2) and len(f1)==len(f3):
  print("Resta de tareas:",d-ST)
else:
  print("resta de las tareas (Recuerda de que no hay Tarea 1 porque las listas no contienen la misma cantidad de caracteres):     ",-ST)
  #Este programa agrega 3 listas para cumplir ciertas tareas con estas, una de ellas es sumar las 3 listas menos el primero y ultimo de cada una de las lista al igual que en las restas
