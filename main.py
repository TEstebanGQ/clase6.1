from utils.menu import menu
from utils.jsonFileHandler import *
from utils.utiliListas import *


PRODUCT_FILE_PATH = "./database/products.json"
options =  (
    "Agregar producto",
    "Mostrar productos",
    "Editar producto",
    "Eliminar producto",
    "BUcscar producto",
    "Salir del programa"
)

while True:
    choise = menu("--- G E S T I O N  D E  P R O D U C T O S ---", options)
    match choise:
        case 1:
            product = {
                "code": input("Ingrese el código del producto: "),
                "name": input("Ingrese el nombre del producto: "),
                "proveedor": input("Ingrese el proveedor del producto: "), 
                "price": float(input("Ingrese el precio del producto: ")),
                "active": True
            }
            dataProducts = readFile(PRODUCT_FILE_PATH)
            dataProducts.append(product)
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 2:
            Products = readFile(PRODUCT_FILE_PATH)
            if len(Products) == 0:
                print("No hay productos registrados.")
            else:
                print("--- P R O D U C T O S  R E G I S T R A D O S---\n")
                print("| Código | Nombre | Proveedor | Precio | Activo |")
                for product in Products:
                    print(f"| {product['code']:<6} | {product['name']:<6} | {product['proveedor']:<9} | {product['price']:<6} | {'Activo' if product['active'] else 'Inactivo':<6} |")
        case 3:
            prodoctCode = input("Ingrese el código del producto a eDITAR: ")
            dataProducts = readFile(PRODUCT_FILE_PATH)
            info = findDictionary(dataProducts, "code", prodoctCode)
            if len(info.keys()) == 0:
                print("Producto no encontrado.")
            else:
                editProd = {
                    "name" : input("Nuevo nombre: ") or info["data"]["name"],
                    "proveedor" : input("Nuevo proveedor: ") or info["data"]["proveedor"],
                    "price" : float(input("Nuevo precio: ") or info["data"]["price"]),
                    "activo" : False if input("Nuevo estado ([A]ctivo/[I]nactivo): ") == "I" else True or info["data"]["active"]
                }
                print(editProd)

           




















        case 4:
            prodoctCode = input("Ingrese el código del producto a eliminar: ")
            dataProducts = readFile(PRODUCT_FILE_PATH)
            info = findDictionary(dataProducts, "code", prodoctCode)
            print(f"Desea borra el producto: {info['data']['code']} - {info['data']['name']}  (S/N)?")


        case 5:
            codeToSearch = input("Ingrese el código del producto a buscar: ")
            dataProducts = readFile(PRODUCT_FILE_PATH)
            for product in dataProducts:
                if product["code"] == codeToSearch:
                    print("Producto encontrado:")
                    print(product)
                    break
            else:
                print("Producto no encontrado.")
        case 0:
            print("Bye!")
            break