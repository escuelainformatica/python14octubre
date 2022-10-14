# dict
producto_dict={'nombre':'cocacola','precio':5000}

# programacion orientada a objeto

class ProductoClase():
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

# clase
# una variable definida por una clase se llama objeto (instancia).
producto_clase=ProductoClase('cocacola',5000)

print(producto_dict['nombre'])
print(producto_clase.nombre)
print(producto_dict)
print(producto_clase)
