
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

def listademails(contactos) -> list:
    lista_mails = []

    for i in contactos:
        lista_mails.append(i.get('email').lower()) 
    
    return lista_mails

def cargar_contactos():
    partes = {}
    contactos_iniciales = []
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            nuevo = linea.strip().split(";")
            partes = {
                "nombre" : nuevo[0],
                "apellido" : nuevo[1],
                "email" : nuevo[2],
                "tlfn" : nuevo[3:],
                }
            contactos_iniciales.append(partes)
        return contactos_iniciales

def pedir_email(contactos_iniciales):
    try:
        email = input("Dime el email a añadir: ")
        lista_mails = listademails(contactos_iniciales)
        estado2= False
        while not estado2:
            if email:
                if email not in lista_mails:
                    if email.count("@") == 1:
                        validar_email(contactos_iniciales,email)
                        return True
                    else:
                        raise ValueError("el email no es un correo válido")
                else:
                    raise ValueError("el email ya existe en la agenda")
            else:
                raise ValueError("el email no puede ser una cadena vacía")
    except ValueError as e:
        print(e)
        email = input("Dime el email a añadir: ")
    else:
        return email

def validar_email(contactos_iniciales:list,email:str) -> bool:
    lista_mails = listademails(contactos_iniciales)
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
    estado = False
    while not estado:
        if tlfn:
            if tlfn.lower() == "x":
                return telefonos_introducidos
            else:
                telefono = tlfn.replace(" ", "")  # quitar los espacios en blanco
                telefono_sin_prefijo = telefono.replace("+34", "")  # quitar el prefijo
                # comprueba si el número de telefono tiene 9 dígitos y son numeros
                if len(telefono_sin_prefijo) == 9 and telefono_sin_prefijo.isnumeric():
                    telefonos_introducidos.append(telefono_sin_prefijo)
                    tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
                else:
                    print("Por favor, introduce un telefono valido (9 dígitos).")
                    tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
        else:
            print("\nNo puedes dejar el número de teléfono vacío.")
            tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")


def agregar_contacto(contactos_iniciales:list) -> dict:

    print("\nVas a agregar un contacto\n")

    nuevo_contacto = {}

    nombre = input("Dime el nombre: ").strip()
    apellido = input("Dime el apellido: ").strip()

    estado = False
    while not estado:

        if nombre and apellido:
            nuevo_contacto["nombre"] = nombre.title()
            nuevo_contacto["apellido"] = apellido.title()
            estado = True

        else:
            print("\nNombre y apellidos no tienen que estar vacios, pon algo")
            nombre = input("Dime el nombre: ").strip()
            apellido = input("Dime el apellido: ").strip()

    
    
    email = pedir_email(contactos_iniciales)

    nuevo_contacto["email"] = email
    
    estado3 = False   

    while not estado3:
        tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
        telefonos_introducidos = validar_telefono(tlfn)
        estado3 = True


    nuevo_contacto["tlfn"] = telefonos_introducidos
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


def buscar_contacto():
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

def agenda(contactos_iniciales: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    #diferencia_sime = OPCIONES_MENU ^ {1,2,3,4,5,6,7,8}
    
    opcion = None
    while opcion != 8:
        
        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 7
        if opcion in OPCIONES_MENU ^ 8:
            
            if opcion == 1:
                nuevo_contacto = agregar_contacto(contactos_iniciales)
                contactos_iniciales.append(nuevo_contacto)
                print("\nContacto añadido a la agenda")
                pulse_tecla_para_continuar()
                borrar_consola()
            
            elif opcion == 2:
                verdad = modificar_contacto(contactos_iniciales)
                if verdad == True:
                    print("Se ha modificado el contacto perfectamente")
                else:
                    print("Este contacto no esta en la agenda")
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
                
        mostrar_menu()
        opcion = pedir_opcion()




def pulse_tecla_para_continuar():
    print("\n")
    os.system("pause")



def main():
    """ Función principal del programa
    """
    borrar_consola()

    
    contactos_iniciales = []

    
    contactos_iniciales = cargar_contactos()


    agregar_contacto(contactos_iniciales)
    pulse_tecla_para_continuar()
    borrar_consola()

    
    eliminar_contacto(contactos_iniciales)
    pulse_tecla_para_continuar()
    borrar_consola()


    mostrar_contactos(contactos_iniciales)
    pulse_tecla_para_continuar()
    borrar_consola()


    agenda(contactos_iniciales)

if __name__ == "__main__":
    main()