print("Bienvenido al programa para saber el area del terreno que te heredo tu tío el narco :D")
print(" ")
p=1 

def a (x,y):
    x=float(input("Cual es el ancho del terreno?: "))
    y=float(input("Cual es el alto del terreno?: "))
    r=x*y
    print("el area del terreno es de ", r)


  
while p == 1:
   a(1,2)
   
   i=int(input("Quiere calcular otro terreno? Si. 1, No. 2 "))
   if i == 2:
      break
   elif i == 1: 
      pre= 1
   
   else:
    print("Solamente puede ingresar 1 o 2 ")
    pre=int(input("Quiere continuar? Si. 1, No. 2 "))
    #Calcula el area del terreno y ademas pregunta si desea continuar
