import pandas as pd

def main():
    ruta_csv = "./alumnos.csv"
    lista = pd.read_csv(ruta_csv)
    print()
    print("Bienvenido a la interfaz de manejo de notas, porfavor elija una de las siguientes opciones:") 
    print()
    print("1. Mostrar promedio de notas guardadas") 
    print("2. Ingresar nuevas notas") 
    print("3. Mostrar promedio de notas de materias") 
    print("4. Mostrar lista de alumnos aprobados")
    print("5. Mostrar lista de alumnos reprobados")

    print()

    seleccion = int(input("Ingresar opcion (cualquier otro numero sera invalido): "))

    if seleccion == 1:
        promedio_notas()
    
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
    

def promedio_notas():
    print("promedio notas")

def ingresar_notas():
    print("ingresar notas")

def promedio_materias():
    print("promedio materias")

def lista_aprobados():
    print("lista aprobados")

def lista_reprobados():
    print("lista reprobados")

main()