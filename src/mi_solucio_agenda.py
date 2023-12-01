
import os
import pathlib
from os import path

RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

OPCIONES_MENU = {1,2,3,4,5,6,7,8}


def borrar_consola():
    #BORRA LA CONSOLA
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def listademails(contactos:list) -> list:
    lista_mails = []
    #mira cada contacto y agrega los correos a una lista
    for contacto in contactos:
        lista_mails.append(contacto.get('email').lower()) 
    
    return lista_mails

def cargar_contactos(contactos:list):
    #el with ya venia pero supongo que simplemenete abre el otro archivo
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            # Divide la linea y crea un diccionario por contacto
            nuevo = linea.strip().split(";")
            partes = {
                "nombre" : nuevo[0],
                "apellido" : nuevo[1],
                "email" : nuevo[2],
                "telefonos" : nuevo[3:],
                }
            contactos.append(partes)

def pedir_email(contactos:list):
    #pide un email y lo valida
    email = input("Dime el email a añadir: ")
    if validar_email(email,contactos):
        return email


def validar_email(email:str,contactos:list) -> bool:
    #validar email valida que el email tenga las condiciones que se le pide,
    lista_mails = listademails(contactos)
    estado2= False
    while not estado2:
        #que no sea una cadena vacia
        if email:
            #se comprueba si existe gracias a la funcion listademails
            if email not in lista_mails:
                #por ultimo compruba que el mail tenga una @
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
    #validar telefono comprueba si el telefono introducido cumple las condiciones 
    telefonos_introducidos = []
    #que no sea una cadena vacia
    if tlfn:
        #reemplaza los espacios y +34 por una cadena vacia por si metemos +3   4  1  234  5678 9
        telefono = tlfn.replace(" ", "") 
        telefono_sin_prefijo = telefono.replace("+34", "") 
        #comprueba que la longitud del telefono sea de 9 y que sean numeros
        if len(telefono_sin_prefijo) == 9 and telefono_sin_prefijo.isnumeric():
            telefonos_introducidos.append(telefono_sin_prefijo)
            return True
        else:
            print("Por favor, introduce un telefono valido (9 dígitos).")
            return False
    else:
        return False

def agregar_contacto(contactos:list) -> dict:

    #agrega un contacto con las siguientes condiciones
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 


    print("\nVas a agregar un contacto\n")

    nuevo_contacto = {}

    #El .strip() hace que si yo pongo Dime el nombre:"                 mario             " solo pille "mario"
    nombre = input("Dime el nombre: ").strip()
    apellido = input("Dime el apellido: ").strip()

    estado = False
    while not estado:
        #comprueba que nombre y apellidos no sean cadenas vacias 
        if nombre and apellido:
            #añade a nuevo_contacto el nombre que hemos introducido con la primera en mayuscula y el resto en minusculas
            nuevo_contacto["nombre"] = nombre.title()
            nuevo_contacto["apellido"] = apellido.title()
            print("\nSe han añadido nombre y apellidos satisfactoriamente")
            estado = True

        else:
            print("\nNombre y apellidos no tienen que estar vacios, pon algo")
            nombre = input("Dime el nombre: ").strip()
            apellido = input("Dime el apellido: ").strip()

    #crea un bucle para pedir_email
    estado = False
    while not estado:
        try:
            email = pedir_email(contactos)
            estado = True
        except ValueError as e:
            print(e)
    #el email se almacena en nuevo_contacto con la llave email
    nuevo_contacto["email"] = email
    print("\nse ha añadido satisfactoriamente el email")
    
    #como los telefonos puede ser uno o muchos en lugar de solo 1 se crea una lista vacia para almacenarlos
    lista_telefonos = []
    tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
    #si no pongo x va a comprobar todo lo que pongamos, y con la funcion validar_telefono comprieba si cumple las condiciones
    while tlfn.lower() != "x":
        valido = validar_telefono(tlfn)
        #si da true añade el telefono a lista_telefono y lo vuelve a pedir
        if valido == True:
            lista_telefonos.append(tlfn)
            tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
        #si es false simplemente lo pide otra vez
        else:
            tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")

    #y la lista la añade a nuevo contacto, con la llave telefono
    nuevo_contacto["telefono"] = lista_telefonos
    
    print("\nSe ha añadido el contacto")
    return nuevo_contacto


def modificar_contacto(contactos:list) :
    #modificar contacto se encarga de modificar el contacto por un email pedido
    
    contacto_a_modificar = input("Dime el gmail del contacto que quieres modificar: ")
    
    #A cada contacto comprueba si el email es el que hemos introdicido 
    for contacto in contactos:
        if contacto.get("email").lower() == contacto_a_modificar.lower():
            #dentro de este if es un copia pega de lo que hay en agregar contacto pero con nuevos nombres
            #comprueba que nombre y apellidos no sean cadenas vacias 
            nuevo_nobmre = input("Dime el nuevo nombre del contacto: ").strip()
            nuevo_apellido = input("Dime el nuevo nombre del contacto: ").strip()
            estado = False
            while not estado:
                if nuevo_nobmre and nuevo_apellido:
                    #reemplaza el nombre y apellidos que hemos introducido con la primera en mayuscula y el resto en minusculas
                    contacto["nombre"] = nuevo_nobmre.title()
                    contacto["apellido"] = nuevo_apellido.title()
                    estado = True

                else:
                    print("\nNombre y apellidos no tienen que estar vacios, pon algo")
                    nuevo_nobmre = input("Dime el nombre: ").strip()
                    nuevo_apellido = input("Dime el apellido: ").strip()

            
            #como los telefonos puede ser uno o muchos en lugar de solo 1 se crea una lista vacia para almacenarlos
            lista_telefonos = []
            tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
            #si no pongo x va a comprobar todo lo que pongamos, y con la funcion validar_telefono comprieba si cumple las condiciones
            while tlfn.lower() != "x":
                valido = validar_telefono(tlfn)
                #si da true añade el telefono a lista_telefono y lo vuelve a pedir
                if valido == True:
                    lista_telefonos.append(tlfn)
                    tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
                #si es false simplemente lo pide otra vez
                else:
                    tlfn = input("Dime el Nº de telefono, si quieres acabar pon x: ")
            contacto["telefonos"] = lista_telefonos
            return True

    else:
        return False

def buscar_contacto(contactos:list, email:str)-> int:
    #devuelbe la posicion de el email que le hayamos introducido
    for i in range(len(contactos)):
        if contactos[i].get("email") == email:
            return i
    return None

def eliminar_contacto(contactos: list, email: str):
    #nos hace darle un email y si es que existe en la lista de contactos lo borrara por la posicion en la que esta
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

def borrar_agenda(contactos):
    #borra la agenda, si dices s se borrara y cualquier otra cosa no se borrara
    elegir = input("vas a vaciar agenda, quieres continuar(s/n)? " )
    if elegir.lower() == "s":
        contactos = []
        print("los contactos se han borrado")
        return contactos

def agenda_inicial(contactos):
    #restaura la cadenana inicial
    cargar_contactos(contactos)
    print("\nSe ha restaurado la agenda")

def lista_criterios() -> set:
    #Es un print de las cosas que puedes elegir para buscar por el criterio
    print("Por que criterio de busqueda quieres buscar:")
    print("1. Nombre")
    print("2. apellido")
    print("3. email")
    print("4. telefono")
    #Aparte de mostrarte las opciones que puedes meter, tambien crea un conjunto para elegir la opcion
    para_eleccion = {1,2,3,4}
    return para_eleccion

def encotrar_nombre(contactos:list,buscar_nombre:str) -> list:
    encontrados = []
    #busca la parte del str que hayamos introducido en los nombres de los contactos EJ: introducimos an pues saldran antonio y daniela 
    for contacto in contactos:
        if buscar_nombre.lower() in contacto["nombre"].lower():
            encontrados.append(contacto)
    return encontrados

def encotrar_apellido(contactos:list,buscar_apellido:str) -> list:
    encontrados = []
    #busca la parte del str que hayamos introducido en los apellidos de los contactos 
    for contacto in contactos:
        if buscar_apellido.lower() in contacto["apellido"].lower():
            encontrados.append(contacto)
    return encontrados
    
def encotrar_mail(contactos:list,buscar_email:str) -> list:
    encontrados = []
    for contacto in contactos:
    #busca la parte del str que hayamos introducido en los emails de los contactos 
        if buscar_email.lower() in contacto["email"].lower():
            encontrados.append(contacto)
    return encontrados
    
def encotrar_telefono(contactos:list,buscar_telefono:str) -> list:
    encontrados = []
    #busca la parte del str que hayamos introducido en los telefonos de los contactos
    for contacto in contactos:
        for telefono in contacto["telefonos"]:
            if buscar_telefono in telefono:
                encontrados.append(contacto)
                #este break es para que no te añada muchas veces el mismo contacto
                break
    return encontrados

def mostrar_contacto_criterio(contactos):
    #te muestra las opciones y te devuelve un set
    para_eleccion = lista_criterios()
    #eliges la opcion
    opcion = pedir_opcion()
    #hace una cosa distinta dependiendo de la opcion que hayamos introducido
    if opcion in para_eleccion:
        if opcion == 1:
            #buscara el contacto por el nombre
            buscar_nombre = input("Dime el nombre que quieres buscar: ").lower()
            encontrados = encotrar_nombre(contactos,buscar_nombre)
            mostrar_contactos(encontrados)
        elif opcion == 2:
            #buscara el contacto por el apellido
            buscar_apellido = input("Dime el apellido que quieres buscar: ").lower()
            encontrados = encotrar_apellido(contactos,buscar_apellido)
            mostrar_contactos(encontrados)
        elif opcion == 3:
            #buscara el contacto por el email
            buscar_email = input("Dime el email que quieres buscar: ").lower()
            encontrados = encotrar_mail(contactos,buscar_email)
            mostrar_contactos(encontrados)
        elif opcion == 4:
            #buscara el contacto por el telefono
            buscar_telefono = input("Dime el telefono que quieres buscar: ")
            encontrados = encotrar_telefono(contactos,buscar_telefono)
            mostrar_contactos(encontrados)

def ordenar_contactos(contactos):
    #esta funcion ordenara los contactos de nuestra agenda
    
    contactos_ordenados = []
    #para cada contacto en la agenda se le recoge el nombre
    nombres = [contacto['nombre'].lower() for contacto in contactos]
    #se ordenan los nombres
    nombres.sort()

    #pillamos el primer nombre y comprobamos si el nombre es el del 1er contacto, si no es asi pasa al siguiente hasta pillar el contacto del primer nombre, y guardara ese contacto en contactos_ordenados 
    for nombre in nombres:
        for contacto in contactos:
            if contacto["nombre"].lower() == nombre:
                contactos_ordenados.append(contacto)
    return contactos_ordenados

def mostrar_contactos(contactos: list):
    #mostrarra todos los contactos ordenados
    #El formato es el siguiente
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    
    print(f"\nAGENDA {len(contactos)}")
    contactos_ordenados = ordenar_contactos(contactos)
    #a cada contacto en contactos_ordenados
    for contacto in contactos_ordenados:
        #los telefonos en lugar de apareces ["123123123","123123124",...] apareceran 123123123/123123124/...
        telefonos = " / ".join(contacto['telefonos'])
        print("---------------")
        print(f"Nombre: {contacto['nombre']} {contacto['apellido']} ({contacto['email']})")
        print(f"Telefonos:{telefonos}")

def mostrar_menu():
    #muestra un menu con todas las opciones
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir")

def pedir_opcion() -> int:
    #nos pedira un numero y comprobara si sirve
    try:
        valor = int(input("Dime la opcion que vas a elegir: "))
    except ValueError:
        valor = -1
        print("Dame un numero y valido.")
    return valor

def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #Es la funcion principal de mi programa, te da el menu de las opciones y dependiendo de cual eligas se egecutara la opcion que hayas elegido
    diferencia_sime = OPCIONES_MENU ^ {8}
    
    opcion = None
    while opcion != 8:
        
        if opcion in diferencia_sime:
            
            #agregara un contacto
            if opcion == 1:
                nuevo_contacto = agregar_contacto(contactos)
                contactos.append(nuevo_contacto)
                print("\nContacto añadido a la agenda")
                pulse_tecla_para_continuar()
                borrar_consola()
            
            #modificara un contacto
            elif opcion == 2:
                verdad = modificar_contacto(contactos)
                if verdad == True:
                    print("Se ha modificado el contacto perfectamente")
                else:
                    print("Este contacto no esta en la agenda")
                pulse_tecla_para_continuar()
                borrar_consola()
            
            #eliminara un contacto
            elif opcion == 3:
                email = input("Dime el email que quieres borrar: ")
                eliminar_contacto(contactos, email)
                pulse_tecla_para_continuar()
                borrar_consola()
                
            #eliminara todos los contactos 
            elif opcion == 4:
                contactos = borrar_agenda(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
                
            #restaurara la agenda inicial
            elif opcion == 5:
                agenda_inicial(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
                
            #mostrara contactos por criterios que tu quieras buscar
            elif opcion == 6:
                mostrar_contacto_criterio(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
                
            #mostrara todos los contactos
            elif opcion == 7:
                mostrar_contactos(contactos)
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
    #El main realmente no tiene mucho, al principio borra la consola , carga los contactos y se va a la funcion agenda
    borrar_consola()

    
    contactos = []

    
    cargar_contactos(contactos)


    agenda(contactos)

if __name__ == "__main__":
    main()