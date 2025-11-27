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
            readFile(PRODUCT_FILE_PATH)
        case 5:
            print("Bye!")
            break