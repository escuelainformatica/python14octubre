# programacion orientada a objeto.




class Libro():

    # constructor
    def __init__(self,titulo:str,autor:str,paginas:int,precio:int):
        # campos
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        self.precio=precio
    def funcion1(self):
        print("esta es una funcion")


libro1=Libro('Harry Potter','J.K',40,4000)

libro1.funcion1()

print(libro1) # object(Libro)
print(f"Titulo :{libro1.titulo}, autor:{libro1.autor}")