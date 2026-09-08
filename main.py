# menu

historial = []

 # FUNCIONES PARA AGREGAR EJERCICIO
def agreagr_ejercicio():
    ejercicio = {
        "semana":int(input("ingrese la semaan: ")),
        "nombre":input("imgrese el nombre del ejercicio: "),
        "series":int(input("imgrese las series: ")),
        "repeticiones":int(input("ingrse las repeticiones. ")),
        "peso kg":float(input("ingrse el peso en kg")) 


    }
    historial.append(ejercicio)
    print("ejercicio agregado correctamente: ")

 # FUNCIONES PARA VER HISTORIAL
def ver_historial():
    if len (historial) == 0:
        print("no hay ejercicio encontrado: ")  
    else:
        print("historial semanal: ")   
        for ejercicio in historial:
            print(ejercicio)
print("======================================")         
  

 # FUNCIONES PARA CALCULAR PROGRESO
def calcular_pogreso():
    if len (historial) == 0:
        print("no hay datos para calcular: ") 
    else:
        mayor = historial [0]
        for ejercicio in historial:
            if ejercicio [3]> mayor[3]:
                mayor = jercicio
        print("mayor peso levantado:",mayor[3],"kg")
        print("ejercicio",mayor[0])

    

 # FUNCIONES PARA BUSCAR EJERCICIO
def buscar_ejercicio():
    buscar = input ("ingrese e1l ejercicio que deseas buscar: ")
    encontrado = False 
    for ejercicio in historial:
        if ejercicio[0]:           
            print("ejercicio encontrado: ")
            print("series:",ejercicio[1])
            print("repeticiones:",ejercicio[2])
            print("peso",ejercicio[3],"kg")
            encontrado = True
        if encontrado == False:
            print("ejercicio no encontrado: ")     


while True:
    print("=========================")
    print("registro de entrenamiento")
    print("=========================")
    print("1. ejercicio del dia")
    print("2. ver historial semanal")
    print("3. cacular progreso")
    print("4. buscar ejercicio")
    print("5. salir")


    opcion = input("seleccione una opcion ")


    if opcion == "1":
        agreagr_ejercicio()

    elif opcion == "2":
        ver_historial()
           
    elif opcion == "3":
        calcular_pogreso()
        
    elif opcion == "4":
        buscar_ejercicio()


    elif opcion == "5":
        print("salir")   
        break        

    else:
        print("opcion no valida")    
print('Gracias por utilizar el sistema')     




