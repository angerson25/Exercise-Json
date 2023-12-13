##Se tienen los datos de un grupo de 5 transacciones referentes a las matrículas de un grupo de estudiantes (código, apellidos, nombres, créditos), almacenadas como jason, crear un arreglo con estas transacciones y a partir del mismo encontrar los apellidos, nombres y numero de creditos matriculados, del estudiante con mayor numero de creditos matriculados generadon esta respuesta con un archivo jason.

import json



# Abrir el archivo JSON
with open('matrijason.json') as json_file:
    # Cargar los datos desde el archivo
    matriculas = json.load(json_file)



# Acceder a los datos como un diccionario de Python
creditosmaximo=0
for persona in matriculas:
    creditospersona = persona['creditos']
    if creditospersona > creditosmaximo:
        creditosmaximo = creditospersona
        nombre = persona['nombre']
        apellido = persona['apellidos']
        
##datos el mayor
print("\nEl estudiante con la mayor cantidad de creditos matriculados es: \nNombre: ",nombre,"\nApellido: ",apellido,"\nCreditos: ",creditosmaximo)
