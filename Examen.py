def menu():
    print("*"*3, " MENU PRINCIPAL ","*"*3 )
    print("1. Stock marca\n2. Busqueda por precio\n3. Listado de productos\n4. Salir")

stock = {"8475HD":[387990,10],
         "2175HD":[327990,4],
         "JjfFHD":[424990,1]}

productos = {"8475HD":["HP",15.6,"8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
             "2175HD":["ACER", 14, "4GB", "SSD", "512GB", "Intel Corei7", "Nvidia GTX1050"],
             "JjfFHD":["ASUS", 14, "4GB", "SSD", "265GB", "Intel Core i5", "Nvidia gtx2080Ti"]}

def stock_marca(marca):
    global stock, productos
    while True:
        for x, i in productos.items():
            if marca == i[0]:
                for j, o in stock.items():
                    print(f"El stock es: {o}")
                    break
            else:
                print("No esta disponible en el stock")
            break
        break
def busqueda_precio(p_min,p_max):
    global stock
    while True:
        if p_min < 10000:
            print("Demasiado bajo")
            continue
        elif p_max > 1000000:
            print("Demasiado alto")
            continue

def ordenar_productos():
    global productos
    print("-"*7, "Listado de Notebooks Ordenados", "-"*7)
    for modelo, carac in productos.items():
        print(carac[0], modelo, carac[2], carac[4], sep=" - ")

while True:
    menu()
    user = input("Ingrese una opcion (1-4): ")
    if user == "1":
        stock_marca(marca = input("Ingrese marca a consultar: ").upper().split())
    elif user == "2":
        try:
            busqueda_precio(p_min = int(input("ingrese precio minimo: ")), p_max =int(input("Ingrese precio maximo: ")))
        except ValueError:
            print("Debe ingresar valores enteros!!")
            continue
    elif user == "3":
        ordenar_productos()
    elif user == "4":
        print("Programa finalizado")
        break
    else:
        print("Debe seleccionar una opcion valida!!")
        continue