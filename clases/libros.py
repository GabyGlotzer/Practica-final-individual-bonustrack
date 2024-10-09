class Libro:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria
        self.disponible = True

    def esta_disponible(self):
        return self.disponible

    def prestar_libro(self):
        self.disponible = False
        return
    
    def devolver_libro(self):
        if self.disponible:
            print(f"El libro {self.nombre} no ha sido prestado")
        else:
            self.disponible = True
            # acá descargar el libro de la lista de libros del usuario

            print(f"Gracias por devolver el libro {self.nombre}")
            
        return

    def mostrar_detalles_libro(self):
        dispo = "" if self.disponible else "NO"
        return f"Libro: {self.nombre} Categoría: {self.categoria} Status: {dispo} disponible"
    
