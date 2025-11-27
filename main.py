from utils.menu import menu
from utils.jsonFileHandler import *


PRODUCT_FILE_PATH = "./database/products.json"
while True:
    choise = menu()

    print(f"Has elegido la opción {choise}")
    match choise:
        case 1:
            product = {
                "code": input("Ingrese el código del producto: "),
                "name": input("Ingrese el nombre del producto: "),
                "price": float(input("Ingrese el precio del producto: ")),
                "active": True
            }
            dataProducts = readFile(PRODUCT_FILE_PATH)
            dataProducts.append(product)
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 2:
            dataProducts = readFile(PRODUCT_FILE_PATH)
            for product in dataProducts:
                print(product)
        case 3:
            codeToEdit = input("Ingrese el código del producto a editar: ")
            dataProducts = readFile(PRODUCT_FILE_PATH)
            for product in dataProducts:
                if product["code"] == codeToEdit:
                    product["name"] = input("Ingrese el nuevo nombre del producto: ")
                    product["price"] = float(input("Ingrese el nuevo precio del producto: "))
                    print("Producto actualizado correctamente.")
                    break
            else:
                print("Producto no encontrado.")
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 4:
            codeToDelete = input("Ingrese el código del producto a eliminar: ")
            dataProducts = readFile(PRODUCT_FILE_PATH)
            for i, product in enumerate(dataProducts):
                if product["code"] == codeToDelete:
                    del dataProducts[i]
                    print("Producto eliminado correctamente.")
                    break
            else:
                print("Producto no encontrado.")
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 5:
            print("Bye!")
            break