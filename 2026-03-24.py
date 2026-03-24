#1.desarrolle un programa que permita ingresar el año actual 
# y el año de nacimiento despliegue por pantalla la edad 
 #declara la variable 

ano_actual = 0
ano_nacimiento = 0 
edad_actual = 0 
ano_actual = int (input ( "ingresa el año en que nos encontramos "))
ano_nacimiento= int (input ("ingresa tu año de nacimiento"))
edad_actual = ano_actual - ano_nacimiento
#SALIDA 
print ("Su edad es", edad_actual,"años")
print(f"Su edad es: {edad_actual} años")  #La f en Python se usa para crear lo que se llama un f-string (cadena formateada).
# Sirve para insertar variables dentro de un texto de forma fácil.


 