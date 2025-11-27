def menu():
    choise = 0
    print("---------------------------------------------")
    print("--- G E S T I O N  D E  P R O D U C T O S ---")
    print("---------------------------------------------")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Salir del programa\n")
    while True:
        try:
            choise = int(input("--> ¿Que desea hacer?: "))
            if choise not in range(1, 6):
                print("--> Opción no válida .....")
            else:break
        except ValueError:
            print("--> Su eleccion debe ser un numero .....")
    return choise
