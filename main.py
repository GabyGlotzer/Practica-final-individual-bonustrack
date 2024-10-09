# Funciones necesarias
#

import random
from clases.libros import Libro
from clases.usuarios import Usuarios



####################################
#   Registro de libros
####################################

def registrar_libro():
    titulo = input("Título del libro? (Vacío=Fin): ").strip().lower()
    if not titulo:
        return  #al menú principal
    categoria = random.choice(["ficcion", "infantil", "suspenso"])  # par hacer más rápido
    #while categoria not in ["ficcion", "infantil", "suspenso"]:
    #    categoria = input("Categoría (Ficción/Infantil/Suspenso)?: ").strip().lower()

    libro = Libro(titulo, categoria)
    return libro
    
def registrar_usuario():
    nombre = input("Nombre del usuario: ")
    dni = random.randint(11111111,22222222)   #input("DNI: ")
    celu = random.randint(33333333,44444444)  #input("Celular: ")
    usuario = Usuarios(nombre, dni, celu)
    return usuario

def pedir_usuario(usuarios):                         # No da la opción de "FIN" ver si es necesaria
    nombre_usuario = input("Nombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
                            # Busca el primer elemento de la lista que cumpla la condición
    return usuario
    
def pedir_nombre_libro(libros):
    nombre_libro = input("Título del libro? (Vacío=Fin): ")
    if not nombre_libro:
        return "fin"
    libro = next((cada_libro for cada_libro in libros if cada_libro.nombre == nombre_libro), None)
                            # Busca el primer elemento de la lista que cumpla la condición
    return libro    


#######################################
#
#  Pedir libros prestados
#
#######################################

def pedir_libros(usuarios, libros):
    nombre_usuario = pedir_usuario(usuarios)
    
    if not nombre_usuario:
        print("Usuario inexistente")
        return
    
    while True:
        libro = pedir_nombre_libro(libros)
        if libro == "fin":
            break  # Sale
        
        if libro:
            if libro.esta_disponible():
                libro.prestar_libro()                           # Actualiza la tabla de libros
                nombre_usuario.llevar_libro(libro)              # Actualiza la tabla de usuarios con los libros
                                                                # llevados
                print(f"Libro: {libro.nombre} prestado con éxito!!!")
            else:
                print(f"El libro: {libro.nombre} no se puede retirar, ya fue prestado")

        else:
            print("Libro Inexistente")

#######################################
#
#  Devolver libros prestados
#
#######################################


def devolver_libros(usuarios, libros):
    nombre_usuario = pedir_usuario(usuarios)
    
    if not nombre_usuario:
        print("Usuario inexistente")
        return
    
    while True:
        libro = pedir_nombre_libro(libros)
        if libro == "fin":
            break  # Sale

        if libro:
            if not libro.esta_disponible():
                #print("Libro: ", libro,"tipo: " ,type(libro))
                if nombre_usuario.se_llevo(libro):
                    libro.devolver_libro()                          # Actualiza la tabla de libros
                    nombre_usuario.retornar_libro(libro)            # Actualiza la tabla de usuarios con los libros
                                                                    # llevados
                    print(f"Libro: {libro.nombre} retornado con éxito!!!")
                else:
                    print(f"El libro: {libro.nombre} no se puede retornar, porque no fue prestado a este usuario")

            else:
                print(f"El libro: {libro.nombre} no se puede retornar, porque no fue prestado")

        else:
            print("Libro Inexistente")


###########################################
#
# Menú Principal
#
###########################################
        
def mostrar_menu():
    print("\n --- Menú de gestión BIBLIOTECA ---")   # el "\n" deja una línea en blanco 
    print("1. Registrar Libros")
    print("2. Registrar Usuarios")
    print("3. Pedir Libros")
    print("4. Devolver Libros")
    print("5. Mostrar detalles de Libros")
    print("6. Mostrar detalles de Usuarios")
    print("7. Mostrar libros disponibles")
    print("8. Mostrar libros prestados")
    print("9. Salir")


def main():
    libros = []
    usuarios = []
    
#
# Bucle para pedir las opciones mediante el menú
#

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            libro = registrar_libro()
            if libro:
                libros.append(libro)
                print("Libro registrado con éxito")
        
        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("Usuario registrado con éxito")
       
        elif opcion == "3":
            pedir_libros(usuarios, libros)

        elif opcion == "4":
            devolver_libros(usuarios, libros)
        
        elif opcion == "5":
            libro = pedir_nombre_libro(libros)
            if libro == "fin":
                break  # Sale
            
            if libro:
                print(libro.mostrar_detalles_libro())
            else:
                print("Libro Inexistente")
        
        elif opcion == "6":
            usuario = pedir_usuario(usuarios)
            
            if usuario:
                usuario.mostrar_usuario(libros)
                
            else:
                print("Usuario Inexistente")

        elif opcion == "7":               # Libros disponibles
            print("#### Libros Disponibles####")
            for cada_libro in libros:
                if cada_libro.disponible:
                    print(f"Libro: {cada_libro.nombre} / Categoría: {cada_libro.categoria} ")

        elif opcion == "8":               # Libros prestados
            print("**** Libros prestados ****")
            for cada_libro in libros:
                if not cada_libro.disponible:
                    print(f"Libro: {cada_libro.nombre} / Categoría: {cada_libro.categoria} ")   
            
        elif opcion == "9":
            print("Saliendo del sistema, Gracias por usar Biblo Plus!!!")
            break

        else:
            print("Opción inválida, intente nuevamente") 

 #  Y esto para que este código se ejecute exclusivamente desde acá (main) y no desde
    #  otro lado

if __name__ == "__main__":
    main()