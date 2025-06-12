import pandas as pd

matriz = [[1, 2, 3], [3, 2, 1]]
for fila in matriz:
    for numero in fila:
        print(numero)

for i in range(len(matriz)):
    for c in range(0, 3):
        print(matriz[i][c])

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
    
    else:
        print("valor invalido")
        main()
    

def mostrar_notas():
    df = pd.read_csv("alumnos.csv")
    # print(df)
    
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
    nueva_lista.append(int(input("Ingrese la nota final: ")))

    nuevo_df = pd.DataFrame([nueva_lista], columns=df.columns)
    df = pd.concat([df, nuevo_df], ignore_index=True)
    df.to_csv("./alumnos.csv", index=False)
    print("agregado correctamente")
    print()
    main()

def promedio_materias():
    df = pd.read_csv("alumnos.csv")
    print()
    print("promedio materias")
    promedio = (df["Nota1"] + df["Nota2"] + df["Nota3"] + df["NotaFinal"])/4
    print()
    print(promedio)
    print()
    main()

def lista_aprobados():
    df = pd.read_csv("alumnos.csv")
    promedio = (df["Nota1"] + df["Nota2"] + df["Nota3"] + df["NotaFinal"])/4
    print()
    print("lista aprobados")
    print()
    
    for i in (len(df["Nombre"])):
        print(df["Nombre"][i] + str(df["NotaFinal"][i]))
    main()
    

def lista_reprobados():
    print("lista reprobados")
    main()



main()