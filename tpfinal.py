import pandas as pd

def main():
    ruta_csv = "./alumnos.csv"
    lista = pd.read_csv(ruta_csv)
    print()
    print("Bienvenido a la interfaz de manejo de notas, porfavor elija una de las siguientes opciones:") 
    print()
    print("1. Mostrar lista guardada") 
    print("2. Ingresar nuevas notas") 
    print("3. Mostrar promedio de notas de materias") 
    print("4. Mostrar lista de alumnos aprobados")
    print("5. Mostrar lista de alumnos reprobados")
    print("6. Mostrar lista de alumnos ordenada alfabeticamente")
    print("7. Mostrar lista de alumnos ordenada segun sus promedios de mayor a menor")
    print()

    seleccion = int(input("Ingresar opcion (cualquier otro numero sera invalido): "))

    # seleccion de opciones

    if seleccion == 1:
        mostrar_notas()
    
    elif seleccion == 2:
        ingresar_notas()
    
    elif seleccion == 3:
        promedio_materias()

    elif seleccion == 4:
        lista_aprobados()
    
    elif seleccion == 5:
        lista_reprobados()
    
    elif seleccion == 6:
        lista_orden_alfabetico()

    elif seleccion == 7:
        lista_orden_promedios()

    else:
        print("Valor invalido")
        main()
    

def mostrar_notas():
    df = pd.read_csv("alumnos.csv") # Leer la lista CSV
    print(df) # mostrar toda la lista
    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()


def ingresar_notas():
    df = pd.read_csv("alumnos.csv")

    nueva_lista = []
    print("ingresar notas")
    print()
    nueva_lista.append(str(input("Ingrese el nombre del alumno/a: "))) # Ingresar nombre del alumno
    print()
    print("Materias:") # Mostrar materias disponibles
    print()
    print("1. Matematica")
    print("2. Literatura")
    print("3. Historia")
    print()
    materia = int(input("Seleccione la materia: ")) # Ingresar materia
    if materia == 1:
        nueva_lista.append("Matematica")
    elif materia == 2:
        nueva_lista.append("Literatura")
    elif materia == 3:
        nueva_lista.append("Historia")
    else:
        print("numero invalido")
        ingresar_notas()
    
    nueva_lista.append(int(input("Ingrese la primera nota: ")))
    nueva_lista.append(int(input("Ingrese la segunda nota: ")))
    nueva_lista.append(int(input("Ingrese la tercera nota: ")))

    nuevo_df = pd.DataFrame([nueva_lista], columns=df.columns) #agregar nueva lista al dataframe
    df = pd.concat([df, nuevo_df], ignore_index=True)
    df.to_csv("./alumnos.csv", index=False)
    print("agregado correctamente")
    print()
    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()

def promedio_materias():
    df = pd.read_csv("alumnos.csv")
    print()
    print("promedio materias")
    promedio = (df["Nota1"] + df["Nota2"] + df["Nota3"])/3 # Calcular promedio de las notas
    print()
    print(promedio)
    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()

def lista_aprobados():
    df = pd.read_csv("alumnos.csv") 
    print()
    print("lista aprobados")
    print()
    
    
    for i in range (len(df["Nombre"])):
        if ((df["Nota1"][i] + df["Nota2"][i] + df["Nota3"][i])/3) >= 7: # Calcular el si el promedio del alumno respectivo es igual o mayor que siete
            print(df["Nombre"][i]+ " esta aprobado en: "+  df["Materia"][i]) # Mostrar el alumno aprobado

    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()
    

def lista_reprobados():
    df = pd.read_csv("alumnos.csv")
    print("lista reprobados")
    print()
    for i in range (len(df["Nombre"])):
        if ((df["Nota1"][i] + df["Nota2"][i] + df["Nota3"][i])/3) < 7: # Calcular el si el promedio del alumno respectivo es menor que siete
            print(df["Nombre"][i]+ " esta reprobado en: "+  df["Materia"][i]) # Mostrar el alumno reprobado
    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()

def lista_promedio():
    df = pd.read_csv("alumnos.csv")
    print()
    print("Lista promedio")
    print()
    promedio = (df["Nota1"] + df["Nota2"] + df["Nota3"] + df["NotaFinal"])/4 # Calcular promedio

    # Mostrar nombre del alumno y su promedio respectivo
    for i in range (len(df["Nombre"])):       
        print("Promedio de "+ df["Nombre"][i] +": "+ str(promedio))

    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()

def lista_orden_alfabetico():
    df = pd.read_csv("alumnos.csv")
    print()
    print("Lista de nombres en orden alfabetico")
    print()
    n = len(df["Nombre"])

    lista_nombres = []

    for i in range (len(df["Nombre"])):
        lista_nombres.append(df["Nombre"][i])

    n = len(lista_nombres)
 
    # Recorrer toda la lista (metodo de ordenamiento burbuja)
    for i in range(n):
        # Últimos i elementos ya están ordenados, no es necesario revisarlos
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes y cambiar si están en el orden incorrecto
            if lista_nombres[j] > lista_nombres[j + 1]:
                lista_nombres[j], lista_nombres[j + 1] = lista_nombres[j + 1], lista_nombres[j]
    
    for h in range (len(lista_nombres)):
        print(lista_nombres[h])
    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()

def lista_orden_promedios():
    df = pd.read_csv("alumnos.csv")
    print()
    print("Lista de alumnos ordenada según sus promedios de mayor a menor")
    print()

    # Calcular el promedio de cada alumno
    df["Promedio"] = (df["Nota1"] + df["Nota2"] + df["Nota3"]) / 3

    # Convertir los datos a una lista de tuplas (Nombre, Promedio)
    lista_promedios = list(zip(df["Nombre"], df["Promedio"]))

    # Implementar el método de ordenamiento selectivo (selection sort)
    n = len(lista_promedios)
    for i in range(n):
        # Encontrar el índice del elemento con el mayor promedio en el resto de la lista
        max_idx = i
        for j in range(i + 1, n):
            if lista_promedios[j][1] > lista_promedios[max_idx][1]:
                max_idx = j
        # Intercambiar el elemento actual con el elemento de mayor promedio
        lista_promedios[i], lista_promedios[max_idx] = lista_promedios[max_idx], lista_promedios[i]

    # Imprimir la lista ordenada
    for nombre, promedio in lista_promedios:
        print(f"{nombre}: {promedio:.2f}")
    print()

main()