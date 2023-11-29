
import os
import pathlib
from os import path

RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

OPCIONES_MENU = {1,2,3,4,5,6,7,8}



def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    contactos = {}
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            nuevo = linea.split(";")
            nombre = nuevo[0]
            apellido = nuevo[1]
            gmail = nuevo[2]
            tlfn = nuevo[3:]


def agregar_contacto():
    print("hola")

def modificar_contacto():
    print("hola")


def eliminar_contacto(contactos: list, email: str):
    try:
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")

def borrar_agenda():
    print("hola")

def agenda_inicial():
    print("hola")

def mostrar_contacto_criterio():
    print("hola")

def mostrar_contactos():
    print("hola")

def mostrar_menu():
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir")

def pedir_opcion() -> int:
    estado = False
    while not estado:
        try:
            valor = int(input("Dime la opcion que vas a elegir: "))
        except:
            print("Dime un numero valido")
        else:
            estado = True
            return valor

#def agenda(contactos: list):
#    estado = False
#    while not estado:
#        mostrar_menu()
#        opcion = pedir_opcion()
#        if opcion in OPCIONES_MENU:
#            estado = True
#            return opcion
#        else:
#            print("Tienes que poner un numero del 1 al 8")

def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    #diferencia_sime = OPCIONES_MENU ^ 
    mostrar_menu()
    opcion = None
    while opcion != 8:
        
        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 7
        if opcion in OPCIONES_MENU:
            
            if opcion == 1:
                agregar_contacto()
                pulse_tecla_para_continuar()
                borrar_consola()
            
            elif opcion == 2:
                modificar_contacto()
                pulse_tecla_para_continuar()
                borrar_consola()
            
            elif opcion == 3:
                eliminar_contacto()
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 4:
                borrar_agenda()
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 5:
                agenda_inicial()
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 6:
                mostrar_contacto_criterio()
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 7:
                mostrar_contactos()
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 8:
                print("Saliendo del programa")
        mostrar_menu()
        opcion = pedir_opcion()




def pulse_tecla_para_continuar():
    print("\n")
    os.system("pause")




def main():
    borrar_consola()

    contactos = []

    cargar_contactos(contactos)
    
    agenda(contactos)


if __name__ == "__main__":
    main()