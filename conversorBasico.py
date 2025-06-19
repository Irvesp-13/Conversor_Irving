def kilometros_a_millas(kilometros):
    return round(kilometros * 0.621371, 2)
def litros_a_galones(litros):
    return round(litros * 0.264172, 2)
def gramos_a_onzas(gramos):
    return round(gramos * 0.035274, 2)
def centimetros_a_pulgadas(centimetros):
    return round(centimetros * 0.393701, 2)

# menu
def menu():
    print("---> Conversor Basico <---")
    print("(1)......... Kilometros a Millas")
    print("(2)......... Litros a Galones")
    print("(3)......... Gramos a Onzas")
    print("(4)......... Centimetros a pulgradas")
    print("(5)......... Salir")
    opc = int(input("Seleccione una opción: "))
    if opc == 1:
        km = float(input("Ingrese la cantidad de kilometros: "))
        print(f"{km} Kilometros es igual a {kilometros_a_millas(km)} Millas")
    elif opc == 2:
        li = float(input("Ingrese la cantidad de litros: "))
        print(f"{li} Litros es igual a {litros_a_galones(li)} Galones")
    elif opc == 3:
        gr = float(input("Ingrese la cantidad de gramos: "))
        print(f"{gr} Gramos es igual a {gramos_a_onzas(gr)} Onzas")
    elif opc == 4:
        cm = float(input("Ingrese la cantidad de centimetros: "))
        print(f"{cm} Centimetros es igual a {centimetros_a_pulgadas(cm)} Pulgadas")
    elif opc == 5:
        print("Saliendo del programa...")
        return
    else:
        print("Opción no válida. Intente de nuevo.")
        menu()

if __name__ == "__main__":
    menu()