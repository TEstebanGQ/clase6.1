def menu(title, options):
    choise = 0
    index = 1
    print("---------------------------------------------")
    print("--- G E S T I O N  D E  P R O D U C T O S ---")
    print("---------------------------------------------")
    for item in options:
        print(f"{index}. {item}")
        index += 1    
    while True:
        try:
            choise = int(input("--> ¿Que desea hacer?: "))
            if choise not in range(1, len(options)+1):
                print("--> Opción no válida .....")
            else:break
        except ValueError:
            print("--> Su eleccion debe ser un numero .....")
    return choise
