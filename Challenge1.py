#1 -IMPRIMIR LOS NUMEROS PARES ENTRE 0 Y 1000.
"""for i in range(0,1000):
    if(i%2==0):
        print(i)"""
#2- IMPRIMIR LOS NUMEROS PRIMOS ENTRE 0 Y 100
 #1ra forma
def isPrime(num):
  for i in range(2, num):
      if num % i == 0:
          return False
  return True

def PrimeNumber(limit):
    for i in range(2,limit+1):
        if isPrime(i) == True:
            print(i)

PrimeNumber(11)
print("------------------------------")
  #2da forma
def buscar_numPrimos(number):
    temporal_list = []
    final_primes_numbers = []
    for i in range (2,number+1):
      for j in range(1,(i+1)):
        if(i % j == 0):
          temporal_list.append(j)
      else:
        if(len(temporal_list) == 2):
          final_primes_numbers.append(i)
          temporal_list.clear()

        temporal_list.clear()
    return final_primes_numbers
print(buscar_numPrimos(11))
print(len(buscar_numPrimos(11)))

#3- IMPRIMIR UN NUMERO E IMPIMIR SU TABLA DE MULTIPLICAR
# INVESTIGAR CICLOS EN PYTON

  #forma 1
num = int(input('ingrese numero :'))

for i in range(0,12):
  print(num, "X", i, " = ", num*i)

print("-----------------------------------")
  #forma 2
def tabla_mult(number):
  for i in range(0,12):
    print(f"{number} x {i} = {number*i} ")

tabla_mult(4)