class Usuarios:
    def __init__(self, nombre, dni, celular):
        self.nombre = nombre
        self.dni = dni
        self.celular = celular
        self.libros_llevados = []
        
    def llevar_libro(self, libro):
        self.libros_llevados.append(libro)

    def retornar_libro(self, libro):
        self.libros_llevados.remove(libro)
    
    def mostrar_usuario(self, libros):
        print(f"Usuario: {self.nombre} DNI: {self.dni} Celu: {self.celular}")
        print("Libros llevados:")

        for libro in self.libros_llevados:
            # Busca el libro en la lista completa de libros usando su nombre
            libro_en_lista = next((lib for lib in libros if lib.nombre == libro.nombre), None)
        
            if libro_en_lista:
                print(f"Libro: {libro_en_lista.nombre}")  # Muestra el título del libro    

    def se_llevo(self, libro):                                      # Este método dice si un libro está en la lista 
        return libro in self.libros_llevados                        # de libros llevados por este usuario
