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
    print(df) 
    print()
    menu = int(input(("Presione 0 para volver al menu: ")))
    if menu == 0:
        main()


def ingresar_notas():
    df = pd.read_csv("alumnos.csv")

    nueva_lista = []
    print("ingresar notas")
    print()
    nueva_lista.append(str(input("Ingrese el nombre del alumno/a: ")))
    print()
    print("Materias:")
    print()
    print("1. Matematica")
    print("2. Literatura")
    print("3. Historia")
    print()
    materia = int(input("Seleccione la materia: "))
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

    nuevo_df = pd.DataFrame([nueva_lista], columns=df.columns)
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
    promedio = (df["Nota1"] + df["Nota2"] + df["Nota3"])/3
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
    print("Lista de promedios de mayor a menor")
    print()
    
    promedio = (df["Nota1"] + df["Nota2"] + df["Nota3"])/3 # Calcular promedio
    lista_promedios = []
    n = len(lista_promedios)
    lista_promedios.append(promedio)

    # Recorrer la lista comenzando desde el segundo elemento
    for i in range(1, len(lista_promedios)):
        valor_actual = lista_promedios[i]
        j = i - 1 
        # Mover los elementos de la lista[0...i-1] que son mayores que valor_actual
        # una posición hacia adelante para hacer espacio para valor_actual
        while j >= 0 and lista_promedios[j] > valor_actual:
            lista_promedios[j + 1] = lista_promedios[j]
            j -= 1 
        # Insertar el valor_actual en su posición correcta
        lista_promedios[j + 1] = valor_actual
        print(lista_promedios)
    

main()