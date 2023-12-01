
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

def listademails(contactos:list) -> list:
    lista_mails = []

    for i in contactos:
        lista_mails.append(i.get('email').lower()) 
    
    return lista_mails

def cargar_contactos(contactos:list):
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            nuevo = linea.strip().split(";")
            partes = {
                "nombre" : nuevo[0],
                "apellido" : nuevo[1],
                "email" : nuevo[2],
                "telefonos" : nuevo[3:],
                }
            contactos.append(partes)

def pedir_email(contactos:list):

    email = input("Dime el email a añadir: ")
    estado = False
    while not estado:
        try:
            if validar_email(email,contactos):
                estado = True
                return email
            else:
                email = input("Dime el email a añadir: ")
        except ValueError as e:
            print(e)
            email = input("Dime el email a añadir: ")


def validar_email(email:str,contactos:list) -> bool:
    lista_mails = listademails(contactos)
    estado2= False
    while not estado2:
        if email:
            if email not in lista_mails:
                if email.count("@") == 1:
                    estado2 = True
                    return True
                else:
                    raise ValueError("el email no es un correo válido")
            else:
                raise ValueError("el email ya existe en la agenda")
        else:
            raise ValueError("el email no puede ser una cadena vacía")

def validar_telefono(tlfn) -> list:
    telefonos_introducidos = []
    if tlfn:
        if tlfn:
            telefono = tlfn.replace(" ", "") 
            telefono_sin_prefijo = telefono.replace("+34", "") 
            
            if len(telefono_sin_prefijo) == 9 and telefono_sin_prefijo.isnumeric():
                telefonos_introducidos.append(telefono_sin_prefijo)
                return True
            else:
                print("Por favor, introduce un telefono valido (9 dígitos).")
                return False
    else:
        return False


def agregar_contacto(contactos:list) -> dict:

    print("\nVas a agregar un contacto\n")

    nuevo_contacto = {}

    nombre = input("Dime el nombre: ").strip()
    apellido = input("Dime el apellido: ").strip()

    estado = False
    while not estado:

        if nombre and apellido:
            nuevo_contacto["nombre"] = nombre.title()
            nuevo_contacto["apellido"] = apellido.title()
            print("\nSe han añadido nombre y apellidos satisfactoriamente")
            estado = True

        else:
            print("\nNombre y apellidos no tienen que estar vacios, pon algo")
            nombre = input("Dime el nombre: ").strip()
            apellido = input("Dime el apellido: ").strip()

    email = pedir_email(contactos)
    nuevo_contacto["email"] = email
    print("\nse ha añadido satisfactoriamente el email")
    lista_telefonos = []
    tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
    while tlfn != "x":
        telefono_introducido = validar_telefono(tlfn)
        lista_telefonos.append(telefono_introducido)
        tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")


    nuevo_contacto["telefono"] = lista_telefonos
    
    print("\nSe ha añadido el contacto")
    return nuevo_contacto

def modificar_contacto(contactos:list) :
    contacto_a_modificar = input("Dime el gmail del contacto que quieres modificar: ")
    
    for contacto in contactos:
        if contacto.get("email").lower() == contacto_a_modificar.lower():
            nuevo_nobmre = input("Dime el nuevo nombre del contacto: ").strip()
            nuevo_apellido = input("Dime el nuevo nombre del contacto: ").strip()
            estado = False
            while not estado:
                if nuevo_nobmre and nuevo_apellido:
                    contacto["nombre"] = nuevo_nobmre.title()
                    contacto["apellido"] = nuevo_apellido.title()
                    estado = True
                
                else:
                    print("\nNombre y apellidos no tienen que estar vacios, pon algo")
                    nuevo_nobmre = input("Dime el nombre: ").strip()
                    nuevo_apellido = input("Dime el apellido: ").strip()

            telefonos_introducidos = []
            estado3 = False   

            while not estado3:
                nuevo_tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")

                if nuevo_tlfn:
                    if nuevo_tlfn.lower() == "x":
                        estado3 = True
                    else:
                        telefono = nuevo_tlfn.replace(" ", "")  # quitar los espacios en blanco
                        telefono_sin_prefijo = telefono.replace("+34", "")  # quitar el prefijo

                        # Verificar si el número de teléfono tiene 9 dígitos
                        if len(telefono_sin_prefijo) == 9 and telefono_sin_prefijo.isnumeric():
                            telefonos_introducidos.append(telefono_sin_prefijo)
                        else:
                            print("Por favor, introduce un telefono valido (9 dígitos sin espacios).")
                else:
                    print("\nNo puedes dejar el número de teléfono vacío.")
            return True
    else:
        return False

def buscar_contacto(contactos_iniciales:list, input_email:str)-> int:

    for i in range(len(contactos_iniciales)):
        if contactos_iniciales[i].get("email") == input_email:
            return i
    return None

def eliminar_contacto(contactos: list, email: str):
    try:
        pos = buscar_contacto(contactos,email)
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
    # vas a vaciar agenda, queires continuar ? s/n

def agenda_inicial(contactos):
    cargar_contactos(contactos)
    print("\nSe ha restaurado la agenda")


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

def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    diferencia_sime = OPCIONES_MENU ^ {8}
    
    opcion = None
    while opcion != 8:
        
        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 7
        if opcion in diferencia_sime :
            
            if opcion == 1:
                nuevo_contacto = agregar_contacto(contactos)
                contactos.append(nuevo_contacto)
                print("\nContacto añadido a la agenda")
                pulse_tecla_para_continuar()
                borrar_consola()
            
            elif opcion == 2:
                verdad = modificar_contacto(contactos)
                if verdad == True:
                    print("Se ha modificado el contacto perfectamente")
                else:
                    print("Este contacto no esta en la agenda")
                pulse_tecla_para_continuar()
                borrar_consola()
            
            elif opcion == 3:
                email = input("Dime el email que quieres borrar: ")
                eliminar_contacto(contactos, email)
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 4:
                borrar_agenda()
                pulse_tecla_para_continuar()
                borrar_consola()
                
            elif opcion == 5:
                agenda_inicial(contactos)
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
                
        mostrar_menu()
        opcion = pedir_opcion()




def pulse_tecla_para_continuar():
    print("\n")
    os.system("pause")



def main():
    """ Función principal del programa
    """
    borrar_consola()

    
    contactos = []

    
    cargar_contactos(contactos)


    agenda(contactos)

if __name__ == "__main__":
    main()