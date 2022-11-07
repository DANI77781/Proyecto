print("""si el pimer numero que ingrese es: 
1-Elevar 
2-Multiplicara
3-sacara la potencia 
4-sumara 
5-sacara la Raiz cuadrada""")


promedio = 0
numero = int(input("Ingrese un numero: "))
while numero <= 0 or numero >= 6:
  print("Numero Invalido")
  numero = int(input("por favor digite de nuevo: "))
numero2 = int(input("Ingrese un segundo numero: "))
if numero == 1:
  elevacion = numero ** numero2
  print(f"El numero {numero} se elevo al {numero2} y el resultado es: {elevacion}")
elif numero == 2:
  multiplicacion = numero * numero2
  print(f"La multiplicacion de {numero} y {numero2} es de: {multiplicacion}")
elif numero == 3:
  for x in range(numero,numero2):
    promedio = promedio + x
  promedio = promedio / 10
  print(f"El promedio de {numero} y {numero2} es de {promedio}")
elif numero == 4:
  suma = numero + numero2
  print(f"La suma de {numero} y {numero2} es de: {suma}")
elif numero == 5:
  suma = numero + numero2
  raiz = pow(suma, 1/2)
  print(f"La suma de {numero} y {numero2} es de: {suma} y su raiz cuadrada es de {raiz}")
