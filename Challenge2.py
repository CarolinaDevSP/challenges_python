"""1) Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una 
divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. """
"""
misDivisas = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

var1 = input('ingresa una divisa :')

for key,value in misDivisas.items():
    if(var1 == key):
        print('su simbolo es :',value)
        break
else: print('no esta en el diccionario')
   """

"""2)Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""
"""
myList = ["Matemáticas","Física","Química","Historia","Lengua"]
temporal_list={}

for curso in myList:
    listNotas={curso:input('ingrese nota del curso '+ curso +" :")}
    print(listNotas)

temporal_list=listNotas
print(listNotas)
"""
"""
##otra forma
myCourses = ["Matemáticas","Física","Química","Historia","Lengua"]
notas=[]

for course in myCourses:
    nota = float(input('ingrese nota del curso '+ course +" :"))
    if nota >=5:
        notas.append(course)
for course in notas:
    myCourses.remove(course)
print('Debes repetir :'+ str(notas))

"""


"""3)Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y 
muestre por pantalla su media."""
"""
numbers = input('ingresa lista de numeros :')
numbers = numbers.split(',')
n=len(numbers)

for i in range(n):
    numbers[i]= int(numbers[i])
numbers = tuple(numbers)

suma=0
for i in numbers:
    suma += i

media=suma/n
print('La media es ', media)
"""

"""4)Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.
"""
"""
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(subjects)"""



"""5)Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y 
<créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""
"""
misAsignaturas = {
    'Matemáticas': 6, 'Física': 4, 'Química': 5
}
sumCred=0
for key,value in misAsignaturas.items():
        print('la asignatura ' + key +' tiene :'+ str(value)+ ' creditos')
        sumCred= sumCred+value
print('tiene un total de : '+str(sumCred)+' creditos') """