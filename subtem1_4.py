import os
nombre_mascotas=[""]*3
edad_mascottas=[0]*3

def insertar():
    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i] = input (f"ingrese nombre mascota: ")
        edad_mascottas[i]= int(input(f"ingrese edad mascota: "))

def mostrar():
    for i in range(len(nombre_mascotas)):
            print(f"nombre:{nombre_mascotas[i]}),edad: {edad_mascottas[i]}")
    input ("p")
    


    
def main():
    global nombre_mascotas ,edad_mascottas
    nombre_mascotas=[""]*3
    edad_mascottas=[0]*3
    opcion =0
    while opcion != 4:
        os.system ('cls' if os.name== 'nt' else 'clear')
        print("[1] Insertar Mascota (nombre | edad)")
        print("[2] Mostrar mascota (nombre | edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Salir")
        opcion = int (input("Elija una opcion "))
        if opcion ==1:
            insertar()

        elif opcion == 2:
            mostrar()
        elif opcion  == 3:
            print("eliminar")
        elif opcion  == 4:
            print("Saliendo...")
        else: print ("Opcion Invalida ")
        if opcion !=4: input (" Prsione para continuar...")

main()
