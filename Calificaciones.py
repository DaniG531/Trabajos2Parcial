A= True
Result = 0
while A:
    B = True
    Calificaciones = []
    while B:
        print("Introduce una de las calificaciones:")
        Numero = float(input())
        Calificaciones.append(Numero)
        print(Calificaciones)
        Ciclo = input("¿Deseas añadir otra calificación?:  ")
        if Ciclo == "N" or Ciclo == "n" or Ciclo == "NO" or Ciclo == "no" or Ciclo == "No" or Ciclo == "nO":
            B = False
    print("")
    Suma = sum(Calificaciones)
    Cal = Suma/len(Calificaciones)
    print(f"Tu Promedio es: {Cal}")
    Ciclo = input("¿Deseas Sacar Otro Promedio?:  ")
    if Ciclo == "N" or Ciclo == "n" or Ciclo == "NO" or Ciclo == "no" or Ciclo == "No" or Ciclo == "nO":
        A = False